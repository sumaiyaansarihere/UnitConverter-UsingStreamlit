
import streamlit as st


# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #8A2BE2; /* Dark Blue */
        color: white;
    }
    
    /* Make selectbox text white */
    div[data-baseweb="select"] > div {
        color: white !important;
             background: black !important;
    }
    
    /* Style all input boxes (text fields) */
    input {
        color: white !important;  /* Text inside input */
        background-color: black !important; /* Input box background */
        border: 2px solid white !important;
        padding: 8px;
        border-radius: 5px;
    }

    /* Make labels (headers) white */
    label {
        color: white !important;
       
    }

    /* Style the Convert button */
    div.stButton > button {
        background-color: black !important;
        color: white !important;
        border-radius: 10px;
        padding: 8px 20px;
        font-size: 16px;
        border: 2px solid white;
    }
    </style>
    """, unsafe_allow_html=True)



st.title("🚀 Unit Converter App")
st.markdown("### ( Converts Length, Weight & Time Instantly! )")
st.write("Welcome! Select a category, enter a value & get the converted result in seconds!")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60 
        elif unit == "Hours to Minutes":
            return value * 60 
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24 



if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"]) 
elif category == "Time":
    unit = st.selectbox("⌛ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])  


value = st.number_input("Enter the value to convert...", min_value=0.0, format="%.2f")

# Convert and Display Result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is: {result:.2f}")
    else:
        st.error("Something went wrong! Please check your input.")

                      


