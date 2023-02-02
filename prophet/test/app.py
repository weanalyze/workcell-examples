from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, Dict, List
import pandas as pd
from io import StringIO, BytesIO
from workcell.integrations.types import FileContent, PandasDataFrame


class DatetimeColumn(str, Enum):
    FOO = "foo"
    BAR = "bar"

# Input preload pandas
class DataFrameInput(BaseModel):
    df: Optional[PandasDataFrame] # order matters
    date_col: Optional[str]
    csv_file: FileContent = Field(
        ..., 
        title="CSV File",
        description="CSV file to be processed.",
    )

    def __init__(self, *args, **kwargs):
        # Pre-load dataframe
        dataframe = pd.read_csv(BytesIO(kwargs['csv_file']), sep=",")
        kwargs['df'] = PandasDataFrame(data=dataframe) 
        kwargs['date_col'] = dataframe['Month'].name
        # Call parent's __init__
        super().__init__(**kwargs)        

class DataFrameOutput(BaseModel):
    data: Dict

def test_pp(input: DataFrameInput) -> DataFrameOutput:
    df = input.df
    data = {
        'date_col': input.date_col,
        'num_row': df.data.shape[0], 
        'num_col': df.data.shape[1], 
    }
    output = DataFrameOutput(data=data)
    return output

