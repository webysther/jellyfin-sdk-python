from itertools import islice
import rich

from typing_extensions import Self
from typing import (
    Any, 
    List, 
    Protocol, 
    Callable
)

from collections.abc import Sequence
from pydantic import BaseModel

class Pagination(Protocol):
    """ Protocol for paginated responses. """
    def next_page(self) -> BaseModel: ...

class Model():
    _model: BaseModel
    
    def __init__(self, model: BaseModel):
        self._model = model

    @property
    def model(self) -> BaseModel:
        """ Returns the generated model """
        return self._model
    
    def __setattr__(self, name, value):
        if name in ("_model", "model"):
            super().__setattr__(name, value)
        elif hasattr(self.model, name):
            setattr(self.model, name, value)
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __getattr__(self, name):
        if hasattr(self.model, name):
            return getattr(self.model, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __str__(self) -> str:
        """Returns the string representation of the model."""
        return self.model.__str__()
    
    def __repr__(self) -> str:
        """Returns a detailed string representation of the Item object, with each attribute on a new line."""
        attrs = []
        if hasattr(self.model.__class__, "model_fields"):
            keys = self.model.__class__.model_fields.keys()
        else:
            keys = self.model.__dict__.keys()
        for key in keys:
            value = getattr(self.model, key, None)
            attrs.append(f"  {key}={value!r}")
        attrs_str = ",\n".join(attrs)
        return f"<{self.__class__.__name__}\n{attrs_str}\n>"
    
    @property
    def pretty(self):
        """Prints a pretty representation of the model using rich."""
        rich.print(self)

class Collection(Sequence):
    _factory: Callable = Model
    _model: Model
    _data: List[BaseModel]
    _pagination: Pagination

    def __init__(self, data: List[BaseModel] | Model, pagination: Pagination = None):
        if not isinstance(data, (list, Model)):
            raise TypeError(f"data must be a list or Model, got {type(data)}")
        
        self._data = data
        self._pagination = pagination

        if isinstance(data, Model):
            self._model = data
            self._data = data.items
            
    def __iter__(self):
        """
        Returns an iterator for the collection.

        Usage:
            collection = ItemCollection(...)
            for item in collection:
                print(collection.current)  # Always shows the current item
        """        
        while True:
            for item in self.data:
                yield self._factory(item)

            if self._pagination is None:
                break

            collection = self._pagination.next_page()
            if len(collection.data) == 0:
                break

            self._model = collection.model
            self._data = collection.data

    @property
    def model(self) -> Model:
        """Returns the reference model."""
        return self._model

    @property
    def data(self) -> List[BaseModel]:
        """Returns the reference list of items inside model."""
        return self._data

    def __getitem__(self, idx) -> Any:
        return self._factory(self.data[idx])
    
    def __len__(self):
        """
        Returns the total number of records in the collection.

        Returns:
            int: The total number of records.
        """
        if not hasattr(self, "model"):
            return len(self.data)

        return self.model.total_record_count

    @property
    def first(self) -> Model:
        if len(self) == 0:
            return None
        return self[0]

    def __repr__(self) -> str:
        if len(self) == 0:
            return f"<{self.__class__.__name__} (no items)>"

        parts = []
        for item in islice(self, 10):
            attrs = repr(item).split(",\n")
            parts.append(",\n".join(attrs[:10]) + "\n  ...")

        if len(self) > 10:
            parts.append(" ...")

        items = '\n'.join(parts)
        return f"<{self.__class__.__name__} items=[\n  {items}\n]>"