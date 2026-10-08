# ============================================================
#  config.py — Central Configuration
# ============================================================
import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
MODEL_DIR = os.path.join(BASE_DIR, "models")
DB_PATH = os.path.join(DATA_DIR, "detections.db")
LOG_PATH = os.path.join(LOG_DIR, "detector.log")

# --- Directories to Monitor ---
# Change these to target folders you want to watch
WATCH_DIRECTORIES = [
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Downloads"),
]

# --- Ransomware Known Extensions ---
RANSOMWARE_EXTENSIONS = {
    ".locked", ".enc", ".encrypted", ".crypto", ".crypt",
    ".locky", ".zepto", ".cerber", ".zzz", ".vault",
    ".petya", ".wcry", ".wncry", ".wncryt", ".sage",
    ".globe", ".dharma", ".adobe", ".java", ".STOP",
    ".djvu", ".pony", ".ransom", ".pays", ".helpme",
}

# --- Detection Thresholds ---
FILE_CHANGE_RATE_THRESHOLD = 10        # files changed per second → alert
CPU_SPIKE_THRESHOLD = 85.0             # CPU % above this → flag
MEMORY_SPIKE_THRESHOLD = 90.0         # RAM % above this → flag
ENTROPY_THRESHOLD = 7.2               # file entropy above this → suspicious
MONITOR_INTERVAL = 1.0                # seconds between checks

# --- Anomaly Detection ---
ANOMALY_CONTAMINATION = 0.05          # 5% expected anomalies (IsolationForest)

# --- Flask Dashboard ---
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
FLASK_DEBUG = False
SECRET_KEY = "ransomware-detector-fyp-2024"
