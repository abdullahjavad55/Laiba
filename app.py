import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Valentine 🩷", page_icon="🩷", layout="centered")

# Page Title
st.markdown(
    "<h1 style='text-align:center; color:#ff2d55;'>Happy Valentine's Day 🩷</h1>",
    unsafe_allow_html=True
)

# Requested line
st.markdown(
    "<h2 style='text-align:center; color:#ff2d55;'>Happy Valentines day my Laiba🩷</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; font-size:18px;'>A little heart just for you 🥰</p>",
    unsafe_allow_html=True
)

# Heart curve
t = np.linspace(0, 2*np.pi, 2000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

fig, ax = plt.subplots(figsize=(7, 7))

# Main heart
ax.plot(x, y, color="red", linewidth=4)
ax.fill(x, y, color="red", alpha=0.65)

# Floating hearts
np.random.seed(7)
for _ in range(20):
    hx = np.random.uniform(-26, 26)
    hy = np.random.uniform(-18, 28)
    size = np.random.uniform(0.25, 0.75)

    tt = np.linspace(0, 2*np.pi, 400)
    xx = size * (16 * np.sin(tt)**3) + hx
    yy = size * (13 * np.cos(tt) - 5 * np.cos(2*tt) - 2 * np.cos(3*tt) - np.cos(4*tt)) + hy

    ax.fill(xx, yy, color="hotpink", alpha=0.30)

# Text INSIDE the plot
ax.text(
    0, -22,
    "Happy Valentines day my Laiba🩷",
    fontsize=18,
    ha="center",
    fontweight="bold",
    color="darkred"
)

ax.axis("equal")
ax.axis("off")

st.pyplot(fig)
