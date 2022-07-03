#question1

print("\nWelcome to my Program")
def isperfectnum(n):
    sum = 0
    sum_all = 0
    for i in range (1,n):
        if n % i == 0:
            sum += i
            sum_all += i
    sum2 = (sum_all+n)//2
    return sum == n , sum2 == n
m = int(input())
print(isperfectnum(m))





#question2

print("\nWelcome to my Program")
x = input("Enter a word : ")
w = ""
for i in x:
    w = i + w
if (x == w):
    print("Yes, word is a palindrome")
else:
    print("No, word isn't a palindrome")






#question 3

print("\nWelcome to my Program")
from math import factorial
def pascaltriangle(numRows):
    for i in range(numRows):
        for j in range(numRows - i + 1):
            print(end = " ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end = " ")

        print("\n")
pascaltriangle(5)






#question 4

print("\nWelcome to my Program")
def ispangram(string):
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in alph :
        if i not in string.lower():
            return False
    return True
string = input("\nEnter a string : ")
print(ispangram(string))






#question 5


print("\nWelcome to my Program")
items = [n for n in input("Enter the elements : ").split('-')]
items.sort()
print("\nSorted elements : ")
print('-'.join(items))







#question 6

print("\nWelcome to my Program")
def student_data(student_id, **kwargs):
    print("\nStudent ID:", student_id)
    if "student_name" in kwargs:
        print("Student Name :", kwargs['student_name'])
    if "student_name" and "student_class" in kwargs:
        print("Student Name :", kwargs['student_name'])
        print("Student Class :", kwargs['student_class'])

student_data(student_id = '21102067', student_name = 'Rakshit')

student_data(student_id='21102067', student_name='Rakshit', student_class='XII')







#question 7

print("\nWelcome to my Program")
class Student:
    pass
class Marks:
    pass
karan=Student()
a_grade=Marks()
print("To check whether they are instances of said classes or not:")
print(isinstance(Rakshit,Student))
print(isinstance(Rakshit,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))







#question 8

print("\nWelcome to my Program")
class solution:
    def sumthree(self,nums):
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums)-2 :
            j , k = i+1 , len(nums)-1
            while j<k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] >0 :
                    k-=1
                else :
                    result.append([nums[i] ,nums[j] ,nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k]== nums[k+1] :
                        k-=1
            i+=1
            while i<len(nums)-2 and nums[i]==nums[i-1]:
                i+=1
        return result
print(solution().sumthree([-25, -10, -7, -3, 2, 4, 8, 10]))








#question 9

print("\nWelcome to my Program")
class solution:
    def validity(self,str1):
        accumulate=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accumulate.append(i)
            elif len(accumulate)==0 or parentheses[accumulate.pop()]!=i:
                return False
        return len(accumulate)==0
print(solution().validity("[)"))
