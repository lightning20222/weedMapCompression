# src/drone_sim.py
import os
import random
from src.preprocessing import mask_to_heatmap

def simulate_drone(mask_paths, drop_prob=0.2):
    """
    Simulate a drone generating weed heatmaps and transmitting them.
    Some packets are dropped to simulate network loss.
    """
    transmitted = []
    for path in mask_paths:
        heatmap = mask_to_heatmap(path)
        if random.random() > drop_prob:  # successful transmission
            transmitted.append(heatmap)
        else:
            print(f"Packet dropped for {os.path.basename(path)}")
    return transmitted
