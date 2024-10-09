print("Aloha! Welcome to the mega quiz of everything! \nI, Atharva, will be your host tonight, and we will choose your questions on luck!")
users_input = input("Initiating coin flip: \nFor Heads input - 1\nFor Tails input - 2\nYour input: ")
print(users_input)
import random
heads = 1
tails = 2
a = random.randint(1, 2)
if a == users_input:

    print("Quiz has begun! You have been assigned the world quiz! Good Luck! ")
    questions = [
        "What is the capital of France?",
        "What is 21 * 21 (Do it in your head!)?",
        "Who wrote 'To Kill a Mockingbird'?"
    ]

    options = [
        ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        ["A. 3", "B. 4", "C. 5", "D. 6"],
        ["A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Jane Austen"]
    ]

    correct_answers = ["A", "B", "A"]


    def argument_valid():
        # Initially, the score is zero.
        score = 0
        # Referring to all the questions in our list
        for i in range(len(questions)):
            # Printing and referring to each of our questions to the "question" set
            print(questions[i])
            # Similarly, for the options list
            for option in options[i]:
                print(option)
            # Upper lets us forget the possibility of our user inputting a or A
            answer = input("Enter your answer (A, B, C, or D): ").upper()
            # Matching the user's input with our answer list, and checking whether right or wrong
            if answer == correct_answers[i]:
                print("Correct!\n")
                score += 1
            else:
                print("Wrong! The correct answer is", correct_answers[i], "\n")
        print("Your final score is:", score, "out of", len(questions))


    argument_valid()


else:
    print("Roll again!")

