import streamlit as st
import os
import tempfile

from utils.audio_utils import extract_loudness_peaks
from utils.transcript_utils import transcribe_video, get_relevant_segments
from utils.video_utils import generate_reels


# -------------------------------------------------
# Streamlit page config
# -------------------------------------------------
st.set_page_config(
    page_title="ByteSize – Automatic Reel Generator",
    layout="centered"
)

st.title("🎬 ByteSize – Automatic Reel Generator")
st.markdown(
    """
    Upload a **long-form video** (lecture, interview, podcast) and automatically
    generate **high-impact short reels** using **multimodal AI**:
    
    - 🔊 Audio loudness (emotion / emphasis)
    - 🧠 Speech understanding (Whisper)
    - 🎥 Automatic reel generation
    - 📱 Reels/TikTok-ready vertical videos
    - 📝 Karaoke-style captions
    """
)

# -------------------------------------------------
# Video upload
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a video file",
    type=["mp4", "mov", "mkv"]
)

if uploaded_file:
    with tempfile.TemporaryDirectory() as tmpdir:
        video_path = os.path.join(tmpdir, uploaded_file.name)

        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("✅ Video uploaded successfully!")

        if st.button("🚀 Generate Reels"):
            with st.spinner("Processing video (this may take a few minutes)..."):

                # -------------------------------------------------
                # Phase 1: Audio loudness
                # -------------------------------------------------
                st.write("🔊 Detecting loudness peaks...")
                peaks = extract_loudness_peaks(video_path, top_k=5)

                # -------------------------------------------------
                # Phase 2: Transcription
                # -------------------------------------------------
                st.write("🧠 Transcribing video with Whisper...")
                segments = transcribe_video(video_path, model_size="base")

                # -------------------------------------------------
                # Phase 3: Multimodal fusion
                # -------------------------------------------------
                st.write("🔗 Matching loudness with meaningful speech...")
                important_segments = get_relevant_segments(
                    segments,
                    peaks,
                    window=15,
                    min_words=6
                )

                if not important_segments:
                    st.warning("⚠️ No high-value moments detected.")
                else:
                    # -------------------------------------------------
                    # Phase 4: Reel generation
                    # -------------------------------------------------
                    st.write("🎬 Generating reels...")
                    reels = generate_reels(
                        video_path,
                        important_segments,
                        clip_duration=40,
                        output_dir="output/clips"
                    )

                    st.success("🎉 Reels generated successfully!")

                    # -------------------------------------------------
                    # Display results
                    # -------------------------------------------------
                    st.subheader("📂 Generated Reels")

                    for i, reel in enumerate(reels, 1):
                        st.markdown(f"## Reel {i}")

                        st.markdown("### 🎥 Horizontal (16:9)")
                        st.video(reel["horizontal"])

                        st.markdown("### 📱 Vertical (9:16)")
                        st.video(reel["vertical"])

                        st.markdown("### 📝 Vertical with Karaoke Captions")
                        st.video(reel["captioned"])
