from LoginService import LoginService
from PortfolioService import PortfolioManager
from RegisterService import RegisterService


class PortfolioUI:

    def __init__(self):
        print("portfolio UI instantiated ")

    def displayMenuAndNavigate(self):
        user_selected_option = False
        option = 0
        while( user_selected_option == False  ):
            try:
                print(f"1) Login \n 2) Sign up \n 3) Restart \n 4) Exit \n")
                option = int(input("Select your option number: "))
                user_selected_option = True
            except Exception as e:
                print( f"Something went wrong with your selection {option}. Please try again" )

        while(option != 4):
            if(option==1):
                user_authenticated = self.displayLoginScreenAndAuthenticate()  # authenticate user access
                if(user_authenticated):
                    self.displayPortfoloAnalysisScreen() #let user provide his portfolio file name now
                    option = 4
            elif(option==2):
                user_created = self.displaySetupAndRegister() #create user account
                if(user_created):
                    user_authenticated = False
                    option=1 # ask user to login
            elif(option == 3):
                self.displayMenuAndNavigate() #restart this function
            elif(option==4):
                print("Good Bye! ")
                return
            else:
                print(f"Invalid Option {option}.Please check your option and retry! ")
                self.displayMenuAndNavigate() # i dont know what user is trying to do


    def displayLoginScreenAndAuthenticate(self):
        valid_user = False
        loginsService = LoginService()

        print("Authenticate User:")
        try:
            while(valid_user==False):
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if(username.isspace() or password.isspace()):
                    raise Exception
                valid_user = loginsService.authenticateUser(username,password)
                return valid_user
        except Exception as problem:
            print(f" Problem Autnenticating {problem}, try again ")


    def displaySetupAndRegister(self):
        regiser_status = False
        registerService = RegisterService()
        try:
            print("Register User")
            while(regiser_status==False):
                username = input("Create Username: ")
                password = input("Create Password: ")
                if(username.isspace() or password.isspace()):
                    raise Exception
                regiser_status =  registerService.registerUser(username,password)
                return regiser_status
        except Exception as problem:
            print(f" Problem Authenticating {problem}, try again ")


    def displayPortfoloAnalysisScreen(self):
        ##get File from user
        portfolio_file_name = input("Please enter your portfolio file name: ")
        portfolioManager = PortfolioManager()
        portfolioManager.processPortfolio(portfolio_file_name)

        if(input("\n Enter X to Exit. Any other Key to continue ") != 'X'):
            self.displayPortfoloAnalysisScreen()

