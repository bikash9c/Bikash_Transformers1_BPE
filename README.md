# 🪶 Bengali BPE Tokenizer

A custom **Byte Pair Encoding (BPE)** tokenizer trained on a **2 MB Bengali corpus**, designed for tokenizing and decoding Bengali text at a **byte level**.  
Built completely from scratch in **Python**, featuring a **reversible encoder–decoder**, **sample Bengali text suggestions**, and a **round-trip validation** interface — deployed on **Hugging Face Spaces**.

---

## 🚀 Project Overview

This project demonstrates how to build a **byte-level BPE tokenizer (like GPT-2’s)** from scratch — trained specifically on Bengali UTF-8 text.  
It provides a **fully reversible tokenizer**, a **compact 5010-token vocabulary**, and a **visual Gradio web app** for testing and verification.

---

## 🧩 Key Features

- 🔤 **Byte-level BPE** — learns merges directly on UTF-8 bytes for full Bengali script coverage.  
- 🔁 **Fully reversible encode/decode** — perfect reconstruction for clean text.  
- 🧠 **Round-trip test built-in** — automatically verifies that `decode(encode(text)) == text`.  
- 💬 **Interactive Gradio UI** — includes sample Bengali sentences that auto-fill the input box.  
- ⚙️ **Compact 5010-token vocabulary** trained from a 2 MB corpus.  
- 🌐 **Deployable on Hugging Face Spaces** or runnable locally with Gradio.

---

## 📂 Repository Structure

bengali-bpe-tokenizer/
│
├── bengali_tokenizer/
│ ├── config.json # Metadata: vocab size, compression ratio, etc.
│ ├── merges.txt # Integer merge pairs (BPE rules)
│ └── vocab.json # Token ID → string mapping
│
├── app.py # Gradio web app with roundtrip + sample text buttons
├── tokenizer.py # Core BengaliBPETokenizer class
├── sample_bengali_text.txt # Example Bengali text for quick testing
├── Bikash_Session_11_BPE.ipynb # Colab notebook used for training
└── README.md # Project documentation



---

## 🧠 Training Summary (Final Version)

| Parameter | Value |
|------------|--------|
| **Corpus** | Bengali UTF-8 text (≈ 2 MB) |
| **Initial Tokens** | 2,097,152 bytes |
| **Target Vocab Size** | 5010 |
| **Base Tokens** | 0 – 255 (byte IDs) |
| **Merged Tokens** | 256 – 5009 |
| **Total Merges** | 4754 |
| **Training Method** | Full recomputation after every merge (no batching) |
| **Training Time** | ≈ 13 minutes on Colab T4 |
| **Final Compression Ratio** | 9.54 × |
| **Final Sequence Length** | 219,911 tokens (from 2,097,152 bytes) |

---

## 📊 Training Logs

Training on 2,097,152 byte tokens (~2 MB of data)

🚀 Starting BPE training: 4754 merges (full recomputation each step)...

📦 Merges: 100/4754 | Current compression: 3.48× | Current length: 602,858
📦 Merges: 500/4754 | Current compression: 5.29× | Current length: 396,305
📦 Merges: 1000/4754 | Current compression: 6.35× | Current length: 330,419
📦 Merges: 2000/4754 | Current compression: 7.61× | Current length: 275,677
📦 Merges: 3000/4754 | Current compression: 8.46× | Current length: 248,019
📦 Merges: 4000/4754 | Current compression: 9.12× | Current length: 230,030
📦 Merges: 4754/4754 | Current compression: 9.54× | Current length: 219,911

✅ Training complete!
✅ Final vocabulary size: 5010
✅ Final compression ratio: 9.54×
📁 Saved -> bengali_tokenizer/merges.txt
📁 Saved -> bengali_tokenizer/vocab.json
📁 Saved -> bengali_tokenizer/config.json





⚙️ Tokenizer Files Explained
File	Description
merges.txt	Integer token-pair merges defining BPE rules
vocab.json	Token ID → string mapping (Bengali glyphs + merged pairs)
config.json	Metadata — vocab size, compression ratio, notes

These three files fully define and reconstruct the tokenizer anywhere.

🧩 Example Output (from Gradio App)
Input:

তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)


Output:


🧩 Token IDs (first 200):
[274, 286, 285, 302, 174, 256, 482, 277, 364, 286, ... ]

🔤 Tokens (first 200):
['ত', 'ো', 'ম', 'া', 'র', ' ', 'ম', 'ং', 'গ', 'ল', ' ', 'হ', 'ো', 'ক', '!', ...]

🔁 Decoded text:
তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)

🧠 Roundtrip Test: ✅ True


🧰 Requirements

python >= 3.9
gradio >= 4.0
tqdm
📜 License
Released under the MIT License — free for research, educational, and commercial use with attribution.

💫 Hugging Face Space
🔗 https://huggingface.co/spaces/bikash9c/bengali-tokenizer-bikash

🪶 Final Result
✅ Efficient 5010-token Bengali Byte-Pair Encoding model

✅ 9.54× compression on 2 MB corpus

✅ Perfect round-trip decode

✅ Interactive Bengali tokenizer app with sample inputs and validation

Subword tokenization is where raw bytes learn to speak Bengali. 🪶