import sqlite3
from datetime import datetime

def create_learning_facet():
	learning_facet_title = raw_input("Learning facet title: ")
	learning_facet_body = raw_input("learning facet body: ")
	date_created = datetime.now()
	time = date_created.strftime('%Y/%m/%d-%H-																																							%M')
	save_facet(learning_facet_title, learning_facet_body, time)

def save_facet(*args):	
	conn = sqlite3.connect('myApp.db')
	cursor = conn.cursor()
	cursor.execute('''
				CREATE TABLE if not exists learning_facets(
				facet_title TEXT NOT NULL, 
				facet_body TEXT NOT NULL, 
				date_created TEXT NOT NULL)
		''')

	print '''
			INSERT INTO learning_facets (facet_title, facet_body, date_created) VALUES ('%s', '%s', '%s')
		''' %(args[0], args[1], args[2])

	cursor.execute('''
			INSERT INTO learning_facets (facet_title, facet_body, date_created) VALUES ('%s', '%s', '%s')
		''' %(args[0], args[1], args[2])) 

	conn.commit()
	conn.close()

create_learning_facet()
