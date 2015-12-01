import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://tylercitrin:9nv683g@localhost/microcalc"
#'postgresql:///' + os.path.join(basedir, 'microcalc.db')
#"postgresql://tylercitrin:9nv683g@localhost/microcalcdb"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
	#postgresql[+driver]://<user>:<pass>@<host>/<dbname>
	#'postgresql://' + os.path.join(basedir, 'app.db')



WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
"""
# cross-site request forgery prevention 
#(note that this setting is enabled by default in current versions of Flask-WTF). 
# In most cases you want to have this option enabled as it makes your app more secure.
"""


#SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
			#"postgresql://tcitrin:9nv683g@localhost:5432/microcalcdb"
			#'postgres://username:password@localhost:5432/dbname'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/DBNAME"