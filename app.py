from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def root():
    return render_template('home.html')
    
@app.route('/login',methods=["POST"])
def login():
    return render_template('login.html',username=request.form["username"],requestMethod=request.method)

if __name__=="__main__":
    app.debug = True
    app.run()