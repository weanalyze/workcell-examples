import streamlit as st
from streamlit_observable import observable

a = st.slider("Alex", value=30)
b = st.slider("Brian", value=20)
c = st.slider("Craig", value=50)

observable("Example Updatable Bar Chart", 
    notebook="@juba/updatable-bar-chart", 
    targets=["chart", "draw"], 
    redefine={
        "data": [
            {"name": "Alex", "value": a},
            {"name": "Brian", "value": b},
            {"name": "Craig", "value": c}
        ],
    },
    hide=["draw"]
)