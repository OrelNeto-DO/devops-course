from flask import Flask, render_template, request, redirect, url_for
import random
import requests

app = Flask(__name__)

# נתיב ראשי עם ברכה ושאלות
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('quiz', username=username))
    return render_template('index.html')

# נתיב לשאלות עם ניחוש גיל ומין
@app.route('/quiz/<username>', methods=['GET', 'POST'])
def quiz(username):
    if request.method == 'POST':
        age = random.randint(18, 60)  # ניחוש אקראי לגיל
        gender = random.choice(['Male', 'Female'])  # ניחוש אקראי למין
        return render_template('quiz.html', username=username, age=age, gender=gender)
    return render_template('quiz.html', username=username)

# נתיב API חתולים
@app.route('/catapi')
def catapi():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_data = response.json()
    cat_image = cat_data[0]['url']
    return render_template('catapi.html', cat_image=cat_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
