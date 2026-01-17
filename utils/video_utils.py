import os
from moviepy import (
    VideoFileClip,
    TextClip,
    CompositeVideoClip
)


# -------------------------------------------------
# Vertical conversion (Reels / Shorts / TikTok)
# -------------------------------------------------
def _convert_to_vertical(
    input_path,
    output_path,
    target_ratio=(9, 16),
    zoom=1.35
):
    """
    Convert horizontal video to vertical (9:16) with zoom.
    Optimized for Reels / TikTok / Shorts.
    MoviePy v2 compatible.
    """
    video = VideoFileClip(input_path)
    w, h = video.size

    # Step 1: center crop to 9:16 width
    target_w = int(h * target_ratio[0] / target_ratio[1])
    x_center = w // 2
    x1 = max(0, x_center - target_w // 2)
    x2 = min(w, x_center + target_w // 2)

    cropped = video.cropped(x1=x1, x2=x2)

    # Step 2: zoom in (crucial for reels)
    zoomed = cropped.resized(zoom)

    # Step 3: final crop to exact 9:16
    zw, zh = zoomed.size
    final_h = int(zw * target_ratio[1] / target_ratio[0])
    y_center = zh // 2
    y1 = max(0, y_center - final_h // 2)
    y2 = y1 + final_h

    final = zoomed.cropped(y1=y1, y2=y2)

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()


# -------------------------------------------------
# Karaoke-style captions (sentence-level)
# -------------------------------------------------
def _add_karaoke_captions(video_clip, local_segments):
    """
    Add sentence-level karaoke-style captions.
    Fully compatible with MoviePy v2.
    """
    caption_clips = []

    for seg in local_segments:
        caption = TextClip(
            text=seg["text"],
            font_size=42,
            color="white",
            method="caption",
            size=(int(video_clip.w * 0.9), None),
        )

        caption = (
            caption
            .with_start(seg["start"])
            .with_end(seg["end"])
            .with_position(("center", "bottom"))
        )

        caption_clips.append(caption)

    return CompositeVideoClip([video_clip] + caption_clips)



# -------------------------------------------------
# Main pipeline: reels + vertical + captions
# -------------------------------------------------
def generate_reels(
    video_path,
    segments,
    clip_duration=40,
    output_dir="output/clips"
):
    """
    Generates:
    - Horizontal reels (16:9)
    - Vertical reels (9:16, zoomed)
    - Vertical reels with karaoke-style captions

    Returns:
    List of dicts with paths.
    """
    os.makedirs(output_dir, exist_ok=True)

    video = VideoFileClip(video_path)
    results = []

    for idx, seg in enumerate(segments, 1):
        center_time = (seg["start"] + seg["end"]) / 2

        start_time = max(0, center_time - clip_duration / 2)
        end_time = min(video.duration, start_time + clip_duration)

        horizontal_path = os.path.join(output_dir, f"reel_{idx}.mp4")
        vertical_path = os.path.join(output_dir, f"reel_{idx}_vertical.mp4")
        captioned_path = os.path.join(
            output_dir, f"reel_{idx}_vertical_captioned.mp4"
        )

        # -------- Horizontal reel --------
        clip = video.subclipped(start_time, end_time)
        clip.write_videofile(
            horizontal_path,
            codec="libx264",
            audio_codec="aac"
        )

        # -------- Vertical reel --------
        _convert_to_vertical(horizontal_path, vertical_path)

        # -------- Karaoke captions --------
        vertical_clip = VideoFileClip(vertical_path)

        local_segments = []
        for s in segments:
            if start_time <= s["start"] <= end_time:
                local_segments.append({
                    "start": s["start"] - start_time,
                    "end": s["end"] - start_time,
                    "text": s["text"]
                })

        if local_segments:
            captioned = _add_karaoke_captions(
                vertical_clip,
                local_segments
            )
            captioned.write_videofile(
                captioned_path,
                codec="libx264",
                audio_codec="aac"
            )
        else:
            vertical_clip.write_videofile(
                captioned_path,
                codec="libx264",
                audio_codec="aac"
            )

        vertical_clip.close()

        results.append({
            "horizontal": horizontal_path,
            "vertical": vertical_path,
            "captioned": captioned_path
        })

    video.close()
    return results
