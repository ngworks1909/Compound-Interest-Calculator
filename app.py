from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"]) / 100
        time = float(request.form["time"])
        compound_frequency = int(request.form["compound_frequency"])
        if compound_frequency == 0:
            return render_template("index.html", result=0)
        amount = principal * (1 + rate/compound_frequency)**(compound_frequency*time)
        result = amount - principal
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)