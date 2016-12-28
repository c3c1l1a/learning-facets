from os.path import expandvars

print expandvars('$HOSTNAME') # Returns 'cecilia'

"""
This method evaluates an enviroment variable given in the input string into a string 
representaion of its value
"""
