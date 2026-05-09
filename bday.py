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

import os
if __name__== "__main__" :
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
