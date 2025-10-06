from STT.RTMicroPhone import stream_microPhone
from STT.sttOffline import stt_vosk
from STT.sttWhisper import stt_whisper
from STT.NetworkStatus import check_server_connectivity

def main():
    network_available = check_server_connectivity("8.8.8.8", 53, 3)
    if network_available:
        print("Network available - Using Whisper (GPU)")
        stt_function = stt_whisper
    else:
        print("Network unavailable - Using Vosk (offline)")
        stt_function = stt_vosk

    stream_microPhone(stt_function, buffer_seconds=3)

if __name__ == "__main__":
    main()
