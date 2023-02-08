from flask import Flask, render_template, request
import numpy as np
import pickle 
from os import name
model_Support_Vector_Machine = pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\SVM_lin.pkl' ,'rb'))
model_DecisionTree =pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\DST.pkl' ,'rb'))
model_KNN =pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\knn.pkl' ,'rb'))
model_Logistic_Regression =pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\LR.pkl' ,'rb'))
model_catboost =pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\clf.pkl' ,'rb'))
model_native_bayes =pickle.load(open('C:\\Users\\Lenovo\\Music\\al - Copy\\DST.pkl' ,'rb'))
app = Flask(__name__, static_folder='templates')
items  =[]
def check_answer (name) :
    if(name  == "Fully Agree") :
        return 3
    elif(name  == "Partially Agree"):
        return 2
    elif(name  == "Slightly Agree"):
        return 1
    elif(name  == "neutral"):
        return 0
    elif(name  == "Slightly disagree"):
        return -1
    elif(name  == "Partially disagree"):
        return -2
    elif(name  == "Fully disagree"):
        return -3
    return 1



@app.route('/home')
@app.route('/')
def home():
    return render_template("page.html")


@app.route('/sub' , methods=['POST' , 'GET'])

def submit():
    # form html to python 
    if request.method == "POST" :
        x = range(21)
        for i in x :
            t =  str(i)
            data1 = request.form[t]
            items.append(check_answer(data1))
    # from python to html
    return render_template("sub.html")

def check_model(name) :
    arr = np.array([items])
    if(name  == "Decision tree"):
        model_DecisionTree.predict(arr)
    elif(name  == "SVM algorithm"):
        model_Support_Vector_Machine.predict(arr)
    elif(name  == "Naive Bayes algorithm"):
        model_native_bayes.predict(arr)
    elif(name == "Logistic regression"):
        model_Logistic_Regression.predict(arr)
    elif(name == "KNN algorithm"):
        model_KNN.predict(arr)
    elif(name == "Catboost alogrithm"):
        model_catboost.predict(arr)
    return model_DecisionTree.predict(arr)

@app.route('/final' , methods=['POST' , 'GET'])

def show_answers():
   
    name=request.form['0']
    reuslt = check_model(name)
    items.clear()
    return render_template("final.html" ,mymarks =reuslt)
    

if __name__ == "__main__":
    app.run(debug=True)



