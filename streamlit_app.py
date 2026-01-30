import streamlit as st

st.set_page_config(layout="wide")

st.title("Toluene Photolysis Virtual Lab")

st.markdown("""
Interactive visualization of UV254-induced toluene photolysis.
""")

st.components.v1.iframe(
    "https://toulensim-octzi7yi.manus.space",
    height=900,
    scrolling=True
)
