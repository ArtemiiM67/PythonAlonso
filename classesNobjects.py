#CODE ALONG: Create a minion class with several attributes - some that are the same 
#for every minion, and some that are different. 
#Create an instance of the class (an object!) and print it to the console.
#The above is the work we did in class, just copy paste it for reference.





#If time permits, continue adding attributes after the whole class portion is done.
#Otherwise, remember you must at least finish the mild task below.


#YOUR TASK: Complete the following to the best of your ability. Thank you to
#			Ms. Shuman for her example tasks!
#MILD 🌶

#1. Create a class called Student that has two attributes: a name, and a grade.

class Student:
    def __init__(self, theName, theGrade, theSavingsAccount=None):
        self.name = theName
        self.grade = theGrade
        if theSavingsAccount:
            self.savings = theSavingsAccount
        else:
            self.savings = 0


# Now create instances of three different students (student1, student2, and student3).
student1 = Student("PoopyHead", "65%")
print(student1.name, student1.grade)

student2 = Student("Skibidi", "85%")
print(student1.name, student1.grade)

student3 = Student("Issac", "100%")
print(student3.name, student3.grade)


#Confirm that the class works by printing out the first student's name.
print("The first student's name is", student1.name)



# MEDIUM 🌶🌶

#2. Create a class called School that has three attributes: a name, a type, and
#	a size (number of students).
class School:
    def __init__(self, theName, theType, theSize):
        self.name = theName
        self.type = theType
        self.size = theSize



#Create instances of three individual schools.
school1 = School("Stuy", "Awesome", 3000)
school2 = School("BTech", "Stupid", 0)
school3 = School("Bababui", "The Best", 100000)


#Confirm that the class works by printing out the name and size of the third school.
print("The name and size of the third school are", school3.name, "and", school3.size)


###
#3. Create a class called House that has four attributes: an address, a number
#	of bathrooms, a price, and a number of bedrooms.

class House:
    def __init__(self, theAddress, theNumberBaths, thePrice, theNumberBeds):
        self.address = theAddress
        self.baths = theNumberBaths
        self.price = thePrice
        self.beds = theNumberBeds

#Create instances of at least three individual houses.
house1 = House("Skibidi Street", 10, 100000, 2)
house2 = House("Toilet Street", 5, 100, 1)
house3 = House("Meow-Meow Street", 15, 20000, 29)

#Confirm that the class works by printing out the address and size of the second house.
print(house2.address, "is the address, and", house2.baths, "is the number of baths, as well as", house2.beds, "being the number of beds for house number 2!")


#SPICY 🌶🌶🌶

#4. Put your three students in a list called my_students, your houses in a list
#	for houses, and your schools in a list for schools.
my_students = [student1, student2, student3]
my_houses = [house1, house2, house3]
my_schools = [school1, school2, school3]


#Iterate (this means use a loop!) over the student list, printing out "_____ is in
#grade __." For each of the students.
for student in my_students:
    print(student.name)


#Iterate over the houses list and print out a description for each one. Do the same
#for your schools lists.
for school in my_schools:
    print(school.name, school.size, school.type)
    
for house in my_houses:
    print(house.beds, house.baths, house.price, house.address)


###
#5. Modify your student class above to include a savings_account value for each
#	student. Change your initializers so that the code still runs. 

#DONE#


#Write some code that compares a student and a house, and determines whether or not
#the student can afford to buy the house.
student4 = Student("PoopyHead", "65%", 100000000)
student5 = Student("Skibidi", "85%", 1000)
student6 = Student("Gay Issac", "100%", 2500000)

my_new_students = [student4, student5, student6]

for student in my_new_students:
    for house in my_houses:
        if student.savings >= house.price:
            print(student.name, "can afford", house.address)
        else:
            print(student.name, "- is too broke for", house.address)