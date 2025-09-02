"""
Module defining types for the Jellyfin API.
"""

from typing import Union
from pydantic import BaseModel

from .base import Model
from .generated import api_10_10, api_10_11

BaseItemQueryResult = Union[
    api_10_10.BaseItemDtoQueryResult,
    api_10_11.BaseItemDtoQueryResult,
    Model
]

BaseItem = Union[
    api_10_10.BaseItemDto,
    api_10_11.BaseItemDto,
    Model
]