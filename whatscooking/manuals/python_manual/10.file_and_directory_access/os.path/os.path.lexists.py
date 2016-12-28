from os.path import lexists, abspath

print lexists('testfile.txt') # returns True
print lexists(abspath('../../../../../bin/')) # Returns True
print lexists(abspath('../../../../bin/')) # Returns False

"""
Similar to os.path.exists.
In some architecures it might return False if permission to execute os.lstat is not granted.

Note:
- It returns True fro broken symlinks. (This is the biggest difference with exists)

"""