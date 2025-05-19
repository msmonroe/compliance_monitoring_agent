import pandas as pd

def load_logs(filepath):
    try:
        df = pd.read_csv(filepath)
        required_columns = {"timestamp", "username", "action", "ip", "status", "message"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"Missing required columns. Found columns: {df.columns.tolist()}")
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"[ERROR] Failed to load logs: {e}")
        return []
