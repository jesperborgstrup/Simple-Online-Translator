'''
Created on Mar 13, 2012

@author: Jesper
'''

class User:
    username = None
    password = None
    name = None
    languages = []
    admin = False

    def __init__(self, username, password, name, languages, admin=False):
        self.username = username
        self.password = password
        self.name = name
        self.languages = languages
        self.admin = admin
        
    def __str__(self):
        return "User %s %s" % ( self.name, self.languages )
        
        