from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from botato.models.user import User
from botato.models.role import Role
from botato.models.user import AvatarDecorationData


class Member(BaseModel):
    """
    Represents a Discord member.

    Documentation:
    https://discord.com/developers/docs/resources/guild#guild-member-object
    """
    model_config = ConfigDict(extra="allow")
    
    user: Optional[User] = None
    nick: Optional[str] = None
    avatar: Optional[str] = None
    banner: Optional[str] = None
    roles: List[Role] = Field(default_factory=list)
    joined_at: str
    premium_since: Optional[str] = None
    deaf: bool
    mute: bool
    flags: int
    pending: Optional[bool] = None
    permissions: Optional[str] = None
    communication_disabled_until: Optional[str] = None
    avatar_decoration_data: Optional[AvatarDecorationData] = None