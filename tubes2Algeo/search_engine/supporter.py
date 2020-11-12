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