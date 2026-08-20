import os

def create_files():
    base_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Performance Prediction System</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --bg-color: #f0fdfa;
            --card-bg: #ffffff;
            --text-main: #1f2937;
            --text-muted: #6b7280;
            --border-color: #e5e7eb;
            --pass-color: #10b981;
            --pass-bg: #f0fdf4;
            --fail-color: #ef4444;
            --fail-bg: #fef2f2;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 3rem 1rem;
            margin: 0;
            box-sizing: border-box;
        }

        .header {
            text-align: center;
            margin-bottom: 2rem;
        }

        .header h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.5rem;
        }

        .header p {
            color: var(--text-muted);
            font-size: 1rem;
        }

        .pass-text { color: var(--pass-color); font-weight: 600; }
        .fail-text { color: var(--fail-color); font-weight: 600; }

        .container {
            width: 100%;
            max-width: 650px;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .card {
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            padding: 2.5rem;
            border: 1px solid var(--border-color);
        }

        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            color: var(--primary);
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }

        .divider::before,
        .divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid #d1d5db;
        }

        .divider:not(:empty)::before {
            margin-right: 1rem;
        }

        .divider:not(:empty)::after {
            margin-left: 1rem;
        }

        .divider svg {
            width: 20px;
            height: 20px;
            margin-right: 8px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .form-group {
            display: flex;
            gap: 1.25rem;
            margin-bottom: 1.5rem;
        }

        .icon-box {
            width: 56px;
            height: 56px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .icon-box svg {
            width: 28px;
            height: 28px;
            fill: currentColor;
        }

        .icon-attendance { background: #e0e7ff; color: #4f46e5; }
        .icon-study { background: #dcfce7; color: #16a34a; }
        .icon-marks { background: #f3e8ff; color: #9333ea; }

        .input-content {
            flex: 1;
        }

        .input-content label {
            display: block;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: #1f2937;
        }

        .form-control {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 1rem;
            transition: all 0.2s;
            box-sizing: border-box;
            color: #111827;
        }

        .form-control::placeholder {
            color: #9ca3af;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }

        .help-text {
            display: block;
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 0.5rem;
        }

        .btn-submit {
            width: 100%;
            padding: 1rem;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            transition: background 0.2s;
            margin-top: 1rem;
        }

        .btn-submit:hover {
            background: var(--primary-hover);
        }

        .btn-submit svg {
            width: 20px;
            height: 20px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .result-card {
            border: 1px solid var(--pass-color);
            border-radius: 8px;
            padding: 1.5rem 2rem;
            display: flex;
            align-items: center;
            gap: 1.5rem;
            background: var(--pass-bg);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        
        .result-card.fail {
            background: var(--fail-bg);
            border-color: var(--fail-color);
        }

        .result-icon {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #d1fae5;
            color: #059669;
        }
        
        .result-card.fail .result-icon {
            background: #fee2e2;
            color: #dc2626;
        }

        .result-icon svg {
            width: 40px;
            height: 40px;
            fill: none;
            stroke: currentColor;
            stroke-width: 3;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .result-content {
            flex: 1;
        }

        .result-content h3 {
            margin: 0 0 0.5rem 0;
            font-size: 1.1rem;
            color: #065f46;
            font-weight: 600;
        }
        
        .result-card.fail .result-content h3 {
            color: #991b1b;
        }

        .result-content .status {
            font-size: 1.8rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
            color: var(--pass-color);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .result-card.fail .result-content .status {
            color: var(--fail-color);
        }

        .result-content p {
            margin: 0;
            color: #064e3b;
            font-size: 0.95rem;
        }
        
        .result-card.fail .result-content p {
            color: #7f1d1d;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Student Performance Prediction System</h1>
        <p>Enter student details below to predict whether the student is likely to <span class="pass-text">Pass</span> or <span class="fail-text">Fail</span>.</p>
    </div>

    <div class="container">
        <div class="card">
            <div class="divider">
                <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                Enter Student Details
            </div>
            
            <form action="/predict" method="POST">
                <div class="form-group">
                    <div class="icon-box icon-attendance">
                        <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    </div>
                    <div class="input-content">
                        <label>Attendance Percentage (%)</label>
                        <input type="number" name="attendance" class="form-control" placeholder="e.g. 85" min="0" max="100" step="1" required {attendance_value}>
                        <span class="help-text">Enter attendance percentage (0 - 100)</span>
                    </div>
                </div>

                <div class="form-group">
                    <div class="icon-box icon-study">
                        <svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    </div>
                    <div class="input-content">
                        <label>Study Hours per Day</label>
                        <input type="number" name="study_hours" class="form-control" placeholder="e.g. 3" min="0" max="24" step="0.1" required {study_hours_value}>
                        <span class="help-text">Enter average study hours per day</span>
                    </div>
                </div>

                <div class="form-group">
                    <div class="icon-box icon-marks">
                        <svg viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
                    </div>
                    <div class="input-content">
                        <label>Previous Exam Marks (%)</label>
                        <input type="number" name="previous_marks" class="form-control" placeholder="e.g. 70" min="0" max="100" step="1" required {previous_marks_value}>
                        <span class="help-text">Enter previous exam marks (0 - 100)</span>
                    </div>
                </div>

                <button type="submit" class="btn-submit">
                    <svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                    Predict Result
                </button>
            </form>
        </div>
"""

    index_html = base_head.replace("{attendance_value}", "").replace("{study_hours_value}", "").replace("{previous_marks_value}", "") + """
    </div>
</body>
</html>
"""

    result_html = base_head.replace("{attendance_value}", 'value="{{ attendance }}"').replace("{study_hours_value}", 'value="{{ study_hours }}"').replace("{previous_marks_value}", 'value="{{ previous_marks }}"') + """
        <div class="result-card {% if result == 'FAIL' %}fail{% endif %}">
            <div class="result-icon">
                {% if result == 'PASS' %}
                <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
                {% else %}
                <svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                {% endif %}
            </div>
            <div class="result-content">
                <h3>Prediction Result</h3>
                <div class="status">
                    {{ result }}
                    {% if result == 'PASS' %}😊{% else %}😞{% endif %}
                </div>
                <p>The student is likely to <strong>{{ result }}</strong>.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

    with open(r'c:\Users\acer\Desktop\project.py\templates\index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    with open(r'c:\Users\acer\Desktop\project.py\templates\result.html', 'w', encoding='utf-8') as f:
        f.write(result_html)

if __name__ == '__main__':
    create_files()
