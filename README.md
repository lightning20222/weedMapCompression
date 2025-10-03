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
streamlit run src/app/streamlit.py
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
Images of the running app

<img width="1920" height="1080" alt="1" src="https://github.com/user-attachments/assets/e6de3f30-6d06-4f5b-bc07-53174a344045" />

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/853ada0b-8493-4fdd-befb-516f2da5bbc3" />

<img width="1920" height="1080" alt="3" src="https://github.com/user-attachments/assets/14e79590-dd25-42e2-8cf2-d3d4aaa1b2b1" />

<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/48868b1b-d732-49e7-ad4d-0df12fb923e1" />

<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/2436a670-053c-4e52-a1a1-e5af3b0ab2dc" />

<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/353c70ef-cc9a-4d9f-af6b-52a1d847670f" />

<img width="1920" height="1080" alt="7" src="https://github.com/user-attachments/assets/71de5841-3698-4544-b17c-9ac1256f117d" />

<img width="1920" height="1080" alt="8" src="https://github.com/user-attachments/assets/2c00c1f5-77df-4474-825a-1c51b7cc344b" />

<img width="1920" height="1080" alt="9" src="https://github.com/user-attachments/assets/2b9f8718-5937-4dd0-b1b5-f61b1c09054a" />

<img width="1920" height="1080" alt="10" src="https://github.com/user-attachments/assets/bb32c1b2-9168-499f-b9fe-8f2b0c3c0a38" />
