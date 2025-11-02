# Medical Summary Generator

AI-powered medical summary generator for brain tumor EHR data with ICD-10 coding.

## Features
- Generate professional medical summaries from patient IDs
- Automatic ICD-10 code assignment
- SQLite database with 1000+ patient records
- Includes patient details, lab reports, MRI analysis, and prescriptions

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python run_summary.py
# Enter Patient ID (P0001 to P1000)
```

## Sample Output
```
PATIENT SUMMARY:

Patient P0005 is a 63-year-old female diagnosed with glioma (ICD-10: C71.9).
MRI findings: Tumor observed in left temporal region. Confidence score: 0.84. 
Treatment: Levetiracetam 500mg Twice daily. Procedure: MRI + Contrast. 
Outcome: Under Observation. Recommended regular follow-up and monitoring.
```

## Database Schema
- **patient_details**: Demographics, conditions, procedures
- **lab_reports**: Blood tests and lab values  
- **mri_analysis_results**: MRI scans and observations
- **prescription**: Medications and dosages

## MRI ANALYSIS RESULT:
For Image_name is collected from the below link: https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset


