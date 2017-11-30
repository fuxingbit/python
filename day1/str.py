#Author: Alienzjn
import getpass

_name = 'zjn'
_password = '123qwe'

name = input("name:")
password = getpass.getpass("password:")

if name == _name and password == _password:
    print("Welcome user {name} login.....".format(name=name))
else:
    print("Invalid name or password!")