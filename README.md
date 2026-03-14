# Face Recognition Attendance System

A simple **Face Recognition based Attendance System** built using Python, OpenCV, and the face_recognition library.  
The system detects and recognizes faces through a webcam and automatically marks attendance in a CSV file with the date and time.

---

## Features

- Real-time face detection using webcam
- Face recognition using pre-trained encodings
- Automatic attendance marking
- Stores attendance in CSV file
- Each entry includes:
  - Name
  - Date
  - Time
- Prevents duplicate attendance entries for the same session

---

## Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- CSV module

---

## Project Structure

```
face-attendance-system
│
├── faces/                # Folder containing images of known people
│   ├── Sameer Shukla.jpg
│   └── PeterParker.jpg
│
├── main.py               # Main program file
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/face-attendance-system.git
cd face-attendance-system
```

### 2. Install dependencies

```bash
pip install cmake
pip install face_recognition
pip install opencv-python
```

OR

```bash
pip install -r requirements.txt
```

---

## How It Works

1. The system loads images of known people from the `faces` folder.
2. It generates **face encodings** for each image.
3. The webcam captures video in real-time.
4. Faces detected in the frame are compared with known encodings.
5. If a match is found:
   - The name is displayed on the screen.
   - Attendance is recorded in a CSV file.
6. Attendance is recorded **only once per person per session**.

---

## Output

The system generates a CSV file named with the current date:

```
YYYY-MM-DD.csv
```

Example:

```
Name,Date,Time
Sameer,2026-03-14,10:23:45
Peter,2026-03-14,10:25:10
```

---

## Future Improvements

- GUI interface
- Database integration (MySQL / Firebase)
- Multiple face detection optimization
- Cloud-based attendance storage
- Mobile camera integration

---

## Author

Developed by **Sameer Shukla**

---

## License

This project is open-source and available under the MIT License.
