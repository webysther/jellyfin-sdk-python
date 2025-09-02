import jmespath, pandas

from logging import warning

from typing import Any, Dict, List
from collections.abc import Iterable
from pydantic import BaseModel

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

    def summary(self, empty: bool = True) -> None:
        """Prints the simple representation of the model.
        
        Args:
            empty (bool): If True, includes all values. If False, omits empty values (None, "", 0, [], {}).
        """
        for prop in self._data.__class__.model_fields.keys():
            value = getattr(self._data, prop)
            if not empty:
                if value is None or value == 0 or value == "":
                    continue

                if isinstance(value, (list, dict, set, tuple)) and not value:
                    continue

            if hasattr(value, 'to_dict'):
                print(f"{prop}:")
                value = value.to_dict()
                for k, v in value.items():
                    if not empty:
                        if v is None or v == 0 or v == "":
                            continue
                        
                        if isinstance(value, (list, dict, set, tuple)) and not value:
                            continue

                    print(f"  {k}: {v}")
                continue
            
            print(f"{prop}: {getattr(self._data, prop)}")

    def search(self, term: str) -> any:
        """Extract value using a simplified XPath-like syntax.
        
        Args:
            term (str): The XPath-like path to the desired attribute.

        Returns:
            any: The value at the specified path, or None if not found.
        """
        return jmespath.search(term, self.to_dict())
