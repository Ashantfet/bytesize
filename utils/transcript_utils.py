import whisper
import subprocess
import tempfile
import os


def _extract_audio(video_path):
    """
    Extract mono 16kHz WAV audio from a video using ffmpeg.
    This works even if the video has no explicit audio stream.
    """
    tmp_wav = tempfile.mktemp(suffix=".wav")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-acodec", "pcm_s16le",
        tmp_wav
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return tmp_wav


def transcribe_video(video_path, model_size="base"):
    """
    Transcribe a video file using OpenAI Whisper.
    Works for both CLI (main.py) and Streamlit (app.py).
    """
    print("🧠 Loading Whisper model...")
    model = whisper.load_model(model_size)

    print("🎧 Extracting audio for Whisper...")
    audio_path = _extract_audio(video_path)

    print("🎙️ Transcribing audio...")
    result = model.transcribe(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": float(seg["start"]),
            "end": float(seg["end"]),
            "text": seg["text"].strip()
        })

    # cleanup temporary audio file
    if os.path.exists(audio_path):
        os.remove(audio_path)

    return segments


def get_relevant_segments(
    segments,
    peak_times,
    window=15,
    min_words=6
):
    """
    Match transcript segments near loudness peaks.
    """
    selected_segments = []

    for peak in peak_times:
        best_segment = None

        for seg in segments:
            if abs(seg["start"] - peak) <= window:
                if len(seg["text"].split()) >= min_words:
                    best_segment = seg
                    break

        if best_segment:
            selected_segments.append(best_segment)

    return selected_segments
