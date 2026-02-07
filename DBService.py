import psycopg2

class DBService:
    def execute_query(query):
        try:
            print(query)

            connection = psycopg2.connect(
                host='localhost',
                port='5432',
                database='postgres',
                user='postgres',
                password='postgres'
            )

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

            cursor.close()
            connection.close()

            print("Query executed and connection closed successfully.")

        except Exception as my_error:
            print(f"Error that was given: {my_error}")
