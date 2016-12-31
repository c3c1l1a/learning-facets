import web
from os import walk, listdir
import pdb


urls = (
	r'/', 'index',
	r'/whats_cooking/', 'whats_cooking'
)

app = web.application(urls, globals())
render = web.template.render('templates', base="base")

class index:
	def GET(self):
		return render.index(urls)

class whats_cooking:
	def GET(self):
		dirs = []
		for item in listdir('whatscooking'):
			global urls 
			urls = urls + ('/whats_cooking/' + item, item)
			globals()[item] =  create_class(item)
			dirs.append(item)
		return render.whatscooking(dirs)

def create_class(class_name):
	print "please create the class"
	GET = lambda self: render.whatcooking_subdirs(display_files(class_name))
	new_class_name = type(class_name, (), {
		'GET': GET
	})
	return new_class_name

def display_files(class_name):
	text_files = []
	for (dirpath, dirnames, filenames) in walk('whatscooking/' + class_name):
		for filename in filenames:
			fp=open(dirpath + '/' + filename,'rU')
			text_files.append(fp.read())
			fp.close()
	return text_files 


if __name__ == "__main__":
	app.run()
	