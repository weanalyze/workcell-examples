from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from workcell.integrations.types import DataFrameOutput


class DummyInput(BaseModel):
    pass

def stocks_disc_fipo(input: DummyInput) -> DataFrameOutput:
    """Future IPO Dates (openbb.stocks.disc.fipo)"""
    df = openbb.stocks.disc.fipo()
    return DataFrameOutput(data=df)
