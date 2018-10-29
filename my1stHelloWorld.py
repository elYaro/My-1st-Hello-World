def welcome():
# says Hello World! or welcomes the User by his/her name if inputed
# go to the working dictionary
# open this file by writing: Python3.6 helloWorld3.py
# you can add different names after 'Python3.6 helloWorld3.py' separated by SPACE
# Examples
# terminal input => helloWorld3.py                  terminal output => "Hello World!" 
# terminal input => helloWorld3.py Yaro             terminal output => "Hello Yaro"
# terminal input => helloWorld3.py Yaro Mike        terminal output => "Hello Yaro and Mike"  
# terminal input => helloWorld3.py Yaro Mike Bob    terminal output => "Sorry, byt I won't talk to more then two people at the same time."  
# terminal input => helloWorld3.py 2                terminal output => "Does you NAME really is a NUMBER? Input correctly pls."  

    import sys # imports Module sys

    argList=(sys.argv) #creates a list called argList

    numberComment="Does you NAME really is a NUMBER? Input correctly pls." # comment if digits

    try:
        if len(argList)>1: 
            int(argList[1]) #if number inputed then comment given. If correct name then jumping to exception
            print(numberComment)
        else: print("Hello World!")
        
    except ValueError:
            if len(argList)>3: #if more then 2 names been typed in
                print("Sorry, byt I won't talk to more then two people at the same time.")
                
            elif len(argList)>2: #if 2 names been typed in
                print("Hello", argList[1], "and", argList[2]) #uses the element with index[1][2] of the list

            elif len(argList)>1: #if 1 name been typed in
                print("Hello", argList[1])               

welcome()
