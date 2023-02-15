from openbb_terminal.sdk import openbb
from pydantic import BaseModel
from typing import Optional
from workcell.integrations.types import PerspectiveTable


class TickerInput(BaseModel):
    ticker: str
    name: Optional[str] = None

def stocks_dd_supplier(input: TickerInput) -> PerspectiveTable:
    """List of Suppliers (openbb.stocks.dd.supplier)"""
    df = openbb.stocks.dd.supplier(input.ticker)
    return PerspectiveTable(data=df)
