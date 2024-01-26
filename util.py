import pdf2image
import base64
import io
import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
PALM_API_KEY = os.getenv("PALM_API_KEY")
genai.configure(api_key=PALM_API_KEY)

def pdf2bytes(upload_file):
    images = pdf2image.convert_from_bytes(pdf_file=upload_file.read(), poppler_path=r'C:\Users\dines\poppler-23.11.0\Library\bin', fmt='jpeg')[:3]
    img_byte_arr = io.BytesIO()
    pdf_parts = {"mime_type": "image/jpeg", "data": ""}
    # images[0].save(img_byte_arr, format='jpeg') # supports single PDF page.
    # pdf_parts["data"] = base64.b64encode(img_byte_arr.getvalue()).decode()
    for val, img in enumerate(images, start=1): # Supports multiple PDF pages.
        img.save(img_byte_arr, format='jpeg')
        pdf_parts["data"] += "\n" + base64.b64encode(img_byte_arr.getvalue()).decode()
    return pdf_parts

def geminiResponse(pdf_upload_file, prompt, job_desc, model_name='gemini-pro-vision'):
    model = genai.GenerativeModel(model_name=model_name)
    pdf_parts = pdf2bytes(pdf_upload_file)
    return model.generate_content([prompt, pdf_parts, job_desc])