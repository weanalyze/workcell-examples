import pandas as pd
# import plotly
import plotly.express as px
from pydantic import BaseModel
from typing import Literal
from workcell.integrations.types import PlotlyPlot


METRICS = Literal["Life Expectancy", "Population", "GDP Per Capita"]
COUNTRIES = Literal["United States", "Canada", "Mexico"]


class PlotInput(BaseModel):
    metric: METRICS
    country: COUNTRIES # (https://www.gapminder.org/data/geo/), case sensitive


def load_data():
    dataframe = px.data.gapminder().rename(columns={
        'year': 'Year', 
        'lifeExp': 'Life Expectancy', 
        'pop': 'Population', 
        'gdpPercap': 'GDP Per Capita'
    })
    return dataframe


def visualization(dataframe, metric, country):
    subset = dataframe[dataframe.country == country]
    fig = px.line(subset, x='Year', y=metric, title=f'{metric} in {country}')
    return fig    


def hello_plotly(input: PlotInput) -> PlotlyPlot:
    """A plotly express fig encode in json format."""
    # Step1. load data
    dataframe = load_data()
    # Step2. create plot
    fig = visualization(dataframe, input.metric, input.country)
    # Step3. wrapped by output
    output = PlotlyPlot(data=fig)
    return output

import workcell
app = workcell.create_app(hello_plotly)