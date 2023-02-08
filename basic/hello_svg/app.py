import requests
from pydantic import BaseModel
from workcell.integrations.types import SVG


class DummyInput(BaseModel):
    pass

def show_svg(input: DummyInput) -> SVG:
    svg_url = "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg"
    svg = requests.get(svg_url).text
    output = SVG(data=svg)
    return output
