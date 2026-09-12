from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# This must match your exact Excel file name
EXCEL_FILE = 'SYNERGY_PROJECT_CONTROL_TOWER_WORLD_CLASS_V3_COMPLETE.xlsx'

# Mapping app roles to your Excel sheet names
ROLE_MAP = {
    'sponsor': '01_Sponsor',
    'pm': '04_PM_Control',
    'team': '05_Team_Command'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data/<role>')
def get_data(role):
    if role not in ROLE_MAP or not os.path.exists(EXCEL_FILE):
        return jsonify([]) # Return empty if no file or role match
        
    try:
        # Read the first 4 rows of the matching Excel sheet
        df = pd.read_excel(EXCEL_FILE, sheet_name=ROLE_MAP[role]).head(4)
        df = df.fillna("N/A") # Replace empty Excel cells with N/A
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        print(f"Error reading Excel: {e}")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
