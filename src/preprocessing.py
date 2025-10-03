# src/preprocessing.py
import cv2
import numpy as np
import os

def mask_to_heatmap(mask_path, grid_size=20):
    """
    Convert a binary weed mask into a weed density heatmap.
    mask_path: path to mask (grayscale, weeds=255, background=0)
    """
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if mask is None:
        raise FileNotFoundError(f"Mask not found: {mask_path}")

    H, W = mask.shape
    cell_h, cell_w = H // grid_size, W // grid_size
    heatmap = np.zeros((grid_size, grid_size))

    for i in range(grid_size):
        for j in range(grid_size):
            y0, y1 = i*cell_h, (i+1)*cell_h
            x0, x1 = j*cell_w, (j+1)*cell_w
            patch = mask[y0:y1, x0:x1]
            heatmap[i, j] = 1.0 - (patch.mean() / 255.0)  # weed density 0–1

    return heatmap
