import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")
        
        self.questions = [
            {
                "question": "Who is the father of C++?",
                "options": ["James Goslings", "Guido Van Rossum", "Bjarne Stroustup", "Dennis Ritchie"],
                "correct_answer": "Bjarne Stroustup"
            },
            {
                "question": "How many continents are there?",
                "options": ["5", "6", "7", "8"],
                "correct_answer": "7"
            },
            {
                "question": "What is 7 multiplied by 9?",
                "options": ["56", "63", "72", "81"],
                "correct_answer": "63"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack()
        
        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_final_results()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["correct_answer"]
        
        if question_data["options"][selected_option] == correct_answer:
            self.score += 1
        
        self.current_question += 1
        self.next_question()

    def show_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = QuizGame(root)
    root.mainloop()
