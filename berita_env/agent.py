from google.adk.agents import Agent
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def scrape_text_from_url(url: str) -> tuple:
    """
    Mengambil judul dan isi dari halaman berita.
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ambil semua teks <p> sebagai isi berita
        paragraphs = soup.find_all('p')
        isi_berita = " ".join(p.get_text() for p in paragraphs).strip()

        # Ambil judul dari tag <title>
        title_tag = soup.find('title')
        judul = title_tag.get_text(strip=True) if title_tag else url

        return judul, isi_berita
    except Exception as e:
        print(f"[ERROR] Gagal mengambil data dari: {url}\n{e}")
        return None, ""

def search_latest_news(query: str) -> dict:
    """
    Melakukan pencarian berita di Google dan menampilkan judul, URL, dan isi awal.
    """
    try:
        print(f"[INFO] Mencari berita untuk: '{query}'")
        urls = list(search(query, num_results=5, lang="id"))
        if not urls:
            return {"status": "error", "error_message": "Tidak ada hasil ditemukan."}

        berita_list = []
        for url in urls[:3]:  # ambil hanya 3 teratas
            judul, isi = scrape_text_from_url(url)
            if isi:
                berita_list.append({
                    "judul": judul,
                    "url": url,
                    "isi": isi[:1000]  # ambil 1000 karakter pertama
                })

        if not berita_list:
            return {"status": "error", "error_message": "Tidak ada isi berita yang bisa diambil."}

        return {"status": "success", "berita": berita_list}

    except Exception as e:
        return {"status": "error", "error_message": f"Terjadi kesalahan saat pencarian: {e}"}

# Agent untuk integrasi sistem
root_agent = Agent(
    name="berita_terbaru_agent",
    model="gemini-2.0-flash",
    description="Agent untuk menampilkan berita terkini dari Google Search dengan judul, URL, dan isi 1000 karakter pertama.",
    instruction="Cari berita dari Google, lalu tampilkan judul, URL, dan isi awal beritanya.",
    tools=[search_latest_news],
)
