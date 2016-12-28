from os.path import commonprefix

print commonprefix(['test/testing/what', 'test/wtf', 'me']) # returns an empty string 
print commonprefix(['test/te', 'test/testing']) # returns 'test/te'


"""
Takes a non optinal list of filepaths and returns a string with the commonprefix in all the 
filepaths. If there is no commonprefix it returns an empty string
"""