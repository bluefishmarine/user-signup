from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

class Validator:
  
  something = "hello"
  
  def validate_input(self,text):
    space = " "
    min = 3
    max = 20  
    return (3<= len(text) <=20 and not(space in text))
  
  def method2(self):
    return self.method()+2



@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submitted", methods=['POST'])
def submitted():
    name = request.form['username']
    password = request.form['password']
    password_verified = request.form['passwordv']
    email = request.form['email']

    error_name = "Username is invalid" #No spaces, <3 or >20
    error_password = "Password is invalid" #No spaces, <3 or >20
    error_match = "Passwords do not match"
    error_email = "Invalid Email"


    return render_template("submitted.html", name = name)

app.run()    

