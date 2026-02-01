#Install psycopg2-binary.  File --Setting--Projects---Search and install that package
# Get DB connection details from DBeaver Host Port Database Username Password. right click DB Navigator.edit connection
#ALTER USER postgres WITH PASSWORD 'postgres';

import psycopg2

try:
    # 1. Establish the connection
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="janak",
        user="postgres",
        password="postgres"
    )

    # 2. Create a cursor object to run queries.
    # Cursor: Think of the "cursor" as a pointer that lets you execute SQL commands and fetch results one by one.
    cursor = connection.cursor()

    # 3. Run the SQL query
    #cursor.execute("select * from INDEX_COMPOSITION")

    # 4. Fetch the results
    # .fetchall() returns a list of tuples (rows)
    #rows = cursor.fetchall()

    #for row in rows:
    #    print(f"Index: {row[0]}, Stock: {row[1]}")

    create_table_query = """
        CREATE TABLE IF NOT EXISTS test_user3 (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email TEXT UNIQUE
        );
        """
    cursor.execute(create_table_query)
    print("Table created successfully!")

    # 3. Insert Data
    # Use %s as placeholders for security (SQL injection prevention)
    insert_query = "INSERT INTO test_user3 (name, email) VALUES (%s, %s);"
    user_data = ("John Doe", "john@example.com")

    cursor.execute(insert_query, user_data)

    # 4. CRITICAL: Commit your changes
    # Without this, your table and data will not be saved!
    connection.commit()
    print("Data inserted successfully!")

    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

except Exception as error:
    print("Error while connecting to PostgreSQL:", error)

