Voice Command Processor 🗣️
A dynamic Python-based application that converts spoken commands into actionable tasks. This project leverages a robust pipeline combining real-time Speech-to-Text (STT) and Natural Language Processing (NLP) to understand and respond to user input.

🌟 Features

Real-time Transcription: Captures audio from the microphone to transcribe speech into text on the fly.

Intelligent Intent Detection: Uses NLP to analyze transcribed text and determine user commands such as "download," "play," or "search."

Offline and Online STT: The application intelligently switches between a lightweight, offline Vosk model and a powerful, online Whisper model based on network connectivity.

Robust Audio Preprocessing: Includes built-in noise reduction and filtering to ensure high accuracy, even in noisy environments.

Cross-platform Compatibility: Designed to be compatible with Windows, macOS, and Linux.

💻 Core Components

main.py: The main entry point that initiates the application. It checks for network status and selects the appropriate STT model.

STT/nlpProcessor.py: This is the core logic for the NLP component. It uses SpaCy, RAKE, and WordNet to extract verbs and keywords, identify synonyms, and detect the user's intent.

STT/RTMicroPhone.py: Handles microphone input and includes a voice activity detection (VAD) system to listen only when speech is detected. It orchestrates the audio-to-text-to-intent pipeline.

STT/sttOffline.py: Contains the code for the offline STT, which uses the Vosk library for fast, on-device transcription.

STT/sttWhisper.py: Contains the code for the online STT, which leverages the high accuracy of OpenAI's Whisper model via the Hugging Face library.

⚙️ Requirements

Python 3.8 or higher

A microphone connected to your computer.

Git for cloning the repository.

🚀 Setup and Installation

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository

Bash
git clone <repository_url>
cd voice-command-processor
2. Create and Activate a Virtual Environment

It is strongly recommended to use a virtual environment to manage project dependencies.

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Python Libraries

Create a requirements.txt file in the project's root directory with the following contents, then install the packages:

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
Run the installation command:

Bash
pip3 install -r requirements.txt
4. Download Language Models

The project requires several data models for its NLP and offline STT functionalities.

SpaCy Model:

Bash
python3 -m spacy download en_core_web_sm
NLTK Data:

Bash
python3 -c "import nltk; nltk.download('punkt'); nltk.download('wordnet');"
Vosk Model:

Download the vosk-model-en-us-0.22 folder from the Vosk website.

Extract the downloaded archive.

Place the extracted folder inside the STT directory. The final path should be STT/vosk-model-en-us-0.22.

🏃 How to Run

After completing the setup, navigate to the project's root directory and run the main script.

Bash
python3 main.py
The program will perform a brief noise calibration. Once complete, it will begin listening for your voice commands.

Example Commands:

"Download the new file."

"Play some music."

"Search for the nearest restaurant."

To stop the program, press Ctrl + C in your terminal.

🧑‍💻 Author

Aman Deep
📧 Email: bhagatamandeep50@gmail.com
🔗 GitHub: Aman-Deep123456

📝 License

This project is open-source under the MIT License.

⭐️ Show Your Support

If you found this helpful or interesting, please consider giving a ⭐️ to the repo!
