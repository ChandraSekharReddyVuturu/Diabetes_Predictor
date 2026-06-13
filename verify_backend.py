import os
import sys

# Append backend folder to path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))

from database import init_db
from downloader import download_all_datasets
from preprocessing import merge_and_preprocess_datasets
from training import train_and_evaluate_all, load_active_model_metadata
from explainability import explain_prediction

def main():
    print("======================================================")
    print("STARTING COMPLETE BACKEND VERIFICATION PIPELINE")
    print("======================================================")
    
    try:
        # Step 1: Initialize the database
        print("\nStep 1: Initializing SQLite Database...")
        init_db()
        print("[SUCCESS] Database initialized successfully.")
        
        # Step 2: Fetch raw datasets
        print("\nStep 2: Downloading/Simulating Datasets...")
        results = download_all_datasets()
        print(f"[SUCCESS] Dataset download results: {results}")
        
        # Step 3: Align, clean, and merge datasets
        print("\nStep 3: Executing Preprocessing and Alignment Pipeline...")
        X_train, X_test, y_train, y_test = merge_and_preprocess_datasets()
        print(f"[SUCCESS] Data preprocessing completed. Train shape: {X_train.shape}, Test shape: {X_test.shape}")
        
        # Step 4: Run multi-model training loop
        print("\nStep 4: Running Multi-Model Training and Selection Loop...")
        best_name, metrics = train_and_evaluate_all(X_train, X_test, y_train, y_test)
        print(f"[SUCCESS] Model training complete. Selected Best Model: {best_name}")
        
        # Step 5: Verify explainability and predictions
        print("\nStep 5: Testing Predictor and SHAP Explainability Engine...")
        sample_patient = {
            "patient_name": "Test Patient Verification",
            "Pregnancies": 1,
            "Glucose": 135.0,
            "BloodPressure": 80.0,
            "SkinThickness": 20.0,
            "Insulin": 85.0,
            "BMI": 29.5,
            "DiabetesPedigreeFunction": 0.40,
            "Age": 42,
            "Gender": 0, # Female
            "Height": 162.0,
            "Weight": 77.4,
            "HbA1c": 5.8,
            "PhysicalActivity": 1,
            "SmokingStatus": 0,
            "FamilyHistory": 1
        }
        res = explain_prediction(sample_patient)
        print(f"Prediction output prediction code: {res['prediction']}")
        print(f"Diabetes Risk probability: {res['risk_score']}%")
        print(f"Explainable AI top positive drivers (SHAP values): {list(res['shap_values'].keys())[:3]}")
        print(f"Generated AI Clinical summary: '{res['summary']}'")
        
        print("\n======================================================")
        print("BACKEND VERIFICATION SUCCESSFUL - CORE ML ENGINE READY")
        print("======================================================")
        
    except Exception as e:
        print(f"\n[FATAL ERROR] Pipeline verification failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
