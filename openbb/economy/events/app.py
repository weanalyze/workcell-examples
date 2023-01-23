from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from workcell.integrations.types import PerspectiveTable


class Input(BaseModel):
    message: str

def economy_events(input: Input) -> PerspectiveTable:
    """Economy events"""
    df = openbb.economy.events()
    return PerspectiveTable(data=df)
