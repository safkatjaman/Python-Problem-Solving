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
sum1 = 0 
while i <= 10:
      sum1 = sum1 + i
      i += 1
print(sum1)



""" Sum of Even """
i = 1
sum2 = 0
while i <= 20:
      if i % 2 == 0:
            sum2 = sum2 + i
      i += 1
print(sum2)



''' Sum of Odd '''
i = 1 
sum3 = 0
while i <= 50:
      if i % 2 != 0:
            sum3 = sum3 + i
      i += 1 
print(sum3)



''' Break in While '''
count1 = 0
while count1 < 10:
      if count1 == 5:
            break
      print(count1)
      count1 += 1



''' Continue in While '''
count2 = 0
while count2 < 10:
      count2 += 1
      if count2 % 2 == 0:
            continue
      print(count2)



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
def numberSubtract(num3, num4):
      return  num3 - num4
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
      count3 = 0
      vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
      for char in sentence:
            if char in vowles:
                  count3 = count3 + 1
      return count3
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
def takingNumber(num5, num6):
      num5 = int(num5)
      num6 = float(num6)
      return num5 * num6

print(takingNumber(input('Please Enter a Number: '), input('Please Enter another Number: ')))

""" Another Solve Of User Input To Number """
firstNumber1 = int(input('Please Enter the first Number: '))
secondNumber1 = float(input('Please Enter the second Number: '))
result1 = firstNumber1 * secondNumber1

print('The multiplication of your numbers is: ', result1)



""" Math Power """
import math
def userInputPower(num7, num8):
      num7 = int(num7)
      num8 = int(num8)
      return(math.pow(num7, num8))
print(userInputPower(input('Please Enter a Number: '), input('Please Enter another Number: ')))

""" Another Solve of Math Power """
baseNumber = int(input('Please Enter Base Number: '))
powerNumber = int(input('Please Enter Power Number: '))
result2 = baseNumber ** powerNumber
print('Your result is: ', result2)



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
firstNumber2 = int(input('Enter first number: '))
secondNumber2 = int(input('Enter second number: '))
printDivisionResult = floorDivision(firstNumber2, secondNumber2)
print(firstNumber2, '/', secondNumber2, '=', printDivisionResult)
print('The floor of ', printDivisionResult, ' is ', math.floor(printDivisionResult))

""" Another solution of Floor Division """
numDiv1 = int(input('Enter first number: '))
numDiv2 = int(input('Enter second number: '))
result3 = numDiv1 // numDiv2
print(result3)



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



""" Max of two """
max1 = int(input('Enter a number: '))
max2 = int(input('Enter another number: '))

result4 = max(max1, max2)
print('The max number is: ', result4)

""" Another solution of Max of two """
maxNum1 = int(input('Enter a number: '))
maxNum2 = int(input('Enter another number: '))

if maxNum1 > maxNum2:
      print(maxNum1, ' is the max number.')
else:
      print(maxNum2, ' is the max number.')

""" Another solution of Max of two """
maxNumber1 = int(input('Enter a number: '))
maxNumber2 = int(input('Enter another number: '))

if maxNumber1 - maxNumber2 > 0:
      print(maxNumber1, ' is the max number.')
else:
      print(maxNumber2, ' is the max number.')



""" Max of three """
maxOfThree1 = int(input('Enter a number: '))
maxOfThree2 = int(input('Enter another number: '))
maxOfThree3 = int(input('Enter another number: '))

result5 = max(maxOfThree1, maxOfThree2, maxOfThree3)
print('The max number is: ', result5)

""" Another solution of Max of three """
maxOfThreeNum1 = int(input('Enter a number: '))
maxOfThreeNum2 = int(input('Enter another number: '))
maxOfThreeNum3 = int(input('Enter another number: '))

if maxOfThreeNum1 > maxOfThreeNum2 and maxOfThreeNum1 > maxOfThreeNum3:
      print('The max number is: ', maxOfThreeNum1)
elif maxOfThreeNum2 > maxOfThreeNum1 and maxOfThreeNum2 > maxOfThreeNum3:
      print('The max number is: ', maxOfThreeNum2)
else: 
      print('The max number is: ', maxOfThreeNum3)



""" Average of numbers """
firstNumber3 = int(input('Enter first number: '))
secondNumber3 = int(input('Enter second number: '))
thirdNumber = int(input('Enter third number: '))
fourthNumber = int(input('Enter fourth number: '))
fifthNumber = int(input('Enter fifth number: '))

numberList = [firstNumber3, secondNumber3, thirdNumber, fourthNumber, fifthNumber]

result6 = (firstNumber3 + secondNumber3 + thirdNumber + fourthNumber + fifthNumber) / len(numberList)
print('Average of the five numbers is: ', round(result6, 2))

""" Another solution of Average of numbers """
len = int(input('How many numbers you want to enter: '))

nums = []

for i in range(0, len):
      element = int(input('Enter element: '))
      nums.append(element)
total1 = sum(nums)
avg1 = total1 / len
print('Average of elements you entered is: ', round(avg1, 2))

""" Another solution of Average of numbers """
length = int(input('How many numbers do you want to enter: '))

total2 = 0

for i in range(0, length):
      elements = int(input('Enter element: '))
      total2 = total2 + elements
avg2 = total2 / length
print('Average of elements you entered is: ', round(avg2, 2))