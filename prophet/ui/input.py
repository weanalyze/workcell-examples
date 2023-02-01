from pydantic import BaseModel, Field


class ProphetInput(BaseModel):
    short_text: str = Field(..., max_length=60, description="Short text property")
    long_text: str = Field(..., description="Unlimited text property")