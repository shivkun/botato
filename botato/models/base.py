from pydantic import BaseModel, Field, ConfigDict


class BotatoBase(BaseModel):
    """
    Base model for Botato.
    """

    some_field: str = Field(..., description="A required string field")

    model_config = ConfigDict(
        extra="allow",
        arbitrary_types_allowed=True,
        json_encoders={
            set: lambda v: list(v),
        },
    )