# necessary imports
import myAudio
import screen
import threading # to handle multiple threads
import ffmpeg # for merging audio and video

# creating threads
t1 = threading.Thread(target=myAudio.start_AudioRecording, daemon=True)
t2 = threading.Thread(target=screen.star_ScreenRecording, daemon=True)
# starting threads
t1.start()
t2.start()
# waiting for threads to complete
t1.join()
t2.join()
print("Recording Completed.")

# merging audio and video files via ffmpeg
input_video = ffmpeg.input('Recording.mp4')
input_audio = ffmpeg.input('recorderFile.wav')
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()

