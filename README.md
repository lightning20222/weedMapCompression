# 🌱 WeedIoT-Project: Drone Data Compression & Aggregation Pipeline

This project implements an **efficient data pipeline for Precision Agriculture**.  
Its core feature is the **significant data compression** of drone-captured weed masks into small heatmaps for efficient transfer, followed by robust **ensemble aggregation** for farm-wide weed density mapping.

## End-to-End Pipeline
```bash
AI → Compression → Transmission → Aggregation → Visualization
```

---

## 🚀 Getting Started

Follow these steps to set up the environment and run the Streamlit visualization dashboard.

### 1. Setup Environment
```bash
# Clone the repository 
git clone https://github.com/lightning20222/weedMapCompression.git
cd weedMapCompression

# Setup Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (requires requirements.txt)
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
streamlit run src/app/streamlit_app.py
```

---

## 📁 Project Structure

```bash
weedMapCompression/
│
├── data/
│   └── cwfid/              # Sample images + masks
│
├── src/
│   ├── preprocessing.py    # Converts mask → weed heatmap (20x20)
│   ├── drone_sim.py        # Simulates drones + packet loss
│   ├── aggregator.py       # Combines drone data into farm-wide map
│   └── app/
│       └── streamlit_app.py # Visualization dashboard
│
├── results/
│   └── screenshots/        # Screenshots for report/slides
│
└── README.md               # Project explanation
```

And the pipeline block:

```bash
pipeline:
AI → Compression → Transmission → Aggregation → Visualization.
```

---

## 🧪 Dataset Source (CWFID)

The data samples are sourced from the **CWFID (Crop/Weed Field Image Dataset)**.  
CWFID provides high-quality field images and corresponding segmentation masks used for crop/weed discrimination in precision agriculture tasks.

- 📂 Dataset Link: [CWFID Dataset](https://github.com/cwfid/dataset)

---

## ▶️ Quick Run

```bash
git clone https://github.com/lightning20222/weedMapCompression.git
cd weedMapCompression
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app/streamlit.py
```

