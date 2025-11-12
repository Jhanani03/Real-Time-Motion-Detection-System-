import cv2
import
timefrom pygame import mixer
from datetime import datetime
# Initialize pygame mixer and alert sound
mixer.init()
alert_sound = 'alert.mp3'
def play_sound():
mixer.music.load(alert_sound)
mixer.music.play()
# Paths and initial settings
timestamps_file = r'C:\Users\kb684\Desktop\system\motion_timestamps.txt'
video_capture = cv2.VideoCapture(0)
first_frame = None
frame_reset_interval = 5
alert_cooldown = 10
last_reset_time = time.time()
last_alert_time = time.time() - alert_cooldown
def
detect_motion(gray_frame):
global first_frame
if first_frame is
None: return False
delta_frame = cv2.absdiff(first_frame, gray_frame)
threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)
contours,
_
=
cv2.findContours(threshold_frame.copy(),
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
return any(cv2.contourArea(c) > 500 for c in contours)
with open(timestamps_file, 'a') as f:
while True:
check, frame = video_capture.read()if not check:
print("Failed to grab frame.
Exiting...") break
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
# Reset the first frame
periodically current_time =
time.time()
if first_frame is None or (current_time - last_reset_time) > frame_reset_interval:
first_frame = gray_frame
last_reset_time = current_time
continue
# Detect motion and handle
alerts if
detect_motion(gray_frame):
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Motion detected at: {timestamp}")
f.write(f"Motion detected at: {timestamp}\n")
f.flush()
if current_time - last_alert_time >
alert_cooldown: play_sound()
last_alert_time = current_time
cv2.imshow("Video Feed", frame)
if cv2.waitKey(1) & 0xFF ==
ord('q'): print("Exiting the
program...") break
# Cleanup mixer.music.stop()
video_capture.release()
cv2.destroyAllWindows()
print("Program terminated.")

