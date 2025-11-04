🪶 Bengali BPE Tokenizer

A custom Byte Pair Encoding (BPE) tokenizer trained on Bengali Wikipedia (~5 MB), designed for tokenizing and decoding Bengali text at a byte level. Built completely from scratch in Python and deployed with an interactive Gradio web app on Hugging Face Spaces.

🚀 Project Overview

This project shows how to create a byte-level BPE tokenizer similar to GPT-2’s tokenizer, trained specifically for Bengali text data. It includes a reversible encoder–decoder, Gradio UI, and deployment-ready tokenizer artifacts.

🧩 Key Features

🔤 Byte-level BPE — learns merges on UTF-8 bytes, ensuring full character coverage.

🔁 Fully reversible encode–decode process (perfect Bengali reconstruction).

⚙️ Compact vocabulary (4.5 K) trained on 5 MB of Wikipedia text.

💬 Interactive Gradio app for testing tokenization visually.

🌐 Deployable on Hugging Face Spaces or runnable locally.

📂 Repository Structure

bengali-bpe-tokenizer/
├── app.py # Gradio interface
├── tokenizer.py # Core tokenizer class (encode/decode)
├── bengali_tokenizer/ # Trained tokenizer artifacts
│ ├── merges.txt # Learned merge pairs
│ ├── vocab.json # Token ID → readable token mapping
│ └── config.json # Metadata
├── train_tokenizer.ipynb # (Optional) Colab training script
└── README.md # Project documentation

🧠 Training Summary

The tokenizer was trained on Bengali Wikipedia (November 2023 dump) using 5 MB of UTF-8 text. The BPE algorithm iteratively merges the most frequent byte pairs, forming subword tokens.

Parameter	Value
Corpus	Bengali Wikipedia
Sample Size	5 MB
Vocabulary Size	4 500
Base Tokens	0–255 (byte IDs)
Merge Tokens	256–4 499
Final Compression Ratio	~3.29×
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

The Gradio app provides an interactive interface to test tokenization and decoding. Users can enter Bengali text, view token IDs and subword segments, and verify that decoding returns the original text.

Run locally:
pip install gradio
python app.py

Or explore on Hugging Face Spaces:
👉 Live Demo (Hugging Face): https://huggingface.co/spaces/bikash9c/BPE_bengali_tokenizer

⚙️ Tokenizer Files Explained
File	Description
merges.txt	List of integer token-pair merges defining the BPE rules.
vocab.json	Maps token IDs to their readable representations (Bengali strings or merged pairs).
config.json	Stores metadata such as vocab size and compression ratio.

These three files are sufficient to reconstruct the tokenizer anywhere.

🧩 Example Output (from Gradio app)

Input:
তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)

Output:
🧩 Token IDs (first 200): [1156, 1756, 1706, 2556, 174, 256, …]
🔤 Tokens (first 200): ['তো', 'মা', 'র', ' ', 'ম', 'ঙ্গল', …]
🔁 Decoded text: তোমার মঙ্গল হোক! (হাঁচি দেওয়ার সময়)

🧰 Requirements

Runtime
python >= 3.9
gradio >= 4.0
tqdm

Optional (for training)
datasets

📜 License

This project is released under the MIT License. You are free to use, modify, and integrate it into your NLP or research workflows.

✍️ Author

Bikash Chakraborty
Data Science & AI Enthusiast
📧 your.email@example.com

🌐 https://huggingface.co/your-username

Subword tokenization is where raw bytes learn to speak Bengali. 🪶

📊 Training Summary (from Logs)

Dataset: Bengali Wikipedia (5 MB sample, UTF-8 encoded)

Initial Tokens: 5,242,880 bytes

Target Vocabulary Size: 4,500

Total Merges: 4,244

Batch Size: 50 merges per recomputation

Total Batches: 85

Training Duration: ~36 minutes

Final Compression Ratio: 3.29×

Final Sequence Length: 1,592,917 tokens (from 5,242,880)

Progress: Smooth and stable — compression steadily improved from 1.3× to 3.29×

Artifacts Saved:

✅ /content/drive/MyDrive/bengali_tokenizer/merges.txt

✅ /content/drive/MyDrive/bengali_tokenizer/vocab.json

✅ /content/drive/MyDrive/bengali_tokenizer/config.json

Notes:

The training converged cleanly with a balanced tradeoff between vocabulary granularity and compression.

Step size of 50 maintained memory safety and efficient batching.

The tokenizer achieves full reversibility on Bengali text.

✅ Final Result:
Efficient 4.5K-token Bengali Byte-Pair Encoding model with ~3.3× compression and perfect decoding accuracy.
