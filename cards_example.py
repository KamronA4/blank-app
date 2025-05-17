
import streamlit as st

st.title("Playground")
st.write(
    '''
    
    This is a sample app that demonstrates the use of 
    various card components using different libraries. 
    
    This is so that we have an idea of how they look and feel for future use.
'''
)

st.info('This is a purely informational message', icon="ℹ️")

from streamlit_card import card

hasClicked = card(
    title="Streamlit Card",
    text="This is a test card",
    image="https://placekitten.com/500/500",
    styles={
        "card": {
            "width": "100%",
            "height": "300px"
        }
    }
)

from streamlit_extras.card import card

clicked = card(
    title="Hello World!",
    text="Some description",
    image="http://placekitten.com/200/300",
    on_click=lambda: print("Clicked!")
)

from streamlit_elements import elements, mui, html
import streamlit as st

with elements("card_example"):
    with mui.Card(sx={"display": "flex", "flexDirection": "column", "height": 300}):
        mui.CardHeader(title="My Card")
        with mui.CardContent(sx={"flex": 1}):
            html.div("Card Content")
        with mui.CardActions():
            mui.Button("Action 1")
            mui.Button("Action 2")
