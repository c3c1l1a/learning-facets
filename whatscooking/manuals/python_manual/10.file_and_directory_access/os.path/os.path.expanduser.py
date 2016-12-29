from os.path import expanduser

print expanduser('~') # Returns '/home/cess'
print expanduser('~/test') # Returns '/home/cess/test'
print expanduser('test/') # Returns 'test/'

"""
This function just exands the user. 
"""