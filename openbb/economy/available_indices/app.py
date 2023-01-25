from openbb_terminal.sdk import openbb
from pydantic import BaseModel
import pandas as pd
from workcell.integrations.types import DataFrameOutput


class DummyInput(BaseModel):
    pass

def economy_available_indices(input: DummyInput) -> DataFrameOutput:
    """Curated List of Global Indices. The index function can request data using a couple of methods. There is a curated list of global indexes which can be entered by symbol or values from the left column of the table below. (openbb.economy.available_indices)"""
    df = pd.DataFrame.from_dict(openbb.economy.available_indices()).transpose()
    return DataFrameOutput(data=df)
