# 🛡 RansomShield — Ransomware Detection System
**Final Year Project | Educational Purpose Only**

---

## 📁 Project Structure

```
ransomware_detector/
├── main.py                  ← Entry point (run this)
├── config.py                ← All settings & thresholds
├── requirements.txt         ← Python dependencies
│
├── core/
│   ├── database.py          ← SQLite storage layer
│   ├── file_monitor.py      ← Watchdog-based file system monitor
│   ├── process_monitor.py   ← psutil CPU/RAM/process monitor
│   └── ml_engine.py         ← IsolationForest anomaly detection
│
├── ui/
│   ├── app.py               ← Flask + SocketIO dashboard backend
│   └── templates/
│       └── dashboard.html   ← Web dashboard (real-time)
│
├── data/
│   └── detections.db        ← SQLite DB (auto-created)
├── logs/
│   └── detector.log         ← Log file (auto-created)
└── models/
    └── isolation_forest.pkl ← ML model (auto-created)
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.9+
- pip

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Watch Directories
Edit `config.py` and update:
```python
WATCH_DIRECTORIES = [
    "C:/Users/YourName/Documents",   # Windows example
    "/home/yourname/Documents",      # Linux example
]
```

### 5. Run the Tool
```bash
python main.py
```

### 6. Open Dashboard
Visit: **http://127.0.0.1:5000**

---

## 🔍 What It Detects

| Detection Type         | Method          | Severity |
|------------------------|-----------------|----------|
| Suspicious file extensions (.locked, .encrypted, etc.) | Rule-based | HIGH |
| High entropy files (likely encrypted) | Shannon Entropy | HIGH |
| Mass file changes (bulk modification) | Rate analysis | CRITICAL |
| CPU / RAM spikes       | psutil thresholds | MEDIUM |
| Suspicious process names | Keyword match | HIGH |
| Behavioral anomalies   | IsolationForest ML | CRITICAL |

---

## ⚡ Detection Thresholds (config.py)

| Setting | Default | Description |
|---------|---------|-------------|
| `FILE_CHANGE_RATE_THRESHOLD` | 10 | Files changed/sec before alert |
| `CPU_SPIKE_THRESHOLD` | 85% | CPU above this → flag |
| `MEMORY_SPIKE_THRESHOLD` | 90% | RAM above this → flag |
| `ENTROPY_THRESHOLD` | 7.2 | Shannon entropy (max 8.0) |
| `ANOMALY_CONTAMINATION` | 0.05 | 5% anomaly rate for ML model |

---

## 🧪 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.9+ |
| File Monitoring | watchdog |
| System Monitoring | psutil |
| ML / Anomaly Detection | scikit-learn (IsolationForest) |
| Web Dashboard | Flask + Flask-SocketIO |
| Real-Time Updates | Socket.IO (WebSocket) |
| Database | SQLite (built-in) |
| Model Persistence | joblib |
| CLI Output | rich |

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard UI |
| `/api/stats` | GET | Summary statistics |
| `/api/detections` | GET | Detection history |
| `/api/snapshots` | GET | System metric history |
| `/api/live` | GET | Real-time CPU/RAM/ML status |
| `/api/model` | GET | ML model info |
| `/api/kill/<pid>` | POST | Terminate a process |

---

## 📝 Notes
- This tool is for **educational and research purposes only**
- Tested on Windows 10/11, Ubuntu 20.04+, macOS 12+
- The ML model auto-bootstraps with synthetic normal data on first run
- All detections are stored in `data/detections.db`
