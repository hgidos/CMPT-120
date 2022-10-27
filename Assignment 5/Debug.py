def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")

    #idk if you want it to only print if it has both so I did that too
    alphIntInput2 = input("Enter letters and numbers")
    if alphIntInput2.isalnum():
        justal = []
        justalstr = ""
        for x in alphIntInput2:
            if x.isalpha():
                justal.append(x)
        for y in justal:
            justalstr = justalstr+str(y)
        justnum = alphIntInput2.replace(justalstr, "")
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
        
               
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    astriskOrAnd = input("Enter an asterisk or ampersand")
    if astriskOrAnd == "*" or astriskOrAnd == "&":
        print ("good")
    else:
        print ("no")
    
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    ab = input("enter an int")
    if ab.isnumeric():
        ab = int(ab)
    else:
        print ("you entered not numbers")
    
    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    hasMarist = input("Enter a string")
    substring = "marist"
    hasMarist = hasMarist.lower()
    if substring in hasMarist:
        print ("your string has marist")
    else:
        print ("you are wrong")
    
    
main()
