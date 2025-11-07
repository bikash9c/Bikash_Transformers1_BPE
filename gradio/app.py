import gradio as gr
import traceback
import sys
from tokenizer import BengaliBPETokenizer
import os
import json

# --- Initialize Tokenizer ---
try:
    tokenizer_dir = "bengali_tokenizer"
    if not os.path.exists(tokenizer_dir):
        raise FileNotFoundError(f"Tokenizer folder '{tokenizer_dir}' not found in Space directory.")

    tokenizer = BengaliBPETokenizer(tokenizer_dir)
    config_path = os.path.join(tokenizer_dir, "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {}

    vocab_size = config.get("vocab_size", len(tokenizer.vocab))
    compression_ratio = config.get("compression_ratio", None)
    init_msg = (
        f"✅ Tokenizer initialized — vocab size: {vocab_size:,} "
        + (f"| compression ratio: {compression_ratio}×" if compression_ratio else "")
    )

    init_exc = None
except Exception:
    init_exc = traceback.format_exc()
    tokenizer = None
    init_msg = "❌ Tokenizer initialization failed."

# ---------------------------------------------------------------------
# Tokenization logic with roundtrip check
# ---------------------------------------------------------------------
def tokenize_text(text):
    """Tokenize Bengali input text and show tokens, decoded output, and roundtrip test."""
    try:
        if init_exc:
            return f"❌ Tokenizer initialization error:\n\n{init_exc}"

        if not tokenizer:
            return "Tokenizer not available."

        if not text.strip():
            return "⚠️ Please enter some Bengali text."

        # Encode and decode
        ids = tokenizer.encode(text)
        decoded = tokenizer.decode(ids)

        # --- Roundtrip Check ---
        roundtrip_ok = (decoded == text)
        roundtrip_msg = "✅ Roundtrip Match: True" if roundtrip_ok else "❌ Roundtrip Match: False"

        # Display up to 200 tokens
        tokens = []
        for i in ids[:200]:
            tok = tokenizer.vocab.get(str(i), f"<{i}>")
            try:
                tokens.append(tok.encode("latin1").decode("utf-8"))
            except Exception:
                tokens.append(tok)

        out = (
            f"🧩 **Token IDs (first 200):**\n{ids[:200]} ...\n\n"
            f"🔤 **Tokens (first 200):**\n{tokens}\n\n"
            f"🔁 **Decoded text:**\n{decoded}\n\n"
            f"🧠 **Roundtrip Test:** {roundtrip_msg}"
        )
        return out

    except Exception:
        tb = traceback.format_exc()
        print(tb, file=sys.stderr)
        return f"⚠️ Error during tokenization:\n\n{tb}"

# ---------------------------------------------------------------------
# Gradio Interface
# ---------------------------------------------------------------------
with gr.Blocks(theme="gradio/soft") as app:
    gr.Markdown("## 🪶 Bengali Byte-Pair Encoding (BPE) Tokenizer")
    gr.Markdown(
        "Byte-level BPE tokenizer trained on **2 MB Bengali corpus** "
        "(vocab = 5010). Enter text below or click a sample to view token IDs, "
        "merged tokens, reconstructed text, and roundtrip verification."
    )

    # Initialization status
    gr.Markdown(f"**{init_msg}**")

    # --- Sample Bengali Texts ---
    gr.Markdown("### ✨ Try with Sample Sentences")
    sample_1 = "আমি বাংলায় গান গাই।"
    sample_2 = "আজ আকাশে মেঘ নেই, রোদ ঝলমলে দিন।"
    sample_3 = "বাংলা আমার মাতৃভাষা।"

    with gr.Row():
        b1 = gr.Button(sample_1)
        b2 = gr.Button(sample_2)
        b3 = gr.Button(sample_3)

    with gr.Row():
        with gr.Column(scale=1):
            text_in = gr.Textbox(
                label="Enter Bengali text",
                placeholder="এখানে বাংলা লিখুন…",
                lines=6,
                elem_id="input-box",
            )
        with gr.Column(scale=1):
            text_out = gr.Textbox(
                label="Tokenized & Decoded Output (with Roundtrip Test)",
                lines=14,
                elem_id="output-box",
            )

    btn = gr.Button("🚀 Tokenize")

    # --- Define button behaviors ---
    b1.click(lambda: sample_1, None, text_in)
    b2.click(lambda: sample_2, None, text_in)
    b3.click(lambda: sample_3, None, text_in)
    btn.click(tokenize_text, inputs=text_in, outputs=text_out)

    gr.Markdown(
        "<br><small>Tokenizer files: <code>vocab.json</code> | <code>merges.txt</code> | <code>config.json</code></small>"
    )

# ---------------------------------------------------------------------
# Launch
# ---------------------------------------------------------------------
if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)