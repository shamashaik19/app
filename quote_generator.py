from flask import Flask, render_template
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "It always seems impossible until it’s done. – Nelson Mandela"
]

@app.route('/')
def home():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
