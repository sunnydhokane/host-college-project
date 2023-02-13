from flask import Flask, render_template, escape, request, redirect
from CollegeAllotment import algorithms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predictCollege')
def predictCollege():
    return render_template("predictCollege.html")

@app.route('/results')
def results():
    a=""
    marks=request.args.get('marks')
    algorithm=request.args.get('algo')
    c=algorithms()
    numbers=[1,2,3,4,5]
    if algorithm=="KNN":
        colleges=c.predictKNN(marks)
        a="multi"
        return render_template("results.html",colleges=colleges,a=a)
    elif algorithm=="SVM":
        college=c.predictSVM(marks)
        colleges=[]
        colleges.append(college)
        a="single"
        return render_template("results.html",colleges=colleges,a=a)
        
@app.route('/colleges')
def colleges():
    return render_template("colleges.html")
   
@app.route('/sortedResults')
def sortedResults():
    start=float(request.args.get('minpercentage'))
    end=float(request.args.get('maxpercentage'))
    results=int(request.args.get('results'))
    c=algorithms()
    my_list=c.get_by_range(start,end,results)
    return render_template("sortedResults.html",my_list=my_list,size=len(my_list))

if __name__ == '__main__':
    from waitress import serve
    serve(app,host='0.0.0.0',port=8080)