from flask import Flask, render_template, redirect, g
import yaml

app = Flask(__name__)

with open('./users_interests/users.yaml', 'r') as file:
    users_dict = yaml.safe_load(file)

def get_total_interests():
    return sum(len(user_details["interests"])
               for user_details in users_dict.values())

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    users = [user.capitalize() for user in users_dict.keys()]
    return render_template("home.html",
                           users=users,
                           total_interests=get_total_interests(),
                           total_users=len(users_dict))

def get_user_details(name):
    users_details = users_dict.get(name.lower())
    if users_details:
        email = users_details.get("email", 'None listed')

        if users_details["interests"]:
            interests = ', '.join(name.capitalize() for name in users_details["interests"]) + '.'
        else:
            interests = f'{name} has listed no interests.'
    
    return (email, interests)

@app.route('/user/<name>')
def user(name):
    if name.lower() not in users_dict.keys():
        return redirect('/home')

    email, interests = get_user_details(name)
    other_users = [user.capitalize() for user in users_dict.keys()
                   if user != name.lower()]

    return render_template("user.html",
                           name=name,
                           email=email,
                           interests=interests,
                           others=other_users,
                           total_interests=get_total_interests(),
                           total_users=len(users_dict))

if __name__ == '__main__':
    app.run(debug=True, port=5003)