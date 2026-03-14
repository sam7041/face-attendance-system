# Install dependencies before running:
# pip install cmake
# pip install face_recognition
# pip install opencv-python

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# --- Load known faces ---
Sameer_image = face_recognition.load_image_file("faces/Sameer Shukla.jpg")
Peter_image = face_recognition.load_image_file("faces/PeterParker.jpg")

# --- Encode known faces ---
Sameer_encoding = face_recognition.face_encodings(Sameer_image)[0]
Peter_encoding = face_recognition.face_encodings(Peter_image)[0]

# Store encodings and names
known_face_encodings = [Sameer_encoding, Peter_encoding]
known_face_names = ["Sameer", "Peter"]

# Copy list for attendance
students = known_face_names.copy()

# Initialize lists
face_locations = []
face_encodings = []

# Get current date for CSV file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Create CSV file for today's attendance
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Date", "Time"])  # Added Date column

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        name = "Unknown"

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Add text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(
                frame,
                f"{name} Present",
                (10, 100),
                font,
                1.5,
                (255, 0, 0),
                3
            )

            # Mark attendance once per student
            if name in students:
                students.remove(name)
                now = datetime.now()
                date_today = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, date_today, current_time])

    # Display video frame
    cv2.imshow("Attendance", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
f.close()
