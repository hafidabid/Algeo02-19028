from mesinkata import *
from stemming import *
from similiaritas import *
DOCS_FOLDER = "..\\test\\*.txt"

filelist = listfile(DOCS_FOLDER)

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

qweri = "playstation"
qweri = stemming(qweri)
qd = makeQueryVektor(qweri)
qd_vektor = toVector(qd)
vektorDokumen = []
for x in filelist:
    vektorDokumen.append(toVector(makeDocsVektor(qd,x)))
hasil_similaritas = []
for x in range(len(vektorDokumen)):
    temp = vektorDokumen[x]
    hasil_similaritas.append(sim(temp,qd_vektor))

urutan_docs = [(hasil_similaritas[x],x) for x in range(len(hasil_similaritas))]
for x in range(len(urutan_docs)):
    for y in range(x,len(urutan_docs)):
        if urutan_docs[y][0]>urutan_docs[x][0]:
            temp = urutan_docs[x]
            urutan_docs[x] = urutan_docs[y]
            urutan_docs[y] = temp

print(urutan_docs)
for x in range(len(hasil_similaritas)):
    dirr = filelist[urutan_docs[x][1]]
    print(getjudul(dirr))

