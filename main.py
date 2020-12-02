"""This is an integration project created during my first semester at
Florida Gulf Coast University. This program takes the user's inputs, &
depending on those inputs, an overall score is produced which determines
what career in technology is best suited for the user."""
__author__ = "Patricia Andreica"

# Reviewed By Jairo Garciga & Robert McNiven
# Resources used: http://greenteapress.com/thinkpython2/thinkpython2.pdf
# https://www.geeksforgeeks.org/python-user-defined-functions/
# https://www.coursera.org/learn/python-data/lecture/HnHCM/6-1-strings
# Course Website

# This is importing a library which contains pre-written code.
import math


# A user-defined function which is a named sequence of statements that
# preform a computation.
# This is a void function because it does not return a value.
def user_introduction():
    """The purpose of this function is to introduce the program to
    the user and receive & store information such as their name."""
    print("Welcome to this quiz. Answer each question to find out what "
          "careers in technology best suit you!\n----")
    # This is a variable to store user input.
    first_name = input("First, let's get your name! What is your first "
                       "name?: ")
    # The string operator "+" concatenates strings.
    # The "sep" parameter specifies the separator between arguments.
    print("Hello " + first_name.capitalize(),
          " I hope you enjoy taking this quiz. There is no right or wrong "
          "answer. Let's get started! \n----", sep="!")


# This is a list which is a sequence of values called elements
# separated by a comma with indices starting at 0.
question_list = ["2) Which sounds most like you? \n A) Methodical & "
                 "analytical \n B) Love to problem-solve \n C) Have an eye"
                 " for detail & aesthetics \n D) Love to plan & "
                 "schedule projects",
                 "3) Let's say you're working on a project. What's the most "
                 "important thing? \n A) Accuracy \n B) Functionality \n C) "
                 "Ensuring user satisfaction \n D) Organization & budget",
                 "4) You would rather be...\n A) Analyzing "
                 "trends/information \n B) Testing & developing software "
                 "to fit user's needs \n C) Maximizing user experience & "
                 "interaction \n D) Managing technology projects",
                 "5) Which project type sounds most appealing? \n A) Creating"
                 " graphs or charts \n B) Building something useful \n C) An"
                 " art project \n D) Preparing & organizing a presentation",
                 "6) How would you describe yourself in one word?\n A) "
                 "Curious \n B) Problem-solver \n C) Creative \n D) Leader"]


# This function passes a parameter.
# Arguments are assigned to variables called parameters.
def multiple_choice_calc_score(user_input):
    """The purpose of this function is to update the user's score with the
    appropriate value depending on user's input, specifically for the
    questions in the list.

    user_input - must be a letter, either A B C or D & is not case-
    sensitive
    Returns the updated score for each question in the list"""
    # Initializing a local variable.
    function_score_1 = 0
    # Chained conditionals are used to check the condition in order
    # until one branch is true, which will then be executed.
    # If no condition is met, it will pass over to the else statement.
    if user_input.lower() == "a":
        function_score_1 += 8
    elif user_input.lower() == "b":
        function_score_1 += 6
    elif user_input.lower() == "c":
        function_score_1 += 4
    elif user_input.lower() == "d":
        function_score_1 += 0
    else:
        # We don't know how many times the user will input an error (if
        # they do), so we use a condition controlled loop. The user will
        # will be forced to enter either A,B,C or D in order to continue.
        while True:
            user_input = input("Input error. Enter A,B,C or D: ")
            if user_input.lower() == "a":
                function_score_1 += 8
                # This is used to break out of an infinite loop once
                # the condition is met.
                break
            elif user_input.lower() == "b":
                function_score_1 += 6
                break
            elif user_input.lower() == "c":
                function_score_1 += 4
                break
            elif user_input.lower() == "d":
                function_score_1 += 0
                break
    # After the function takes the argument, it returns the return
    # value.
    return function_score_1


def yes_or_no(user_input_2):
    """The purpose of this function is to update the user's score with
    the appropriate value depending on user's input.

    user_input_2 - must be the words either "yes" or "no" & is not case-
    sensitive
    Returns the updated score depending on user input"""
    function_score_2 = 0
    if user_input_2.lower() == "yes":
        function_score_2 += 4
    elif user_input_2.lower() == "no":
        function_score_2 += 8
    else:
        # No matter what, the statement will be True.
        while True:
            user_input_2 = input("Input error. Enter either 'yes' or "
                                 "'no': ")
            if user_input_2.lower() == "yes":
                function_score_2 += 4
                break
            elif user_input_2.lower() == "no":
                function_score_2 += 8
                break
    return function_score_2


