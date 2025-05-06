from botato.models.base import BotatoBase, Field
from botato.models.snowflake import Snowflake
from typing import Optional


class AvatarDecorationData(BotatoBase):
    """
    Represents the avatar decoration data for a Discord user.
    """
    
    asset: str
    sku_id: Snowflake


class User(BotatoBase):
    """
    Represents a Discord user.

    Documentation:
    https://discord.com/developers/docs/resources/user#user-object
    
    Note: Example Nullable and Optional fields
    - FIELD                     TYPE
    - `optional_field?`         string
    - `nullable_field`          ?string
    - `optional_and_nullable?` ?string
    
    Examples:
    - User(id=123456789012345678, username="example", discriminator="0001", global_name=None, avatar=None, ...) 
    -> this is valid because all required fields are present, even if some are None.
    - User(id=123456789012345678, username="example", discriminator="0001", global_name=None, ...) 
    -> this is invalid because `avatar` is required but not provided, is missing.
    """
    
    # Required, non-nullable
    id: Snowflake
    username: str
    discriminator: str
    
    # Required, nullable (must be present, can be None)
    global_name: Optional[str] = Field(...)
    avatar: Optional[str] = Field(...)
    
    # Optional, non-nullable
    bot: Optional[bool] = Field(default=False)
    system: Optional[bool] = Field(default=False)
    mfa_enabled: Optional[bool] = Field(default=False)
    locale: Optional[str] = Field(default="en-US")
    verified: Optional[bool] = Field(default=False)
    flags: Optional[int] = Field(default=0)
    premium_type: Optional[int] = Field(default=0)
    public_flags: Optional[int] = Field(default=0)
    
    # Optional, nullable (can be None)
    banner: Optional[str] = Field(default=None)
    accent_color: Optional[int] = Field(default=None)
    email: Optional[str] = Field(default=None)
    avatar_decoration_data: Optional[AvatarDecorationData] = Field(default=None)