from pydantic import BaseModel, ConfigDict
from typing import Optional


class Role(BaseModel):
    """
    Represents a Discord role.
    """
    model_config = ConfigDict(extra="allow")
    
    id: str
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool