alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet.insert(0, ' ')
alphabet = tuple(alphabet)  # 1 will correspond to "a" instead of 0 so that converstion doesn't have to happen after
# the fact. also, 0 can be used as a space that won't be later removed.


def listToString(inputList):  # i feel like there is a better solution to this but idk
    outputString = ""
    for item in inputList:  # for each letter in the list,
        outputString += item  # add it to a new string
    return outputString  # and return the string once all of the letters have been added


while True:
    inputStr = input('Type in numbers to convert. >>')
    if inputStr.lower() == "exit":
        exit()
    if not inputStr:  # checks if the inputted string is empty
        print('Input cannot be empty.')
        continue

    numberList = inputStr.split(" ")  # turns the string into a list of numbers, using spaces as seperators
    print(numberList)
    try:
        while numberList[-1] == "": numberList.pop(-1) # this removes any trailing empty items from the list (which would have originally
            # been trailing spaces)
    except IndexError: # handles if the input consists of only spaces
        print('Input cannot be empty.')
        continue
    letterList = []

    for i in numberList:  # for every item in the inputted list,
        try:
            number = int(i)  # turn it into an integer,
        except ValueError:   # if it's a number
            print('Enter only numbers from 0-26 and spaces.')
            break 
        try:
            letter = alphabet[number]  # and turn that integer into a letter,
        except IndexError:  # if that number is in range of the alphabet.
            print('One or more of your numbers are over 26.')
            break
        letterList.append(letter)  # add that letter to the answer,
        # print(letter)

    print(listToString(letterList).title())  # and print it in title case