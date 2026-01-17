import os
from moviepy import VideoFileClip


def generate_reels(
    video_path,
    segments,
    clip_duration=40,
    output_dir="output/clips"
):
    """
    Generate short video reels around important transcript segments.
    Compatible with MoviePy v2+
    """
    os.makedirs(output_dir, exist_ok=True)

    video = VideoFileClip(video_path)
    reel_paths = []

    for idx, seg in enumerate(segments, 1):
        # Center the reel around the important segment
        center_time = (seg["start"] + seg["end"]) / 2

        start_time = max(0, center_time - clip_duration / 2)
        end_time = min(video.duration, start_time + clip_duration)

        output_path = os.path.join(output_dir, f"reel_{idx}.mp4")

        # ✅ MoviePy v2 method
        clip = video.subclipped(start_time, end_time)

        clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            verbose=False,
            logger=None
        )

        reel_paths.append(output_path)

    video.close()
    return reel_paths
