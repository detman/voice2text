import speech_recognition as sr
import sys
import os
from datetime import datetime


def audio2text(file):
    """
    get audio as text
    """
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.listen(source)

    print(f'fetching text {file}')
    text = r.recognize_google(audio, language="de_DE.utf8")
    print(f'fetched text {file}: {text}')
    return text

if len(sys.argv) == 1:
    cmd = sys.argv[0]
    print(f'usage {cmd} dir|file')
else:
    dir = sys.argv[1]
    audios = []
    if os.path.isdir(dir):
        if not dir.endswith('/'):
            dir += '/'

        for root, subfolders, files in os.walk(dir):
            folder = root[len(dir):]
            audios.extend( [ folder + '/' + f for f in files if f.endswith('.WAV')])

        audios.sort(key=lambda x: os.path.getmtime(dir + x))

    else:
        audios.append(dir)

    """
    loop over all WAV files
    """
    with open(dir + 'audio.txt', 'w') as f:
        for file in audios:
            audio = dir + file
            if not os.path.exists(audio):
                print(f'file not found: {audio}')
                continue

            try:
                text = audio2text(audio)
            except Exception as e:
                print(f'error fetching text fpr {file}: {e}')
                continue

            time = os.path.getmtime(audio)
            f.write(datetime.fromtimestamp(time).isoformat() + ' ' + file + '\n')
            f.write(text + '\n')
            f.write('\n')
