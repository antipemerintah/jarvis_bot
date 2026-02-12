import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
from datetime import datetime

class JarvisAssistant:
    def __init__(self, owner_name="Tuan Kian"):
        # Inisialisasi speech recognizer
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        
        # Inisialisasi text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Kecepatan bicara
        self.engine.setProperty('volume', 0.9)  # Volume
        
        # Nama pemilik
        self.owner_name = owner_name
        
        # Status aktif/tidak aktif
        self.is_active = False
        
        # Mapping perintah ke aksi
        self.commands = {
            'youtube': self.open_youtube,
            'instagram': self.open_instagram,
            'whatsapp': self.open_whatsapp,
            'google': self.open_google,
            'chrome': self.open_chrome,
            'jam': self.tell_time,
            'tanggal': self.tell_date,
            'siapa kamu': self.introduce_self,
            'bantuan': self.show_help,
            'keluar': self.exit_assistant,
            'tutup': self.exit_assistant,
        }
        
        print("\n" + "="*50)
        print("🤖 JARVIS ASSISTANT DIMULAI")
        print("="*50)
        print("💡 Katakan 'Jarvis' untuk mengaktifkan")
        print("="*50 + "\n")
    
    def speak(self, text):
        """Bot berbicara"""
        print(f"🤖 JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Mendengarkan perintah suara"""
        try:
            with sr.Microphone() as source:
                print("🎤 Mendengarkan...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5)
                
                # Mengubah suara menjadi teks
                command = self.recognizer.recognize_google(audio, language='id-ID')
                print(f"👤 Anda: {command}")
                return command.lower()
        
        except sr.UnknownValueError:
            print("❌ Tidak jelas, coba lagi")
            return None
        except sr.RequestError as e:
            print(f"❌ Error koneksi: {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def check_wake_word(self, command):
        """Cek apakah ada kata 'jarvis' di perintah"""
        if command and 'jarvis' in command:
            self.is_active = True
            self.speak(f"Baik, {self.owner_name}")
            return True
        return False
    
    def open_youtube(self):
        """Membuka YouTube"""
        self.speak("Membuka YouTube untuk Anda, Tuan")
        webbrowser.open("https://www.youtube.com")
    
    def open_instagram(self):
        """Membuka Instagram"""
        self.speak("Membuka Instagram")
        webbrowser.open("https://www.instagram.com")
    
    def open_whatsapp(self):
        """Membuka WhatsApp Web"""
        self.speak("Membuka WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    
    def open_google(self):
        """Membuka Google"""
        self.speak("Membuka Google")
        webbrowser.open("https://www.google.com")
    
    def open_chrome(self):
        """Membuka Google Chrome"""
        try:
            subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            self.speak("Membuka Chrome")
        except:
            self.speak("Chrome tidak ditemukan di komputer Anda")
    
    def tell_time(self):
        """Memberitahu waktu saat ini"""
        time_now = datetime.now().strftime("%H:%M")
        self.speak(f"Waktu sekarang adalah pukul {time_now}")
    
    def tell_date(self):
        """Memberitahu tanggal saat ini"""
        date_now = datetime.now().strftime("%d %B %Y")
        self.speak(f"Tanggal hari ini adalah {date_now}")
    
    def introduce_self(self):
        """Memperkenalkan diri"""
        self.speak(f"Nama saya adalah Jarvis. Saya adalah asisten pribadi Anda, {self.owner_name}")
    
    def show_help(self):
        """Menampilkan bantuan"""
        help_text = f"""
        📋 PERINTAH JARVIS:
        - "Buka YouTube" - Membuka YouTube
        - "Buka Instagram" - Membuka Instagram
        - "Buka WhatsApp" - Membuka WhatsApp
        - "Buka Google" - Membuka Google
        - "Buka Chrome" - Membuka Chrome
        - "Jam" atau "Berapa jam" - Menampilkan waktu
        - "Tanggal" - Menampilkan tanggal
        - "Siapa kamu" - Memperkenalkan diri
        - "Keluar" atau "Tutup" - Menutup Jarvis
        """
        print(help_text)
        self.speak("Sudah ditampilkan daftar perintah")
    
    def exit_assistant(self):
        """Menutup assistant"""
        self.speak(f"Baik, {self.owner_name}. Sampai jumpa! Terima kasih telah menggunakan saya")
        exit()
    
    def process_command(self, command):
        """Memproses perintah"""
        if not command:
            return
        
        # Cek setiap command
        for key, action in self.commands.items():
            if key in command:
                action()
                return
        
        # Jika command tidak dikenali
        self.speak("Maaf, Tuan. Saya tidak mengerti perintah itu. Katakan 'Bantuan' untuk melihat daftar perintah")
    
    def run(self):
        """Menjalankan assistant"""
        while True:
            try:
                command = self.listen()
                
                # Cek apakah ada kata 'jarvis'
                if self.check_wake_word(command):
                    # Mendengarkan perintah berikutnya
                    actual_command = self.listen()
                    if actual_command:
                        self.process_command(actual_command)
                    self.is_active = False
                
            except KeyboardInterrupt:
                print("\n\n👋 Jarvis dimatikan oleh pengguna")
                self.speak("Selamat tinggal, Tuan")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    # Buat instance Jarvis dengan nama pemilik
    jarvis = JarvisAssistant(owner_name="Tuan Kian")
    
    # Mulai running
    jarvis.run()
