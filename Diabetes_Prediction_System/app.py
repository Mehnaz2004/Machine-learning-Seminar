import streamlit as st
import pickle as pkl

# Load the trained model
modelfile = open("model.pkl", "rb")
model = pkl.load(modelfile)
modelfile.close()

# Define the prediction function
def predict_diabetes(glucose, bloodpressure):
    glucose = float(glucose)
    bloodpressure = float(bloodpressure)

    # Make a prediction using the trained model
    prediction = model.predict([[glucose, bloodpressure]])
    if prediction[0] == 0:
        return "Non-Diabetic"
    else:
        return "Diabetic"

# Streamlit application
st.title("Diabetes Prediction App")  # Sets the title of the app

st.write("This app predicts whether a person is diabetic or non-diabetic based on glucose and blood pressure levels.")  # Provides a brief description of the app

# Input fields for glucose and blood pressure
glucose_input = st.text_input("Enter glucose level:")  # Text input for glucose level with an empty string as the default value
bloodpressure_input = st.text_input("Enter blood pressure level:")  # Text input for blood pressure level with an empty string as the default value

# Predict button
if st.button("Predict"):  # Button that triggers the prediction logic when clicked
    if glucose_input and bloodpressure_input:  # Ensures both inputs are provided
        try:
            # Get prediction
            prediction = predict_diabetes(glucose_input, bloodpressure_input)  # Calls the prediction function with user inputs
            st.success(f"Prediction: {prediction}")  # Displays the prediction result in a success message box
        except ValueError:
            st.error("Please enter valid numeric values for glucose and blood pressure.")  # Shows an error message for invalid numeric inputs
    else:
        st.warning("Please fill in both glucose and blood pressure levels.")  # Warns the user if inputs are missing
