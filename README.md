# 🤖 JARVIS ASSISTANT BOT

Bot suara AI yang bisa mendengarkan perintah dan melakukan aksi di PC Anda.

## 📋 Fitur Utama

- 🎤 Mendengarkan perintah suara
- 🗣️ Respons bicara yang natural
- 🌐 Membuka website (YouTube, Instagram, Google, WhatsApp)
- ⏰ Memberitahu waktu dan tanggal
- 🎯 Memahami perintah dalam Bahasa Indonesia

## 🎯 Cara Kerja

1. **Dengarkan "Jarvis"** - Program akan mendengarkan kata `"jarvis"`
2. **Bot Merespons** - Jarvis akan berkata `"Baik, Tuan Kian"`
3. **Tunggu Perintah** - Setelah itu jelaskan perintah Anda
4. **Eksekusi** - Bot akan melakukan aksi sesuai perintah

## 📝 Contoh Penggunaan

```
Anda: "Jarvis"
Bot: "Baik, Tuan Kian"
Anda: "Buka YouTube"
Bot: "Membuka YouTube untuk Anda, Tuan" → YouTube dibuka di browser
```

## 🛠️ Instalasi

### 1. Install Python (jika belum ada)
- Download dari https://www.python.org/downloads/
- Pastikan centang ☑️ "Add Python to PATH"

### 2. Install Dependencies
Buka Command Prompt atau PowerShell di folder `tes ai bot`, lalu ketik:

```bash
pip install -r requirements.txt
```

### 3. Install PyAudio (Windows)
Jika ada error di PyAudio, install manual:

```bash
pip install pipwin
pipwin install pyaudio
```

## 🚀 Menjalankan Bot

Ketik di PowerShell/Command Prompt:

```bash
python jarvis_assistant.py
```

Atau double-click file `jarvis_assistant.py`

## 🎤 Perintah yang Tersedia

| Perintah | Aksi |
|----------|------|
| "Jarvis, buka YouTube" | Membuka YouTube |
| "Jarvis, buka Instagram" | Membuka Instagram |
| "Jarvis, buka WhatsApp" | Membuka WhatsApp Web |
| "Jarvis, buka Google" | Membuka Google |
| "Jarvis, buka Chrome" | Membuka Google Chrome |
| "Jarvis, jam" | Memberitahu waktu |
| "Jarvis, tanggal" | Memberitahu tanggal |
| "Jarvis, siapa kamu" | Menjawab identitas |
| "Jarvis, bantuan" | Menampilkan bantuan |
| "Jarvis, keluar" | Menutup Bot |

## 🔧 Kustomisasi

Edit di bagian ini untuk mengganti nama:

```python
jarvis = JarvisAssistant(owner_name="Tuan Kian")
```

Ganti `"Tuan Kian"` dengan nama Anda sendiri.

## ⚠️ Troubleshooting

### Masalah: "No module named 'speech_recognition'"
**Solusi:** 
```bash
pip install SpeechRecognition
```

### Masalah: Error PyAudio
**Solusi Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

### Masalah: Microphone tidak terdeteksi
- Periksa microphone di Settings → Sound
- Test microphone di Control Panel

### Masalah: Bot tidak mengerti suara
- Berbicara lebih jelas
- Kurangi suara sekitar
- Cek volume microphone

## 📦 File Structure

```
tes ai bot/
├── jarvis_assistant.py    ← File utama bot
├── requirements.txt       ← Daftar dependencies
└── README.md             ← File ini
```

## 💡 Tips

1. **Koneksi Internet** - Pastikan online (untuk speech recognition)
2. **Microphone** - Gunakan microphone berkualitas untuk input yang lebih baik
3. **Background Noise** - Jalankan di tempat yang tenang
4. **Bahasa Indonesia** - Bot dioptimalkan untuk Bahasa Indonesia

## 🎓 Versi Berikutnya

Fitur yang bisa ditambahkan:
- ✨ Membuka aplikasi lokal (.exe)
- ✨ Weather information
- ✨ E-mail integration
- ✨ Reminder & alarm
- ✨ Multiple language support

---

**Dibuat dengan ❤️ untuk Tuan Kian**
