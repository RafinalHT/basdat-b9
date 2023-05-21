from django.db import connection

def query(query):
    res = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("set search_path to babadu;")
        except Exception as e:
            res = e
            connection.rollback()
        
        try:
            cursor.execute(query)
            if query.strip().lower().startswith("select"):
                res = cursor.fetchall()
            else:
                res = f"{cursor.rowcount} row(s) affected"
                connection.commit()
        except Exception as e:
            res = e
            connection.rollback()
    return res
