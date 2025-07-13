import gradio as gr
import parselmouth
from parselmouth.praat import call
import numpy as np
import pickle

# Load model and scaler
with open("parkinsons_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Feature extractor
def extract_features(file_path):
    snd = parselmouth.Sound(file_path)
    if snd.get_total_duration() < 0.5:
        raise ValueError("Audio too short")

    pitch = snd.to_pitch()
    harmonicity = call(snd, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)

    if pitch.count_voiced_frames() == 0:
        raise ValueError("No voiced frames found")

    mfcc = call(snd, "To MFCC", 13, 0.025, 0.01, 100, 50.0, 8000.0)
    num_frames = call(mfcc, "Get number of frames")
    if num_frames == 0:
        raise ValueError("No MFCC frames extracted")

    mfcc_means = {}
    for i in range(1, 14):
        coeff_vals = [call(mfcc, "Get value", i, f) for f in range(1, num_frames + 1)]
        mfcc_means[f'mfcc_{i}'] = np.mean(coeff_vals)

    features = {
        **mfcc_means,
        "hnr": call(harmonicity, "Get mean", 0, 0),
        "pitch_mean": call(pitch, "Get mean", 0, 0, "Hertz"),
        "pitch_min": call(pitch, "Get minimum", 0, 0, "Hertz", "Parabolic"),
        "pitch_max": call(pitch, "Get maximum", 0, 0, "Hertz", "Parabolic")
    }

    return np.array(list(features.values())).reshape(1, -1)

# Gradio interface
def predict_parkinsons(audio):
    try:
        features = extract_features(audio)
        scaled = scaler.transform(features)
        prediction = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0][prediction]
        label = "🧠 Parkinson's Detected" if prediction == 1 else "✅ Healthy"
        return f"{label}\nConfidence: {prob:.2%}"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

gr.Interface(
    fn=predict_parkinsons,
    inputs=gr.Audio(type="filepath", label="Upload .wav file"),
    outputs="text",
    title="Parkinson's Disease Voice Detector 🎤🧠",
    description="Upload a sustained vowel sound (like 'ahhh') to detect Parkinson's based on acoustic features."
).launch()
