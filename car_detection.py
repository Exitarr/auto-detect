import cv2
import numpy as np

def detect_cars(input_image_data):
    # Convert binary data to numpy array
    nparr = np.fromstring(input_image_data, np.uint8)

    # Decode numpy array to image
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    # Load the pre-trained car classifier
    car_cascade = cv2.CascadeClassifier('static/cars.xml')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gauss_image = cv2.GaussianBlur(gray_image, (5, 5), 0)


    # Detect cars in the image
    cars = car_cascade.detectMultiScale(gauss_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #cars = car_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=7, minSize=(60, 60))

    # Draw rectangles around the detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Encode image to binary data

    retval, buffer = cv2.imencode('.jpg', image)
    output_image_data = buffer.tobytes()

    return output_image_data