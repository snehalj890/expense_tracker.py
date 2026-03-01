import json
import os

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer  # Correct option (e.g., 'A')

    def to_dict(self):
        return {"question": self.question, "options": self.options, "answer": self.answer}

class Quiz:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_score(self, name, score):
        self.scores.append({"name": name, "score": score})
        with open(self.filename, "w") as file:
            json.dump(self.scores, file, indent=4)

    def start_quiz(self):
        questions = [
            Question("Python is a?", ["A. Snake", "B. Programming Language", "C. Car", "D. Fruit"], "B"),
            Question("2 + 2 =", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
        ]
        name = input("Enter your name: ")
        score = 0
        for q in questions:
            print(f"\n{q.question}")
            for opt in q.options:
                print(opt)
            ans = input("Your answer (A/B/C/D): ").upper()
            if ans == q.answer:
                score += 1
        print(f"\n{name}, your score is {score}/{len(questions)}")
        self.save_score(name, score)

    def view_scores(self):
        if not self.scores:
            print("No scores yet.")
            return
        print("\n Past Scores:")

        for s in self.scores:
            print(f"{s['name']}: {s['score']}")

def main():
    quiz = Quiz()
    while True:
        print("\n=== Mini Quiz App ===")
        print("1. Start Quiz")
        print("2. View Scores")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            quiz.start_quiz()
        elif choice == "2":
            quiz.view_scores()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()