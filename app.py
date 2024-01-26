import streamlit as st
from util import geminiResponse


input_prompt = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

st.set_page_config('Application Tracking System')
st.title('Application Tracking System')
job_desc = st.text_area(label='Add Job Descrption')
upload_file = st.file_uploader(label='Upload your Resume in PDF File only')
if st.button(label='submit'):
    if upload_file:
        with st.spinner(text='Waiting for model response...'):
            data = geminiResponse(pdf_upload_file=upload_file,
                                  prompt=input_prompt,
                                  job_desc=job_desc)
            st.write(data.text)
    else:
        st.write('Please upload your resume.')
        


