from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from botato.models.user import User
from botato.models.role import Role


class Emoji(BaseModel):
    """
    Represents a Discord emoji.
    
    Documentation:
    https://discord.com/developers/docs/resources/emoji#emoji-object
    """
    model_config = ConfigDict(extra="allow")
    
    id: Optional[str] = None
    name: Optional[str] = None
    roles: List[Role] = Field(default_factory=list)
    user: Optional[User] = None
    require_colons: bool = False
    managed: bool = False
    animated: bool = False
    available: bool = True