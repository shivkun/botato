from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from botato.models.emoji import Emoji

class ReactionCountDetails(BaseModel):
    """
    Represents the details of a reaction count.
    """
    model_config = ConfigDict(extra="allow")
    
    burst: int
    normal: int
    

class Reaction(BaseModel):
    """
    Represents a reaction to a message.
    """
    model_config = ConfigDict(extra="allow")
    
    count: int
    count_details: Optional[ReactionCountDetails] = None
    me: bool
    me_burst: bool
    emoji: Emoji
    burst_colors: Optional[List[str]] = None