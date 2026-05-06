from flask import Flask, render_template, redirect, g
import yaml

app = Flask(__name__)

@app.before_request
def setup_users_dict():
    with open('./users_interests/users.yaml', 'r') as file:
        g.users_dict = yaml.safe_load(file)

@app.route('/')
def index():
    users = [user.capitalize() for user in g.users_dict.keys()]

    return render_template("home.html", content=users)

@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5003)