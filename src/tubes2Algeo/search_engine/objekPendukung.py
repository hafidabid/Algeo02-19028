class HasilPencarian:
    def __init__(self,id,judul,fileloc,sastrawifile):
        self.id = id
        self.title = judul
        self.ori_file = fileloc
        self.stemmed_file = sastrawifile
        self.similaritas =0
        self.vectorDict= {}
        self.preview = ""
        self.jumlahkata = 0

    
    def setsimilaritas(self,similaritas):
        self.similaritas = similaritas
    
    def setpreview(self,previewdocs):
        self.preview = previewdocs
    
    def setvectorDict(self,vdict):
        self.vectorDict=vdict

    def setJumlahKata(self,number):
        self.jumlahkata = number