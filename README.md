# 🚀 ByteSize – Automatic Viral Reel Generator

**Mastering the Attention Economy with Multimodal AI**

ByteSize is a **multimodal AI pipeline** that automatically extracts **high-impact, reel-worthy moments** from long-form videos (lectures, podcasts, interviews) and converts them into **short viral clips**.

This project was built as part of the **ByteSize Sage AI Hackathon** and focuses on **engineering clarity, multimodal reasoning, and real video outputs**.

---

## 🎯 Problem We Solve

Long-form videos contain valuable insights, but:

* Viewers consume content in **30–60 second bursts**
* Manually finding highlights is **time-consuming**
* High-value moments often remain **hidden**

**ByteSize automatically finds and extracts these moments.**

---

## 🧠 Core Idea (Multimodal Intelligence)

We combine **two complementary signals**:

1. **Audio Energy (How it’s said)**
   → Detects excitement, emphasis, emotional peaks
2. **Speech Content (What is said)**
   → Filters meaningful, advice-driven moments

By **fusing audio + text**, ByteSize finds moments that are both:

* Energetic 🔥
* Meaningful 🧠

---

## 🧩 System Architecture

```
Long Video
   │
   ├── Audio Extraction (ffmpeg)
   │     └── Loudness Peaks (Librosa RMS)
   │
   ├── Speech-to-Text (Whisper)
   │     └── Timestamped Transcripts
   │
   ├── Multimodal Fusion
   │     └── Match Loud Moments with Meaningful Speech
   │
   └── Reel Generation (MoviePy)
         └── 3–5 Short MP4 Clips
```

---

## ⚙️ Tech Stack

* **Python 3**
* **ffmpeg** – audio extraction
* **Librosa** – audio loudness analysis
* **OpenAI Whisper** – speech-to-text with timestamps
* **MoviePy** – video cutting & export

---

## 🧪 How It Works (Step-by-Step)

### Phase 1: Video Validation

Ensures the video loads correctly and extracts metadata.

### Phase 2: Audio Loudness Peak Detection

* Computes RMS energy over time
* Selects top **distinct loudness peaks**
* These represent **emotional / emphasized moments**

### Phase 3: Transcript Understanding

* Transcribes full video using Whisper
* Keeps timestamps for every spoken segment
* Filters out filler speech

### Phase 4: Multimodal Fusion

* Aligns transcript segments near loudness peaks
* Keeps only **meaningful sentences**
* Produces final timestamps for reels

### Phase 5: Reel Generation

* Cuts **30–45 second clips**
* Exports **3–5 MP4 reels** automatically

---

## ▶️ How to Run

### 1️⃣ Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Ensure `ffmpeg` is installed:

```bash
ffmpeg -version
```

---

### 2️⃣ Add Input Video

Place your test video at:

```
input/test_video.mp4
```

---

### 3️⃣ Run the Pipeline

```bash
python main.py
```

---

### 4️⃣ Output

Generated reels will appear in:

```
output/clips/
 ├── reel_1.mp4
 ├── reel_2.mp4
 ├── reel_3.mp4
 ├── reel_4.mp4
 └── reel_5.mp4
```

---

## 🎥 Demo Video

📌 **A full screen-recording demo is included showing the pipeline running end-to-end and generating reels.**
(Required by hackathon submission guidelines.)

---

## 💡 Why This Project Stands Out

* ✅ **True multimodal reasoning** (audio + text)
* ✅ Handles **real long-form videos**
* ✅ Produces **actual shareable MP4 outputs**
* ✅ Clean, explainable engineering decisions
* ✅ Scales to longer videos easily

This is **not a toy demo** — it reflects how real content-intelligence systems are built.

---

## 🚧 Limitations & Future Work

* Smart vertical cropping (face tracking) – *optional extension*
* Dynamic captions & hooks – *optional extension*
* Sentiment scoring / emotion classification
* GPU acceleration for faster transcription

---

## 🏁 Conclusion

**ByteSize** turns a single long video into a **week’s worth of short-form content**, making education and insights more accessible, engaging, and shareable.

This project demonstrates how **multimodal AI can directly solve real creator problems** with clean engineering and practical outputs.

---

### 👤 Author

**Ashant Kumar** 
ByteSize Sage AI Hackathon


