import glob

def read_query(kalimat):
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
    with open(filename,'r') as file:
        for line in file:
            for word in line.split():
                List.append(word)

    return List

listfile = glob.glob('test\\*.txt')
if (listfile == []):  #preventif kalau beda directory
    listfile = glob.glob('..\\test\\*.txt')

# contoh
print(read_query('test queerryyyyy'))
print(read_doc(listfile[0]))