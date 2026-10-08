"""
╔══════════════════════════════════════════════════════════╗
║   RansomShield — Safe Attack Simulator                  ║
║   Final Year Project Demo Tool                          ║
║   ⚠ EDUCATIONAL PURPOSE ONLY — No real encryption      ║
╚══════════════════════════════════════════════════════════╝

This script simulates ransomware BEHAVIOR only:
  - Creates files with suspicious extensions
  - Modifies many files rapidly (mass change rate)
  - Spikes CPU usage
  - Does NOT actually encrypt or delete any real files
"""

import os, sys, time, threading, random, string

# ── Config ────────────────────────────────────────────────────
DEMO_FOLDER = os.path.join(os.path.expanduser("~"), "Documents", "RansomDemo")
EXTENSIONS  = [".locked", ".encrypted", ".enc", ".wcry", ".crypt"]

def banner():
    print("\n" + "="*55)
    print("  RansomShield — Safe Attack Simulator")
    print("  Final Year Project Demo")
    print("="*55)
    print("\n  This will simulate a ransomware attack safely.")
    print("  - Creates temp files in ~/Documents/RansomDemo/")
    print("  - Spikes CPU usage temporarily")
    print("  - All files deleted after demo")
    print("  - NO real files are touched\n")

def choose_attack():
    print("  Choose Attack Type:")
    print("  [1] Suspicious File Extension  (HIGH alert)")
    print("  [2] Mass File Change           (CRITICAL alert)")
    print("  [3] CPU Spike                  (MEDIUM alert)")
    print("  [4] Full Attack Demo           (ALL alerts)")
    print("  [0] Exit\n")
    return input("  Enter choice: ").strip()

# ── Attack 1: Suspicious Extension ───────────────────────────
def attack_extension():
    print("\n  [ATTACK 1] Creating suspicious extension files...")
    os.makedirs(DEMO_FOLDER, exist_ok=True)
    files = []
    for i, ext in enumerate(EXTENSIONS):
        path = os.path.join(DEMO_FOLDER, f"document_{i+1}{ext}")
        with open(path, "w") as f:
            f.write(f"This is a simulated encrypted file {i+1}\n" * 10)
        files.append(path)
        print(f"  Created: document_{i+1}{ext}")
        time.sleep(0.3)
    print("\n  Dashboard should show: HIGH alert — Suspicious Extension")
    print("  Check your browser at http://127.0.0.1:5000")
    input("\n  Press Enter to cleanup files...")
    for p in files:
        try: os.remove(p)
        except: pass
    print("  Files cleaned up!")

# ── Attack 2: Mass File Change ────────────────────────────────
def attack_mass_change():
    print("\n  [ATTACK 2] Simulating mass file change (ransomware speed)...")
    os.makedirs(DEMO_FOLDER, exist_ok=True)
    files = []
    print("  Creating 30 files rapidly...")
    for i in range(30):
        ext = random.choice(EXTENSIONS)
        path = os.path.join(DEMO_FOLDER, f"file_{i:03d}{ext}")
        with open(path, "w") as f:
            rnd = ''.join(random.choices(string.ascii_letters, k=200))
            f.write(rnd)
        files.append(path)
        if i % 5 == 0:
            print(f"  Files created: {i+1}/30")
        time.sleep(0.05)  # Very fast — like real ransomware

    print("\n  Dashboard should show: CRITICAL alert — Mass File Change!")
    print("  Check Live Alert Feed in browser!")
    input("\n  Press Enter to cleanup...")
    for p in files:
        try: os.remove(p)
        except: pass
    try: os.rmdir(DEMO_FOLDER)
    except: pass
    print("  Cleaned up!")

# ── Attack 3: CPU Spike ───────────────────────────────────────
def attack_cpu():
    print("\n  [ATTACK 3] Spiking CPU for 15 seconds...")
    print("  Watch CPU meter on dashboard go to 80-100%!")
    print("  Dashboard should show: MEDIUM alert — CPU Spike")
    stop_flag = threading.Event()

    def cpu_burn():
        while not stop_flag.is_set():
            # Burn CPU with math operations
            x = 0
            for i in range(100000):
                x += i * i

    # Start 4 threads to max CPU
    threads = [threading.Thread(target=cpu_burn, daemon=True) for _ in range(4)]
    for t in threads: t.start()

    for remaining in range(15, 0, -1):
        print(f"  CPU spike running... {remaining}s remaining", end="\r")
        time.sleep(1)

    stop_flag.set()
    print("\n  CPU spike stopped!")
    print("  Check dashboard for MEDIUM alert.")

# ── Attack 4: Full Demo ───────────────────────────────────────
def attack_full():
    print("\n  [FULL DEMO] Starting complete attack simulation...")
    print("  Keep dashboard open in browser!\n")
    time.sleep(1)

    print("  PHASE 1: Suspicious Extensions (5 files)...")
    os.makedirs(DEMO_FOLDER, exist_ok=True)
    phase1_files = []
    for i, ext in enumerate(EXTENSIONS):
        path = os.path.join(DEMO_FOLDER, f"target_doc_{i+1}{ext}")
        with open(path, "w") as f:
            f.write("Simulated encrypted content\n" * 20)
        phase1_files.append(path)
        print(f"  Created: target_doc_{i+1}{ext}")
        time.sleep(0.4)

    print("\n  Waiting 5 seconds — check HIGH alert on dashboard...")
    time.sleep(5)

    print("\n  PHASE 2: Mass File Change (30 files fast)...")
    phase2_files = []
    for i in range(30):
        ext = random.choice(EXTENSIONS)
        path = os.path.join(DEMO_FOLDER, f"bulk_{i:03d}{ext}")
        with open(path, "w") as f:
            f.write(''.join(random.choices(string.printable, k=500)))
        phase2_files.append(path)
        time.sleep(0.04)
    print("  30 files created rapidly!")
    print("  Check CRITICAL alert — Mass File Change!")

    print("\n  Waiting 5 seconds...")
    time.sleep(5)

    print("\n  PHASE 3: CPU Spike (10 seconds)...")
    stop_flag = threading.Event()
    def burn():
        while not stop_flag.is_set():
            x = sum(i*i for i in range(50000))
    threads = [threading.Thread(target=burn, daemon=True) for _ in range(4)]
    for t in threads: t.start()
    for i in range(10, 0, -1):
        print(f"  CPU burning... {i}s", end="\r")
        time.sleep(1)
    stop_flag.set()
    print("\n  CPU spike done!")

    print("\n  DEMO COMPLETE! Check dashboard:")
    print("  - Live Alert Feed: Multiple alerts")
    print("  - Detection History: New entries")
    print("  - Stats cards updated")

    input("\n  Press Enter to cleanup all demo files...")
    for p in phase1_files + phase2_files:
        try: os.remove(p)
        except: pass
    try: os.rmdir(DEMO_FOLDER)
    except: pass
    print("  All demo files cleaned up! System is safe.")

# ── Main ──────────────────────────────────────────────────────
def main():
    banner()
    while True:
        choice = choose_attack()
        if   choice == "1": attack_extension()
        elif choice == "2": attack_mass_change()
        elif choice == "3": attack_cpu()
        elif choice == "4": attack_full()
        elif choice == "0":
            print("\n  Exiting simulator. Goodbye!\n")
            break
        else:
            print("  Invalid choice!")
        print("\n" + "-"*55)

if __name__ == "__main__":
    main()