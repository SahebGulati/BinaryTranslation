#input questions

#time in hours (integer between 0 and 23 and 0 and 59, respectively)
def inputQuestion():
    #return input
    return input("What time is it? Please us HH:MM format: ")

#normal time variable equals returned input
normalTime = inputQuestion()
#checks to confirm that formatting is correct and create robust code
#check if length is 5 characters (as it would be in HH:MM format)
if len(normalTime) != 5:
    #error, re ask question and call function
    print("Please use correct formatting!")
    normalTime = inputQuestion()

#check to see if colon is present in correct location
if normalTime.find(":") != 2:
    #error, re ask question and call function
    print("Please use correct formatting!")
    normalTime = inputQuestion()

#seperate normalTime input into seperate h and m variables
#retrieve index values from beginning to where colon is
h = normalTime[:normalTime.index(":")]
#retrieve values from characters after colon to the end of array
m = normalTime[normalTime.index(":")+1:]

#confirm that h and m are integers
if h.isnumeric() and m.isnumeric():
    # data type hours = integer - so it can be converted to binary
    h = int(h)
    # data type minutes = integer - so it can be converted to binary
    m = int(m)

    #if hour/minute input values are permissible, proceed
    if h <= 24 and m <= 59:
        #using function bin() to convert, "b" converts integer to binary equivalent
        hoursToBinary = format(h, "b")
        minutesToBinary = format(m, "b")

        #Print converted values in correct format
        print("The time is " + hoursToBinary + ":" + minutesToBinary)

    #If format of input impermissible
    else:
        #Error message
        print("Invalid input! Please type an hour value between 0 and 23 and a minute value between 0 and 59. Thanks!")

#error message, restart
else:
    print("Invalid input! Please use integers and correct formatting!")
    normalTime = inputQuestion()
