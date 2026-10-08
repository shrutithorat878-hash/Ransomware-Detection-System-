#!/usr/bin/env python3
# ============================================================
#  main.py — Entry Point: Ransomware Detection Tool
#  Final Year Project | Educational Purpose Only
# ============================================================
import os
import sys
import logging
import threading
import time
from datetime import datetime

# Fix Windows Unicode issue — force UTF-8 output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from config import LOG_PATH, LOG_DIR, DATA_DIR, MODEL_DIR
from core.database import init_db
from core.file_monitor import FileMonitor
from core.process_monitor import ProcessMonitor
from core.ml_engine import get_model_info
from ui.app import run_dashboard, broadcast_alert, set_monitors

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Logging Setup
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger("Main")


def alert_handler(alert: dict):
    sev = alert.get("severity", "INFO")
    msg = alert.get("message", "")
    color = {"CRITICAL": "bold red", "HIGH": "orange3", "MEDIUM": "yellow", "INFO": "cyan"}.get(sev, "white")
    console.print(f"[{color}][{sev}][/] {msg}")
    broadcast_alert(alert)


def print_banner():
    banner = Text()
    banner.append("  RansomShield v1.0\n", style="bold red")
    banner.append("  Final Year Project - Ransomware Detection Tool\n", style="dim")
    banner.append(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", style="dim")
    console.print(Panel(banner, border_style="red", padding=(0, 2)))


def main():
    print_banner()

    console.print("[cyan]*[/] Initialising database...")
    init_db()

    console.print("[cyan]*[/] Loading ML model...")
    info = get_model_info()
    console.print(f"   Model: {info['type']} | Estimators: {info['n_estimators']} | Contamination: {info['contamination']}")

    console.print("[cyan]*[/] Starting file monitor...")
    file_monitor = FileMonitor(alert_callback=alert_handler)
    file_monitor.start()

    console.print("[cyan]*[/] Starting process monitor...")
    process_monitor = ProcessMonitor(alert_callback=alert_handler)
    process_monitor.start()

    set_monitors(process_monitor)

    console.print("[cyan]*[/] Launching dashboard at http://127.0.0.1:5000")
    console.print("[green]OK[/] All systems running. Press Ctrl+C to stop.\n")

    try:
        run_dashboard()
    except KeyboardInterrupt:
        console.print("\n[yellow]Shutting down...[/]")
    finally:
        file_monitor.stop()
        process_monitor.stop()
        console.print("[green]OK[/] Clean shutdown complete.")


if __name__ == "__main__":
    main()
