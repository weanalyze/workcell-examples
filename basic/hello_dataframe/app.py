from pydantic import BaseModel
import pandas as pd
from workcell.integrations.types import DataFrameOutput

class DummyInput(BaseModel):
    pass

def hello_dataframe(input: DummyInput) -> DataFrameOutput:
    """Returns a pandas DataFrame in Arrow format."""
    d = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [None, 0.1, -1.5]}
    df = pd.DataFrame(data=d)
    output = DataFrameOutput(data=df)
    return output
