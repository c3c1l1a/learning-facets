import hashlib
import os

def readfile(file):
	f = open(file, 'rU')
	content = f.read()
	f.close()
	return content

def writefile(file, content):
	f = open(file, 'w+')
	f.write(content)
	f.close()

def copy(src_file, dest_file):
	src_file_content = readfile(src_file)
	writefile(dest_file, src_file_content)
	
def increament_revision(file_name):
	new_file = md5_file_encrypt(file_name)
	return new_file

def md5_file_encrypt(file):
	hasher = hashlib.md5()
	file_content = readfile(file)
	hasher.update(file_content)
	hashed_content = hasher.hexdigest()
	return hashed_content 

def commit():
	# initial commit
	print "committing.."
	new_file_name = increament_revision("whatscooking/testfiles/pythonfile.py")
	print new_file_name
	copy('whatscooking/testfiles/pythonfile.py', '.vcs/objects/{}'.format(new_file_name))
	writefile('.vcs/master', new_file_name)	

def checkout():
	latest_revision = readfile('.vcs/master')
	copy('.vcs/objects/{}'.format(latest_revision), 'file.txt')



