class Student:

    #constructor
    def __init__(self, l_myid, l_myname, l_myage):
        print("Object instantiated for id", l_myid,l_myname, l_myage)
        self.my_id = l_myid
        my_name = l_myname
        self.name = my_name
        self.my_age = l_myage

    def say_my_name(self):
        print(" My Name is  ",self.name)
        self.__say_my_age()
        #self.__my_private_method()

    def __say_my_age(self):
        print(" My age is ",self.my_age)



