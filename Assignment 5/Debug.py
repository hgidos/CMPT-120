def main():
    #checking if the input is a string
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")

        
    #checking if the input is an int
    intInput = input("enter an int")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")

    
    #checks if the input includes either ints or is a string, no weird characters
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")


    #idk if you want it to only print if it has both so I did that too
    #taking an input
    alphIntInput2 = input("Enter letters and numbers")
    #checking if this input doesn't include weird characters
    if alphIntInput2.isalnum():
        #creating an empty list for just the letters in input
        justal = []
        #creating a string for this list to get compiled into 
        justalstr = ""
        #x is the spot that the for loop is running through
        for x in alphIntInput2:
        #if the spot in alphIntInput2 is a letter it will add it to the justal list
            if x.isalpha():
                justal.append(x)
        #making a string of all the alp characters in alphIntInput2 by taking the list and adding it to a string
        for y in justal:
            justalstr = justalstr+str(y)
        #creating a string of just the numbers in the input by taking out the string of letters created by justalstr
        justnum = alphIntInput2.replace(justalstr, "")
        #checking if both the seperate strings for just the letters and numbers actually are alpha and numeric 
        if justnum.isnumeric() and justalstr.isalpha():
            print ("Letters and numbers!")
        elif justnum.isnumeric():
            print ("No, just numbers")
        elif justalstr.isalpha():
            print ("no, just letters")
        else:
            print ("no, weird characters :(")
    else:
        print ("weird characters :(")
        
               
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")

        
    astriskOrAnd = input("Enter an asterisk or ampersand")
    if astriskOrAnd == "*" or astriskOrAnd == "&":
        print ("good")
    else:
        print ("no")
    
        
    checkifint = input("enter an int")
    #if input is a number this if statement is checking that then changing the str to an int if true 
    if checkifint.isnumeric():
        checkifint = int(checkifint)
    else:
        print ("you entered not numbers")


    hasMarist = input("Enter a string")
    substring = "marist"
    #making the entire string lowercase so it isn't case sensitive 
    hasMarist = hasMarist.lower()
    if substring in hasMarist:
        print ("your string has marist")
    else:
        print ("you are wrong")
    
    
main()
