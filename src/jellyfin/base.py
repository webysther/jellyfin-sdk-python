from itertools import islice
from logging import warning

from typing import (
    Any, 
    Dict, 
    List, 
    Protocol, 
    Callable, 
    TypeVar, 
    Generic
)

from collections.abc import Iterable, Sequence
from pydantic import BaseModel
from .generated import BaseItemDtoQueryResult

JellyfinModel = TypeVar('JellyfinModel', bound=BaseModel)

class Pagination(Protocol):
    """ Protocol for paginated responses. """
    def next_page(self) -> BaseModel: ...

class GeneratedModelWrapper(Generic[JellyfinModel]):
    _model: JellyfinModel
    
    def __init__(self, model: JellyfinModel):
        self._model = model

    @property
    def model(self) -> BaseModel:
        """ Returns the generated model """
        return self._model
    
    @property
    def items(self) -> List[BaseModel] | None:
        """ Returns the list of items if present in the model, otherwise None """
        return self._items

    def __str__(self) -> str:
        """Returns the string representation of the model."""
        return str(self.model)
    
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
    
    def summary(self, empty: bool = False, size: int = 80, limit: int = 100) -> None:
        """Prints the simple representation of the model.
        
        Args:
            empty (bool): If True, includes all values. If False, omits empty values (None, "", 0, [], {}).
        """
        if hasattr(self.model.__class__, "model_fields"):
            keys = self.model.__class__.model_fields.keys()
        else:
            keys = self.model.__dict__.keys()
        for i, key in enumerate(keys):
            if limit and i >= limit:
                break
            value = getattr(self.model, key, None)
            if not empty:
                if value is None or value == 0 or value == "":
                    continue

                if isinstance(value, (list, dict, set, tuple)) and not value:
                    continue

            value_str = str(getattr(self.model, key))
            if len(value_str) > size:
                value_str = value_str[:size].rstrip() + "..."

            print(f"{key}={value_str}")

class GeneratedListWrapper(Sequence):
    _model: GeneratedModelWrapper
    _data: List[BaseModel]
    
    def __init__(self, data: List[BaseModel] | GeneratedModelWrapper):
        self._data = data
        
        if isinstance(data, GeneratedModelWrapper):
            self._model = data
            self._data = self._model.items

    @property
    def factory(self) -> Callable:
        return GeneratedModelWrapper

    @property
    def data(self) -> List[BaseModel]:
        """Returns the reference list of items inside model."""
        return self._data

    def __getitem__(self, idx) -> Any:
        return self.factory(self.data[idx])

    def __len__(self):
        return len(self.data)

    @property
    def first(self) -> GeneratedModelWrapper:
        return self.factory(self.data[0])

    def filter(self, criteria: dict) -> Self:
        return [
            obj for obj in self.data
            if all(getattr(obj, k, None) == v for k, v in criteria.items())
        ]

    def __repr__(self) -> str:
        if len(self) == 0:
            return f"<{self.__class__.__name__} (no items)>"

        parts = []
        for item in islice(self.items, 10):
            attrs = repr(item).split(",\n")
            parts.append(",\n".join(attrs[:10]))
            if len(attrs) > 10:
                parts.append(", ...\n")

        if len(self) > 10:
            parts.append("  ...")

        return f"<{self.__class__.__name__} items=[\n  {',\n'.join(parts)}\n]>"