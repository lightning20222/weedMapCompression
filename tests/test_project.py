"""
Unit tests for WeedIoT Project.

- Verifies mask-to-heatmap conversion (preprocessing.py)
- Checks aggregation of multiple heatmaps (aggregator.py)
- Tests drone simulation with optional packet loss (drone_sim.py)

Ensures all modules work correctly and produce expected shapes/values.
"""
"""
Run this file using the following command: 
pytest tests/      
"""

import os
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import mask_to_heatmap
from src.aggregator import aggregate_heatmaps
from src.drone_sim import simulate_drone

def test_heatmap_generation():
    mask_path = "data/cwfid/masks/003_mask.png"
    heatmap = mask_to_heatmap(mask_path, grid_size=20)
    assert heatmap.shape == (20, 20)
    assert (0 <= heatmap).all() and (heatmap <= 1).all()

def test_aggregation():
    h1 = np.ones((20,20))
    h2 = np.zeros((20,20))
    agg = aggregate_heatmaps([h1, h2])
    assert agg.shape == (20,20)
    assert np.allclose(agg, 0.5)

def test_drone_sim():
    mask_dir = "data/cwfid/masks/"
    paths = [os.path.join(mask_dir, f) for f in os.listdir(mask_dir) if f.endswith(".png")]
    outputs = simulate_drone(paths[:3], drop_prob=0.0) 
    assert len(outputs) == 3
