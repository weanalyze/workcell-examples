from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from typing import Optional
from workcell.integrations.types import DataFrameOutput


class TickerInput(BaseModel):
    ticker: str
    name: Optional[str] = None

def stocks_dd_sec(input: TickerInput) -> DataFrameOutput:
    """List of SEC Filings. Gets a DataFrame of the recent SEC filings submitted by the company and a link to view each one. (openbb.stocks.dd.sec )"""
    df = openbb.stocks.dd.sec(input.ticker)
    return DataFrameOutput(data=df)
