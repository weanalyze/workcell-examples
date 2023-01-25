from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from workcell.integrations.types import DataFrameOutput


class DummyInput(BaseModel):
    pass

def stocks_disc_pipo(input: DummyInput) -> DataFrameOutput:
    """Past IPO Dates (openbb.stocks.disc.pipo)"""
    df = openbb.stocks.disc.pipo()
    return DataFrameOutput(data=df)
