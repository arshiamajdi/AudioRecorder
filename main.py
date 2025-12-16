import myAudio
import screen
import threading
import ffmpeg

t1 = threading.Thread(target=myAudio.start_AudioRecording, daemon=True)
t2 = threading.Thread(target=screen.star_ScreenRecording, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()

print("Recording Completed.")

input_video = ffmpeg.input('Recording.mp4')

input_audio = ffmpeg.input('recorderFile.wav')

ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()

