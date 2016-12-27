import web # wft

urls = ('/', 'index')

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
	def GET(self):
		greetings = "Hello there"
		return render.index(greeting = greetings)


if __name__ == "__main__":
	app.run()

