from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def birthday():
    if request.method=="POST":
        if request.form["password"]=="13052009":
            return render_template("birthday.html")
            
        else:
            return "incorrect date"
        
    return render_template("web.html")

if __name__== "__main__" :
    app.run(debug=True)