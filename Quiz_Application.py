# A quiz application and count the score of user
# score board: correct and wrong
# question number wise correct and wrong score
# show answer for all question only after completing all questions
# random question by category
# check question number with random number

# Questions and Answers // add more questions below:
questions = {
    "1. What is the capital of Nepal? ": "Kathmandu",
    "2. What is the largest country in the world? ": "Russia",
    "3. What is the largest desert in the world? ": "Sahara",
    "4. What is the biggest forest? ": "Amazon",
    "5. What is the longest river? ": "Nile"
}

# Function to ask the questions and check the answers


def quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("You got", score, "out of", len(questions), "questions correct.")


quiz(questions)


print("Correct Answers")
for i, value in enumerate(questions.values()):
    print(str(i+1) + ". " + value)
