import myAudio
import screen
import threading

t1 = threading.Thread(target=myAudio.start_AudioRecording, daemon=True)
t2 = threading.Thread(target=screen.star_ScreenRecording, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()

print("Recording Completed.")