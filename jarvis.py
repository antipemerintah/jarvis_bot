"""
JARVIS ASSISTANT BOT
Bot asisten dengan voice recognition dan text-to-speech
"""

import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime

class Jarvis:
    def __init__(self, owner="Tuan Kian"):
        try:
            # Init microphone & recognizer
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 4000
            
            # Init text-to-speech
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            
            self.owner = owner
            self.running = True
            
            print("\n" + "="*60)
            print("🤖 JARVIS ASSISTANT BOT - SIAP DIGUNAKAN")
            print("="*60)
            print("💬 Katakan: 'Jarvis' untuk mulai")
            print("📋 Perintah: buka youtube, buka google, jam, tanggal, dll")
            print("="*60 + "\n")
            
        except Exception as e:
            print(f"❌ Error inisialisasi: {e}")
            exit(1)
    
    def speak(self, text):
        """Bot berbicara"""
        try:
            print(f"🤖 JARVIS: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"⚠️ Error bicara: {e}")
    
    def listen(self):
        """Dengarkan suara"""
        try:
            with sr.Microphone() as source:
                print("🎤 Mendengarkan...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
            
            # Convert ke text
            text = self.recognizer.recognize_google(audio, language='id-ID')
            print(f"👤 Anda: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            print("❌ Suara tidak jelas")
            return None
        except sr.RequestError as e:
            print(f"❌ Error: {e}")
            return None
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
            return None
    
    def open_website(self, url, name):
        """Buka website"""
        try:
            self.speak(f"Membuka {name}")
            webbrowser.open(url)
        except Exception as e:
            print(f"Gagal membuka: {e}")
    
    def execute_command(self, cmd):
        """Jalankan perintah"""
        if not cmd:
            return
        
        # YouTube
        if 'youtube' in cmd:
            self.open_website('https://www.youtube.com', 'YouTube')
        
        # Instagram
        elif 'instagram' in cmd:
            self.open_website('https://www.instagram.com', 'Instagram')
        
        # WhatsApp
        elif 'whatsapp' in cmd:
            self.open_website('https://web.whatsapp.com', 'WhatsApp')
        
        # Google
        elif 'google' in cmd:
            self.open_website('https://www.google.com', 'Google')
        
        # Chrome
        elif 'chrome' in cmd:
            try:
                subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                self.speak('Membuka Chrome')
            except:
                self.speak('Chrome tidak ditemukan')
        
        # Jam
        elif 'jam' in cmd or 'waktu' in cmd:
            waktu = datetime.now().strftime('%H:%M')
            self.speak(f'Waktu sekarang adalah {waktu}')
        
        # Tanggal
        elif 'tanggal' in cmd or 'hari' in cmd:
            tanggal = datetime.now().strftime('%d %B %Y')
            self.speak(f'Tanggal hari ini {tanggal}')
        
        # Siapa kamu
        elif 'siapa' in cmd:
            self.speak(f'Nama saya Jarvis, asisten pribadi {self.owner}')
        
        # Keluar
        elif 'keluar' in cmd or 'tutup' in cmd:
            self.speak(f'Sampai jumpa {self.owner}')
            self.running = False
        
        else:
            self.speak('Perintah tidak dimengerti')
    
    def run(self):
        """Jalankan bot"""
        while self.running:
            try:
                # Dengarkan kata kunci
                cmd = self.listen()
                
                if cmd and 'jarvis' in cmd:
                    self.speak(f'Baik, {self.owner}')
                    
                    # Dengarkan perintah
                    perintah = self.listen()
                    if perintah:
                        self.execute_command(perintah)
            
            except KeyboardInterrupt:
                print("\n\n👋 Bot dihentikan")
                self.speak('Selamat tinggal')
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")

# Jalankan bot
if __name__ == '__main__':
    bot = Jarvis(owner='Tuan Kian')
    bot.run()
