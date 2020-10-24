# By: Patricia Andreica
# This is a BuzzFeed style quiz. Based on the question, the user will
# input an answer. Every input is stored into one variable, initialized to 0,
# which is updated with a value depending on that input. When all inputs are
# entered, the variable will be tested to see which condition it fits,
# generating a final outcome for the user, which is what career in technology
# is best suited for the user.
# Help from Stack Overflow, Think Python 2e & Youtube
# Reviewed by Jairo Garciga & Robert McNiven

# This is importing a library which contains pre-written code
import math

print("Welcome to this quiz. Answer each question to find out what careers in "
      "technology best suit you!\n----")
# Inputs are stored in each variable // Values are stored as strings in order
# to be combined with other strings
# Assignment operator assigns value to variables
name = input("First, let's get your name! What is your name?: ")
# String operator + concatenates strings which combines strings together
# Sep parameter specifies the separator between arguments
print("Hello " + name.capitalize(), " I hope you enjoy taking this quiz. "
                                    "There is no right or wrong answer. "
                                    "Let's get started! \n----", sep="!")


# User defined function which is a named sequence of statements that preforms
# a computation. First line is the header, which contains the def keyword,
# the function name, & the parameter. The rest is called the body.
# Arguments are assigned to variables called parameters / like a placeholder
def calc_score(user_input):
    # Initializing a local variable
    function_score = 0
    if user_input.lower() == "yes":
        function_score += 2
    elif user_input.lower() == "no":
        function_score += 8
    else:
        while True:
            user_input = input("Input error. Try again: ")
            if user_input.lower() == "yes":
                function_score += 2
                break
            elif user_input.lower() == "no":
                function_score += 8
                break
    return function_score


def main():
    print("1) Would you enjoy giving presentations as a part of your job?")
    user_input = input("Enter 'yes' or 'no' only: ")
    # Calling a function, user_input is passed as an argument and gets
    # received as a parameter
    score_1 = calc_score(user_input)
    # After function takes argument, it returns the final value of the
    # function; known as return value
    return score_1


# Call to main while also storing the final value to a variable; call to a
# function is what invokes the function
score = main()

# This is a list: sequence of values called elements separated by a comma
# where indices start at 0
question_list = [
    "2) Which sounds most like you?:\n A) Methodical & analytical \n B) Love "
    "to problem-solve \n C) Have an eye for detail & aesthetics \n D) Love "
    "to plan & schedule projects & collaborate with others", "3) Let's say "
    "your working on a project. What's the most important thing?: \n A) "
    "Accuracy \n B) Functionality \n C) Ensuring user satisfaction \n D)"
    " Organization & budget ", "4) You would rather be....\n A) Analyzing "
    "trends/information \n B) Testing & developing software to fit users needs"
    " \n C) Maximizing user experience/interaction \n D) Managing technology "
    "projects", "5) Which project type sounds to most appealing?: \n A) "
    "Creating graphs or charts  \n B) Building something useful \n C) Art "
    "project \n D) Preparing and organizing a presentation", "6) How would you"
    " describe yourself in one word?:\n A) Curious \n B) Problem-solver \n C)"
    " Creative \n D) Leader  "]
# For loop iterates over the list; we know how many elements we want it to
# traverse
# Builtin in function, range() returns the sequence from the list
# len() returns the length of the list, or the number of elements, starting
# from [0] (the 1st element)
for answer in range(len(question_list)):
    print(question_list[answer])
    answer = input("Enter your answer (A,B,C,or D): ")
    # Chained conditionals / Each condition is checked in order until one
    # branch is true, which will be executed.That number is updated in the
    # variable // Shortcut operators used; essentially means addition
    # .lower() converts uppercase strings to lowercase
    if answer.lower() == "a":
        score += 8
    elif answer.lower() == "b":
        score += 6
    elif answer.lower() == "c":
        score += 4
    elif answer.lower() == "d":
        score += 2
    else:
        # While loop will loop until a condition is no longer True; we don't
        # know how many times the loop should run.
        while True:
            answer = input("Error. Please try again: ")
            if answer.lower() == "a":
                score += 8
                # Break exits the loop once the condition is met & avoids an
                # infinite loop (typically should avoid).
                break
            elif answer.lower() == "b":
                score += 6
                break
            elif answer.lower() == "c":
                score += 4
                break
            elif answer.lower() == "d":
                score += 2
                break

# Arithmetic Operators & Logical Operators
question_7 = int(input("7) On a scale of 1-5, 1 being the lowest,"
                       " how much do you enjoy math: "))
# Division / Input is 1
# Keyword NOT: a logical operator where if statements are not True, the return
# value will be True
# ! = means not equal to. This specific statement is false, so keyword NOT
# returns True
if not question_7 / 1 != 1:
    score += 2
# Modulus operator; divides two numbers & returns remainder / Input is 2
elif question_7 % 3 == question_7:
    score += 2
# Multiplication / Subtraction / Input is 3
elif question_7 * 3 - 6 == 3:
    score += 6
# Power raised / Input is 4
# Keyword OR is a logical operator, only one of the conditions must be true in
# order to execute the code
# Math is the library, sqrt is the library function, and inside the
# parenthesis is the argument
elif question_7 ** 2 == 16 or (math.sqrt(question_7)) == 2:
    score += 6
# Floor division; divides & rounds down to whole number / Addition / Input is 5
# Logical operator and keyword, both conditions must be true for code to
# be executed.
elif question_7 // 3 + 4 and question_7 / 1 == 5:
    score += 10
else:
    while True:
        question_7 = int(input("Invalid input. PLease try again. "))
        if question_7 == 1 or question_7 == 2:
            score += 2
            break
        elif question_7 == 3 or question_7 == 4:
            score += 6
            break
        elif question_7 == 5:
            score += 10
            break
print("")
# Converting the score to a string to that it can be concatenated
# End parameter appends a comma and space instead of a newline
print("Results:")
print("You received a score of", str(score) + "/58. Therefore", end=",")
# Final score is tested between a range of numbers through the relational
# operator <= & one output is generated
if 47 <= score <= 58:
    print(" you seem to be very analytical & have strong quantitative skills."
          " \nCareers: Data scientist, data analyst")
elif 27 <= score <= 46:
    print(" you seem to be logical and love problem-solving. \nCareers: "
          "Software developer, software engineer")
elif 15 <= score <= 26:
    print(" you have an eye for aesthetics & design & are very "
          "detail-oriented. \nCareers: UI/UX designer, front-end"
          " developer")
elif 2 <= score <= 14:
    print(" you love to collaborate with others & plan projects. \nCareers:"
          " IT project manager")
else:
    print("Error")
print("")
# String operator *, concatenates to output 5 ! signs
print("Thanks for taking this quiz", name.capitalize() + "!" * 5)
