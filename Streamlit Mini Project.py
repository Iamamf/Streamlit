# Import the Streamlit library
import streamlit as st 

# Give a title to the app
st.title('Welcome to the BMI Calculator') 

# Take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0, step=0.1)

# Take height input with a radio button to choose height format
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

# Height input based on the selected format
if status == 'cms':
    height = st.number_input('Height in centimeters', min_value=0.0, step=0.1)
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
    else:
        bmi = None

elif status == 'meters':
    height = st.number_input('Height in meters', min_value=0.0, step=0.01)
    if height > 0:
        bmi = weight / (height ** 2)
    else:
        bmi = None

else:  # status == 'feet'
    height = st.number_input('Height in feet', min_value=0.0, step=0.1)
    if height > 0:
        bmi = weight / (((height / 3.28)) ** 2)
    else:
        bmi = None

# Calculate BMI when button is clicked
if st.button('Calculate BMI'):
    if bmi:
        st.text(f"Your BMI Index is {bmi:.2f}.")  # Formatting to 2 decimal places

        # Provide interpretation based on BMI value
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:  # bmi >= 30
            st.error("Extremely Overweight")
    else:
        st.warning("Please enter a valid height greater than 0.")
