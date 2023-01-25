from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from workcell.integrations.types import DataFrameOutput


class DummyInput(BaseModel):
    pass

def economy_events(input: DummyInput) -> DataFrameOutput:
    """Economic Calendar (openbb.economy.events)"""
    df = openbb.economy.events()
    return DataFrameOutput(data=df)
