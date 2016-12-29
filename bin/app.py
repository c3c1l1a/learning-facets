import web
import os
urls = (
	r'/', 'index',
	r'/display_files', 'display_files' 
)



app = web.application(urls, globals())
render = web.template.render('templates', base="base")

class index:
	def GET(self):
		text = "This is the new string now"
		return render.index()

class display_files:
	def GET(self):
		fp=open('whatscooking/testfiles/jsfile.txt','r')
		text=fp.read()
		fp.close()
		return render.file_display(text) 
if __name__ == "__main__":
	app.run()