# importing the required packages
import pyautogui
import cv2
import numpy as np
import time
from pynput.keyboard import Listener, Key

stop_ScreenFlag = False
def ScreenkeyPressed(key):
    if key == Key.space:
        print("Screen Recording Stopped.")
        global stop_ScreenFlag 
        stop_ScreenFlag = True
        return False

def star_ScreenRecording():
    
    # Specify resolution (the wrong resolution may cause error so choose according to your screen)
    resolution = (3024, 1964)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"mp4v")

    # Specify name of Output file
    filename = "Recording.mp4"

    # Specify frames rate.
    fps = 4.5

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # # optional: To display the recording screen uncomment below code
    # # Create an Empty window
    # cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # # Resize this window
    # cv2.resizeWindow("Live", 480, 270)

    print("Screen Recording Started... Press Space to Stop.")
    listener = Listener(on_press=ScreenkeyPressed)
    listener.start()

    while True:
        try:
            start = time.time()
            # Take screenshot using PyAutoGUI
            img = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(img)

            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write it to the output file
            out.write(frame)

            # # Optional: Display the recording screen
            # cv2.imshow('Live', frame)

            # Calculate time taken to capture the screen then set the FPS
            end = time.time()
            diff = (end-start)*1000
            print('time: {:6.2f} ms | {:5.2f} FPS'.format(diff, 1000/diff ))

            cv2.waitKey(1)

            if stop_ScreenFlag:
                break

        except KeyboardInterrupt:
            break


    # Release the Video writer
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    star_ScreenRecording()