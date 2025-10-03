import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys, os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)
IMAGE_DIR = os.path.join(PROJECT_ROOT, "data", "cwfid", "images")
MASK_DIR  = os.path.join(PROJECT_ROOT, "data", "cwfid", "masks")

from src.preprocessing import mask_to_heatmap
from src.aggregator import aggregate_heatmaps


st.title("🌱 WeedIoT Simulator - Precision Farming")

image_dir = IMAGE_DIR
mask_dir = MASK_DIR


image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(".png")])
mask_files  = sorted([f for f in os.listdir(mask_dir) if f.endswith(".png")])

if not image_files or not mask_files:
    st.error("No images/masks found in data/cwfid/.")
else:
    selected = st.selectbox("Choose an image:", image_files)

    # Match mask (assumes same numeric ID in filename: 005_image.png <-> 005_mask.png)
    mask_file = selected.replace("image", "mask")
    mask_path = os.path.join(mask_dir, mask_file)
    image_path = os.path.join(image_dir, selected)

    # Load
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    st.subheader("1. Original Image")
    st.image(image, caption=selected, use_container_width=True)

    st.subheader("2. Ground Truth Weed Mask")
    st.image(mask, caption=mask_file, channels="GRAY")

    # Generate compressed heatmap
    heatmap = mask_to_heatmap(mask_path, grid_size=20)

    st.subheader("3. Compressed Weed Density Heatmap")
    fig, ax = plt.subplots()
    cax = ax.matshow(heatmap, cmap="Greens")
    fig.colorbar(cax)
    st.pyplot(fig)

    # Transmission metrics
    original_size = os.path.getsize(image_path)
    compressed_size = heatmap.nbytes
    bandwidth_saved = (1 - compressed_size / original_size) * 100

    st.subheader("4. Transmission Metrics")
    st.write(f"Original image size: {original_size/1024:.2f} KB")
    st.write(f"Compressed heatmap size: {compressed_size/1024:.2f} KB")
    st.write(f"Bandwidth saved: {bandwidth_saved:.1f}%")
