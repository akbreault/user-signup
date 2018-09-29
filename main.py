from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_home_page_form():
    return render_template('home-page.html', title='Signup')

def valid_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    elif " " in username:
        return False
    return True

def valid_password(password):
    if len(password) < 3 or len(password) > 20:
        return False
    elif " " in password:
        return False
    return True

def matching_password(password, password_confirmation):
    if len(password_confirmation) < 3 or len(password_confirmation) > 20:
        return False
    elif password != password_confirmation:
        return False
    return True

def valid_email(email):
    email = str(email)
    if "@" not in email or "." not in email:
        return False 
    elif email.count('@') > 1 or email.count(".") > 1:
        return False
    elif " " in email:
        return False
    elif len(email) < 3 or len(email) > 20:
        return False
    return True
    


@app.route("/", methods=['POST'])
def valid_input():
    username = request.form['username']
    password = request.form['password']
    password_confirmation = request.form['password-confirmation']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_confirmation_error = ''
    email_error = ''

    if not valid_username(username):
        username_error = 'Not a valid username'

    if not valid_password(password):
        password_error = 'Not a valid password'

    
    if valid_password(password):
        if not matching_password(password, password_confirmation):
            password_confirmation_error = 'Passwords do not match'
    
    if len(email) != 0:
        if not valid_email(email):
            email_error = "Not a valid email"
            email = ''
   
    if not username_error and not password_error and not password_confirmation_error and not email_error:
        username = str(username)
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('home-page.html', title='Signup', username_error=username_error, password_error=password_error,
        password_confirmation_error = password_confirmation_error, email_error = email_error, username=username, email=email) 



@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome-page.html', title='Welcome!', username=username)


app.run()

