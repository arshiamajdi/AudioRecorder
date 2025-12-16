# Python Application Project

## Overview
This project is a Python-based application composed of multiple modules that work together to handle program logic, screen interaction, and audio-related functionality.  
The project is designed to run inside a **Python virtual environment** to avoid system conflicts and dependency issues.

## Project Structure

├── main.py # Entry point of the application
├── screen.py # Handles screen / UI-related logic
├── myAudio.py # Handles audio-related functionality
├── README.md # Project documentation


## Requirements
- Python 3.9 or higher
- macOS, Linux, or Windows

- ## Screen Recording FPS & Audio Sync Notes

During development, the screen recording initially appeared **too fast** and ended earlier than the audio recording. This was caused by a **mismatch between the VideoWriter FPS setting and the actual frame capture rate**.

### Root Cause
- OpenCV’s `VideoWriter(fps=...)` does **not** control how fast frames are captured.
- It only tells the video player **how fast to play back the frames**.
- The program was only able to capture approximately **4–5 frames per second** due to screen resolution and processing overhead.
- However, the video was being written with a **higher FPS value**, causing the output video to:
  - Play too fast
  - End earlier than the audio track

### How This Was Fixed
- The actual capture speed was measured in real time.
- The `VideoWriter` FPS was set to **match the real capture rate** (approximately **4.5 FPS**).
- This ensured that the number of frames written matched the playback speed, keeping the video duration aligned with the audio recording.

### Key Takeaway
To maintain proper audio/video synchronization:
- The FPS passed to `cv2.VideoWriter` **must match the real frame capture rate**.
- Using `cv2.waitKey()` to control timing is unreliable and should not be used for FPS control.
- For smoother video, the screen resolution must be reduced or frame capture must be optimized before increasing FPS.

### Recommended Settings (Current Implementation)
- Video FPS: ~4.5 FPS (matches measured capture speed)
- Frame timing based on real capture performance
- Audio recorded independently and merged after recording

This approach ensures correct playback speed and prevents audio/video desynchronization.

Credit: https://forum.opencv.org/t/video-speed-is-very-fast/4269

