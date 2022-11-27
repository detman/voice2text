# audio2text

This script converts the WAV audios produced by Phillips VoiceTracer and converts them to ascii text. text is written into a audio.txt file. existing content will be overwritten.

## installation (mac)

```bash
brew install portaudio 
python3 -m venv env
source env/bin/activate

pip install pyaudio
pip install SpeechRecognition
```
