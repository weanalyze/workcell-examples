from pydantic import BaseModel
import altair as alt
from vega_datasets import data
from workcell.integrations.types import AltairPlot


def plot_london_tube_lines():
    boroughs = alt.topo_feature(data.londonBoroughs.url, 'boroughs')
    tubelines = alt.topo_feature(data.londonTubeLines.url, 'line')
    centroids = data.londonCentroids.url

    background = alt.Chart(boroughs).mark_geoshape(
        stroke='white',
        strokeWidth=2
    ).encode(
        color=alt.value('#eee'),
    ).properties(
        width=700,
        height=500
    )

    labels = alt.Chart(centroids).mark_text().encode(
        longitude='cx:Q',
        latitude='cy:Q',
        text='bLabel:N',
        size=alt.value(8),
        opacity=alt.value(0.6)
    ).transform_calculate(
        "bLabel", "indexof (datum.name,' ') > 0  ? substring(datum.name,0,indexof(datum.name, ' ')) : datum.name"
    )

    line_scale = alt.Scale(domain=["Bakerloo", "Central", "Circle", "District", "DLR",
                                "Hammersmith & City", "Jubilee", "Metropolitan", "Northern",
                                "Piccadilly", "Victoria", "Waterloo & City"],
                        range=["rgb(137,78,36)", "rgb(220,36,30)", "rgb(255,206,0)",
                                "rgb(1,114,41)", "rgb(0,175,173)", "rgb(215,153,175)",
                                "rgb(106,114,120)", "rgb(114,17,84)", "rgb(0,0,0)",
                                "rgb(0,24,168)", "rgb(0,160,226)", "rgb(106,187,170)"])

    lines = alt.Chart(tubelines).mark_geoshape(
        filled=False,
        strokeWidth=2
    ).encode(
        alt.Color(
            'id:N',
            legend=alt.Legend(
                title=None,
                orient='bottom-right',
                offset=0
            ),
            scale=line_scale
        )
    )

    plot = background + labels + lines    
    return plot

def plot_mark_point():
    url = data.cars.url  # URL/path to json data
    # plot altair
    plot = alt.Chart(url).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q'
    )
    return plot

class DummyInput(BaseModel):
    pass

def hello_altair(input: DummyInput) -> AltairPlot:
    chart = plot_london_tube_lines()
    # export chart
    output = AltairPlot(data=chart)
    return output