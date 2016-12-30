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
	split_name = file_name.split('.')
	new_file = split_name[0]+ "." + str(int(split_name[1]) + 1)
	return new_file

def commit():
	newFileName = increament_revision(readfile('.vcs/master'))
	copy('file.txt', '.vcs/objects/{}'.format(newFileName))
	writefile('.vcs/master', newFileName)

def checkout():
	latest_revision = readfile('.vcs/master')
	copy('.vcs/objects/{}'.format(latest_revision), 'file.txt')