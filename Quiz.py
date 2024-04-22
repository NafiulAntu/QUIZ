# ----------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)

# ----------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0
# ----------------------------


def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")
    print("Answers: ",end=" ")

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end= " ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = (correct_guesses/len(questions)*100)
    print("Your score is: "+ str(score)+"%")


# ----------------------------


def play_again():
    response = input("Do you want to play again?: (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who invented Drone ?: ": "A",
    "What was the year ?:": "B",
    "How many types of drones are there in the world ?: ": "C",
    "Is that Netanyahu human ?: ": "A"
}

options = [["A. Abraham Karim", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerburg"],
           ["A.1970", "B.1991", "C.2000", "D.2014"],
           ["A. 1", "B. 3", "C. 4", "D. 6"],
           ["A.Not at all", "B.False", "C.Something else", "D.Ask Biden or American"]]

new_game()


while play_again():
    new_game()

print("Byeeeeee!!")

