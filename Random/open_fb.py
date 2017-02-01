'''
Purpose: To demonstrate how to access a URL using python urllib.request module
'''

import urllib.request

with urllib.request.urlopen('https://www.facebook.com') as f:
    print(f.read(300)) #Just printing bytecode object

    print(f.read(300).decode('utf-8')) #Decode with utf-8
