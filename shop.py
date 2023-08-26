from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
name = "Kuromi"

# Sample database to store the logged-in username
logged_in_user = None

@app.route("/") # same as @app.get('/')
def welcome():
    return "<p>Welcome to Bingus Coffee!</p>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in_user
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            logged_in_user = username
            return redirect(url_for('success'))
        else:
            return "Username Not Provided."
    else:
        return render_template('login.html')  # Render the login form


@app.route('/success', methods=['GET'])
def success():
    global logged_in_user
    if logged_in_user:
        return f" Hi, {logged_in_user}<br>Don't Be Depresso, Sip Some Espresso at BingusCoffee!"
    else:
        return "No User Logged in!"


@app.route('/logout', methods=['GET'])
def logout():
    global logged_in_user
    logged_in_user = None  # Clear logged_in_user 
    return redirect(url_for('welcome'))  # Redirect to the home page


