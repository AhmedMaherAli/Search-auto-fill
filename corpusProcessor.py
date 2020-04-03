import re
import numpy as np

biwordsFreq=dict()
triwordsFreq=dict()
wordsFrequency=dict()
uniqeWords=[]



def readCorpus():
    file=open("C:\\Users\\hp\\Desktop\\20160025 20160014 20160322\\flaskWebVersion\\bin\\myCorpusf.txt","r",encoding="utf-8")
    s=""
    s+=file.read()
    print("Corpus Length is:", len(s))
    return s

def processCorpus(corpus):
    newCorpus=corpus
    newCorpus=re.sub('[-—؛\d+\[\]\.+\n+\:+\،؟+\(\)«»]',' ',newCorpus)
    newCorpus=re.sub('(ّ)?(َ)?(ً)?(ُ)?(ٌ)?(ِ)?(ٍ)?(~)?(ْ)?', "",newCorpus)
    newCorpus=re.sub('[(\\ufeff)(\\U00100001)+]', '', newCorpus)
    newCorpus=re.sub(' +', ' ', newCorpus)
    return newCorpus

def makeWordsFreq(newCorpus):
    wordslist=newCorpus.split(' ')

    for word in wordslist:
        if word not in uniqeWords:
            uniqeWords.append(word)
            wordsFrequency[word]=wordslist.count(word)

    return uniqeWords,wordslist,wordsFrequency


def makeBiTriWordsFreqs(wordslist):
    biwordslist=[]
    triwordslist=[]
    for i in range(1,len(wordslist)):
        biwordslist.append(wordslist[i-1]+" "+wordslist[i])

    for i in range(2,len(wordslist)):
        triwordslist.append(wordslist[i-2]+" "+wordslist[i-1]+" "+wordslist[i])


    for word in biwordslist:
        biwordsFreq[word]=biwordslist.count(word)

    for word in triwordslist:
        triwordsFreq[word]=triwordslist.count(word)


    return biwordsFreq,triwordsFreq




def constractFrequancies(newCorpus):
    uniqeWords,wordslist,wordsFrequency=makeWordsFreq(newCorpus)
    biwordsFreq,triwordsFreq=makeBiTriWordsFreqs(wordslist)

    return uniqeWords,wordsFrequency,biwordsFreq,triwordsFreq



def fillInput(inpt):
    splitedInpt=inpt.split(" ")
    inptLn=len(splitedInpt)
    props=dict()

    inpt=splitedInpt[inptLn-2]+" "+splitedInpt[inptLn-1]
    for word in uniqeWords:
        key=inpt+" "+word
        if key in triwordsFreq:
            p=triwordsFreq[key]/(biwordsFreq[inpt]*wordsFrequency[splitedInpt[0]])

        else:
            p=0

        props[key]=p

    props=sorted(props.items(), key =
                 lambda kv:(kv[1], kv[0]),reverse=True)

    return props










"""



incase of probability calculated on the entire sentence not just last two words, just replace this function with the above one

def fillInput(inpt,uniqeWords,wordsFrequency,biwordsFreq,triwordsFreq):
    splitedInpt=inpt.split(" ")
    inptLn=len(splitedInpt)
    props=dict()
    firstprop=0
    base=""
    for i in range(0,inptLn-2):
        base+=(splitedInpt[i]+" ")

    if inptLn <2:
        return props
    for cnt in range(0,inptLn-2):
        if (splitedInpt[cnt]+" "+splitedInpt[cnt+1]+" "+splitedInpt[cnt+2]) in triwordsFreq and (splitedInpt[cnt]+" "+splitedInpt[cnt+1]) in biwordsFreq and splitedInpt[cnt] in wordsFrequency:
            tripart=triwordsFreq[splitedInpt[cnt]+" "+splitedInpt[cnt+1]+" "+splitedInpt[cnt+2]]
            bipart=biwordsFreq[splitedInpt[cnt]+" "+splitedInpt[cnt+1]]
            t=tripart/(bipart*wordsFrequency[splitedInpt[cnt]])
            firstprop+=np.log10(t)

    inpt=splitedInpt[inptLn-2]+" "+splitedInpt[inptLn-1]
    for word in uniqeWords:
        key=inpt+" "+word

        if key in triwordsFreq:
            p=triwordsFreq[key]/(biwordsFreq[inpt]*wordsFrequency[splitedInpt[0]])
            p=np.log10(p)+firstprop
        else:
            p=0
        print(key,' ',p)
        key=base+" "+key
        props[key]=p

    props=sorted(props.items(), key =
                 lambda kv:(kv[1], kv[0]),reverse=True)
    return props

    """
