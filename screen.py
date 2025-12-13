# importing the required packages
import pyautogui
import cv2
import numpy as np
import sys

from pynput.keyboard import Key, Listener

stop_flag = False
def keyPressed(key):
    if key == Key.space:
        print("Recording Stopped.")
        global stop_flag 
        stop_flag = True
        return False

# Specify resolution (the wrong resolution may cause error so choose according to your screen)
resolution = (3024, 1964)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Specify name of Output file
filename = "Recording.mp4"

# Specify frames rate.
fps = 5.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# # optional: To display the recording screen uncomment below code
# # Create an Empty window
# cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# # Resize this window
# cv2.resizeWindow("Live", 480, 270)

print("Recording Started... Press Space to Stop.")
listener = Listener(on_press=keyPressed)
listener.start()

while True:
    try:
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

        cv2.waitKey(130)

        if stop_flag:
            break

    except KeyboardInterrupt:
        break


# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
