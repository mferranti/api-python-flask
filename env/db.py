from flask.ext.mysql import MySQL

mysql = MySQL()
	     
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'taringa_mysql'
app.config['MYSQL_DATABASE_DB'] = 'taringa'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)


