"""
JARVIS ASSISTANT BOT - VERSI WINDOWS TTS (Alternative)
Menggunakan Windows Speech API (lebih stable)
"""

import webbrowser
import subprocess
from datetime import datetime

try:
    from comtypes.client import CreateObject
    WINDOWS_SPEECH = True
except:
    WINDOWS_SPEECH = False
    print("[WARNING] Windows Speech API tidak tersedia")

class Jarvis:
    def __init__(self, owner="Tuan Kian"):
        self.owner = owner
        self.running = True
        
        if WINDOWS_SPEECH:
            try:
                self.tts = CreateObject("SAPI.SpVoice")
                
                # Dapatkan semua voice yang tersedia
                voices = self.tts.GetVoices()
                voice_list = []
                for i in range(voices.Count):
                    voice = voices.Item(i)
                    voice_list.append(voice)
                    print(f"[VOICE {i}] {voice.GetAttribute('Name')}")
                
                # Pilih voice terbaik (prefer female/natural voices)
                # Coba gunakan voice terakhir atau female voice
                if len(voice_list) > 1:
                    # Prefer voice selain default
                    preferred_voice = voice_list[-1]
                else:
                    preferred_voice = voice_list[0]
                
                self.tts.Voice = preferred_voice
                
                # Set properties untuk suara lebih natural
                self.tts.Rate = -2  # Slower speech (lebih natural)
                self.tts.Volume = 100
                
                print(f"[OK] Voice: {preferred_voice.GetAttribute('Name')}")
                self.speak_method = "windows"
            except Exception as e:
                print(f"[WARNING] Error setup voice: {e}")
                self.speak_method = "print_only"
        else:
            self.speak_method = "print_only"
        
        print("\n" + "="*60)
        print("[JARVIS] JARVIS ASSISTANT BOT - WINDOWS TTS")
        print("="*60)
        print(f"[INFO] Mode: {self.speak_method}")
        print("[INFO] Ketik: 'jarvis' kemudian perintah")
        print("[INFO] Website: youtube, instagram, google, whatsapp, facebook, tiktok, twitter")
        print("[INFO] Aplikasi: chrome, edge, notepad, kalkulator, file")
        print("[INFO] Info: jam, tanggal, siapa, bantuan, keluar")
        print("="*60 + "\n")
    
    def speak(self, text):
        """Bot berbicara menggunakan Windows Speech"""
        try:
            print("[JARVIS] " + text)
            
            if self.speak_method == "windows":
                self.tts.Speak(text, 1)
            
        except Exception as e:
            print("[ERROR] Speak error: " + str(e))
    
    def open_website(self, url, name):
        """Buka website"""
        try:
            self.speak("Membuka " + name)
            webbrowser.open(url)
        except Exception as e:
            print("[ERROR] Gagal membuka: " + str(e))
    
    def execute_command(self, cmd):
        """Jalankan perintah"""
        if not cmd:
            return
        
        # Website
        if 'youtube' in cmd:
            self.open_website('https://www.youtube.com', 'YouTube')
        elif 'instagram' in cmd:
            self.open_website('https://www.instagram.com', 'Instagram')
        elif 'whatsapp' in cmd or 'wa' in cmd:
            self.open_website('https://web.whatsapp.com', 'WhatsApp')
        elif 'google' in cmd:
            self.open_website('https://www.google.com', 'Google')
        elif 'facebook' in cmd or 'fb' in cmd:
            self.open_website('https://www.facebook.com', 'Facebook')
        elif 'tiktok' in cmd:
            self.open_website('https://www.tiktok.com', 'TikTok')
        elif 'twitter' in cmd:
            self.open_website('https://www.twitter.com', 'Twitter')
        elif 'linkedin' in cmd:
            self.open_website('https://www.linkedin.com', 'LinkedIn')
        elif 'github' in cmd:
            self.open_website('https://www.github.com', 'GitHub')
        
        # Aplikasi
        elif 'chrome' in cmd:
            try:
                subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                self.speak('Membuka Chrome')
            except:
                self.speak('Chrome tidak ditemukan')
        elif 'edge' in cmd:
            try:
                subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
                self.speak('Membuka Edge')
            except:
                self.speak('Edge tidak ditemukan')
        elif 'notepad' in cmd or 'catatan' in cmd:
            try:
                subprocess.Popen('notepad.exe')
                self.speak('Membuka Notepad')
            except:
                self.speak('Notepad tidak ditemukan')
        elif 'kalkulator' in cmd or 'calc' in cmd:
            try:
                subprocess.Popen('calc.exe')
                self.speak('Membuka Kalkulator')
            except:
                self.speak('Kalkulator tidak ditemukan')
        elif 'file' in cmd or 'explorer' in cmd or 'folder' in cmd:
            try:
                subprocess.Popen('explorer.exe')
                self.speak('Membuka File Manager')
            except:
                self.speak('File Manager tidak ditemukan')
        
        # Info
        elif 'jam' in cmd or 'waktu' in cmd:
            waktu = datetime.now().strftime('%H:%M')
            self.speak('Waktu sekarang adalah ' + waktu)
        elif 'tanggal' in cmd or 'hari' in cmd:
            tanggal = datetime.now().strftime('%d %B %Y')
            self.speak('Tanggal hari ini ' + tanggal)
        elif 'siapa' in cmd:
            self.speak('Nama saya Jarvis, asisten pribadi ' + self.owner)
        elif 'bantuan' in cmd or 'help' in cmd:
            bantuan = """
[BANTUAN] PERINTAH JARVIS:
[WEBSITE] youtube, instagram, whatsapp, google, facebook, tiktok, twitter, linkedin, github
[APLIKASI] chrome, edge, notepad, kalkulator, file
[INFO] jam, tanggal, siapa, bantuan, keluar
"""
            print(bantuan)
            self.speak('Bantuan ditampilkan')
        elif 'keluar' in cmd or 'tutup' in cmd or 'exit' in cmd:
            self.speak('Sampai jumpa ' + self.owner)
            self.running = False
        else:
            self.speak('Perintah tidak dimengerti')
    
    def run(self):
        """Jalankan bot"""
        while self.running:
            try:
                user_input = input("\n[INPUT] Anda: ").strip().lower()
                
                if not user_input:
                    continue
                
                if user_input.startswith('jarvis'):
                    perintah = user_input.replace('jarvis', '', 1).strip()
                    
                    if perintah:
                        self.speak('Baik, ' + self.owner)
                        self.execute_command(perintah)
                    else:
                        self.speak('Ada yang bisa saya bantu, ' + self.owner + '?')
                else:
                    self.speak('Ketik "jarvis" terlebih dahulu')
            
            except KeyboardInterrupt:
                print("\n[INFO] Bot dihentikan")
                self.speak('Selamat tinggal')
                break
            except Exception as e:
                print("[ERROR] " + str(e))

if __name__ == '__main__':
    bot = Jarvis(owner='Tuan Kian')
    bot.run()
