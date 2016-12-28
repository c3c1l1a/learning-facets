from os import path


print path.basename('test/test') #returns test
print path.basename('test/test/') #returns an empty string

"""
Implements os.path.split but returns the second part of the returned value
"""
