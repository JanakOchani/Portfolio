from PortfolioDBService import PortfolioDBService


class RegisterService:

    def __init__(self):
        print ("Register Service instantiated ")

    def registerUser (self, username, password):
        regiser_status = False
        try:
            db = PortfolioDBService()
            db.executeQuery("""
                    CREATE TABLE IF NOT EXISTS portfolio_users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(100) UNIQUE,
                        password TEXT UNIQUE
                    );
                    """)
            db.executeQuery(f"""
                    INSERT INTO portfolio_users ( username, password ) 
                        values (
                                    '{username}','{password}'            
                                );
                    """)
            regiser_status = True
            print(f"User {username} registered ")
        except Exception as error:
            regiser_status = False
            print("Registration failed ",error)

        return regiser_status