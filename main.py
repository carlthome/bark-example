from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav

# Download and load all models.
preload_models()

# Generate audio from text.
text_prompt = """
    ♪ In the jungle, the mighty jungle, the lion barks tonight ♪
"""
audio_array = generate_audio(text_prompt)

# Play text in notebook.
Audio(audio_array, rate=SAMPLE_RATE)

# Save audio to file.
write_wav("output.wav", SAMPLE_RATE, audio_array)
