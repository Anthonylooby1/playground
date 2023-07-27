from flask import Flask, render_template


app = Flask(__name__)  

@app.route('/play')          
def hello_world():
    return render_template("index.html")

@app.route('/play/<string:color>/<int:num>')
def success(color,num):
    return render_template("index.html", color=color, num = num)

@app.route('/say/flask')
def hello():
    return "Hi Flask"

@app.route('/say/michael')
def based():
    return "Hi michael"

@app.route('/repeat/<string:name>/<int:num>')
def repeat(name,num):
    return f"Hi, {name * num} "

@app.route('/testing/<string:name>/<int:num>')
def big_test(name,num):
    return render_template("hello.html", name=name,num=num)

if __name__=="__main__":    
    app.run(debug=True)  
