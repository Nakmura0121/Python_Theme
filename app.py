from flask import Flask, render_template, redirect, url_for, request
import psycopg2
from user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

@app.route('/')
def book_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)