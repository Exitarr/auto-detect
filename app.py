import os
import json
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to save data to JSON file
def save_to_json(data):
    db_file = os.path.join('static/uploads', 'db.json')
    if os.path.exists(db_file):
        with open(db_file, 'r') as f:
            db = json.load(f)
    else:
        db = []
    
    db.append(data)
    
    with open(db_file, 'w') as f:
        json.dump(db, f, indent=4)

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
        
        # Encode image to base64
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
        
        # Prepare data to save
        data = {
            'id': len(os.listdir('static/uploads')) + 1,  # Generate ID based on number of files
            'name': name,
            'image': encoded_string
        }
        
        # Save data to JSON file
        save_to_json(data)
        
        return render_template('output.html',id=data['id'], name=data['name'], image=data['image'])
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
