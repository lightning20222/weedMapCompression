# src/aggregator.py
import numpy as np

def aggregate_heatmaps(list_of_heatmaps):
    """Average multiple drone heatmaps into one farm-wide map."""
    if not list_of_heatmaps:
        return None
    return np.mean(np.stack(list_of_heatmaps, axis=0), axis=0)
