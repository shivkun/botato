from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class EmbedField(BaseModel):
    """
    Represents a field in an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    name: str
    value: str
    inline: Optional[bool] = None
        

class EmbedAuthor(BaseModel):
    """
    Represents the author of an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    name: str
    url: Optional[str] = None
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None
        

class EmbedProvider(BaseModel):
    """
    Represents a provider of an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    name: Optional[str] = None
    url: Optional[str] = None
        

class EmbedVideo(BaseModel):
    """
    Represents a video in an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
        
        
class EmbedImage(BaseModel):
    """
    Represents an image in an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
        
        
class EmbedThumbnail(BaseModel):
    """
    Represents a thumbnail in an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None
        
        
class EmbedFooter(BaseModel):
    """
    Represents a footer in an embed.
    """
    model_config = ConfigDict(extra="allow")
    
    text: str
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None
        
    
class Embed(BaseModel):
    """
    Represents an embed in a Discord message.
    
    Documentation:
    https://discord.com/developers/docs/resources/message#embed-object
    """
    model_config = ConfigDict(extra="allow")
    
    title: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    timestamp: Optional[str] = None
    color: Optional[int] = None
    footer: Optional[EmbedFooter] = None
    image: Optional[EmbedImage] = None
    thumbnail: Optional[EmbedThumbnail] = None
    video: Optional[EmbedVideo] = None
    provider: Optional[EmbedProvider] = None
    fields: Optional[List[EmbedField]] = None