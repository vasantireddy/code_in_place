import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])

    # Handle division to avoid decimal and zero division
    if operator == '/':
        num1 = num1 * num2  # ensures clean division
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, round(answer, 2)

def run_quiz(num_questions=10):
    score = 0

    print("🧠 Welcome to the Math Quiz!\n")
    for i in range(1, num_questions + 1):
        question, correct_answer = generate_question()
        print(f"Q{i}: {question} = ?")

        try:
            user_input = float(input("Your answer: "))
            if round(user_input, 2) == correct_answer:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer was: {correct_answer}\n")
        except ValueError:
            print(f"❌ Invalid input! Correct answer was: {correct_answer}\n")

    print(f"🎉 Quiz Over! You scored {score} out of {num_questions}.")

if __name__ == "__main__":
    run_quiz()
