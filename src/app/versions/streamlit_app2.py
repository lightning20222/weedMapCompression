# src/app/streamlit_app.py

'''
run with 

source venv/bin/activate
streamlit run src/app/streamlit.py
'''
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys
import time

# -----------------------------
# 1️⃣ Project root and imports
# -----------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(PROJECT_ROOT)

from src.preprocessing import mask_to_heatmap
from src.aggregator import aggregate_heatmaps
from src.drone_sim import simulate_drone

# -----------------------------
# 2️⃣ Paths to cwfid dataset
# -----------------------------
IMAGE_DIR = os.path.join(PROJECT_ROOT, "data", "cwfid", "images")
MASK_DIR  = os.path.join(PROJECT_ROOT, "data", "cwfid", "masks")

image_files = sorted([f for f in os.listdir(IMAGE_DIR) if f.endswith(".png")])
mask_files  = sorted([f for f in os.listdir(MASK_DIR) if f.endswith(".png")])

st.title("🌱 WeedIoT Simulator - Precision Farming (cwfid)")

if not image_files or not mask_files:
    st.error("No images/masks found in data/cwfid/.")
else:
    # -----------------------------
    # 3️⃣ Image selection
    # -----------------------------
    selected = st.selectbox("Choose an image:", image_files)

    # Load image and mask
    image_path = os.path.join(IMAGE_DIR, selected)
    mask_file = selected.replace("image", "mask")
    mask_path = os.path.join(MASK_DIR, mask_file)

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    st.subheader("1. Original Image")
    st.image(image, caption=selected, use_container_width=True)

    st.subheader("2. Ground Truth Weed Mask")
    st.image(mask, caption=mask_file, channels="GRAY")

    # -----------------------------
    # 4️⃣ Multi-drone simulation (cwfid)
    # -----------------------------
    st.subheader("3. Drone Data Transmission Simulation")

    col_a, col_b = st.columns(2)
    with col_a:
        num_rows = st.slider("Drone rows", min_value=1, max_value=4, value=2)
    with col_b:
        num_cols = st.slider("Drone columns", min_value=1, max_value=5, value=3)
    
    num_drones = num_rows * num_cols
    drop_prob = st.slider("Packet loss probability", min_value=0.0, max_value=0.5, value=0.0, step=0.05)

    # Each drone sends the same cwfid mask for demo
    drone_masks = [mask_path] * num_drones
    drone_heatmaps = simulate_drone(drone_masks, drop_prob=drop_prob)

    # -----------------------------
    # 5️⃣ Visualize packet traveling
    # -----------------------------
    st.markdown("**Data packets traveling from drones to base station:**")

    # Create placeholder for animation
    animation_placeholder = st.empty()

    # Arrange drones in a grid
    drone_positions = []
    for row in range(num_rows):
        for col in range(num_cols):
            x = col * 1.5 + 1
            y = row * 1.5 + 1
            drone_positions.append((x, y))
    
    # Base station at the center-right
    base_position = (num_cols * 1.5 + 2, (num_rows * 1.5) / 2 + 0.5)

    # Animate packets
    for step in np.linspace(0, 1, 10):
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Set dynamic limits based on grid size
        ax.set_xlim(-0.5, num_cols * 1.5 + 3)
        ax.set_ylim(-0.5, num_rows * 1.5 + 1.5)
        ax.axis('off')

        # Plot drones in grid
        for i, pos in enumerate(drone_positions):
            ax.scatter(*pos, s=300, c='blue', zorder=3, marker='^', edgecolors='black', linewidths=2)
            ax.text(pos[0], pos[1]-0.3, f"D{i+1}", ha='center', fontsize=8, weight='bold')

        # Plot base station
        ax.scatter(*base_position, s=500, c='red', zorder=3, marker='s', edgecolors='black', linewidths=2)
        ax.text(base_position[0], base_position[1]+0.4, "Base Station", ha='center', fontsize=10, weight='bold')

        # Plot packets traveling
        for i, pos in enumerate(drone_positions):
            if i < len(drone_heatmaps) and drone_heatmaps[i] is not None:
                x = pos[0] + step * (base_position[0] - pos[0])
                y = pos[1] + step * (base_position[1] - pos[1])
                ax.plot([pos[0], x], [pos[1], y], c='green', linewidth=2, zorder=2, alpha=0.6)
                ax.scatter(x, y, s=80, c='limegreen', zorder=4, edgecolors='darkgreen', linewidths=1)
            else:
                # Show dropped packet with X
                ax.scatter(pos[0], pos[1], s=200, c='red', marker='x', zorder=4, linewidths=3)
                ax.text(pos[0], pos[1]-0.5, "Dropped", ha='center', fontsize=7, color='red', style='italic')
        
        # Add grid lines for field visualization
        for row in range(num_rows + 1):
            ax.axhline(y=row*1.5 + 0.25, color='lightgray', linestyle='--', linewidth=0.5, alpha=0.3)
        for col in range(num_cols + 1):
            ax.axvline(x=col*1.5 + 0.25, color='lightgray', linestyle='--', linewidth=0.5, alpha=0.3)

        animation_placeholder.pyplot(fig)
        plt.close(fig)
        time.sleep(0.1)

    # -----------------------------
    # 6️⃣ Aggregate drone data
    # -----------------------------
    st.subheader("4. Aggregated Farm-wide Weed Heatmap (cwfid)")

    valid_heatmaps = [h for h in drone_heatmaps if h is not None]
    
    if valid_heatmaps:
        farm_heatmap = aggregate_heatmaps(valid_heatmaps)

        fig2, ax2 = plt.subplots(figsize=(8, 6))
        cax = ax2.matshow(farm_heatmap, cmap="Greens")
        ax2.set_title("Average Weed Density Across All Drones", pad=20)
        fig2.colorbar(cax, label="Weed Density (0-1)")
        st.pyplot(fig2)
        plt.close(fig2)

        # -----------------------------
        # 7️⃣ Transmission metrics
        # -----------------------------
        original_size = os.path.getsize(image_path) * num_drones
        compressed_size = sum([h.nbytes for h in valid_heatmaps])
        bandwidth_saved = (1 - compressed_size / original_size) * 100
        packets_received = len(valid_heatmaps)
        packets_sent = num_drones

        st.subheader("5. Transmission Metrics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Packets Sent", packets_sent)
            st.metric("Packets Received", packets_received)
        
        with col2:
            st.metric("Original Size (all drones)", f"{original_size/1024:.2f} KB")
            st.metric("Compressed Size", f"{compressed_size/1024:.2f} KB")
        
        with col3:
            st.metric("Bandwidth Saved", f"{bandwidth_saved:.1f}%")
            success_rate = (packets_received / packets_sent) * 100
            st.metric("Success Rate", f"{success_rate:.1f}%")
    else:
        st.error("All packets were dropped! Try reducing the packet loss probability.")