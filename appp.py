from flask import Flask
from flask import render_template

app=Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/case1")
def case1():
    return render_template("case1.html")

@app.route("/case2")
def case2():
    return render_template("case2.html")


if __name__=="__main__": #如果以主程式執行
    app.run() #啟動伺服器