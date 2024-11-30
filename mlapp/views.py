# mlapp/views.py
from django.shortcuts import render
from joblib import load

def predict(request):
    prediction = None  # Initialize prediction variable
    
    if request.method == 'GET':
        # Get the input value from the query string (years of experience)
        x_value = request.GET.get('x')
        
        if x_value:
            try:
                # Convert the input value to float
                x_value = float(x_value)
                
                # Load the trained model
                model = load('mlapp/model.joblib')

                # Make the prediction using the model
                prediction = model.predict([[x_value*100]])[0]  # Get the prediction (first item)
            
            except ValueError:
                # In case of invalid input
                prediction = "Invalid input, please enter a number."

    # Render the 'predict.html' template and pass the prediction to the context
    return render(request, 'mlapp/predict.html', {'prediction': prediction})
# mlapp/views.py
from django.shortcuts import render
from joblib import load

def index(request):
    # Simply render a welcome page or home page
    return render(request, 'mlapp/index.html')
