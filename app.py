from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def calc():
    return render_template("calc.html")

@app.route('/brew')
def brew():
    return render_template("brew.html")


if __name__ == '__main__':
    app.run(debug=True)