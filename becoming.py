# PROBLEM 1 Create a function with the variable below. 
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
    def problem1(): # !! : there is nothing in this function
    def arrayForProblem2(): # !! : there is nothing in this function 

    def arrayForProblem2():
        listNames = [ "Kenn", "Kevin", "Erin", "Meka"]
    # a.Print the 3rd element of the numberList.
        print(listNames[3]) # !! : the third element is index position 2
        listNames[3]= "Meka" # !! : not sure what you are doing here but it does not relate to the instructions
    # b. Print the size of the array
        listNames = [4] # !! : not sure what your are doing here
        print(listNames) # !! : you did not print the SIZE of the array (len())
    # c. DeletelistNames [4] the second element.
        listNames.append("Kevin") # !! : you did not DELETE an item
        print(listNames)
    # d. Print the 3rd element.
        print [3] ="Meka" # !! : this is not how you print 

# PROBLEM 2 Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while(userInput != 'q'):
        userInput = input("Try again")

# PROBLEM 4 Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function
CreateArray= [1,2,3,4,5]
# !! : this does not meet the requirements 
for everyNum in createArray:
    if createArray < 6:
        print(f"The numbers 1,2,3,4,5 ")

        print(f"The numbers 5,4,3,2,1 ")