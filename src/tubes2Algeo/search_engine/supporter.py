import glob
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def txtToStr(fileloc):
    a = ""
    with open(fileloc,'r',errors="ignore") as f:
        for x in f:
            a =a+x
    
    return a

def ignoreSpace(teks):
    s = ""
    for x in teks:
        if(x!=" "):s=s+x
    return s

def stemming(string):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(string)

def convertdir(olddir):
    newstr = ""
    for x in range(len(olddir)):
        if(olddir[x]=='/'):
            newstr=newstr+"\\"
        else:
            newstr=newstr+olddir[x]
    
    return newstr

def getFileExtension(f):
    stry = ""
    if "." in f:
        a = 0
        while(f[a]!="."):
            a=a+1
        stry = f[a::]
        return stry
    else:
        return stry

def read_query(kalimat):
    #kalimat = stemming(kalimat)
    List = []
    temp = ''
    for char in kalimat:
        if char != ' ':
            temp = temp + char
        elif((char == ' ') and (temp != '')):
            List.append(temp)
            temp = ''

    List.append(temp)
    return(List)

def read_doc(filename):
    strr =""
    with open(filename,'r',errors="ignore") as file:
        for line in file:
            strr = strr+line

    return read_query(strr)

def listfile(filedir):
    return  glob.glob(filedir)

def getparentdir(childdir):
    n = len(childdir)-1
    flag = True
    while(childdir[n]!="\\" and childdir[n]!="/" and flag):
        childdir=childdir[:n:]
        n=n-1
        if(n<1) : flag = False
    return childdir

def getfilename(directory):
    a = getparentdir(directory)
    s=""
    for x in range(len(a),len(directory)):
        s = s+directory[x]

    return s

def getjudul(filee, isapath = False):
    a = filee
    if isapath: 
        a = getfilename(filee)
    a = a[:len(a)-4:]
    return a

def dotproduct(V1,V2):
    sum = 0
    for i in range(len(V1)):
        sum = sum+(V1[i]*V2[i])
    return(sum)

def length(V):
    sum = 0
    for i in range(len(V)):
        sum += V[i]**2
    return(sum**0.5)

def sim(V1,V2):
    a = (length(V1)*length(V2))
    return(dotproduct(V1,V2)/a)

def makeQueryVektor(query):
    retdict = dict()
    wordlist = read_query(query)
    for x in wordlist:
        if x in retdict.keys():
            retdict[x] = retdict[x]+1
        else:
            retdict[x] = 1

    return retdict

def makeDocsVektor(Qdict,fileloc):
    retdict = dict()
    wordlist = read_doc(fileloc)
    for x in Qdict:
        retdict[x] = 0
    for x in wordlist:
        if x in Qdict.keys() and x in retdict.keys():
            retdict[x]=retdict[x]+1

    return retdict

def toVector(anDict):
    retlist = []
    for x in anDict:
        temp = anDict[x]
        retlist.append(int(temp))

    return retlist

def appendKK(oldarr,apendeeArr):
    for x in apendeeArr:
        if (not(x in oldarr)):
            oldarr.append(x)
    
    return oldarr

def makeNolDict(dictarr):
    retrn = dict()
    for x in dictarr:
        if x not in retrn.keys():
            retrn[x] = 0
    return retrn

def hitungKamusKata(globaldict, qparse):
    for x in qparse:
        if x in globaldict.keys():
            globaldict[x] = globaldict[x]+1
        else:
            globaldict[x] = 1
    
    return globaldict

def sortDictionary(aDict):
    dictlist = list(aDict.keys())
    dictlist2 = list(aDict.keys())
    newdict = dict()
    for x in range(len(dictlist)):
        for y in range(x+1,len(dictlist)):
            if aDict[dictlist[y]] > aDict[dictlist[x]]:
                temp = dictlist2[y]
                dictlist2[y] = dictlist2[x]
                dictlist2[x] = temp
    
    for x in dictlist2:
        newdict[x] = aDict[x]
    
    return newdict

def getPrevDocs(fileloc):
    a = txtToStr(fileloc)
    n = len(a)
    newstr = ""
    cnt = 0
    while((a[cnt]!=" " or cnt<300) and cnt<n):
        newstr=newstr+a[cnt]
        cnt=cnt+1
    
    newstr = newstr + " .... (click title to see details)"
    return newstr