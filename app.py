from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = 'SYNERGY_PROJECT_CONTROL_TOWER_WORLD_CLASS_V3_COMPLETE.xlsx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data/<role>')
def get_data(role):
    try:
        if not os.path.exists(EXCEL_FILE):
            return jsonify([{"Metric": "Excel file missing", "Value": "Check filename"}])
            
        df = pd.read_excel(EXCEL_FILE)
        
        data = []
        for _, row in df.iterrows():
            title = str(row.iloc[0]) if len(row) > 0 else "Metric"
            val = str(row.iloc[1]) if len(row) > 1 else "N/A"
            data.append({ "title": title, "value": val })
            
        return jsonify(data)
    except Exception as e:
        return jsonify([{"Metric": "Error reading file", "Value": str(e)}])

if __name__ == '__main__':
    app.run(debug=True)
