import gradio as gr
import traceback
import sys
from tokenizer import BengaliBPETokenizer
import os

# --- Try to construct tokenizer on startup ---
try:
    tokenizer_dir = "bengali_tokenizer"
    if not os.path.exists(tokenizer_dir):
        raise FileNotFoundError(f"Tokenizer folder '{tokenizer_dir}' not found in Space directory.")

    tokenizer = BengaliBPETokenizer(tokenizer_dir)
    init_exc = None
except Exception:
    init_exc = traceback.format_exc()
    tokenizer = None


# --- Tokenize Function ---
def tokenize_text(text):
    """Tokenize Bengali input text and show tokens + decoded output."""
    try:
        if init_exc:
            return f"❌ Tokenizer initialization error:\n\n{init_exc}"

        if not tokenizer:
            return "Tokenizer not available."

        ids = tokenizer.encode(text)
        decoded = tokenizer.decode(ids)

        # Map first 200 token IDs to readable Bengali tokens if possible
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
            f"🔁 **Decoded text:**\n{decoded}"
        )
        return out

    except Exception:
        tb = traceback.format_exc()
        print(tb, file=sys.stderr)
        return f"⚠️ Error during tokenization:\n\n{tb}"


# --- Gradio App UI ---
with gr.Blocks(theme="gradio/soft") as app:
    gr.Markdown("## 🪶 Bengali BPE Tokenizer")
    gr.Markdown(
        "Byte-level BPE tokenizer trained on Bengali corpus (~5 MB). "
        "Enter text below to see token IDs, merged tokens, and decoded output."
    )

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
                label="Tokenized & Decoded Output",
                lines=12,
                elem_id="output-box",
            )

    btn = gr.Button("🚀 Tokenize")
    btn.click(tokenize_text, inputs=text_in, outputs=text_out)

    gr.Markdown(
        "<br><small>Trained tokenizer files: <code>vocab.json</code> + <code>merges.txt</code></small>"
    )

# --- Launch (auto in Space) ---
if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)