# 🧠 Parkinson's Disease Voice Detection using Machine Learning 🎤

A lightweight and interactive web app to **screen Parkinson's Disease** from **voice samples** using acoustic biomarkers like MFCCs, jitter, shimmer, pitch, and HNR — built with **Python**, **Parselmouth**, **Scikit-learn**, and **Gradio**.

---

## 🎯 Objective
Parkinson’s Disease (PD) affects motor control — and speech patterns are one of the earliest indicators. This app aims to make **early, accessible screening** possible using just a 2–3 second "ahh" voice recording.

---

## 💡 How It Works
1. 🎤 The user uploads a `.wav` file with sustained vowel sound ("ahhh").
2. 📊 We extract acoustic features using **Praat (via Parselmouth)**.
3. 🤖 The extracted features are scaled and passed to a trained **Random Forest** model.
4. 🧠 The app returns prediction: **Parkinson’s Detected** or **Healthy**, along with confidence.

---

## 🧪 Features Used
- **MFCCs (1–13)**: Mel-Frequency Cepstral Coefficients for speech texture
- **Pitch (mean, min, max)**: Voice frequency stability
- **Jitter (local)**: Micro-variations in pitch
- **Shimmer (local)**: Variability in amplitude
- **HNR**: Harmonic-to-noise ratio (voice clarity)

---

## 📦 Folder Structure

```
├── app.py                        # Main Gradio application
├── parkinsons_model.pkl         # Trained Random Forest model
├── scaler.pkl                   # StandardScaler used during training
├── requirements.txt             # Dependencies
├── .gitignore                   # Ignore unnecessary files
├── LICENSE                      # MIT License for open use
└── README.md                    # Project description (this file)
```

---

## 🚀 Usage Instructions

### 🔧 Installation
```bash
git clone https://github.com/your-username/parkinsons-voice-detector.git
cd parkinsons-voice-detector
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
python app.py
```
Visit `http://localhost:7860` to access the web app in your browser.

### 🎤 Input Instructions
- Record a **2–3 second "ahhh" sound**.
- Make sure the environment is **quiet**, with **steady tone** and **neutral speech**.
- Upload `.wav` file and get instant prediction.

---

## 📊 Sample Output
```text
✅ Healthy
Confidence: 81.23%
```
```text
🧠 Parkinson's Detected
Confidence: 91.75%
```

---

## 🤖 Model Details
| Model         | Accuracy | Notes                                |
|---------------|----------|--------------------------------------|
| Random Forest | ~86%     | Trained on extracted features from 81 voice samples |

- Trained on `.wav` files with extracted biomedical voice biomarkers.
- Model built for **educational and research purposes only**.

---

## 🧠 Why This Matters
- **Accessible**: No need for clinical visits to get preliminary screening.
- **Non-invasive**: Just requires a voice sample.
- **Affordable & Open**: Free and reproducible for students, clinicians, and researchers.

---

## 📚 Dataset Used
- Source: [Voice Samples for Parkinson's Disease (Figshare)](https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127)
- 🎙️ Includes `.wav` recordings from both PD patients and healthy individuals
- ✅ Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> ⚠️ Note: This repo **does not include** raw dataset files. Please download them from the above link.

---

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🔗 Live Demo Screenshot
<img width="1875" height="892" alt="image" src="https://github.com/user-attachments/assets/b9df36bf-69ab-4e80-9c4e-a418c74a8bd7" />

---

## 🧑‍💻 Author
**Kamireddy Keerthi Reddy**  
[LinkedIn](https://www.linkedin.com/in/keerthi-reddy-a2571927a/) • [GitHub](https://github.com/Keerthi7903)  
📧 keerthireddy7903@gmail.com


---

## 💬 Contact & Contributions
Pull requests, feature ideas, or UI suggestions are welcome! Feel free to open an issue.

```
🔭 I’m currently working on: Real-time ML apps using voice/audio analysis
🌱 I’m currently learning: Deep Learning & TensorFlow
👯 I’m looking to collaborate on: Healthcare + AI Projects
🤔 I’m looking for help with: Improving accuracy with large speech datasets
💬 Ask me about: AI/ML, Web Dev, Voice Feature Extraction
📫 How to reach me: keerthireddy7903@gmail.com
😄 Pronouns: she/her
⚡ Fun fact: I built this app using real patient voices!
```

