# 🌾 Drone-Based Weed Density Analysis: Data Compression & Aggregation

This document outlines the efficient method for processing drone-captured weed mask images to generate a robust, farm-wide weed density map.  
The core strategy involves significant **data compression** at the drone level, followed by **ensemble averaging** at the server to enhance reliability.

---

## 1. Motivation: Efficiency Through Compression

The raw data is a **full mask image (512×512 pixels)**, representing 262,144 data points per drone.  
Transmitting this full image is inefficient, wasting bandwidth and slowing real-time analysis.

**Goal:** Compress this information by focusing only on the weed density, achieving a massive data reduction while retaining the essential field information.

---

## 2. Heatmap Generation (Data Compression)

Each drone transforms its $512 \times 512$ mask into a small **$20 \times 20$ heatmap**, reducing the data from 262,144 values to just 400 values — a **99.85% reduction**.

### Compression Steps

1. **Grid Split:** The $512 \times 512$ mask is divided into a $20 \times 20$ grid, creating 400 cells.  
2. **Density Calculation:** In each cell, the average weed pixel intensity (weed pixel count ÷ total pixel count) is computed.  
3. **Normalization:** The cell average is normalized between 0 (no weeds) and 1 (full weeds).  

**Formula for Heatmap Cell $(i, j)$:**

$$
\text{heatmap}[i,j] \;=\; \frac{1}{255} \cdot \frac{1}{|C_{i,j}|} 
\sum_{(y,x) \in C_{i,j}} \text{mask}[y,x]
$$

- $C_{i,j}$ = set of pixels inside cell $(i, j)$  
- $|C_{i,j}|$ = number of pixels in that cell  

**Analogy:** Like taking a high-resolution satellite photo and dividing the farmland into a **$20 \times 20$ chessboard**, then calculating and sending only *“how green (weedy) is each square?”*

---

## 3. Aggregation Across Drones (Noise Reduction)

Each drone sends its $20 \times 20$ density map to the central server.  
The final farm-wide map is created using **ensemble averaging**.

**Process:** We average the heatmaps from all $N$ drones that viewed a section of the field.

**Formula for Farm Heatmap:**

$$
\text{farm\_heatmap} \;=\; \frac{1}{N} \sum_{k=1}^{N} \text{heatmap}_k
$$

- $N$ = number of drones  
- $\text{heatmap}_k$ = map from drone $k$  

**Benefit:** Averaging multiple drones’ maps reduces noise, minimizes the impact of packet loss, and ensures the final farm-wide map is **more robust and reliable** — similar to averaging repeated measurements in science experiments.

---

## 4. How to Explain Verbally

- “Each drone compresses its mask into a simple $20 \times 20$ density map — like reducing a high-resolution image into a low-resolution summary.”  
- “This is efficient because we only care about density of weeds, not the exact pixel values.”  
- “When we combine multiple drones, we average their heatmaps. This ensures the final farm-wide map is more robust, just like averaging multiple measurements in an experiment to reduce error.”  

---

## 5. Analogy for Professor

- **Heatmap generation:** Like taking a satellite photo and dividing farmland into a chessboard, then asking *“how green is each square?”*  
- **Aggregation:** Like having multiple satellites look at the same field and then averaging their answers to get the most reliable picture.  
