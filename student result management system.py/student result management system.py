# -----------------------------------------------MINI PROJECT-------------------------------------------------------------

# ---------------------------------------STUDENT RESULT MANAGEMENT SYSTEM-------------------------------------------------

# PROBLEM STATEMENT :

# Write a Python program that takes a student’s basic details and subject marks, checks that all marks are between
# 0 and 100, stores them properly, and then shows a clear report with total marks, average, and percentage.
# If any mark is invalid or missing, the program should handle it safely.

# CODE :

class Student:
    def __init__(self, name, age, id):
        self.name = name 
        self.age = age
        self.id = id
        self.marks = []

    @staticmethod
    def criteria():
        print("here are the following conditions for entering your marks :")
        print("Marks should not be negative ")
        print("Marks should be in between the limit of 100")
        print("please enter your marks")
        
    def validatemarks(self, marks):
        maxmarks = 100
        for m in marks:
            if m < 0 or m > maxmarks:
                print("invalid marks :", marks)
                print("please enter your marks again and check the following condition !")
                return
        
        self.marks = marks
        print("here are your marks :", self.marks)
        print("marks saved successfully !")

    @staticmethod
    def details1():
        print("here are your details----")
            
    def display(self):
        print("name :", self.name)
        print("age :", self.age)
        print("id :", self.id)
        print("marks :", self.marks)
        print("--------------------")

    @staticmethod
    def details2():
        print("here is sum of your marks---")

    def add(self):
        total = sum(self.marks)
        print(total)

        print("--------------------")

    @staticmethod
    def details3():
        print("here is average of your marks---")

    def average(self):
        avg = round(sum(self.marks) / len(self.marks), 2)
        print(avg)

        print("----------------------")


    @staticmethod
    def details4():
        print("here is percentage of your marks---")

    def percentage(self):
        total_max = len(self.marks) * 100   
        per = round((sum(self.marks) / total_max) * 100, 2) 
        print(per)  

    print("--------------------")


    def fullreport(self):

        s1.details1()
        s1.display()

        s1.details2()
        s1.add()

        s1.details3()
        s1.average()

        s1.details4()
        s1.percentage()



s1 = Student("zaira",18, 11)

s1.criteria()
s1.validatemarks([20,100,80])

s1.fullreport()


# SAMPLE OUTPUT:

# here are the following conditions for entering your marks :
# Marks should not be negative 
# Marks should be in between the limit of 100
# please enter your marks
# here are your marks : [20, 100, 80]
# marks saved successfully !
# here are your details----
# name : zaira
# age : 18
# id : 11
# marks : [20, 100, 80]
# --------------------
# here is sum of your marks---
# 200
# --------------------
# here is average of your marks---
# 66.67
# ----------------------
# here is percentage of your marks---
# 66.67