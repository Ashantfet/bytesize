from moviepy import VideoFileClip

from utils.audio_utils import extract_loudness_peaks
from utils.transcript_utils import transcribe_video, get_relevant_segments
from utils.video_utils import generate_reels

VIDEO_PATH = "input/test_video.mp4"


def main():
    # =========================
    # Phase 1: Video Load Check
    # =========================
    print("🔍 Loading video...")
    clip = VideoFileClip(VIDEO_PATH)
    print("✅ Video loaded successfully")
    print("Duration:", clip.duration)
    print("Resolution:", clip.size)
    clip.close()

    # =========================
    # Phase 2: Audio Loudness Peaks
    # =========================
    print("\n🔥 Detecting loudness peaks...")
    peaks = extract_loudness_peaks(VIDEO_PATH, top_k=5)

    print("🔥 Loudness peaks (seconds):")
    for t in peaks:
        print(f" - {t:.2f}s")

    # =========================
    # Phase 3: Transcription + Fusion
    # =========================
    print("\n🧠 Transcribing video with Whisper...")
    segments = transcribe_video(VIDEO_PATH, model_size="base")

    print("🔗 Matching transcript segments with loudness peaks...")
    important_segments = get_relevant_segments(
        segments,
        peaks,
        window=15,
        min_words=6
    )

    print("\n✨ High-value moments identified:")
    if not important_segments:
        print("⚠️ No suitable moments found. Exiting.")
        return

    for i, seg in enumerate(important_segments, 1):
        print(
            f"{i}. [{seg['start']:.2f}s - {seg['end']:.2f}s] "
            f"{seg['text']}"
        )

    # =========================
    # Phase 4: Reel Generation
    # =========================
    print("\n🎬 Generating reels...")
    reels = generate_reels(
        VIDEO_PATH,
        important_segments,
        clip_duration=40
    )

    print("\n✅ Reels generated successfully:")
    for r in reels:
        print(" -", r)


if __name__ == "__main__":
    main()
