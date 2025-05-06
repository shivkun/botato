from botato.models.base import BotatoBase, Field
from botato.models.snowflake import Snowflake
from typing import Optional, List

class RoleTag(BotatoBase):
    """
    Represents a tag associated with a Discord role.
    """
    
    bot_id: Optional[Snowflake] = Field(default=None)
    integration_id: Optional[Snowflake] = Field(default=None)
    subscription_listing_id: Optional[Snowflake] = Field(default=None)
    
    """
    Fields `premium_subscriber`, `available_for_purchase`, and `guild_connections`
    have a type `null` which represent booleans: they will be present and set to `null`
    if they are "true", and will be not present if they are "false".
    
    Defaulting to `false` for these fields makes them not present.
    """
    premium_subscriber: Optional[bool] = Field(default=False)
    available_for_purchase: Optional[bool] = Field(default=False)
    guild_connections: Optional[bool] = Field(default=False)

class Role(BotatoBase):
    """
    Represents a Discord role.
    """
    
    # Required, non-nullable
    id: Snowflake
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    flags: int
    
    # Optional, non-nullable
    tags: Optional[List[RoleTag]] = Field(default={})
    
    # Optional, nullable (can be None)
    icon: Optional[str] = Field(default=None)
    unicode_emoji: Optional[str] = Field(default=None)