from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from typing import Optional
from workcell.integrations.types import DataFrameOutput


class TickerInput(BaseModel):
    ticker: str
    name: Optional[str] = None

def stocks_dd_customer(input: TickerInput) -> DataFrameOutput:
    """List of Customers (openbb.stocks.dd.customer)"""
    df = openbb.stocks.dd.customer(input.ticker)
    return DataFrameOutput(data=df)
