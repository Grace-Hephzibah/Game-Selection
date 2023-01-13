import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'>GAMING CATEGORIES</h1>", unsafe_allow_html=True)
st.write("---------------------")

games = ["Action", "Adventure", "Puzzle", "Studies", "Multiplayer", "Board",
         "Arcade", "Music", "Simulation", "Strategy", "Word"]

c1, c2, c3, c4 = st.columns([4,1,2,1])
with c1:
    game_choice = st.selectbox("Pick A Game Type", games)

with c2:
    st.write("")

with c3:
    image = Image.open("Asset/" + game_choice + ".png")
    st.image(image, width = 100, use_column_width="auto")

with c4:
    st.write("")

st.write("---------------------")

st.write("Repo Link: ")

text = "*By Jael Lois & Grace Hephzibah For @MLH_GHW_2023Jan - Finding And Using Libraries*"
style = '<p style="font-family: cursive; text-align: center;">' + text + '</p>'
st.markdown(text, unsafe_allow_html=True)