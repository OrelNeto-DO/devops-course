from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            return f'''
                <link rel="stylesheet" href="/static/style.css">
                <div class="container">
                    <h1>Hello {name}! Welcome to our app!</h1>
                    {get_navigation_links()}
                </div>
            '''
    return '''
        <link rel="stylesheet" href="/static/style.css">
        <div class="container">
            <h1>Welcome!</h1>
            <form method="POST" class="form-group">
                <label>What's your name?</label><br>
                <input type="text" name="name" class="input-field"><br>
                <input type="submit" value="Submit" class="button">
            </form>
        </div>
    '''

@app.route('/cats')
def cats():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_data = response.json()
    cat_image_url = cat_data[0]['url']
    
    return f'''
        <link rel="stylesheet" href="/static/style.css">
        <div class="container">
            <h1>Cute Cats! 🐱</h1>
            <div class="image-container">
                <img src="{cat_image_url}" alt="Random Cat" class="cat-image">
            </div>
            <button onclick="location.reload()" class="button">Show Another Cat</button>
            {get_navigation_links()}
        </div>
    '''

@app.route('/jokes')
def jokes():
    jokes_list = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What did the grape say when it got stepped on? Nothing, it just let out a little wine!",
        "Why don't eggs tell jokes? They'd crack up!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why can't a nose be 12 inches long? Because then it would be a foot!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What did the ocean say to the shore? Nothing, it just waved!"
    ]
    joke = random.choice(jokes_list)
    
    return f'''
        <link rel="stylesheet" href="/static/style.css">
        <div class="container">
            <h1>Random Jokes 😄</h1>
            <div class="joke-text">
                {joke}
            </div>
            <button onclick="location.reload()" class="button">New Joke</button>
            {get_navigation_links()}
        </div>
    '''

@app.route('/gender-guesser', methods=['GET', 'POST'])
def gender_guesser():
    if request.method == 'POST':
        height = int(request.form.get('height', 0))
        shoe_size = int(request.form.get('shoe_size', 0))
        likes_shopping = request.form.get('likes_shopping') == 'yes'
        plays_video_games = request.form.get('plays_video_games') == 'yes'
        likes_sports = request.form.get('likes_sports') == 'yes'
        
        score = 0
        if height > 175: score += 1
        if shoe_size > 42: score += 1
        if likes_shopping: score -= 1
        if plays_video_games: score += 1
        if likes_sports: score += 1
        
        guess = "male" if score > 0 else "female"
        confidence = abs(score) * 20
        
        return f'''
            <link rel="stylesheet" href="/static/style.css">
            <div class="container">
                <h1>Result</h1>
                <h2>Based on your answers, I guess you are: {guess}</h2>
                <p>Confidence level: {min(confidence, 100)}%</p>
                <button onclick="window.location.href='/gender-guesser'" class="button">Try Again</button>
                {get_navigation_links()}
            </div>
        '''
    
    return f'''
        <link rel="stylesheet" href="/static/style.css">
        <div class="container">
            <h1>Gender Guesser 🤔</h1>
            <form method="POST" class="form-group">
                <div class="form-field">
                    <label>Height (cm):</label><br>
                    <input type="number" name="height" class="input-field" required>
                </div>
                
                <div class="form-field">
                    <label>Shoe Size (EU):</label><br>
                    <input type="number" name="shoe_size" class="input-field" required>
                </div>
                
                <div class="form-field">
                    <label>Do you like shopping?</label><br>
                    <select name="likes_shopping" class="input-field">
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                
                <div class="form-field">
                    <label>Do you play video games?</label><br>
                    <select name="plays_video_games" class="input-field">
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                
                <div class="form-field">
                    <label>Do you like sports?</label><br>
                    <select name="likes_sports" class="input-field">
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                
                <input type="submit" value="Guess!" class="button">
            </form>
            {get_navigation_links()}
        </div>
    '''

def get_navigation_links():
    return '''
        <nav class="navigation">
            <a href="/" class="nav-link">Home</a> |
            <a href="/cats" class="nav-link">Cats</a> |
            <a href="/jokes" class="nav-link">Jokes</a> |
            <a href="/gender-guesser" class="nav-link">Gender Guesser</a>
        </nav>
    '''

if __name__ == '__main__':
    app.run(debug=True)