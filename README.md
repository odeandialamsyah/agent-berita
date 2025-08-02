# 📰 News Agent dengan Google ADK

Agent cerdas yang dibangun menggunakan [Google Agent Development Kit (ADK)](https://ai.google.dev/) untuk **mengambil dan menampilkan berita terkini** berdasarkan hasil pencarian Google. Agent ini menampilkan **judul berita, URL asli, dan ringkasan isi (1000 karakter pertama)** langsung dari situs berita terpercaya.

---

## 🚀 Fitur Utama

- 🔎 Pencarian berita terkini menggunakan Google Search
- 📄 Menampilkan judul dan isi berita (tanpa LLM, langsung dari sumber asli)
- 🔗 Menyediakan URL berita asli, bukan hanya domain
- ⚙️ Dibangun dengan ADK dan model Gemini dari Google

---

## 📦 Prasyarat

Sebelum menjalankan agent ini, pastikan kamu telah menginstal pustaka berikut:

```bash
pip install google-adk requests 
pip install beautifulsoup4 
pip install googlesearch-python
```

---

## 📁 Struktur Folder

```
berita_agent/
├── agent.py
├── __init__.py
└── .env
```

---

## 🧠 Kemampuan Agent

Agent ini akan merespons kueri Anda dengan format JSON berikut:

```json
{
  "status": "success",
  "berita": [
    {
      "judul": "AI Bantu Diagnosa Kanker Lebih Cepat",
      "url": "https://www.kompas.com/tekno/read/2025/08/01/ai-diagnosa-kanker",
      "isi": "Para peneliti telah berhasil mengembangkan sistem AI baru yang dapat menganalisis hasil scan medis..."
    },
    ...
  ]
}
```

---

## ▶️ Menjalankan Agent

Setelah semua siap:

```bash
adk web
```

Buka browser ke [http://localhost:8000](http://localhost:8000) dan gunakan antarmuka chat untuk bertanya tentang berita terkini.

---

## 💬 Contoh Prompt

- `"Berita terbaru tentang kecerdasan buatan di Indonesia"`
- `"Apa yang terjadi di pasar kripto minggu ini?"`
- `"Kabar terkini teknologi ramah lingkungan"`

---

## 📝 Catatan

- Agent ini **tidak membuat ringkasan buatan** — isi berita diambil langsung dari sumber resmi.
- Hasil bisa bervariasi tergantung ketersediaan dan struktur situs berita.
- Cocok digunakan untuk: jurnalis, peneliti, pembuat aplikasi berita otomatis.

---

## 👨‍💻 Kontributor

Dikembangkan menggunakan Python dan [Google ADK](https://ai.google.dev/).  
Terinspirasi dari artikel Medium karya [Esther Irawati](https://medium.com/@esther.irawati/creating-an-agent-for-visual-learners-5af090219143)

---

## 📄 Lisensi

Lisensi MIT — silakan gunakan, modifikasi, dan bagikan kembali dengan mencantumkan atribusi.
