🗣️ Voice Command Processor

A dynamic Python-based application that converts spoken commands into actionable tasks. This project leverages a robust pipeline combining real-time Speech-to-Text (STT) and Natural Language Processing (NLP) to understand and respond to user input.

🌟 Features

Real-time Transcription: Captures audio from your microphone and transcribes speech into text on the fly.

Intelligent Intent Detection: Uses NLP to analyze transcribed text and determine user commands like "download," "play," or "search."

Offline and Online STT: Automatically switches between a lightweight, offline Vosk model and a powerful, online Whisper model based on your network connectivity.

Robust Audio Preprocessing: Includes built-in noise reduction and filtering for high accuracy, even in noisy environments.

Cross-platform Compatibility: Designed to work seamlessly on Windows, macOS, and Linux.

💻 Core Components

The project's architecture is designed for modularity and clarity. Here's a quick overview of the main components:

main.py: The application's entry point. It handles network status checks and selects the appropriate STT model.

STT/nlpProcessor.py: The core NLP logic. It uses SpaCy, RAKE, and WordNet to extract verbs and keywords, identify synonyms, and detect user intent.

STT/RTMicrophone.py: Manages microphone input, includes a voice activity detection (VAD) system, and orchestrates the entire audio-to-text-to-intent pipeline.

STT/sttOffline.py: Contains the logic for the offline Vosk STT model, enabling fast, on-device transcription.

STT/sttWhisper.py: Contains the logic for the online Whisper STT model, leveraging its high accuracy via the Hugging Face library.

⚙️ Requirements

Python 3.8 or higher

A microphone connected to your computer

Git for cloning the repository

🚀 Setup and Installation

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository

Bash
git clone https://github.com/Aman-Deep123456/voice-command-processor.git
cd voice-command-processor
2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies and avoid conflicts with other Python projects.

Bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
3. Install Python Libraries

Install all necessary packages using the requirements.txt file.

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
The program will perform a brief noise calibration. Once complete, it will begin listening for your voice commands. To stop the program, press Ctrl + C in your terminal.

Example Commands:

"Download the new file."

"Play some music."

"Search for the nearest restaurant."

🧑‍💻 Author

Aman Deep

📧 Email: bhagatamandeep50@gmail.com

🔗 GitHub: Aman-Deep123456

⭐️ Show Your Support

If you found this project helpful or interesting, please consider giving a ⭐️ to the repository! Your support is greatly appreciated.

📝 License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
