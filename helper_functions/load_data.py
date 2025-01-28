import os
import pandas as pd

def load_data(file_name):
    if os.path.exists(file_name):
        return pd.read_excel(file_name, engine="openpyxl", dtype=str)
    else:
        return pd.DataFrame(columns=["ADDRESS", "EMAIL", "PHONE #", "AGE", "EMP ID", "DOD ID", "M/F", "SSN", "NAME (UMR)",
                                     "RANK", "MOS", "PHASE", "RSID", "ENLISTMENT", "SHIP", "RETURN", "UIC", "STATE",
                                     "OPAT", "OPAT LV", "HEIGHT", "MAX WT", "FINSERVE", "M/S", "DEP", "FLU SHOT"])
