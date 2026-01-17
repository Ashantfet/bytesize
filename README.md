# 🎬 ByteSize – Automatic Reel Generator with Multimodal AI

**Turn long videos into viral-ready short clips automatically.**

ByteSize is a **multimodal AI system** that analyzes long-form videos (lectures, podcasts, interviews) and automatically extracts **high-impact moments**, converts them into **platform-ready vertical reels**, and overlays **karaoke-style captions** — all with **zero manual editing**.

This project was built for a hackathon to demonstrate **real-world multimodal reasoning, engineering robustness, and creator-focused AI**.

---

## 🚀 What Problem Does ByteSize Solve?

Long videos contain valuable insights, but:

* Viewers prefer **30–60 second short-form content**
* Manually finding highlights is **slow and subjective**
* Reformatting for **Reels / Shorts / TikTok** is tedious
* Adding captions takes time

**ByteSize automates the entire pipeline.**

---

## 🧠 Core Idea (Why This Is Multimodal)

ByteSize fuses **two complementary signals**:

### 🔊 Audio Intelligence (How it’s said)

* Detects **loudness / emphasis peaks**
* Captures excitement, stress, or importance

### 🧠 Language Understanding (What is said)

* Uses **OpenAI Whisper** to transcribe speech
* Keeps **word-level timestamps**
* Filters out filler speech

### 🔗 Multimodal Fusion

Only moments that are:

* **Energetic** (audio peak)
* **Meaningful** (spoken content)

are selected as highlights.

---

## 🧩 System Architecture

```
Long Video
   │
   ├── Audio Extraction (ffmpeg)
   │     └── Loudness Peaks (Librosa)
   │
   ├── Speech-to-Text (Whisper)
   │     └── Timestamped Segments
   │
   ├── Multimodal Fusion
   │     └── High-Value Moments
   │
   ├── Reel Generation (MoviePy)
   │     ├── Horizontal Clips (16:9)
   │     ├── Vertical Clips (9:16, zoomed)
   │     └── Karaoke-Style Captions
   │
   └── Streamlit UI (Demo)
```

---

## ✨ Key Features

* ✅ Automatic highlight detection
* ✅ Audio + text multimodal reasoning
* ✅ Horizontal reels (16:9)
* ✅ **Vertical reels optimized for Shorts / Reels / TikTok**
* ✅ **Adaptive zoom & reframing**
* ✅ **Karaoke-style timed captions**
* ✅ CLI pipeline + interactive UI

---

## ⚙️ Tech Stack

* **Python 3**
* **ffmpeg** – audio & video processing
* **Librosa** – audio loudness analysis
* **OpenAI Whisper** – speech-to-text with timestamps
* **MoviePy v2** – video editing & caption overlays
* **Streamlit** – interactive demo UI

---

## ▶️ How to Run (CLI Pipeline)

### 1️⃣ Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Ensure ffmpeg is installed:

```bash
ffmpeg -version
```

---

### 2️⃣ Add Input Video

Place a long video at:

```
input/test_video.mp4
```

---

### 3️⃣ Run

```bash
python main.py
```

---

### 4️⃣ Output

```
output/clips/
├── reel_1.mp4
├── reel_1_vertical.mp4
├── reel_1_vertical_captioned.mp4
├── reel_2_vertical_captioned.mp4
├── ...
```

These files are **directly uploadable** to:

* Instagram Reels
* YouTube Shorts
* TikTok

---

## 🖥️ How to Run (Streamlit Demo UI)

```bash
streamlit run app.py
```

### What the UI shows:

* Upload video
* Automatic processing
* Horizontal reel
* Vertical reel
* Captioned vertical reel

This is **judge-friendly and demo-ready**.

---

## 📝 Karaoke-Style Captions (Optional Feature)

* Captions are generated automatically
* Timed using Whisper timestamps
* Sentence-level “karaoke” effect
* High-contrast text for engagement

> No manual transcription or editing required.

---

## 🧠 Why This Project Stands Out

* ✅ Real multimodal reasoning (not a toy demo)
* ✅ Handles real long videos
* ✅ Produces real MP4 outputs
* ✅ Platform-native formatting
* ✅ Robust engineering (API changes, edge cases handled)
* ✅ Clear separation: backend pipeline + UI

---

## 🚧 Limitations & Future Work

* Face-aware smart cropping (MediaPipe)
* Word-level karaoke highlighting
* Auto hook text at top
* Background blur instead of crop
* GPU acceleration

---

## 🏁 Conclusion

**ByteSize** turns one long video into **multiple viral-ready short clips**, saving creators hours of manual work.

It demonstrates how **multimodal AI can directly solve real creator problems** with practical, production-style engineering.

---

## 👤 Author

**Ashant Kumar**
Hackathon Submission – ByteSize

---
