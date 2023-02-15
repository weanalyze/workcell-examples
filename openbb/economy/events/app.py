from openbb_terminal.sdk import openbb
from pydantic import BaseModel
import pandas as pd
from workcell.integrations.types import PerspectiveTable


class DummyInput(BaseModel):
    pass

def economy_events(input: DummyInput) -> PerspectiveTable:
    """Economic Calendar (openbb.economy.events)"""
    df = pd.DataFrame.from_dict(openbb.economy.events()).transpose()
    output = PerspectiveTable(data=df.reset_index())
    return output
