from pydoccano import Doccano

doccano = Doccano(address='http://192.168.2.4:80',
                  username='admin', password='password')

my_user = doccano.me
print(my_user)

print(doccano.projects[0].details)
print(doccano.projects[0].documents.details)
print(doccano.users.details)
print(doccano.projects[0].documents[1].annotations.details)
