class TestClass:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet_user(self):
        print(f"Greetings",self.name,"!")
        self.__what_country()

    def __what_country(self):
        print(" My age is ",self.country)



