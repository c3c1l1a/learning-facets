from os.path import exists, abspath

print exists('..') # Returns True
print exists('testfile.txt') # returns True
print exists(abspath('../../../../../bin/')) # Returns True
print exists(abspath('../../../../bin/')) # Returns False


"""
This function return True if a filepath exists. In some architetures however it might return 
False if permission is not granted to execute os.stat()

Note:
	- Returns False on broken symbolic links
"""
