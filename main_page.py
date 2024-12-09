import streamlit as st

st.markdown("# Welcome to No Smash!🅿️🚗")
st.sidebar.markdown("# No Smash 🅿️🚗")

st.markdown("# Please Read Below First!📚")
st.write("This app has been designed to work with San Francisco.🌉")
st.write("To get started, click the button below and follow the steps.✅")

st.page_link("pages/1Settings.py", label="1️⃣ Settings: Language options and manually generate an AI Assistant", help="Language options and assistant setup.")
st.page_link("pages/2ReportAnalysis.py", label="2️⃣ Report Analysis: Analyzes a street within given address, streets, and date range. ", help="Analyzes a street within given date range.")
st.page_link("pages/ParkingAdvice.py", label="3️⃣ Parking Advice: General parking advice from AI within given street, date, time, environment, and weather", help="Get general parking advice here.")



#Initialize the session state
if 'source_language' not in st.session_state:
    st.session_state['source_language'] = "English"
if 'target_language' not in st.session_state:
    st.session_state['target_language'] = "English"
