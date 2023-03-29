# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pairs
# display eack question to the user and allow them to answer
# tell them if they are righ or wrong
# show the final result when the quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Australia?",
        "answer": "Vienna"
    },
}

score = 0
for key, value in quiz.items():
    print(value["answer"])
    print(value["question"])
    Answer = input("Answer: ")
    if(Answer.lower() == value["answer"].lower()):
        print("Correct")
        score = score + 1
        print("Your score is: ", str(score))
        print("")
        print("")
    else:
        print("Invalid answer")
        print("The answer is", value["answer"])
        print("")
        print("")

print(f"You got {str(score)} out of 7 questions correctly")
print(f"Your percentage is {str(int(score/7 * 100))}")