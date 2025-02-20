questions = ("Which team won the last FIFA World Cup?: ",
             "Who is the all-time top scorer in the Champions League?: ",
             "Which club did Lionel Messi start his professional career with?: ",
             "How many players does a team have on the field during a match?: ",
             "What is the name of the most prestigious club tournament in Europe?: ")

options = (("A. Brazil", "B. France", "C. Argentina", "D. Germany"),
           ("A. Lionel Messi", "B. Cristiano Ronaldo", "C. Robert Lewandowski", "D. Karim Benzema"),
           ("A. Paris Saint-Germain", "B. Newell’s Old Boys", "C. FC Barcelona", "D. Manchester City"),
           ("A. 9", "B. 10", "C. 11", "D. 12"),
           ("A. Copa Libertadores", "B. Europa League", "C. UEFA Champions League", "D. Premier League"))

answers = ("C", "B", "C", "C", "C")
guesses = []

score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-------------------------")
print("        RESULTS          ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")