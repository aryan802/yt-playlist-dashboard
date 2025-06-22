# 🎬 YouTube Playlist Analyzer Dashboard

An interactive web app to analyze YouTube playlists — shows total duration, views, upload dates, and lets you download a summary as CSV.

### 🚀 Features
- Enter any YouTube playlist URL
- See playlist title, total/average duration
- Interactive video table with duration, views, upload date, URL
- Export summary to CSV

### 🔧 Built With
- Python 🐍
- [Streamlit](https://streamlit.io/) for the dashboard
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for playlist data
- pandas for data processing

---

### ▶️ Run Locally

```bash
git clone https://github.com/aryan802/youtube-playlist-analyzer-dashboard.git
cd youtube-playlist-analyzer-dashboard
pip install -r requirements.txt
streamlit run app.py
