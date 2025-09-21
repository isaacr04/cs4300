def returnTypes(variables):
    types = []
    for variable in variables:
        types.append(type(variable))
        
    return types


def demonstrateVariables():
    int = 5
    float = 3.14
    string = "This is a string"
    boolean = True

    return returnTypes([int, float, string, boolean])

if __name__ == "__main__":
    print(demonstrateVariables())