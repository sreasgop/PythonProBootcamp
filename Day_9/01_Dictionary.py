def main():

    

    programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again",
        "Loop" : "The action of doing something over and over again",
    }
    
    print(programming_dictionary)
    
    # ACCESSING VALUES IN DICTIONARY
    # Accesing the values of a dictionary: Using keys
    # print(programming_dictionary["Bug"])
    # print(programming_dictionary["Function"])
    # print(programming_dictionary["Loop"])
    
    # Accessing the keys of a dictionary: using .keys() method
    # print(programming_dictionary.keys())
    
    # Accessing the values of a dictinoary: using .values() method
    # print(programming_dictionary.values())
    
    # Accessing the values of a dictionary: using .items() method
    # print(programming_dictionary.items())
    
    # Iterating through the enire dictionary: 
    # for i, j in programming_dictionary.items():
    #     print(i, end=': ')
    #     print(j)
        
        
    # ADDING NEW VALUES IN DICTIONARY
    # programming_dictionary["OOP"] = "A programming paradigm where we use objects and classes to combine data and functions together"
    
    # for i, j in programming_dictionary.items():
    #     print(i, end=': ')
    #     print(j)
        
    
    # Create an empty dictionary: 
    empty_dictionary = {}
    
    # Wipe an existing dictionary: 
    # programming_dictionary = {}
    # programming_dictionary.clear()
    

    
    
if __name__ == "__main__":
    main()