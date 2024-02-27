def age():
    global currentAge
    global birthYear
    
    currentAge = currentYear - birthYear
    print(f"Your age is {currentAge}")    

currentYear = int(input('Current year: '))
birthYear = int(input('Birth year: '))

age()

