from flask import Flask, request, redirect, render_template, url_for
import cgi
import re


app = Flask(__name__)
app.config['DEBUG'] = True

class Validator:
  
  def validate_input(self,text):
    space = " "
    min = 3
    max = 20  
    return (3<= len(text) <=20 and not(space in text))
  
  def password_match(self,input1,input2):
    return (input1 == input2)

  def validate_email(self,input):
      regex = r"\w+@\w+\.\w+"
      if re.match(regex,input):
          return (True)
      else:
          return (False)
    

error = ""

@app.route("/")
def index():
    return render_template("form.html", errors=error)


@app.route("/submitted")
def submitted():
    return render_template("submitted.html")


@app.route("/", methods=['POST'])
def validate():
    name = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password_verified = cgi.escape(request.form['passwordv'])
    email = cgi.escape(request.form['email'])


    errors = {
        "error_name" : "",
        "error_password" : "",
        "error_match" : "",
        "error_email" : "",
        "contains_error" : False
    }

    if not Validator.validate_input('self',name):
        errors['error_name'] = "Username is invalid" #No spaces, <3 or >20
        errors['contains_error'] = True

    if not Validator.validate_input('self',password):
        errors['error_password'] = "Password is invalid" #No spaces, <3 or >20
        errors['contains_error'] = True

    if not Validator.password_match('self',password,password_verified):
        errors['error_match'] = "Passwords do not match"   
        errors['contains_error'] = True

    if email and not Validator.validate_email('self',email):
        errors['error_email'] = "Invalid Email"          
        errors['contains_error'] = True

    if errors['contains_error']:
        return render_template("form.html", name=name, email=email, errors=errors)

    return redirect("/submitted?name=" + name)

app.run()    

