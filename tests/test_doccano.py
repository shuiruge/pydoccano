from pydoccano import Doccano

doccano = Doccano('http://localhost:80', 'admin', 'password')

docs = doccano.projects[1].documents
doc = docs[10]
anns = doc.annotations
