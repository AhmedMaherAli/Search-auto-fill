import datetime
from flask import Flask,render_template,request,session
from corpusProcessor import readCorpus,processCorpus,constractFrequancies,fillInput


app= Flask(__name__)

@app.route("/")      #default page will be
def index():
    return render_template("index.html")

@app.route("/api",methods=["GET","POST"])      #default page will be
def hello():


    inpt=request.form.get("inpt")
    suggestions=[]
    props=fillInput(inpt)
    for i in range(0,min(7,len(props))):
        if props[i][1]>0:
            suggestions.append(props[i][0])

    return render_template("index.html",suggestions=suggestions)

@app.route("/corpuloader",methods=["GET","POST"])
def loadData():
    corpus=readCorpus()
    newCorpus=processCorpus(corpus)
    uniqeWords,wordsFrequency,biwordsFreq,triwordsFreq=constractFrequancies(newCorpus)

    return render_template("index.html",msg="loaded")
app.run('0.0.0.0',port=5000)
