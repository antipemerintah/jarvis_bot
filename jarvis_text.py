"""
JARVIS ASSISTANT BOT - TEXT VERSION
Bot asisten dengan text input (ideal untuk testing)
"""

import pyttsx3
import webbrowser
import subprocess
from datetime import datetime

class Jarvis:
    def __init__(self, owner="Tuan Kian"):
        try:
            # Init text-to-speech
            self.engine = pyttsx3.init()
            
            # Set properties untuk suara lebih natural
            self.engine.setProperty('rate', 130)  # Lebih lambat = lebih natural
            self.engine.setProperty('volume', 0.95)
            
            # Pilih voice terbaik (jika ada multiple voices)
            try:
                voices = self.engine.getProperty('voices')
                if len(voices) > 1:
                    # Prefer voice terakhir (biasanya lebih natural)
                    self.engine.setProperty('voice', voices[-1].id)
                    print(f"[VOICE] {voices[-1].name}")
            except:
                pass
            
            self.owner = owner
            self.running = True
            
            print("\n" + "="*60)
            print("[JARVIS] JARVIS ASSISTANT BOT - VERSI TEXT (NATURAL VOICE)")
            print("="*60)
            print("[INFO] Ketik: 'jarvis' kemudian perintah")
            print("[INFO] Website: youtube, instagram, google, whatsapp, facebook, tiktok, twitter, linkedin, github")
            print("[INFO] Aplikasi: chrome, edge, notepad, kalkulator, file")
            print("[INFO] Info: jam, tanggal, siapa, bantuan, keluar")
            print("="*60 + "\n")
            
        except Exception as e:
            print("[ERROR] Inisialisasi error: " + str(e))
            exit(1)
    
    def speak(self, text):
        """Bot berbicara"""
        try:
            print("[JARVIS] " + text)
            if self.engine is None:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)
                self.engine.setProperty('volume', 0.9)
            
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print("[ERROR] Bicara error: " + str(e))
            # Reinitialize engine jika error
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)
                self.engine.setProperty('volume', 0.9)
            except:
                pass
    
    def open_website(self, url, name):
        """Buka website"""
        try:
            self.speak("Membuka " + name)
            webbrowser.open(url)
        except Exception as e:
            print("Gagal membuka: " + str(e))
    
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
        elif 'whatsapp' in cmd or 'wa' in cmd:
            self.open_website('https://web.whatsapp.com', 'WhatsApp')
        
        # Google
        elif 'google' in cmd:
            self.open_website('https://www.google.com', 'Google')
        
        # Facebook
        elif 'facebook' in cmd or 'fb' in cmd:
            self.open_website('https://www.facebook.com', 'Facebook')
        
        # TikTok
        elif 'tiktok' in cmd or 'tik tok' in cmd:
            self.open_website('https://www.tiktok.com', 'TikTok')
        
        # Twitter
        elif 'twitter' in cmd or 'x.com' in cmd:
            self.open_website('https://www.twitter.com', 'Twitter')
        
        # LinkedIn
        elif 'linkedin' in cmd:
            self.open_website('https://www.linkedin.com', 'LinkedIn')
        
        # GitHub
        elif 'github' in cmd:
            self.open_website('https://www.github.com', 'GitHub')
        
        # Chrome
        elif 'chrome' in cmd:
            try:
                subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                self.speak('Membuka Chrome')
            except:
                self.speak('Chrome tidak ditemukan')
        
        # Edge
        elif 'edge' in cmd:
            try:
                subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
                self.speak('Membuka Edge')
            except:
                self.speak('Edge tidak ditemukan')
        
        # Notepad
        elif 'notepad' in cmd or 'catatan' in cmd:
            try:
                subprocess.Popen('notepad.exe')
                self.speak('Membuka Notepad')
            except:
                self.speak('Notepad tidak ditemukan')
        
        # Calculator
        elif 'kalkulator' in cmd or 'calc' in cmd:
            try:
                subprocess.Popen('calc.exe')
                self.speak('Membuka Kalkulator')
            except:
                self.speak('Kalkulator tidak ditemukan')
        
        # File Manager
        elif 'file' in cmd or 'explorer' in cmd or 'folder' in cmd:
            try:
                subprocess.Popen('explorer.exe')
                self.speak('Membuka File Manager')
            except:
                self.speak('File Manager tidak ditemukan')
        
        # Jam
        elif 'jam' in cmd or 'waktu' in cmd or 'berapa jam' in cmd:
            waktu = datetime.now().strftime('%H:%M')
            self.speak('Waktu sekarang adalah ' + waktu)
        
        # Tanggal
        elif 'tanggal' in cmd or 'hari' in cmd:
            tanggal = datetime.now().strftime('%d %B %Y')
            self.speak('Tanggal hari ini ' + tanggal)
        
        # Siapa kamu
        elif 'siapa' in cmd:
            self.speak('Nama saya Jarvis, asisten pribadi ' + self.owner)
        
        # Bantuan
        elif 'bantuan' in cmd or 'help' in cmd:
            bantuan = """
[BANTUAN] PERINTAH JARVIS - WEBSITE:
[CMD] - buka youtube    -> YouTube
[CMD] - buka instagram  -> Instagram
[CMD] - buka whatsapp   -> WhatsApp Web
[CMD] - buka google     -> Google Search
[CMD] - buka facebook   -> Facebook
[CMD] - buka tiktok     -> TikTok
[CMD] - buka twitter    -> Twitter
[CMD] - buka linkedin   -> LinkedIn
[CMD] - buka github     -> GitHub

[BANTUAN] PERINTAH JARVIS - APLIKASI:
[CMD] - buka chrome     -> Google Chrome
[CMD] - buka edge       -> Microsoft Edge
[CMD] - buka notepad    -> Notepad
[CMD] - buka kalkulator -> Calculator
[CMD] - buka file       -> File Manager

[BANTUAN] PERINTAH JARVIS - INFO:
[CMD] - jam/waktu       -> Lihat waktu sekarang
[CMD] - tanggal/hari    -> Lihat tanggal hari ini
[CMD] - siapa           -> Bot memperkenalkan diri
[CMD] - bantuan/help    -> Tampilkan bantuan (ini)
[CMD] - keluar/tutup    -> Tutup bot
"""
            print(bantuan)
            self.speak('Bantuan sudah ditampilkan')
        
        # Keluar
        elif 'keluar' in cmd or 'tutup' in cmd or 'exit' in cmd:
            self.speak('Sampai jumpa ' + self.owner)
            self.running = False
        
        else:
            self.speak('Perintah tidak dimengerti. Ketik bantuan untuk melihat daftar perintah')
    
    def run(self):
        """Jalankan bot"""
        while self.running:
            try:
                # Input dari user
                user_input = input("\n[INPUT] Anda: ").strip().lower()
                
                if not user_input:
                    continue
                
                # Cek apakah dimulai dengan 'jarvis'
                if user_input.startswith('jarvis'):
                    # Ambil perintah setelah 'jarvis'
                    perintah = user_input.replace('jarvis', '', 1).strip()
                    
                    if perintah:
                        self.speak('Baik, ' + self.owner)
                        self.execute_command(perintah)
                    else:
                        self.speak('Ada yang bisa saya bantu, ' + self.owner + '?')
                else:
                    self.speak('Ketik "jarvis" terlebih dahulu untuk mengaktifkan saya')
            
            except KeyboardInterrupt:
                print("\n\n[INFO] Bot dihentikan")
                self.speak('Selamat tinggal')
                break
            except Exception as e:
                print("[ERROR] " + str(e))

# Jalankan bot
if __name__ == '__main__':
    bot = Jarvis(owner='Tuan Kian')
    bot.run()
