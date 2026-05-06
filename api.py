# from flask import Flask, jsonify
# import pymysql
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# DB_CONFIG = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASSWORD"),
#     "database": os.getenv("DB_NAME")
# }

# def get_connection():
#     return pymysql.connect(**DB_CONFIG)

# # ================= TOTAL PATIENTS =================
# @app.route('/total-patients')
# def total_patients():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT COUNT(*) FROM dc_patient_billing")
#     count = cursor.fetchone()[0]

#     conn.close()
#     return jsonify({"total_patients": count})


# # ================= LAST DIALYSIS =================
# @app.route('/last-dialysis/<patient_id>')
# def last_dialysis(patient_id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT MAX(billing_date)
#     FROM dc_patient_billing
#     WHERE patient_id = %s
#     """
#     cursor.execute(query, (patient_id,))
#     result = cursor.fetchone()[0]

#     conn.close()
#     return jsonify({"last_dialysis": str(result)})


# # ================= TOP BRANCHES =================
# @app.route('/top-branches')
# def top_branches():
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT branch_name, COUNT(patient_id) AS patient_count
#     FROM dc_patient_billing
#     GROUP BY branch_name
#     ORDER BY patient_count DESC
#     LIMIT 5
#     """
#     cursor.execute(query)
#     result = cursor.fetchall()

#     conn.close()

#     data = []
#     for row in result:
#         data.append({
#             "branch_name": row[0],
#             "patient_count": row[1]
#         })

#     return jsonify({"top_branches": data})


# # ================= BILLING =================
# @app.route('/billing')
# def billing():
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT COUNT(patient_id)
#     FROM dc_patient_billing
#     WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
#     """
#     cursor.execute(query)
#     total = cursor.fetchone()[0]

#     conn.close()

#     return jsonify({"billing": total})


# # ================= RUN =================
# if __name__ == "__main__":
#     app.run(debug=True)

# ----------API Secured -----------------------

# from flask import Flask, jsonify, request
# import pymysql
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# API_KEY = os.getenv("API_KEY")

# DB_CONFIG = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASSWORD"),
#     "database": os.getenv("DB_NAME")
# }

# def get_connection():
#     return pymysql.connect(**DB_CONFIG)

# def check_api_key():
#     key = request.headers.get("x-api-key")
#     return key == API_KEY

# # ================= TOTAL PATIENTS =================
# @app.route('/total-patients')
# def total_patients():
#     if not check_api_key():
#         return jsonify({"error": "Unauthorized"}), 401

#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT COUNT(*) FROM dc_patient_billing")
#     count = cursor.fetchone()[0]

#     conn.close()
#     return jsonify({"total_patients": count})

# # ================= LAST DIALYSIS =================
# @app.route('/last-dialysis/<patient_id>')
# def last_dialysis(patient_id):
#     if not check_api_key():
#         return jsonify({"error": "Unauthorized"}), 401

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT MAX(billing_date)
#     FROM dc_patient_billing
#     WHERE patient_id = %s
#     """
#     cursor.execute(query, (patient_id,))
#     result = cursor.fetchone()[0]

#     conn.close()
#     return jsonify({"last_dialysis": str(result)})

# # ================= TOP BRANCHES =================
# @app.route('/top-branches')
# def top_branches():
#     if not check_api_key():
#         return jsonify({"error": "Unauthorized"}), 401

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT branch_name, COUNT(patient_id) AS patient_count
#     FROM dc_patient_billing
#     GROUP BY branch_name
#     ORDER BY patient_count DESC
#     LIMIT 5
#     """
#     cursor.execute(query)
#     result = cursor.fetchall()

#     conn.close()

#     data = [{"branch_name": r[0], "patient_count": r[1]} for r in result]

#     return jsonify({"top_branches": data})

# # ================= BILLING =================
# @app.route('/billing')
# def billing():
#     if not check_api_key():
#         return jsonify({"error": "Unauthorized"}), 401

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     SELECT COUNT(patient_id)
#     FROM dc_patient_billing
#     WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
#     """
#     cursor.execute(query)
#     total = cursor.fetchone()[0]

#     conn.close()

#     return jsonify({"billing": total})

# # ================= RUN =================
# if __name__ == "__main__":
#     app.run(debug=True)

# ----------- submenu updated with sql logic -------------------

from flask import Flask, jsonify, request
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def get_connection():
    return pymysql.connect(**DB_CONFIG)

def check_api_key():
    return request.headers.get("x-api-key") == API_KEY

# ================= BILLING TOTAL =================
@app.route('/billing-total')
def billing_total():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(patient_id) FROM dc_patient_billing")
    total = cursor.fetchone()[0]

    conn.close()
    return jsonify({"billing": total})

# ================= BILLING BY BRANCH =================
@app.route('/billing/<branch_id>')
def billing_branch(branch_id):
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(patient_id)
        FROM dc_patient_billing
        WHERE branch_id = %s
    """, (branch_id,))

    total = cursor.fetchone()[0]
    conn.close()

    return jsonify({"billing": total})

# ================= BILLING LAST 30 DAYS =================
@app.route('/billing-30days')
def billing_30():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(patient_id)
        FROM dc_patient_billing
        WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
    """)

    total = cursor.fetchone()[0]
    conn.close()

    return jsonify({"billing": total})

# ================= BILLING LAST 30 DAYS BY BRANCH =================
@app.route('/billing-30days/<branch_id>')
def billing_30_branch(branch_id):
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(patient_id)
        FROM dc_patient_billing
        WHERE branch_id = %s
        AND billing_date >= CURDATE() - INTERVAL 30 DAY
    """, (branch_id,))

    total = cursor.fetchone()[0]
    conn.close()

    return jsonify({"billing": total})

# ================= TOP BRANCHES =================
@app.route('/top-branches')
def top_branches():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT branch_name, COUNT(patient_id)
        FROM dc_patient_billing
        GROUP BY branch_name
        ORDER BY COUNT(patient_id) DESC
        LIMIT 5
    """)

    result = cursor.fetchall()
    conn.close()

    return jsonify({
        "top_branches": [{"branch_name": r[0], "patient_count": r[1]} for r in result]
    })

# ================= TOP BRANCHES LAST 30 DAYS =================
@app.route('/top-branches-30days')
def top_branches_30():
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT branch_name, COUNT(patient_id)
        FROM dc_patient_billing
        WHERE billing_date >= CURDATE() - INTERVAL 30 DAY
        GROUP BY branch_name
        ORDER BY COUNT(patient_id) DESC
        LIMIT 5
    """)

    result = cursor.fetchall()
    conn.close()

    return jsonify({
        "top_branches": [{"branch_name": r[0], "patient_count": r[1]} for r in result]
    })

# ================= LAST DIALYSIS =================
@app.route('/last-dialysis/<patient_id>')
def last_dialysis(patient_id):
    if not check_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(billing_date)
        FROM dc_patient_billing
        WHERE patient_id = %s
    """, (patient_id,))

    result = cursor.fetchone()[0]
    conn.close()

    return jsonify({"last_dialysis": str(result)})

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)