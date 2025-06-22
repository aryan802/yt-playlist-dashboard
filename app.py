import streamlit as st
import pandas as pd
from datetime import timedelta
import yt_dlp

st.set_page_config(page_title="YouTube Playlist Analyzer", layout="wide")

st.title("🎬 YouTube Playlist Analyzer")

playlist_url = st.text_input("Enter YouTube Playlist URL:")

if playlist_url:
    with st.spinner("🔍 Fetching playlist data..."):
        ydl_opts = {
            'skip_download': True,
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
            'extract_flat': False,
            'dump_single_json': True,
            'user_agent': 'Mozilla/5.0',
            'geo_bypass': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(playlist_url, download=False)
        except Exception as e:
            st.error(f"Failed to fetch data: {e}")
            st.stop()

        entries = info.get('entries', [])
        playlist_title = info.get('title', 'Untitled Playlist')

        records = []
        for idx, video in enumerate(entries, 1):
            if not video:
                continue
            records.append({
                'Index': idx,
                'Title': video.get('title', '')[:60],
                'Duration (s)': video.get('duration') or 0,
                'Views': video.get('view_count') or 0,
                'Uploaded': video.get('upload_date') or "",
                'URL': video.get('webpage_url') or video.get('url'),
            })

        df = pd.DataFrame(records)
        df['Duration'] = df['Duration (s)'].apply(lambda s: str(timedelta(seconds=int(s))))
        total_dur = timedelta(seconds=int(df['Duration (s)'].sum()))
        avg_dur = timedelta(seconds=int(df['Duration (s)'].mean()))

        st.subheader(f"📃 {playlist_title}")
        col1, col2, col3 = st.columns(3)
        col1.metric("🎞️ Total Videos", len(df))
        col2.metric("🕒 Total Duration", str(total_dur))
        col3.metric("⏱️ Average Duration", str(avg_dur))

        st.markdown("### 📊 Playlist Details")
        st.dataframe(df[['Index', 'Title', 'Duration', 'Views', 'Uploaded', 'URL']], use_container_width=True)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, "playlist_summary.csv", "text/csv", key='download-csv')
