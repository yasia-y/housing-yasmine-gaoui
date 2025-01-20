from flask import Flask, request, jsonify
import psycopg2

# Initialisation de l'application Flask
app = Flask(__name__)

# Fonction pour établir une connexion PostgreSQL
def connect_to_database(db_name, user, password, host, port):
    return psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)

# Connexion initiale à la base de données 'postgres'
def setup_database():
    conn = connect_to_database("postgres", "postgres", "2005", "127.0.0.1", "5432")
    conn.autocommit = True
    cursor = conn.cursor()

    # Vérification de l'existence de la base de données 'house'
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", ("house",))
    if not cursor.fetchone():
        cursor.execute("CREATE DATABASE house;")
        print("Base de données 'house' créée.")
    else:
        print("La base de données 'house' existe déjà.")

    cursor.close()
    conn.close()

# Création de la table 'houses' si elle n'existe pas
def ensure_table_exists():
    conn = connect_to_database("house", "postgres", "2005", "127.0.0.1", "5432")
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute('''
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name = 'houses'
        );
    ''')

    if not cursor.fetchone()[0]:
        cursor.execute('''
            CREATE TABLE houses (
                house_id SERIAL PRIMARY KEY,
                longitude FLOAT,
                latitude FLOAT,
                housing_median_age INT,
                total_rooms INT,
                total_bedrooms INT,
                population INT,
                households INT,
                median_income FLOAT,
                median_house_value FLOAT,
                ocean_proximity VARCHAR(255)
            );
        ''')
        print("Table 'houses' créée.")
    else:
        print("Table 'houses' déjà existante.")

    cursor.close()
    conn.close()

# Récupération de toutes les maisons
def fetch_houses():
    conn = connect_to_database("house", "postgres", "2005", "127.0.0.1", "5432")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM houses;")
    results = cursor.fetchall()

    # Conversion des résultats en liste de dictionnaires
    column_names = [desc[0] for desc in cursor.description]
    houses = [dict(zip(column_names, row)) for row in results]

    cursor.close()
    conn.close()
    return houses

# Ajout d'une nouvelle maison
def insert_house(house_data):
    conn = connect_to_database("house", "postgres", "2005", "127.0.0.1", "5432")
    cursor = conn.cursor()

    query = '''
        INSERT INTO houses (
            longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
            population, households, median_income, median_house_value, ocean_proximity
        ) VALUES (%(longitude)s, %(latitude)s, %(housing_median_age)s, %(total_rooms)s, %(total_bedrooms)s,
                  %(population)s, %(households)s, %(median_income)s, %(median_house_value)s, %(ocean_proximity)s)
    '''

    cursor.execute(query, house_data)
    conn.commit()

    cursor.close()
    conn.close()

# Endpoint pour récupérer toutes les maisons
@app.route('/houses', methods=['GET'])
def get_houses():
    return jsonify(fetch_houses())

# Endpoint pour ajouter une nouvelle maison
@app.route('/houses', methods=['POST'])
def add_house():
    house_data = request.json
    insert_house(house_data)
    return jsonify({"message": "Maison ajoutée avec succès."}), 201

if __name__ == '__main__':
    setup_database()
    ensure_table_exists()
    app.run(host='0.0.0.0', port=5000, debug=True)
