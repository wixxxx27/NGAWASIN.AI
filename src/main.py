import argparse
import sys
import platform
from .detector import NgawasinDetector

def main():
    parser = argparse.ArgumentParser(description="NGAWASIN.AI Student Monitoring")
    subparsers = parser.add_subparsers(dest="command")

    # Command terminal
    subparsers.add_parser("start", help="Jalankan deteksi & dashboard terminal")
    subparsers.add_parser("status", help="Cek status sistem & fitur")

    args = parser.parse_args()

    if args.command == "start":
        detector = NgawasinDetector()
        try:
            detector.run_inference()
        except KeyboardInterrupt:
            print("\n[INFO] Sistem dihentikan.")
            detector.is_running = False
    elif args.command == "status":
        print("\n================== NGAWASIN.AI ==================")
        print("Status           : Ready")
        print(f"Platform         : {platform.system()} {platform.release()}")
        print("Core Engine      : YOLOv8 Object Detection")
        print("Display HUD      : Cyber HUD Live Overlay")
        print("=================================================\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


