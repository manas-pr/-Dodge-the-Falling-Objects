import streamlit as st
import subprocess

st.title("Pygame Web Integration")

st.write("Click the button below to start the game.")

if st.button("Start Game"):
    subprocess.Popen(["python", "game.py"])
