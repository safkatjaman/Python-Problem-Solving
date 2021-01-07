friends = ['Ross', 'Monica', 'Chandler', 'Joey', 'Rachel', 'Safkat']
friends.pop()
friends.append('Phoebe')

lastIndex = friends[5]
print(lastIndex)

printLength = len(friends)
print(printLength)

getIndexNumber = friends.index('Phoebe')
print(getIndexNumber)

""" For loop """
for friendPrint in friends:

      if friendPrint == 'Rachel':
            """ Skipping with continue keyword """
            continue 
      print(friendPrint)



""" While loop """
i = 1
sum = 0 
while i <= 10:
      sum = sum + i
      i += 1
print(sum)



""" Sum of Even """
i = 1
sum = 0
while i <= 20:
      if i % 2 == 0:
            sum = sum + i
      i += 1
print(sum)



''' Sum of Odd '''
i = 1 
sum = 0
while i <= 50:
      if i % 2 != 0:
            sum = sum + i
      i += 1 
print(sum)



''' Break in While '''
count = 0
while count < 10:
      if count == 5:
            break
      print(count)
      count += 1



''' Continue in While '''
count = 0
while count < 10:
      count += 1
      if count % 2 == 0:
            continue
      print(count)



''' First Function in Python '''
def brushYourTeeth():
      print('Take the toothbrush')
      print('Put paste on the brush')
      print('Clean teeth')
      print('Wash the toothbrush')
      print('Rinse your mouth')
brushYourTeeth()



''' Parameter in a Function '''
def numberMultiplication(num):
      print(num * 5)
numberMultiplication(5)



''' Multiple Parameter in a Function '''
def multipleParameter(num1, num2):
      print(num1 + num2)
multipleParameter(10, 10)



''' Return in a Function '''
def numberSubtract(num1, num2):
      return  num1 - num2
subtraction = numberSubtract(10, 10)
print(subtraction)



""" Leap Year """
userInput = input('Enter a year: ')
userInput = int(userInput)
if userInput % 400 == 0:
      print(userInput, 'is a leap year')
elif userInput % 100 == 0:
      print(userInput, 'is not a leap year')
elif userInput % 4 == 0:
      print(userInput, 'is a leap year')
else:
      print(userInput, 'is not a leap year')



""" Word Count """
userInput2 = input('Write about yourself! At least 50 words: ')
count2 = 0
for char in userInput2:
      if char == ' ':
            count2 = count2 + 1
""" Add another count = count + 1 for the last word """
count2 = count2 + 1
print(count2)



""" Count Vowles """
def count_vowles(sentence):
      count = 0
      vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      for char in sentence:
            if char in vowles:
                  count = count + 1
      return count
print(count_vowles(input('Please Enter a Sentence: ')))



""" Remove Duplicate """
def remove_duplicate(items):
      unique = []
      for item in items: 
            if item not in unique:
                  unique.append(item)
      return unique
numbers = [1, 2, 4, 5, 1 ,23, 345, 235, 1, 5, 0, 6, 2, 1, 4, 5, 7]
print(remove_duplicate(numbers))



""" Fibonacci Series """
def fibonacci(num):
      fibo = [0, 1]
      i = 2
      while i <= num:
            next_fibo = fibo[i - 1] + fibo[i - 2]
            fibo.append(next_fibo)
            i = i + 1
      return fibo
print(fibonacci(9))



""" User Input To Number """
def takingNumber(num1, num2):
      num1 = int(num1)
      num2 = float(num2)
      return num1 * num2

print(takingNumber(input('Please Enter a Number: '), input('Please Enter another Number: ')))

""" Another Solve Of User Input To Number """
firstNumber = int(input('Please Enter the first Number: '))
secondNumber = float(input('Please Enter the second Number: '))
result = firstNumber * secondNumber

print('The multiplication of your numbers is: ', result)



""" Math Power """
import math
def userInputPower(num1, num2):
      num1 = int(num1)
      num2 = int(num2)
      return(math.pow(num1, num2))
print(userInputPower(input('Please Enter a Number: '), input('Please Enter another Number: ')))

""" Another Solve of Math Power """
baseNumber = int(input('Please Enter Base Number: '))
powerNumber = int(input('Please Enter Power Number: '))
result = baseNumber ** powerNumber
print('Your result is: ', result)



""" Random Number """
import random

input1 = int(input('Enter the first number: '))
input2 = int(input('Enter the second number: '))
number = random.randint(input1, input2)
print(number)



""" Floor Division """
import math

def floorDivision(number1, number2):
      return number1 / number2
firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))
printDivisionResult = floorDivision(firstNumber, secondNumber)
print(firstNumber, '/', secondNumber, '=', printDivisionResult)
print('The floor of ', printDivisionResult, ' is ', math.floor(printDivisionResult))

""" Another solution of Floor Division """
numDiv1 = int(input('Enter first number: '))
numDiv2 = int(input('Enter second number: '))
result = numDiv1 // numDiv2
print(result)



""" Swap Two Variables """
swapNumber1 = int(input('Enter first number: '))
swapNumber2 = int(input('Enter second number: '))
swapNumber3 = swapNumber2
swapNumber4 = swapNumber1
print('Swapped numbers: ', swapNumber3, ', ', swapNumber4)

""" Another solution of Swap Two Variables """
swapping1 = int(input('Enter first number: '))
swapping2 = int(input('Enter second number: '))
print('First Number: ', swapping1, '\nSecond Number: ', swapping2)
temp = swapping1
swapping1 = swapping2
swapping2 = temp
print('Swapped first number: ', swapping1, '\nSwapped second number: ', swapping2)

""" Another solution of Swap Two Variables """
swappingNum1 = int(input('Enter first number: '))
swappingNum2 = int(input('Enter second number: '))
print('First Number: ', swappingNum1, '\nSecond Number: ', swappingNum2)
swappingNum1, swappingNum2 = swappingNum2, swappingNum1
print('Swapped first number: ', swappingNum1, '\nSwapped second number: ', swappingNum2)

""" Another solution of Swap Two Variables """
swappingNumber1 = int(input('Enter first number: '))
swappingNumber2 = int(input('Enter second number: '))
print('First Number: ', swappingNumber1, '\nSecond Number: ', swappingNumber2)
swappingNumber1 = swappingNumber1 + swappingNumber2
swappingNumber2 = swappingNumber1 - swappingNumber2
swappingNumber1 = swappingNumber1 - swappingNumber2
print('Swapped first number: ', swappingNumber1, '\nSwapped second number: ', swappingNumber2)