from flask import Flask,render_template,request
import pickle


app =Flask(__name__)
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login" , methods =["POST"])
def login1():
    e=request.form.get("T1")
    p=request.form.get("T2")
    if e=="abc" and p=="123":
        return "Login Sucess"
    else:
        return "Failed"
    

@app.route("/addition")
def add():
    return render_template("addition.html")

@app.route("/addition" , methods =["POST"])
def add1():
    Num1=int(request.form.get("N1"))
    Num2=int(request.form.get("N2"))
    Num3=Num1+Num2
    return render_template("addition.html", Number3=Num3)


@app.route("/NB")
def NB():
    return render_template("NB.html")

@app.route("/NB" , methods =["POST"])
def NB1():
    L1=[]
    L1.append(int(request.form.get("N1")))
    L1.append(int(request.form.get("N2")))
    L1.append(int(request.form.get("N3")))
    L1.append(int(request.form.get("N4")))

    
    with open("NB.pkl", "rb") as f:
        model=pickle.load(f)
    
    predy=model.predict([L1])[0]
    if predy==1:
        result="Yes"

    else:
        result="No"
    return render_template("NB.html", Answer=result)


@app.route("/RF")
def RF():
    return render_template("RF.html")

@app.route("/RF" , methods =["POST"])
def RF1():
    L1=[]
    L1.append(int(request.form.get("N1")))
    L1.append(int(request.form.get("N2")))
    L1.append(int(request.form.get("N3")))
    L1.append(int(request.form.get("N4")))

    with open("RF.pkl", "rb") as f:
        model=pickle.load(f)
    
    predy=model.predict([L1])[0]
    if predy==1:
        result="Yes"

    else:
        result="No"
    return render_template("RF.html", Answer=result)





if __name__=="__main__":
        app.run(debug=True,port=5000)