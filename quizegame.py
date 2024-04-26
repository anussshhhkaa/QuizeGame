def ask_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        try:
            answer = int(input("Enter your answer (1-" + str(len(options))+ "):"))
            if 1 <= answer <= len(options):
                return answer - 1
            else:
                print("Invlid input. Please enter a number between 1 and", len(options))
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_answer(answer, correct_answer):
   if answer == correct_answer:
      print("Correct!")
      return True
   else:
      print("Incorrect. The correct answer is;", correct_answer + 1)
      return False
   
def main():
    questions = [
       "Which character is used in Python to make a single line comment?",
       "Which one of the following is the correct extension of the Python file?",
       "Which of the following words cannot be a variable in python language?"
    ]
    options = [
       ["/", "!", "#"],
       [".py", ".python", ".p"],
       ["_val", "try", "_try_"]
    ]
    answers = [2, 0, 1]

    score = 0
    for i, question in enumerate(questions):
       answer = ask_question(question, options[i])
       if check_answer(answer, answers[i]):
          score += 10

    print("Your final score is:", score, "/", 30)

if __name__ == "__main__":
   main()