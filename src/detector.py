import cv2
import os
import threading
import time
from ultralytics import YOLO

class NgawasinDetector:
    def __init__(self, model_path='dataTRAINING.pt'):
        # LOAD MODEL YOLO RINGAN
        self.model = YOLO(model_path)
        
        # STATE DAN KONFIGURASI SISTEM
        self.is_running = False
        self.ai_enabled = True
        self.audio_enabled = True
        self.selected_sound = 'kaget.mp3'
        
        # STATE UNTUK ALARM AKTIF
        self.distraction_active = False
        self.is_playing = False
        
        # TIMER DAN WAKTU TUNGGU
        self.last_phone_alert_time = 0
        self.phone_alert_cooldown = 4.0
        
        # STATISTIK TOTAL PELANGGARAN HP
        self.stats_phone_count = 0
        
        # BATAS UPDATE TAMPILAN TERMINAL
        self.last_terminal_update = 0
        
        print(f"[INFO] NGAWASIN.AI: Model {model_path} Siap.")

    def play_alarm(self):
        try:
            import playsound
            sound_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), self.selected_sound)
            if os.path.exists(sound_path):
                playsound.playsound(sound_path, block=True)
        except Exception:
            pass
        finally:
            self.is_playing = False

    def render_terminal_dashboard(self):
        """GAMBAR DASHBOARD PADA TERMINAL"""
        # BERSIHKAN LAYAR TERMINAL UTAMA
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=========================================")
        print("        NGAWASIN.AI MONITOR HUD          ")
        print("=========================================")
        
        status = "DISTRAKSI! (HP TERDETEKSI)" if self.distraction_active else "NORMAL / FOKUS"
        print(f" Status Sistem    : {status}")
        print(f" Total Pelanggaran: {self.stats_phone_count} kali")
        
        print("=========================================")
        print(" Tekan [Q] pada jendela kamera untuk keluar.")

    def run_inference(self):
        self.is_running = True
        
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # BERSIHKAN TERMINAL PERTAMA KALI
        os.system('cls' if os.name == 'nt' else 'clear')
        
        while cap.isOpened() and self.is_running:
            ret, frame = cap.read()
            if not ret:
                break
                
            t_now = time.time()
            labels = []
            annotated_frame = frame.copy()
            
            if self.ai_enabled:
                results = self.model(frame, imgsz=320, conf=0.5, verbose=False, stream=True)
                for r in results:
                    annotated_frame = r.plot()
                    labels = [self.model.names[int(c)] for c in r.boxes.cls]

                    if 'phone' in labels:
                        self.distraction_active = True
                        
                        # TULIS TEKS PERINGATAN KAMERA
                        cv2.putText(annotated_frame, "!!! DISTRAKSI: HP !!!", (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        
                        # COOLDOWN DAN ALARM SUARA
                        if t_now - self.last_phone_alert_time > self.phone_alert_cooldown:
                            self.stats_phone_count += 1
                            self.last_phone_alert_time = t_now
                            
                            if self.audio_enabled and not self.is_playing:
                                self.is_playing = True
                                threading.Thread(target=self.play_alarm, daemon=True).start()
                    else:
                        self.distraction_active = False
            else:
                self.distraction_active = False

            # TAMPILAN WINDOW KAMERA
            cv2.imshow("NGAWASIN.AI - Live Monitor HUD", annotated_frame)
            
            # UPDATE TAMPILAN DASHBOARD BERKALA
            if t_now - self.last_terminal_update > 0.4 or self.distraction_active:
                self.render_terminal_dashboard()
                self.last_terminal_update = t_now
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        # BERSIHKAN SEMUA WINDOW KAMERA
        self.is_running = False
        cap.release()
        cv2.destroyAllWindows()