def number_calc_score(user_input_3):
    """The purpose of this function is to update the user's score with the
    appropriate value depending on user's input.

    user_input_3 - must only be a number between 1 & 5 inclusive
    Returns the updated score depending on user input"""
    function_score_3 = 0
    # Division operator preforms division.
    # Keyword NOT is a logical operator where if statements are not
    # True, the return value will be True.
    if not user_input_3 / 1 != 1:
        function_score_3 += 2
    # Modulus operator which divides two numbers & returns the remainder.
    elif user_input_3 % 3 == user_input_3:
        function_score_3 += 2
    # Multiplication & subtraction operators.
    elif user_input_3 * 3 - 6 == 3:
        function_score_3 += 6
    # Exponent operator.
    # Keyword OR is a logical operator where only one of the conditions
    # must be true for code to be executed.
    # "math" is the library, "sqrt" is the library function, and inside
    # the parenthesis is the argument.
    elif user_input_3 ** 2 == 16 or (math.sqrt(user_input_3)) == 2:
        function_score_3 += 6
    # Addition & floor division operator which divides & rounds down to
    # a whole number.
    # Keyword AND is a logical operator where both conditions must
    # be true for the code to be executed.
    elif user_input_3 // 3 + 4 and user_input_3 / 1 == 5:
        function_score_3 += 10
    else:
        while True:
            user_input_3 = int(input("Input error. Please enter a valid "
                                     "number 1-5: "))
            if user_input_3 == 1 or user_input_3 == 2:
                function_score_3 += 2
                break
            elif user_input_3 == 3 or user_input_3 == 4:
                function_score_3 += 6
                break
            elif user_input_3 == 5:
                function_score_3 += 10
                break
    return function_score_3


def main():
    """The purpose of this function is to direct calls to all of
    the functions in the program and produce a final score.

     Returns the sum of the score from all functions"""
    # Calling a function which is what invokes the function.
    user_introduction()
    overall_score = 0
    # This will get passed as an argument to call the specific function.
    user_input_2 = input("1) Do you enjoy giving presentations? \nEnter "
                         "either 'yes' or 'no': ")
    overall_score += yes_or_no(user_input_2)
    # This count controlled For loop iterates over the question list.
    # Function len() takes the list as a parameter and returns the
    # number of elements in the list.
    for user_input in range(len(question_list)):
        print(question_list[user_input])
        user_input = input("Enter A,B,C or D: ")
        # This is updating the score for every input while the loops runs.
        overall_score += multiple_choice_calc_score(user_input)
    while True:
        # If line of code does not cause an exception, it will pass over.
        try:
            user_input_3 = int(input("7) On a scale of 1-5, 1 being the "
                                     "lowest, how much do you enjoy math? "
                                     "\n Enter a number 1-5: "))
        # If user inputs anything other than a number, an exception
        # occurs which must be handled.
        except ValueError:
            print("Input error. Please enter a valid number 1-5")
        else:
            break
    overall_score += number_calc_score(user_input_3)
    return overall_score


# Call to main while also storing the return value into a variable for
# continued use.
final_score = main()

print("")
# Converting the score to a string to that it can be concatenated.
# The "end" parameter appends a comma and space instead of a newline.
print("Results:")
print("You received a score of", str(final_score) + "/58. Therefore", end=",")
# The final score is tested between a range of numbers through the
# relational operator <= & one final output is generated for the user.
if 45 <= final_score:
    print(" you seem to be very analytical & have strong quantitative skills."
          " \nCareers: Data scientist, Data analyst")
elif 31 <= final_score <= 44:
    print(" you seem to be logical and love problem-solving. \nCareers: "
          "Software developer, Software engineer, Cyber-security")
elif 17 <= final_score <= 30:
    print(" you have an eye for aesthetics & design & are very "
          "detail-oriented. \nCareers: UI/UX designer, Front-end"
          " developer, UX engineer")
elif final_score <= 16:
    print(" you love to collaborate with others & plan projects. \nCareers:"
          " IT project manager")
else:
    print(" result could not be produced.")
print("")
# String operator *, concatenates to output 5 ! signs.
print("Thank you for taking this quiz" + "!" * 5)

