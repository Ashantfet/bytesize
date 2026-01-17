import whisper


def transcribe_video(video_path, model_size="base"):
    """
    Transcribe a video file using OpenAI Whisper.

    Args:
        video_path (str): Path to input video
        model_size (str): Whisper model size ("tiny", "base", "small", "medium")

    Returns:
        List of dicts with keys: start, end, text
    """
    print("🧠 Loading Whisper model...")
    model = whisper.load_model(model_size)

    print("🎙️ Transcribing audio...")
    result = model.transcribe(video_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": float(seg["start"]),
            "end": float(seg["end"]),
            "text": seg["text"].strip()
        })

    return segments


def get_relevant_segments(
    segments,
    peak_times,
    window=15,
    min_words=6
):
    """
    Match transcript segments near loudness peaks.

    Args:
        segments (list): Output of transcribe_video
        peak_times (list): Loudness peak timestamps (seconds)
        window (int): Time window around peak (± seconds)
        min_words (int): Minimum words to keep a segment

    Returns:
        List of selected transcript segments
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
