"""Sandy's First Real Code"""

__author__ = "Sandy Sardinas"


# Ver. 1.0
# This program is currently a budget assistant for Gundam model kit collectors.
# It currently helps you calculate total cost. In the future I plan to add the
# ability to check total vs budget and give warning. Also, the ability to
# recommend models based on user input.

# Ver. 2.0
# I have added the over budget warning and the ability to recommend models.
# Still to do would be to make sure user can't crash the program by
# inputting unexpected things. Some parts of the code have it but not fully
# realized yet.

# Ver. Final
# Added main function.
# Made sure all inputs were user-proofed.


def main():
    """Main function."""
    print(
        "Greetings Gundam afficionado. This budget assistant will help you \n"
        "calculate how many model kits you can buy, and give you a chance \n"
        "to win a million bucks!")
    print("")

    # Here we collect user input while using conditional statements and
    # loops to avoid invalid inputs
    # budget = float(input("What is your budget?\nPlease enter a number:\n"))
    while True:
        try:
            budget = float(input("What is your budget?\nPlease enter a "
                                 "number:\n"))
            break
        except ValueError:
            print("Error. Please enter an amount using numeral symbols")

    grade = None
    grade_loop = True
    while grade_loop:
        grade = input("Choose a quality grade for your models.\nH|R|M|P:\n")
        if grade.upper() == "H":
            grade_loop = False
        elif grade.upper() == "R":
            grade_loop = False
        elif grade.upper() == "M":
            grade_loop = False
        elif grade.upper() == "P":
            grade_loop = False
        else:
            print("Invalid Input.")

    mb_gundam = None
    mb_gundam_loop = True
    while mb_gundam_loop:
        mb_gundam = input(
            "Would you like Mobile Suits or a Gundams?\nType M or "
            "G\n")
        if mb_gundam.upper() == "M":
            mb_gundam_loop = False
        elif mb_gundam.upper() == "G":
            mb_gundam_loop = False
        else:
            print("Invalid Input.")

    while True:
        try:
            quantity = float(
                input("How many models would you like?\nPlease enter "
                      "a number:\n"))
            break
        except ValueError:
            print("Error. Please enter an amount using numeral symbols")

    sub_total = None
    if mb_gundam.upper() == "M":
        if grade.upper() == "H":
            sub_total = quantity * 20
        elif grade.upper() == "R":
            sub_total = quantity * 25
        elif grade.upper() == "M":
            sub_total = quantity * 40
        elif grade.upper() == "P":
            sub_total = quantity * 70
    elif mb_gundam.upper() == "G":
        if grade.upper() == "H":
            sub_total = quantity * 25
        elif grade.upper() == "R":
            sub_total = quantity * 35
        elif grade.upper() == "M":
            sub_total = quantity * 50
        elif grade.upper() == "P":
            sub_total = quantity * 100
    else:
        print("Error")

    # Here we use + and - operators to calculate savings
    if sub_total >= 100:
        total_cost = sub_total + (.06 * sub_total) - 20
    else:
        total_cost = (sub_total + (.06 * sub_total)) / (10 / 9)

    savings = sub_total + (.06 * sub_total) - total_cost

    # Now we print all the results making use of + and * as string operators
    print("Your budget is: " + str(budget))
    print("You chose the grade: " + str(grade))
    print("You wanted " + str(int(quantity)) + " kits")
    print("Total Cost:", end=" ")
    print("$", format(total_cost, '.2f'), sep="")
    print("Congratulations" + "!" * 5)
    print("You could save $", format(savings, '.2f'), sep="")
    print("")

    # Here we are trying to get clever and use // and % to make a siggestion
    # how the
    # client can spend his surplus budget.
    if budget - total_cost >= 20:
        surplus = float(budget - total_cost)
        print("Your surplus is $", format(surplus, '.2f'), sep="")
        print("You could still afford more kits. For example, you could buy",
              int(surplus // 20), "more Mobile Suits, and have at least $",
              format(surplus % 20, '.2f'), "left over.")

    elif (budget - total_cost) < 20 and (budget - total_cost > 0):
        surplus = float(budget - total_cost)
        print("Your surplus is $", format(surplus, '.2f'), sep="")

    # getting creative again and hoping two wrongs make a right!
    elif not (budget - total_cost != 0):
        print("Wow! You are a very efficient shopper.")
        print("You spent all your money.")

    else:
        surplus = float(total_cost - budget)
        print("You are $", format(surplus, '.2f'), " over budget!", sep="")
    print("")

    suggestion_choice_loop = True
    while suggestion_choice_loop:
        suggestion_choice = input("Would you like us to suggest some kits?\n"
                                  "Type y or n:\n")
        if suggestion_choice.upper() == "Y":
            suggestion_choice_loop = False
            suggest_gundam(budget, grade, mb_gundam)
        elif suggestion_choice.upper() == "N":
            suggestion_choice_loop = False
            print("Ok")
            print("")
        else:
            print("Invalid input.")
            print("")

    naming_choice_loop = True
    while naming_choice_loop:
        naming_choice = input("Would you like to name your gundam?\n""If you "
                              "purchase any, the names will be printed on " 
                              "the\n ""boxes?\n""Type y or n:\n")
        if naming_choice.upper() == "Y":
            gundam_naming(quantity)
            naming_choice_loop = False
        elif naming_choice.upper() == "N":
            print("Ok")
            print("")
            naming_choice_loop = False
        else:
            print("Invalid input.")
            print("")

    # Lastly a marketing scam.
    print(
        "Thank you for using this budget assistant. As a reward here is an \n"
        "opportunity to earn a million bucks")
    while True:
        try:
            scam = float(input("Answer quickly: What is 87^34?\n"))
            break
        except ValueError:
            print("Error. Please enter an amount using numeral symbols")
    if scam == 87 ** 34:
        print("Sorry, while your answer is correct you did not answer "
              "quickly \n""enough. Better luck next time")
    else:
        print("Sorry, that is not correct. Better luck next time")


# This function sorts out which kit to recommend to the buyer based on their
# budget and preferences while using and or Boolean operators.
def suggest_gundam(budget, grade, mb_gundam):
    """Takes in budget, grade, and type of model. Returns a suggestion."""
    if grade.upper() == "P" and mb_gundam.upper() == "G" and budget >= 200:
        print("Based on your inputs we recommend you purchase the Perfect\n"
              "Grade Gundam RX-78-2.")
    elif grade.upper() == "P" and mb_gundam.upper() == "M" and budget >= 200:
        print("Based on your inputs we recommend you purchase the Perfect\n"
              "Grade MS-06S Char's Zaku II.")
    elif grade.upper() == "M" and mb_gundam.upper() == "G" and budget >= 100:
        print("Based on your inputs we recommend you purchase the Master\n"
              "Grade Gundam Dynames.")
    elif grade.upper() == "M" and mb_gundam.upper() == "M" and budget >= 100:
        print("Based on your inputs we recommend you purchase the Master\n"
              "Grade Grimgerde.")
    elif ((grade.upper() == "R" or budget >= 100) and mb_gundam.upper() ==
          "M"):
        print("Based on your inputs we recommend you purchase the Real\n"
              "Grade Sazabi.")
    elif ((grade.upper() == "R" or budget >= 100) and mb_gundam.upper() ==
          "G"):
        print("Based on your inputs we recommend you purchase the Real\n"
              "Grade Nu Gundam.")
    elif (grade.upper() == "H" or budget < 100) and mb_gundam.upper() == "G":
        print("Based on your inputs we recommend you purchase the High\n"
              "Grade Gundam Barbatos Lupus.")
    elif (grade.upper() == "H" or budget < 100) and mb_gundam.upper() == "M":
        print("Based on your inputs we recommend you purchase the High\n"
              "Grade MS-06 Zaku II Type C/C-5.")
    else:
        print("you should never see this")


# This function gives the customer the choice to customize their boxes with
# names while using a for, in, and range.
def gundam_naming(quantity):
    """Takes in a quantity number and names and returns a list."""
    gundam_name_list = []
    for x in range(int(quantity)):
        gundam_name_list.append(input("Enter name: "))
    print("You entered:\n", gundam_name_list, "\nAre these correct?:\n"
                                              "Type y or n:")
    correction_choice = input()
    if correction_choice.upper() == "N":
        gundam_naming(quantity)
    elif correction_choice.upper() == "Y":
        print("Ok")
        print("")
    else:
        print("Invalid input.")
        print("")


main()

# Sources:
# Stackoverflow.com
# https://sites.google.com/site/profvanselow
# Valerio (Chuchy) Sardinas. Taught me about global variables and answered
# many questions.
# Andy Sardinas. Gundam expert.
