import cv2
from deepface import DeepFace
import threading

cam = cv2.VideoCapture(0)
points = []

def emotion_predict(frame):
    global points
    try:
        result = DeepFace.analyze(frame, actions=['emotion'])
        if isinstance(result, list) and len(result) > 0:
            for face in result:
                if 'region' in face and 'dominant_emotion' in face:
                    x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
                    emotion = face['dominant_emotion']
                    points = [x, y, w, h, emotion]
                else:
                    print("No face detected or no emotion found.")
        else:
            print("No valid result returned.")
    except Exception as e:
        print(f"Error in emotion prediction: {e}")

def cam_runner():
    global points
    count = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            raise Exception("Failed to capture image")
        
        if count % 30 == 0:
            threading.Thread(target=emotion_predict, args=(frame,)).start()

        if points:
            x, y, w, h, emotion = points
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            print(f"Emotion: {emotion}")

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

    cam.release()
    cv2.destroyAllWindows()

def video_runner(video_path):
    global points
    cam = cv2.VideoCapture(video_path)
    count = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        
        if count % 30 == 0:
            threading.Thread(target=emotion_predict, args=(frame,)).start()

        if points:
            x, y, w, h, emotion = points
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

    cam.release()
    cv2.destroyAllWindows()

def image_runner(image_path):
    global points
    image = cv2.imread(image_path)
    threading.Thread(target=emotion_predict, args=(image,)).start()

    while True:
        if points:
            x, y, w, h, emotion = points
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(image, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Emotion Detection', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    source = input("Enter the source (webcam, video file path, or image file path): ").strip()
    if source == 'webcam':
        cam_runner()
    elif source.endswith(('.mp4', '.avi', '.mov')):
        video_runner(source)
    elif source.endswith(('.jpg', '.jpeg', '.png')):
        image_runner(source)
    else:
        raise ValueError("Unsupported source type. Use 'webcam', video file path, or image file path.")

