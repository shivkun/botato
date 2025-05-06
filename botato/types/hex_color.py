"""
This defines a new type of 'hex' that is used to represent a hex value.
This allows more control and validation over a standard 'str' type.
"""
import re
from pydantic.validators import str_validator

class HexColor(str):
    _pattern = re.compile(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
    
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield cls.validate
        
    @classmethod
    def validate(cls, v: str) -> 'HexColor':
        match = cls._pattern.fullmatch(v)
        if not match:
            raise ValueError(f"{v} is not a valid hex color")
        
        hex_value = match.group(1).lower()
        
        if len(hex_value) == 3:
            hex_value = ''.join(c*2 for c in hex_value)
            
        return cls(f'#{hex_value}')