import pyaudio
import wave
from pynput.keyboard import Key, Listener

stop_AudioFlag = False
def keyPressed(key):
    if key == Key.space:
        print("Recording Stopped.")
        global stop_AudioFlag 
        stop_AudioFlag = True
        return False

def start_AudioRecording():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = "recorderFile.wav"

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)

    frames = []

    print("Recording Started... Press Space to Stop.")
    listener = Listener(on_press=keyPressed)
    listener.start()

    while True:
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
        except KeyboardInterrupt:
            break
        if stop_AudioFlag:
            break


    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

if __name__ == "__main__":
    start_AudioRecording()