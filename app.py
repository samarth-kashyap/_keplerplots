import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Example data
np.random.seed(42)
x = np.random.rand(100) * 100
y = np.random.rand(100) * 100
z1 = np.random.rand(100) * 50
z2 = np.random.rand(100) * 100
z3 = np.random.rand(100) * 200

# Sidebar controls
st.sidebar.header("Scatter Plot Controls")

x_scale = st.sidebar.selectbox("X-axis scale", ["linear", "log"])
y_scale = st.sidebar.selectbox("Y-axis scale", ["linear", "log"])

size_var = st.sidebar.selectbox("Marker size based on", ["None", "z1", "z2", "z3"])
color_var = st.sidebar.selectbox("Color based on", ["None", "z1", "z2", "z3"])

# Map selected variable
size_data = None
color_data = None

if size_var != "None":
    size_data = locals()[size_var]
    size_data = (size_data - size_data.min() + 1) * 10  # Scale for visibility

if color_var != "None":
    color_data = locals()[color_var]

# Plotting
fig, ax = plt.subplots()

scatter = ax.scatter(x, y, 
                     s=size_data if size_data is not None else 50, 
                     c=color_data if color_data is not None else 'blue', 
                     cmap='viridis', alpha=0.7, edgecolor='k')

ax.set_xscale(x_scale)
ax.set_yscale(y_scale)
ax.set_xlabel("X")
ax.set_ylabel("Y")

if color_data is not None:
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label(color_var)

st.pyplot(fig)

