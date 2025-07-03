import os
import whisper
import torch

def test_whisper_model_download():
    print("Starting Whisper model download test...")

    # Check for PyTorch availability
    if torch.cuda.is_available():
        print("CUDA is available. Using GPU for Whisper.")
        device = "cuda"
    else:
        print("CUDA not available. Using CPU for Whisper.")
        device = "cpu"

    try:
        # Load the 'base' Whisper model. This will download it if not already present.
        print(f"Attempting to load 'base' Whisper model on {device}...")
        model = whisper.load_model("base", device=device)
        print("Whisper 'base' model loaded successfully.")

        # Optional: You can list downloaded models if needed (Whisper stores them in a default location)
        # print("Downloaded models might be located in:", os.path.expanduser("~/.cache/whisper"))

        # Create a dummy audio file for testing (or use a real one if you have)
        # For simplicity, we'll just check if the model loaded.
        # If you want to do a full test, you'd need an audio file.
        # Example to transcribe a dummy audio (you'd need to record or download one first)
        # audio_path = "path/to/your/audio.mp3"
        # if os.path.exists(audio_path):
        #     print(f"Transcribing {audio_path}...")
        #     result = model.transcribe(audio_path)
        #     print("Transcription:", result["text"])
        # else:
        #     print(f"No audio file found at {audio_path} for full transcription test.")
        #     print("Model load successful, which indicates download is complete.")

    except Exception as e:
        print(f"An error occurred during Whisper model loading: {e}")
        print("Please ensure you have sufficient disk space and an active internet connection for the initial download.")
        print("Also check PyTorch installation: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu (or for CUDA)")

if __name__ == "__main__":
    test_whisper_model_download()