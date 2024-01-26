# APPLICATION(RESUME) TRACKING SYSTEM.

# HOW TO RUN?
### STEPS:

clone the repository

```bash
Project Repo: https://github.com/dinesh1618/ATS-System-LLM--Google-Gemini-.git
```

### STEP 01:- Create a conda environment

```bash
conda install -n infoapp python3.8 -y
```

```bash
conda activate infoapp
```

### STEP 02:- Install  packages
```bash
pip install -r requirements.txt
```

### STEP 03:- Create a GOOGLE API KEY from https://makersuite.google.com/ and replace in .env file
```bash
PALM_API_KEY=*******************************
```

### STEP 04:- Download " poppler" zip file from "https://pypi.org/project/pdf2image/" to support "pdf2image" library. Replace with "poppler_path" in util.py file or set "bin" PATH to environment.

### STEP 05:- Run app.py
```bash
python -m streamlit run app.py
```