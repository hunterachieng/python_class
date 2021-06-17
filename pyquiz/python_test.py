
#Question 1
x = [100,110,120,130,140,150]
new_list = [ a*5 for a in x]
print(new_list)

#Question 2
def divisible_by_three(n):
    for num in range(1,n):
        if num%3 == 0:
            print(num)
divisible_by_three(20)

#Question 3
def flatten_list():
    flat_list = []
    x = [[1,2],[3,4],[5,6]]
    for a in x:
        for b in a:
            flat_list.append(b)
    return flat_list
print(flatten_list())

#Question 4

def smallest(a):   
    a.sort()    
    return a[0]
print(smallest([3,6,8,2,4,1,5,7]))

#Question 5
def duplicate(x):
    a = set(x)
    x = list(a)
    return x
print(duplicate(["a","b","a","e","d","b","c","e","f","g","h"]))
    
#Question 6
def divisible_by_seven():
    number_list = []
    for num in range(100,200):
        if num%7 == 0:
            number_list.append(num)
    return number_list

print(divisible_by_seven())

#Question 7

students = [{"age":19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18,"name":"Teresa"},{"age":22,"name":"Asha"}]
def greeting():
    for student in students:
        name = student["name"]
        age = student["age"]
        year_born = 2021 - age
        print (f"Hello {name}, you were born in the year {year_born}")

greeting()

#Question 8
class Rectangle():
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def area(self):
        A = self.width * self.length
        return A
    def perimeter(self):
       P = 2*(self.length + self.width)
       return P

rectangle = Rectangle(10,30)
print(rectangle.area())
print(rectangle.perimeter())
        
        
    

    
