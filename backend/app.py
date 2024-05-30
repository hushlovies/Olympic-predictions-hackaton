import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

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
    
@app.route('/')
def home():

    athlete_count_result = query_db("SELECT COUNT(*) AS total FROM athlete")
    if "error" in athlete_count_result:
        return jsonify({"message": "Impossible de récupérer le nombre d'athlètes", "error": athlete_count_result["error"]}), 500
    total_athletes = athlete_count_result[0]['total']

    country_count_result = query_db("SELECT COUNT(*) AS total FROM country")
    if "error" in country_count_result:
        return jsonify({"message": "Impossible de récupérer le nombre de pays", "error": country_count_result["error"]}), 500
    total_countries = country_count_result[0]['total']

    return jsonify({"totalAthletes": total_athletes, "totalCountries": total_countries})

@app.route('/athletes')
def athletes():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    offset = (page - 1) * per_page

    name_filter = request.args.get('name', '')
    country_filter = request.args.get('country', '')
    year_filter = request.args.get('year', '')
    participation_filter = request.args.get('participation', '')

    # Jointure avec la table country
    query = """
    SELECT a.*, c.country_name 
    FROM athlete a
    LEFT JOIN country c ON a.country_3_letter_code = c.country_3_letter_code
    WHERE """
    
    conditions = []
    
    if name_filter:
        conditions.append(f"a.athlete_full_name LIKE '%{name_filter}%'")
    if country_filter:
        conditions.append(f"c.country_3_letter_code LIKE '%{country_filter}%'")
    if year_filter:
        conditions.append(f"a.athlete_year_birth LIKE '%{year_filter}%'")
    if participation_filter:
        conditions.append(f"a.games_participations LIKE '%{participation_filter}%'")
    
    if conditions:
        query += " AND ".join(conditions)
    else:
        query += "1"  # Si aucune condition, cette partie de la requête renvoie toujours vrai

    query += f" ORDER BY a.athlete_full_name LIMIT {per_page} OFFSET {offset}"

    results = query_db(query)
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer les données", "error": results["error"]}), 500
    
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/countries')
def countries():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 25))
    offset = (page - 1) * per_page
    
    # Query to fetch paginated results
    query = f"""
    SELECT 
    c.country_3_letter_code,
    c.country_name,
    COALESCE(sr.gold, 0) + COALESCE(wr.gold, 0) AS total_gold,
    COALESCE(sr.silver, 0) + COALESCE(wr.silver, 0) AS total_silver,
    COALESCE(sr.bronze, 0) + COALESCE(wr.bronze, 0) AS total_bronze,
    COALESCE(a.athlete_count, 0) AS athlete_count
    FROM 
        country c
    LEFT JOIN 
        (
            SELECT 
                country_3_letter_code,
                SUM(CASE WHEN medal_type = 'GOLD' THEN 1 ELSE 0 END) AS gold,
                SUM(CASE WHEN medal_type = 'SILVER' THEN 1 ELSE 0 END) AS silver,
                SUM(CASE WHEN medal_type = 'BRONZE' THEN 1 ELSE 0 END) AS bronze
            FROM 
                summer_results
            GROUP BY 
                country_3_letter_code
        ) AS sr ON c.country_3_letter_code = sr.country_3_letter_code
    LEFT JOIN 
        (
            SELECT 
                country_3_letter_code,
                SUM(CASE WHEN medal_type = 'GOLD' THEN 1 ELSE 0 END) AS gold,
                SUM(CASE WHEN medal_type = 'SILVER' THEN 1 ELSE 0 END) AS silver,
                SUM(CASE WHEN medal_type = 'BRONZE' THEN 1 ELSE 0 END) AS bronze
            FROM 
                winter_results
            GROUP BY 
                country_3_letter_code
        ) AS wr ON c.country_3_letter_code = wr.country_3_letter_code
    LEFT JOIN 
        (
            SELECT 
                country_3_letter_code, 
                COUNT(*) AS athlete_count
            FROM 
                athlete
            GROUP BY 
                country_3_letter_code
        ) AS a ON c.country_3_letter_code = a.country_3_letter_code
    GROUP BY 
        c.country_3_letter_code, c.country_name
        """
    query += f" ORDER BY c.country_name LIMIT {per_page} OFFSET {offset}"

    results = query_db(query)

    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    
    return jsonify({"message": "Data recup!", "data": results})


@app.route('/medals')
def medals():
    results = query_db("SELECT * FROM medals LIMIT 25")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/olympics') 
def olympics():
    results = query_db("SELECT * FROM olympics LIMIT 25")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/summer_results')
def summer_results():
    results = query_db("SELECT * FROM summer_results LIMIT 1")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

@app.route('/winter_results')
def winter_results():
    results = query_db("SELECT * FROM winter_results LIMIT 1")
    if "error" in results:
        return jsonify({"message": "Impossible de récupérer des données", "error": results["error"]}), 500
    return jsonify({"message": "Data recup!", "data": results})

if __name__ == "__main__":
    app.run(debug=True)
