class PortfolioEnvironment:

    #instance variable -- this is dictionary that maintain key value pair
    properties = {}

    #this is constructor method - it calls method to load properties from file into dictionary
    def __init__(self):
        self.properties = self.load_properties_to_dict("env.properties")
        #print(" Environment instatiated")

    #this method can be called by any other class to get the value of parameter
    def getProperty(self, propertyName):
        propertyValue = self.properties[propertyName]
        #print("Got the request for property ",propertyName,propertyValue)

        return propertyValue

    #loads properites from file into dictionary objects
    def load_properties_to_dict(self,filename):
        my_dict = {}
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Split once at the first '=' to handle values that may contain '='
                if "=" in line:
                    key, value = line.split("=", 1)
                    my_dict[key.strip()] = value.strip()
        return my_dict

    def getEnvironementProperty(propertyName):
        return PortfolioEnvironment().getProperty("api_key")

#testing this calls
parameterName = "api_key"
print("Property ",parameterName, " = " , PortfolioEnvironment.getEnvironementProperty(parameterName))
