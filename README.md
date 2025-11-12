

---

## 🎯 Motion Detection and Alert System

This Python script implements a **real-time motion detection and alert system** using **OpenCV** and **Pygame**.
It continuously monitors live video feed from the webcam and plays an alert sound whenever motion is detected.

### 🔍 Key Features

* **Real-Time Motion Detection:**
  Continuously compares live frames to a reference frame to detect movement.
* **Automatic Frame Reset:**
  The reference (baseline) frame resets every few seconds (`frame_reset_interval`) to adapt to lighting changes or gradual movements.
* **Timestamp Logging:**
  Each motion event is recorded with a precise timestamp in a text file (`motion_timestamps.txt`).
* **Audio Alert System:**
  Uses `pygame.mixer` to play a sound (`alert.mp3`) whenever significant motion is detected.
* **Smart Cooldown:**
  Prevents repeated alerts using an adjustable cooldown period (`alert_cooldown`).
* **Safe Exit:**
  Press **‘q’** anytime to exit gracefully and release the camera feed.

### ⚙️ Tech Stack

* **OpenCV:** For video capture, frame processing, and motion detection.
* **Pygame Mixer:** For playing alert sounds.
* **Python datetime module:** For timestamp logging.

### 💡 Summary

This script acts as a **lightweight security or activity monitoring tool**, useful for detecting movement in a room, lab, or entrance.
It’s designed for reliability, minimal resources, and easy modification — ideal for projects involving **assistive technology, surveillance, or alert systems**.

---

Would you like me to rewrite your code to make it **clean, formatted, and error-free** (so indentation, imports, and comments are all fixed)? It’d look great in a README or as a separate `.py` file.
