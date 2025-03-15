numberList = []
total = 0
average = 0

for i in range(5):
    number = int(input("Enter a number:"))
    numberList.append(number)

maxNum = numberList[0] #default
minNum = numberList[0]
for num in numberList:
    total += num
    average = total / len(numberList)
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num

print(f"The sum of the numbers in the list: {total}")
print(f"The average of the numbers in the list: {average}")
print(f"The max number of the numbers in the list: {maxNum}")
print(f"The min number of the numbers in the list: {minNum}")

print("***********************")

wordList = []
while True:
    word = input("Enter a word(Press 'q' to finish):")
    if word.lower() == 'q':
        break
    wordList.append(word)
print(f"Reverse list: {wordList[::-1]}")

print("***********************")

myList = [1,2,3,34,23,1231,43546,567,34,14,34,55,26,1,2,34]
uniqueList = []

for i in myList:
    if i not in uniqueList:
        uniqueList.append(i)
print(uniqueList)