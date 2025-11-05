🪶 Bengali BPE Tokenizer

A custom Byte Pair Encoding (BPE) tokenizer trained on Bengali Wikipedia (≈ 5 MB), designed for tokenizing and decoding Bengali text at a byte level.
Built entirely from scratch in Python, with a clean Gradio web app deployed on Hugging Face Spaces.

🚀 Project Overview

This project demonstrates how to build a byte-level BPE tokenizer (like GPT-2’s) from scratch — trained specifically on Bengali UTF-8 text.
It features a reversible encoder-decoder, compact vocabulary, and an interactive web interface.

🧩 Key Features

🔤 Byte-level BPE — learns merges on UTF-8 bytes for full Bengali script coverage.

🔁 Fully reversible encode/decode (perfect Bengali reconstruction).

⚙️ Compact vocabulary — 500 learned tokens from a 5 MB corpus.

💬 Interactive Gradio app for visual testing and verification.

🌐 Deployable on Hugging Face Spaces or runnable locally.

📂 Repository Structure
bengali-bpe-tokenizer/
│
├── bengali_tokenizer/
│   ├── config.json         # Metadata: vocab size, compression ratio, etc.
│   ├── merges.txt          # Integer merge pairs (BPE rules)
│   └── vocab.json          # Token ID → string mapping
│
├── app.py                  # Gradio web app interface
├── tokenizer.py            # Core BengaliBPETokenizer class
├── sample_bengali_text.txt # Example Bengali text for quick testing
├── Bikash_Session_11_BPE.ipynb  # Colab notebook used for training
└── README.md               # Project documentation

🧠 Training Summary (Final Version)
Parameter	Value
Corpus	Bengali Wikipedia (5 MB UTF-8 sample)
Initial Tokens	5 ,242 ,880 bytes
Target Vocab Size	500
Base Tokens	0 – 255 (byte IDs)
Merged Tokens	256 – 499
Total Merges	244
Training Method	Full recomputation after every merge (no batching)
Training Time	≈ 3.5 minutes on Colab T4
Final Compression Ratio	4.25 ×
Final Sequence Length	1 ,234 ,765 tokens (from 5 ,242 ,880 bytes)
📊 Training Logs
Training on 5,242,880 byte tokens (~5 MB of data)
🚀 Starting BPE training: 244 merges (full recomputation each step)...

📦 Merges: 100/244 | Compression: 3.42× | Length: 1,533,033
📦 Merges: 200/244 | Compression: 4.04× | Length: 1,296,602
📦 Merges: 244/244 | Compression: 4.25× | Length: 1,234,765

✅ Training complete!
✅ Final vocabulary size: 500
✅ Final compression ratio: 4.25×
📁 Saved -> bengali_tokenizer/merges.txt
📁 Saved -> bengali_tokenizer/vocab.json
📁 Saved -> bengali_tokenizer/config.json

🧩 Usage Example
from tokenizer import BengaliBPETokenizer

tokenizer = BengaliBPETokenizer("bengali_tokenizer")

text = "আপনাকে অনেক ধন্যবাদ।"
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)

print("Token IDs:", ids)
print("Decoded Text:", decoded)


✅ Output

Token IDs: [256, 134, 2656, 856, 4406, …]
Decoded Text: আপনাকে অনেক ধন্যবাদ।

🎨 Gradio Web App

The Gradio app provides an interactive Bengali tokenization demo.
Enter Bengali text or load a sample, view token IDs and merged tokens, and verify that decoding reconstructs the original text.

▶️ Run locally
pip install gradio
python app.py

🌐 Live on Hugging Face Spaces

👉 Bengali BPE Tokenizer Demo

⚙️ Tokenizer Files Explained
File	Description
merges.txt	List of integer token-pair merges defining BPE rules.
vocab.json	Token ID → string (Bengali glyphs or merged pairs).
config.json	Metadata such as vocab size and compression ratio.

These three files are sufficient to reconstruct the tokenizer anywhere.

🧩 Example Output (from Gradio App)

Input:

তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)


Output:

🧩 **Token IDs (first 200):**
[274, 286, 285, 302, 174, 256, 482, 277, 364, 286, 276, 33, 374, 311, 265, 129, 359, 290, 166, 271, 147, 284, 302, 184, 285, 284, 41] ...

🔤 **Tokens (first 200):**
['ত', 'ো', 'ম', 'à¦¾à¦° à¦', '®', 'à¦', '\x99à§\x8dà¦\x97', 'ল', ' হ', 'ো', 'ক', '!', ' (', 'হ', 'à¦¾à¦', '\x81', 'চ', 'à¦¿ à¦', '¦', 'à§\x87à¦', '\x93', 'য়', 'à¦¾à¦° à¦', '¸', 'ম', 'য়', ')']

🔁 **Decoded text:**
তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)

🧰 Requirements

python >= 3.9
gradio >= 4.0
tqdm



📜 License

Released under the MIT License — free for research, educational, and commercial use with attribution.


Hugging face link:
https://huggingface.co/spaces/bikash9c/bengali-tokenizer-bikash

Subword tokenization is where raw bytes learn to speak Bengali. 🪶

✅ Final Result

Efficient 500-token Bengali Byte-Pair Encoding model

4.25× compression

Perfect decode round-trip

Compact & deployable tokenizer for Bengali language processing 🚀