from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def stemming(string):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    return stemmer.stem(string)

print(stemming("kamulah satu satunya yang cocok menjadi pendampingku"))