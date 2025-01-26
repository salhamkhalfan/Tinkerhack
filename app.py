from flask import Flask, render_template, request,jsonify

# Create a Flask app
app = Flask(__name__)

# Define a route
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)


