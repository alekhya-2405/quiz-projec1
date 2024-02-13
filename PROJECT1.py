import random

def display_question(question_number, question, options):
    print(f"\nQuestion {question_number + 1}: {question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_answer():
    while True:
        try:
            user_answer = int(input("\nEnter the number of your answer: "))
            if 1 <= user_answer <= 4:
                return user_answer
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_answer(question_number, user_answer, correct_answer, options):
    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}: {options[correct_answer - 1]}\n")
        return 0

def play_quiz(questions):
    score = 0
    for i, question_data in enumerate(questions):
        question = question_data['question']
        options = question_data['options']
        correct_answer = question_data['correct']

        display_question(i, question, options)
        user_answer = get_user_answer()
        score += evaluate_answer(i, user_answer, correct_answer, options)

    print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")
questions_data = [
    {
        'question': 'What is the capital of Japan?',
        'options': ['Seoul', 'Beijing', 'Tokyo', 'Bangkok'],
        'correct': 3
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct': 1
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['Charles Dickens', 'Jane Austen', 'William Shakespeare', 'Mark Twain'],
        'correct': 3
    },
    {
        'question': 'Which programming language is often used for machine learning?',
        'options': ['Java', 'Python', 'C++', 'JavaScript'],
        'correct': 2
    }
]

if __name__ == "__main__":
    random.shuffle(questions_data)  
    play_quiz(questions_data)
