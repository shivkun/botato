from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from botato.models.user import User
from botato.models.member import Member
from botato.models.role import Role
from botato.models.channel import ChannelMention
from botato.models.embed import Embed
from botato.models.reaction import Reaction
from botato.models.channel import Channel
    

class Attachment(BaseModel):
    """
    Represents an attachment in a Discord message.
    """
    model_config = ConfigDict(extra="allow")
    
    id: str
    filename: str
    title: Optional[str] = None
    description: Optional[str] = None
    content_type: Optional[str] = None
    size: int
    url: str
    proxy_url: str
    height: Optional[int] = None
    width: Optional[int] = None
    ephemeral: Optional[bool] = None
    duration_secs: Optional[float] = None
    waveform: Optional[str] = None
    flags: Optional[int] = None


class Message(BaseModel):
    """
    Represents a Discord message object.

    Documentation:
    https://discord.com/developers/docs/resources/message#messages-resource
    """
    model_config = ConfigDict(extra="allow")
    
    id: str
    channel_id: str
    author: User
    content: str
    timestamp: str
    edited_timestamp: Optional[str] = None
    tts: bool
    mention_everyone: bool
    mentions: List[User] = Field(default_factory=list)
    mention_roles: List[Role] = Field(default_factory=list)
    mention_channels: List[ChannelMention] = Field(default_factory=list)
    attachments: List[Attachment] = Field(default_factory=list)
    embeds: List[Embed] = Field(default_factory=list)
    reactions: List[Reaction] = Field(default_factory=list)
    nonce: Optional[str | int] = None
    pinned: bool
    webhook_id: Optional[str] = None
    type: int
    activity: Optional[dict] = None
    application: Optional[dict] = None
    application_id: Optional[str] = None
    flags: Optional[int] = None
    message_reference: Optional[dict] = None
    message_snapshots: Optional[List[dict]] = None
    referenced_message: Optional["Message"] = None
    interaction_metadata: Optional[dict] = None
    interaction: Optional[dict] = None
    thread: Optional[Channel] = None
    components: Optional[List[dict]] = None
    sticker_items: Optional[List[dict]] = None
    stickers: Optional[List[dict]] = None
    position: Optional[int] = None
    role_subscription_data: Optional[dict] = None
    resolved: Optional[dict] = None
    poll: Optional[dict] = None
    call: Optional[dict] = None