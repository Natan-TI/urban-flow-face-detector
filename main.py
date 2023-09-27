import cv2
import dlib

# Load dlib face detector
detector = dlib.get_frontal_face_detector()

# Start webcan video
cap = cv2.VideoCapture(0)

while True:
    # Capture a webcam frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    # Count the number of faces detected
    num_faces = len(faces)

    # Draw rectangles around detected faces
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # View the number of people detected
    cv2.putText(frame, f'Pessoas: {num_faces}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # View the resulting frame
    cv2.imshow('Detecção Facial', frame)

    # Check if the user pressed the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close the window
cap.release()
cv2.destroyAllWindows()
