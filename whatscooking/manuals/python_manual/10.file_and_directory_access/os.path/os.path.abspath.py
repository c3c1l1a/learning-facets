from os import path 

print path.abspath('bin/app.py')

"""
- Calling os.path.abspath with and empty string returns a the current working directory
- Calling os.path.abspath with a partial pathname contructs a fully fully qualified path name 
out of it, based on the current working directory
- Calling os.path.abspath with a full path name simply returns it
Note 
	- The pathnames you pass to os.path.abspath do not need to exist
	- os.path.abspath not only constructs full path names it also normalizes them. i.e 
	  os.path.abspath('bin/../local/bin') becames /usr/local/bin. Normalizing means made easier
- In most systems this is similar to os.path.normpath
"""