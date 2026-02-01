#Install psycopg2-binary.  File --Setting--Projects---Search and install that package
# Get DB connection details from DBeaver Host Port Database Username Password. right click DB Navigator.edit connection
#ALTER USER postgres WITH PASSWORD 'postgres';

import psycopg2

from PortfolioEnvironment import PortfolioEnvironment


class PortfolioDBService:

    def __init__(self):
        print("DB Service instantiated")

    def getDBConnection(self):
        try:
            env = PortfolioEnvironment()
            # 1. Establish the connection
            connection = psycopg2.connect(
                host=env.getProperty("db_hostName"),port=env.getProperty("db_portNumber"),database=env.getProperty("db_databaseName"),user=env.getProperty("db_userName"), password=env.getProperty("db_password")
            )
            return connection
        except Exception as problem:
            print(f" There was problem getting connection {problem}")


    def selectQuery(self, query):
        try:
            # 1. Establish the connection
            connection = self.getDBConnection()
            #print(f" Query is {query}")
            # 2. Create a cursor object to run queries.
            # Cursor: Think of the "cursor" as a pointer that lets you execute SQL commands and fetch results one by one.
            sqlEditor = connection.cursor()
            sqlEditor.execute(query)
            #print(f"Query executed successfully! {query}")

            # 4. Fetch the results
            # .fetchall() returns a list of tuples (rows)
            rows = sqlEditor.fetchall()
            #for row in rows:
            #    print(f"Index: {row[0]}, Stock: {row[1]}")
            # 4. CRITICAL: Commit your changes
            # Without this, your table and data will not be saved!

            if connection:
                sqlEditor.close()
                connection.close()
                print("PostgreSQL connection is closed")
            return rows
        except Exception as error:
            print("Error while connecting to PostgreSQL:", error)

    def executeQuery(self, query):
        try:
            # 1. Establish the connection
            connection = self.getDBConnection()

            # 2. Create a cursor object to run queries.
            # Cursor: Think of the "cursor" as a pointer that lets you execute SQL commands and fetch results one by one.
            sqlEditor = connection.cursor()
            sqlEditor.execute(query)
            #print(f"Query executed successfully! {query}")

            # 4. Fetch the results
            # .fetchall() returns a list of tuples (rows)
            #rows = sqlEditor.fetchall()
            #for row in rows:
            #    print(f"Index: {row[0]}, Stock: {row[1]}")
            # 4. CRITICAL: Commit your changes
            # Without this, your table and data will not be saved!
            connection.commit()
            #print("Commit Done!")

            if connection:
                sqlEditor.close()
                connection.close()
                print("PostgreSQL connection is closed")

        except Exception as error:
            print("Error while connecting to PostgreSQL:", error)
            raise error

