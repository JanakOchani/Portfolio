from PortfolioDBService import PortfolioDBService


class LoginService:

    def __init__(self):
        print("Login Service instantiated")

    def authenticateUser(self,username,password):
        valid_user= False
        try:
            db = PortfolioDBService()
            rows = db.selectQuery(f"""
                                    SELECT * FROM portfolio_users 
                                    WHERE USERNAME ='{username}' AND PASSWORD ='{password}';
                                    """)

            if (len(rows) > 0):
                print("User authenticated")
                valid_user = True
            else:
                print(f"Invalid Credentials {username} and {password}. Try again!")
                valid_user = False

        except Exception as error:
            print("Problem in authenticating user ",error)

        return valid_user