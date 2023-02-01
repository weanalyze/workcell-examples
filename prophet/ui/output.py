from pydantic import BaseModel, Field


class ProphetOutput(BaseModel):
    short_text: str = Field(..., max_length=60, description="Short text property")
    long_text: str = Field(..., description="Unlimited text property")