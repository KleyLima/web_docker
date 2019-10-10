import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='kleyton',
                             password='kleysql',
                             db='db_mass',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT nome FROM people WHERE id_people={}".format(1)
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

