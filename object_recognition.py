```python
import cv2
import numpy as np
import tensorflow as tf

class ObjectRecognition:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    def preprocess_image(self, image):
        # Resize and normalize the image for the model
        image = cv2.resize(image, (224, 224))
        image = image.astype('float32') / 255
        image = np.expand_dims(image, axis=0)
        return image

    def predict_object(self, image):
        # Preprocess the image and predict the object
        image = self.preprocess_image(image)
        prediction = self.model.predict(image)
        return np.argmax(prediction)

    def recognize_and_track(self, video_path):
        # Open the video file
        video = cv2.VideoCapture(video_path)

        while(video.isOpened()):
            ret, frame = video.read()
            if not ret:
                break

            # Recognize the object in the frame
            object_id = self.predict_object(frame)
            print(f'Recognized object: {object_id}')

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video capture and close windows
        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    object_recognition = ObjectRecognition('path_to_your_model.h5')
    object_recognition.recognize_and_track('path_to_your_video.mp4')
```
