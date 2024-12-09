import os
import openai
import streamlit as st
import pandas as pd
from openai import OpenAI

st.sidebar.markdown("# Settings ⚙️")

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

languages = pd.read_csv('datasets/world-languages-simple.csv')

with st.form(key="settings"):

    st.title("Language Settings")
    c1, c2 = st.columns([1, 1], gap="medium")
    with c1:
        st.session_state['source_language'] = st.selectbox('Select Input Language', languages)
    with c2:
        st.session_state['target_language'] = st.selectbox('Select Output Language', languages)
    st.form_submit_button("Confirm changes")

    st.title("Assistant Setup")
    c3, c4 = st.columns([1, 1], gap="medium")
    with c3:
        create_submitted = st.form_submit_button("Create assistant")
        st.caption("Creates an assistant and uploads the associated 24.6MB dataset.")
    with c4:
        cleanup_submited = st.form_submit_button("Cleanup")
        st.caption("Deletes the dataset associated with your assistant.")
    st.caption("Check assistants at: https://platform.openai.com/assistants")

    if create_submitted:
        file = client.files.create(
        file=open("datasets/SF_050124_INTERSECTIONS.csv", "rb"),
        purpose='assistants'
        )

        assistant = client.beta.assistants.create(
            name="Vehicle Theft Data Analysis",
            instructions="\
            You will receive a point and date range from a .csv file (from January 2018 to May 2024) for analysis.\n\
            # 1. With the date range, check the number of incidents that occurred in that range and tell the user. Don't check the file if the date range is invalid. Immediately stop.\n\
            # 2. With the street name, check the intersections. Pay attention under the incident_description column for the number of incidents.\n\
            # 3. Tell the user the overall number of incidents in the city that occurred within that date range compared to the number of incidents that occurred that occurred within that date range for the given street.\n\
            Keep it text only.\n\
            Take a break before responding and make sure you are returning accurate info.",
            tools=[{"type": "code_interpreter"}],
            file_ids=[file.id],
            model="gpt-3.5-turbo",
            )

        if 'assistant_key' not in st.session_state:
            st.session_state['assistant'] = assistant.id
        if 'file_key' not in st.session_state:
            st.session_state['file'] = file.id

    if cleanup_submited:
        client.beta.assistants.files.delete(
            assistant_id=st.session_state['assistant'],
            file_id=st.session_state['file']
            )