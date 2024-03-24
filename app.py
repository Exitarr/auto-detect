import base64
from flask import Flask, render_template, request
from car_detection import detect_cars

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the form
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        file = request.files['file']
        
        if file.filename == '':
            return 'No selected file'
        
        # Read image file as binary
        image_data = file.read()

        # Pass image data to car_detection.py and get output image
        output_image_data = detect_cars(image_data)
        
        # Encode output image to base64 for display
        output_image_base64 = base64.b64encode(output_image_data).decode('utf-8')
        
        # Encode input image to base64 for display
        encoded_string = base64.b64encode(image_data).decode('utf-8')
        
        # Prepare data to display
        data = {
            'name': name,
            'image': encoded_string,
            'output_image': output_image_base64
        }
        
        return render_template('output.html', data=data)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
