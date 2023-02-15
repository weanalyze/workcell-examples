from openbb_terminal.sdk import openbb
from pydantic import BaseModel
import pandas as pd
from workcell.integrations.types import PerspectiveTable


class DummyInput(BaseModel):
    pass

def stocks_disc_fipo(input: DummyInput) -> PerspectiveTable:
    """Future IPO Dates (openbb.stocks.disc.fipo)"""
    df = pd.DataFrame(openbb.stocks.disc.fipo())
    output = PerspectiveTable(data=df)
    return output
