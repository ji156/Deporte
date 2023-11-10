import psycopg2

# Configuración de las credenciales
database_name = "reto_deportes"
database_user = "ji156"
database_password = "admin"
database_host = "localhost"
database_port = 5432
database_table = "clasificacion_laLiga"

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    host=database_host,
    port=database_port,
    user=database_user,
    password=database_password,
    database=database_name
)

# Crea un cursor
cursor = conn.cursor()

# Ejecuta una consulta para verificar los registros
cursor.execute(f"SELECT * FROM {database_table} LIMIT 60")
rows = cursor.fetchall()

# Muestra los resultados
for row in rows:
    print(row)

# Cierra la conexión
conn.close()
