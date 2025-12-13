import pyaudio
import wave
# import keyboard
# import time

from pynput.keyboard import Key, Listener

stop_flag = False
def keyPressed(key):
    if key == Key.space:
        print("Recording Stopped.")
        global stop_flag 
        stop_flag = True
        return False


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "recorderFile.wav"

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

frames = []
# print("Press 'space' to start recording audio.")
# keyboard.wait('space')
# print('Recording... Press "space" to stop.')
# time.sleep(0.2)

print("Recording Started... Press Space to Stop.")
listener = Listener(on_press=keyPressed)
listener.start()

while True:
    try:
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)
    except KeyboardInterrupt:
        break
    # if keyboard.is_pressed('space'):
    #     print("Stopping recording.")
    #     time.sleep(0.2)
    #     break
    if stop_flag:
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
