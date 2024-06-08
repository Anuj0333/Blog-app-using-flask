from flask import Flask
app=Flask(__name__)


        

@app.route("/")
def Hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>"\
    "<p>this is paragraph tag</p>"\
    "<ing src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXphdnl4cDhoc3EzeWsyc3Z1aWZodjNoM2VoMTB3bWNoN3JxZXk3eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2QZZMUmvtFYYBUWY/giphy.gif' width=200>"

@app.route("/bye")
def bye():
    return "bye"

@app.route("/username/<name>/<int:number>")
def greeting(name,number):
    return f"hello {name},you got {number}. "

if __name__=="__main__":
    app.run(debug=True)