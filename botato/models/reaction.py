from botato.models.base import BotatoBase
from typing import Optional, List
from botato.models.emoji import Emoji
from botato.types.hex_color import HexColor

class ReactionCountDetails(BotatoBase):
    """
    Represents the details of a reaction count.
    """
    
    burst: int
    normal: int
    

class Reaction(BotatoBase):
    """
    Represents a reaction to a message.
    """
    
    count: int
    count_details: ReactionCountDetails
    me: bool
    me_burst: bool
    emoji: Emoji
    burst_colors: List[HexColor]