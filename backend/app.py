import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

config = {
    'user': '360831_admin',
    'password': 'changeMeLater',
    'host': 'mysql-projethackathon.alwaysdata.net',
    'database': 'projethackathon_projet2024',
    'raise_on_warnings': True,
    'port': 3306
}

app = Flask(__name__)
CORS(app)

def query_db(query):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results
    except mysql.connector.Error as err:
        return {"error": str(err)}

@app.route('/athletes') #OK
def athletes():
    results = query_db("SELECT * FROM athlete LIMIT 100")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/countries')#OK
def countries():
    results = query_db("SELECT * FROM country")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/medals') #OK vide
def medals():
    results = query_db("SELECT * FROM medals LIMIT 25")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/olympics') #OK vide
def olympics():
    results = query_db("SELECT * FROM olympics LIMIT 25")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/summer_results') #OK vide
def summer_results():
    results = query_db("SELECT * FROM summer_results LIMIT 1")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/winter_results') #OK vide
def winter_results():
    results = query_db("SELECT * FROM winter_results LIMIT 1")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

if __name__ == "__main__":
    app.run(debug=True)
