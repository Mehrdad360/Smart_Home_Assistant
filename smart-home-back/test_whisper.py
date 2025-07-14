import os
import whisper
import torch

def test_whisper_model_download():
    print("Starting Whisper model download test...")

    if torch.cuda.is_available():
        print("CUDA is available. Using GPU for Whisper.")
        device = "cuda"
    else:
        print("CUDA not available. Using CPU for Whisper.")
        device = "cpu"

    try:
        print(f"Attempting to load 'base' Whisper model on {device}...")
        model = whisper.load_model("base", device=device)
        print("Whisper 'base' model loaded successfully.")


    except Exception as e:
        print(f"An error occurred during Whisper model loading: {e}")
        print("Please ensure you have sufficient disk space and an active internet connection for the initial download.")
        print("Also check PyTorch installation: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu (or for CUDA)")

if __name__ == "__main__":
    test_whisper_model_download()