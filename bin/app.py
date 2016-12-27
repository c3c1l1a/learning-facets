import web

urls = ('/', 'index')

app = web.application(urls, globals())
render = web.template.render('templates')

class index:
	def GET(self):
		text = "This is the new string now"
		return render.index(text=text)

if __name__ == "__main__":
	app.run()