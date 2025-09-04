from itertools import islice
from logging import warning

from typing_extensions import Self
from typing import (
    Any, 
    Dict, 
    List, 
    Protocol, 
    Callable, 
    TypeVar
)

from collections.abc import Iterable, Sequence
from pydantic import BaseModel
from .generated import BaseItemDtoQueryResult

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

    def __str__(self) -> str:
        """Returns the string representation of the model."""
        return self._model.__str__()
    
    def __repr__(self) -> str:
        """Returns a detailed string representation of the Item object, with each attribute on a new line."""
        attrs = []
        if hasattr(self._model.__class__, "model_fields"):
            keys = self._model.__class__.model_fields.keys()
        else:
            keys = self._model.__dict__.keys()
        for key in keys:
            value = getattr(self._model, key, None)
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

class Collection(Sequence):
    _factory: Callable = Model
    _model: Model
    _data: List[BaseModel]

    def __init__(self, data: List[BaseModel] | Model):
        self._data = data

        if isinstance(data, Model):
            self._model = data
            self._data = self._model.items

    @property
    def data(self) -> List[BaseModel]:
        """Returns the reference list of items inside model."""
        return self._data

    def __getitem__(self, idx) -> Any:
        return self._factory(self.data[idx])

    def __len__(self):
        return len(self.data)

    @property
    def first(self) -> Model:
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