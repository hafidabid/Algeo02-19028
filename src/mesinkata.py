import glob
from src.stemming import *


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
    List = []
    strr =""
    with open(filename,'r',errors="ignore") as file:
        for line in file:
            strr = strr+line

    return read_query(strr)



def listfile(filedir):
    return  glob.glob(filedir)

def getparentdir(childdir):
    n = len(childdir)-1
    while(childdir[n]!="\\"):
        childdir=childdir[:n:]
        n=n-1
    return childdir

def getfilename(directory):
    a = getparentdir(directory)
    s=""
    for x in range(len(a),len(directory)):
        s = s+directory[x]

    return s

def getjudul(filee):
    a = getfilename(filee)
    a = a[:len(a)-4:]
    return a
