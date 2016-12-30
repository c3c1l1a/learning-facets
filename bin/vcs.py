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

