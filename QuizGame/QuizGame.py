from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

class Quiz:
    def __init__(self):
        self.questions = [
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Go", "Au", "Ag", "Gd"],
        "answer": "Au"
    },
    {
        "question": "What is the smallest bone in the human body?",
        "options": ["Humerus", "Stapes", "Tibia", "Femur"],
        "answer": "Stapes"
    },
    {
        "question": "Who is known as the father of modern physics?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Albert Einstein"
    },
    {
        "question": "Who wrote the play \"Romeo and Juliet\"?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the opening line of Charles Dickens' \"A Tale of Two Cities\"?",
        "options": [
            "\"It was the best of times, it was the worst of times\"",
            "\"Call me Ishmael\"",
            "\"Happy families are all alike; every unhappy family is unhappy in its own way\"",
            "\"It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife\""
        ],
        "answer": "\"It was the best of times, it was the worst of times\""
    },
    {
        "question": "Who wrote the novel \"To Kill a Mockingbird\"?",
        "options": ["J.K. Rowling", "Ernest Hemingway", "F. Scott Fitzgerald", "Harper Lee"],
        "answer": "Harper Lee"
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1918", "1915", "1912", "1905"],
        "answer": "1912"
    },
    {
        "question": "Who was the first president of the United States?",
        "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "In what year did World War II end?",
        "options": ["1950", "1939", "1945", "1941"],
        "answer": "1945"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "answer": "Ottawa"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Nile", "Amazon", "Mississippi", "Yangtze"],
        "answer": "Nile"
    },
    {
        "question": "Which continent is the largest by land area?",
        "options": ["Asia", "Africa", "North America", "Europe"],
        "answer": "Asia"
    },
    {
        "question": "Who directed the movie \"Jurassic Park\"?",
        "options": ["James Cameron", "Steven Spielberg", "Christopher Nolan", "Quentin Tarantino"],
        "answer": "Steven Spielberg"
    },
    {
        "question": "What is the highest-grossing film of all time (adjusted for inflation)?",
        "options": ["Gone with the Wind", "Avatar", "Titanic", "Avengers: Endgame"],
        "answer": "Gone with the Wind"
    },
    {
        "question": "Who played the character Neo in the movie \"The Matrix\"?",
        "options": ["Tom Cruise", "Brad Pitt", "Leonardo DiCaprio", "Keanu Reeves"],
        "answer": "Keanu Reeves"
    }
]


        self.score = 0
        self.current_question = 0

quiz_instance = Quiz()

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        answer = request.form['answer']
        correct_answer = quiz_instance.questions[quiz_instance.current_question]['answer']
        if answer.lower() == correct_answer.lower():
            quiz_instance.score += 1
        quiz_instance.current_question += 1

    if quiz_instance.current_question < len(quiz_instance.questions):
        question = quiz_instance.questions[quiz_instance.current_question]
        return render_template('quiz.html', question=question)
    else:
        score = quiz_instance.score
        quiz_instance.score = 0
        quiz_instance.current_question = 0
        return render_template('results.html', score=score, num_questions=len(quiz_instance.questions))

if __name__ == "__main__":
    app.run(debug=True)
