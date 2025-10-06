Voice Command Processor 🗣️
This project is a Python-based voice command processor that converts spoken language into text using a Speech-to-Text (STT) model and then analyzes the text using Natural Language Processing (NLP) to detect the user's intent. It is designed to be a core component for a voice-controlled application.

🌟 Features

Real-time Transcription: Captures audio from the microphone in real-time.

Intelligent Intent Detection: Uses NLP to analyze transcribed text and determine user commands like "download," "play," or "search."

Offline and Online STT: Automatically switches between an offline VOSK model and an online Whisper model based on network connectivity.

Robust Audio Preprocessing: Includes noise reduction and filtering to improve transcription accuracy.

Cross-platform Compatibility: Designed to run on Windows, macOS, and Linux.

💻 Core Components

main.py: The entry point of the application. It checks for network connectivity and selects the appropriate STT model before starting the audio stream.

STT/nlpProcessor.py: The brain of the project. It handles text analysis using SpaCy and RAKE to extract verbs and keywords, identifies synonyms, and determines the user's intent from a list of predefined actions.

STT/RTMicroPhone.py: Manages the microphone input. It includes a voice activity detection (VAD) system to listen only when speech is detected and passes the audio to the selected STT model.

STT/sttOffline.py: Contains the logic for the offline STT using the Vosk library.

STT/sttWhisper.py: Contains the logic for the online STT using the Whisper model from Hugging Face.

⚙️ Requirements

Python 3.8 or higher

pip (Python package installer)

A microphone connected to your computer.

🚀 Setup and Installation

Follow these steps to get the project up and running.

1. Clone the Repository

Bash
git clone <repository_url>
cd voice-command-processor
2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Python Libraries

Install all the necessary packages from the requirements.txt file (you will need to create this file yourself with the following contents):

Plaintext
sounddevice
numpy
webrtcvad
noisereduce
scipy
spacy
rake-nltk
nltk
rapidfuzz
vosk
torch
torchaudio
transformers
distro
Now, run the installation command:

Bash
pip3 install -r requirements.txt
4. Download Language Models

The project requires several data models for its NLP and offline STT capabilities.

SpaCy Model:

Bash
python3 -m spacy download en_core_web_sm
NLTK Data:

Bash
python3 -c "import nltk; nltk.download('punkt'); nltk.download('wordnet');"
Vosk Model:

Download the vosk-model-en-us-0.22 folder from the Vosk website.

Extract the downloaded archive.

Place the extracted folder inside the STT directory. Your file path should look like STT/vosk-model-en-us-0.22.

🏃 How to Run

Navigate to the project's root directory and run the main script.

Bash
python3 main.py
The program will first perform a short noise calibration. Once complete, it will start listening for your voice commands.

Example Commands:

"Download the new file."

"Play some music on the computer."

"Search for the nearest restaurant."

To stop the program, press Ctrl + C in your terminal.
