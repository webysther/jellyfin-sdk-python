import jmespath, pandas

from logging import warning

from typing import Any, Dict, List, Protocol
from collections.abc import Iterable
from pydantic import BaseModel
from .generated import BaseItemDtoQueryResult

class CollectionPagination(Protocol):
    """ Protocol for paginated collections """
    def next_page(self) -> BaseModel: ...

class Model(BaseModel):
    def to_str(self) -> str:
        """ Signature method for generated models"""
        return self._data.to_str()

    def to_json(self) -> str:
        """ Signature method for generated models"""
        return self._data.to_json()
    
    def to_dict(self) -> Dict[str, Any]:
        """ Signature method for generated models"""
        return self._data.to_dict()
    
    def __str__(self) -> str:
        """Returns the string representation of the model."""
        return self.to_str()

    def __getattr__(self, name: str) -> Any:
        """Returns the value of the specified attribute from the item data.
        
        Args:
            name (str): The name of the attribute to retrieve.
            
        Returns:
            Any: The value of the specified attribute, or None if not found.
        """
        try:
            return super().__getattr__(name)
        except AttributeError:
            pass
        
        try:
            if self._data and hasattr(self._data, name):
                return getattr(self._data, name)
        except Exception:
            return None

        return None

    @property
    def to_df(self) -> pandas.DataFrame:
        """ Returns a DataFrame """
        data = self.to_dict()

        if isinstance(data, list):
            return pandas.DataFrame(data)
        return pandas.DataFrame([data])

    def summary(self, empty: bool = False, size: int = 80, limit: int = 100) -> None:
        """Prints the simple representation of the model.
        
        Args:
            empty (bool): If True, includes all values. If False, omits empty values (None, "", 0, [], {}).
        """
        if hasattr(self._data.__class__, "model_fields"):
            keys = self._data.__class__.model_fields.keys()
        else:
            keys = self._data.__dict__.keys()
        for key in keys:
            if limit and limit <= 0:
                break
            value = getattr(self._data, key, None)
            if not empty:
                if value is None or value == 0 or value == "":
                    continue

                if isinstance(value, (list, dict, set, tuple)) and not value:
                    continue

            value_str = str(getattr(self._data, key))
            if len(value_str) > size:
                value_str = value_str[:size].rstrip() + "..."

            limit -= 1
            print(f"{key}={value_str}")

    def search(self, term: str) -> any:
        """Extract value using a simplified XPath-like syntax.
        
        Args:
            term (str): The XPath-like path to the desired attribute.

        Returns:
            any: The value at the specified path, or None if not found.
        """
        return jmespath.search(term, self.to_dict())

class Single(Model):
    _naming: str = "Single"
    _data: BaseModel = None
    
    def __init__(self, item: BaseModel):
        """
        Initializes the Item class.

        Args:
            item (BaseModel): The single item data.
        """
        self._data = item
        
    def __repr__(self) -> str:
        """Returns a detailed string representation of the Item object, with each attribute on a new line."""
        attrs = []
        if hasattr(self._data.__class__, "model_fields"):
            keys = self._data.__class__.model_fields.keys()
        else:
            keys = self._data.__dict__.keys()
        for key in keys:
            value = getattr(self._data, key, None)
            attrs.append(f"  {key}={value!r}")
        attrs_str = ",\n".join(attrs)
        return f"<{self._naming}\n{attrs_str}\n>"

class ListCollection(Model):
    _naming: str = "Collection"
    _single: Callable = Single
    _data: List[BaseModel] = None
    
    @property
    def _list(self) -> List[BaseModel]:
        """Returns the reference list of items."""
        return self._data

    def __init__(self, collection: List[BaseModel]):
        """
        Initializes the ItemCollection class.
        
        Args:
            collection (List[BaseModel]): The collection of items.
        """
        self._data = collection
        self._iterator = None
        self._current = None
    
    @property
    def items(self) -> List[Single]:
        """
        Returns the list of items in the collection.
        
        Returns:
            List[Single]: A list of User objects.
        """
        if self._list is None:
            return []
        
        for item in self._list:
            yield self._single(item)

    def __iter__(self):
        """
        Returns an iterator for the collection.

        Usage:
            collection = ItemCollection(...)
            for item in collection:
                print(collection.current)  # Always shows the current item
        """
        self._iterator = iter(self._list)
        self._current = None            
        return self

    def __next__(self):
        """
        Returns the next item in the iteration.
        """
        self._current = next(self._iterator)
        return self._current
    
    def __len__(self):
        """
        Returns the number of items in the collection.
        """
        return len(self._list)

    @property
    def current(self):
        """
        Returns the current item in the iteration.
        """
        return self._current

    @property
    def all(self) -> List[Single]:
        """
        Returns all items in the collection as a list.

        Returns:
            List[Single]: A list of all Single objects.
        """
        return list(self.items)

    @property
    def total(self) -> int:
        """
        Returns the total number of records in the collection.

        Returns:
            int: The total number of records.
        """
        return self.__len__()
    
    def first(self, attr: str, value: Any) -> Single | None:
        """
        Returns the first item that matches the specified attribute and value.
        
        Args:
            attr (str): The attribute to search by.
            value (Any): The value to match.
            
        Returns:
            Single | None: The first matching item, or None if not found.
        """
        for item in self.filter({attr: value}, limit=1).items:
            return item
        return None

    def filter(self, criteria: dict, limit: int = None) -> 'ListCollection':
        """
        Returns a list of items that match the specified criteria.
        
        Args:
            criteria (dict): A dictionary of attribute-value pairs to filter by.
            limit (int, optional): The maximum number of items to return. Defaults to None (no limit).
            
        Returns:
            List[Single]: A list of Single objects that match the criteria.
        """
        if self._list is None:
            return []

        result = []
        for item in self._list:
            match = True
            for key, value in criteria.items():
                if getattr(item, key, None) != value:
                    match = False
                    break
            if match:
                result.append(item)
                if limit is not None and len(result) >= limit:
                    break

        return self.__class__(copy.deepcopy(result))

    def __repr__(self) -> str:
        if len(self) == 0:
            return f"<{self._naming} (no items)>"

        items_repr = ""
        size = 10
        
        for item in self.items:
            size -= 1
            if size < 0:
                break

            attrs = repr(item).split(',\n')
            items_repr += ",\n".join(attrs[:10])

            if len(attrs) > 10:
                items_repr += ", ...\n"

        if len(self) > 10:
            items_repr += "  ..."
        return (
            f"<{self._naming} total={self.total} items=[\n  {items_repr}\n]>"
        )