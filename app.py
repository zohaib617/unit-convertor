import streamlit as st 

st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight And Time Isntantly")
st.write("Welocme! Slect A Category, enter a value and get the coverted result in real time ")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to pound":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Second to minuts":
            return value / 60
        elif unit == "Minuts to seconds":
            return value * 60
        elif unit == "Minuts to Hours":
            return value / 60
        elif unit == "Hours to minuts":
            return value * 60
        elif unit == "Hours to day":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        return 0
    
if category == "Length":
    unit = st.selectbox("📏 Select Conversation", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation", ["Kilograms to pound","Pounds to kilograms"])
    
elif category == "Time":
    unit = st.selectbox("⏲ Select Conversation",["Second to minuts","Minuts to seconds","Minuts to Hours","Hours to minuts","Hours to day","Days to hours"])
    
value = st.number_input("Enter value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit ) # type: ignore
    st.success(f"The rsult is {result:.2f}") 