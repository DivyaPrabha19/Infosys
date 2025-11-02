import sqlite3

# Simple version without transformers
def get_patient_summary(patient_id):
    conn = sqlite3.connect('brain_tumor_ehr_fixed.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM patient_details WHERE Patient_ID = ?", (patient_id.strip(),))
    patient = cursor.fetchone()
    
    if not patient:
        return f"No patient found with ID: {patient_id}"
    
    cursor.execute("SELECT * FROM mri_analysis_results WHERE Patient_ID = ?", (patient_id.strip(),))
    mri = cursor.fetchone()
    
    cursor.execute("SELECT * FROM prescription WHERE Patient_ID = ?", (patient_id.strip(),))
    prescription = cursor.fetchone()
    
    conn.close()
    
    name, age, gender = patient[1], patient[2], patient[3]
    condition = patient[4].lower()
    procedure = patient[5]
    outcome = patient[7]
    
    # ICD codes
    icd_code = "C71.0" if "glioblastoma" in condition else "C71.9" if "glioma" in condition or "tumor" in condition else "Z51.11"
    
    summary = f"""PATIENT SUMMARY:

Patient {patient_id} is a {age}-year-old {gender.lower()} diagnosed with {condition} (ICD-10: {icd_code}).
"""
    
    if mri:
        summary += f"MRI findings: {mri[4]}. Confidence score: {mri[3]}. "
    
    if prescription:
        summary += f"Treatment: {prescription[2]} {prescription[3]} {prescription[4]}. "
    
    summary += f"Procedure: {procedure}. Outcome: {outcome}. Recommended regular follow-up and monitoring."
    
    return summary

# Test with different patients
patient_id = input("Enter Patient ID: ")
print(get_patient_summary(patient_id))