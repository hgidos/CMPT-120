#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random

class student:
    def __init__(self, name, studentId, year, major, gpa):
        self.name = name
        self.studentId = studentId
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsProgram(self):
        if self.gpa > 3.5:
            return ("true")
        else:
            return ("false")

    def freeLunch(self):
        randomNum = random.randint(000000,999999)
        if randomNum==self.studentId:
            return ("winner!")
        else:
            return ("Loser!")
    
    
    
def main():
    student1 = student("Hannah", 343230, "f", "cybersecurity", 4.0)
    print("Does ", student1.name, " win free lunch? ", student1.freeLunch(), "eligible for honors program? " , student1.honorsProgram())
    student2 = student("Amanda", 938201, "s", "music education", 3.8)
    print("Does ", student2.name, " win free lunch? ", student2.freeLunch(), "eligible for honors program? " , student2.honorsProgram())
    student3 = student("Ryan", 329432, "f", "computer science", 3.2)
    print("Does ", student3.name, " win free lunch? ", student3.freeLunch(), "eligible for honors program? " , student3.honorsProgram())
    #create three students and check if they get free lunch and if they qualify for honors
    
    
main()
