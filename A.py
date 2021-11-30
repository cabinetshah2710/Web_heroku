from types import MethodType
from flask import Flask , render_template , request
from flask.wrappers import Response

app1 = Flask(__name__)

@app1.route("/")
def fun():
    return render_template("index.html")

@app1.route("/submit", methods = ['POST']) 
def submit():
    #html -> .py
    if request.method == "POST":
         name = request.form["username"] 
         country = request.form["Countryname"]
    
    return render_template("submit.html",n = name, c = country)

@app1.route("/Registration" , methods =['POST'])
def reg():
    return render_template("/Registration.html")

@app1.route("/index" , methods = ['POST'])
def back():
    return render_template("/index.html")
    


if __name__ == "__main__":
    app1.run(debug=True)  

