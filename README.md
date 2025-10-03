```bash
WeedIoT-Project/
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


```bash
pipeline:
AI → Compression → Transmission → Aggregation → Visualization.
```


## If you want to run this project:

```bash 
git clone <repo>
cd WeedIoT-Project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app/streamlit_app.py
```
