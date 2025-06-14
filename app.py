from flask import Flask, render_template, request
import pickle
import pandas as pd 
import time

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    # Simulate delay for processing
    time.sleep(3)

    # Retrieve form data
    try:
        square_feet = float(request.form.get('squareFeet'))
        bedrooms = int(request.form.get('bedrooms'))
        bathrooms = int(request.form.get('bathrooms'))
        garden_available = 1 if request.form.get('gardenAvailable') == 'Yes' else 0
        pool_available = 1 if request.form.get('poolAvailable') == 'Yes' else 0
        year_built = int(request.form.get('yearBuilt'))
        floor_level = int(request.form.get('floor_level'))
        location_score = float(request.form.get('locationScore'))
        distance_to_center = float(request.form.get('distanceToCenter'))
        garage_size = float(request.form.get('garage_size'))
    except (ValueError, TypeError):
        return render_template('index.html', prediction_text="Error: Please fill in all fields correctly.")

    # Prepare input data for prediction (you can modify this according to the expected features)
    input_data = pd.DataFrame({
        'Square_Feet': [square_feet],
        'Num_Bedrooms': [bedrooms],
        'Num_Bathrooms': [bathrooms],
        'Num_Floors': [floor_level],
        'Year_Built': [year_built],
        'Has_Garden': [garden_available],
        'Has_Pool': [pool_available],
        'Garage_Size': [garage_size],
        'Location_Score': [location_score],
        'Distance_to_Center': [distance_to_center]
    })

    # Predict using the model
    predicted_price = model.predict(input_data)
    
    # Display the prediction result
    return render_template(
        'index.html', 
        prediction_text=f'Estimated House Price: ${predicted_price[0]:,.2f}'
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
