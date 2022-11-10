class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department

        
class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
           
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")

            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def carColor(self):
        if self.color == "yellow":
            return ("yellow car")
        else:
            return ("not yellow car")
    
   
def main():
    dog1 = Dog("Thor", 2)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    newEmployee = Employee("Anthony", 232,"random")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    cake1 = Cake("lemon", "vanilla")
    print(cake1.flavor, cake1.frosting)
    
    
    #and now create another cake and print it out
    cake2 = Cake("chocolate", "raspberry")
    print(cake2.flavor, cake2.frosting)
    
    
    #create a cat!
    cat1 = Cat("Winnie",2, "short")
    #create another cat!
    cat2 = Cat("Shirley", 5, "short")
    
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    car1 = Car("Honda CRV", 2008, "silver")
    print(car1.carColor())
    #Now print out the function you made for car :)

main()
