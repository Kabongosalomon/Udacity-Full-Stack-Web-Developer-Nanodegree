# Improt Flask class from Flask libary
from flask import Flask, render_template
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)


# import CRUD Operations 
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# add decorators
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')

def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	#output = ''
	#for i in items:
	#	output += i.name
	#	output += '</br>'
	#	output += i.price
	#	output += '</br>'
	#	output += i.description
	#return output
	return render_template('menu.html', restaurant = restaurant, items = items)

#Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/')

def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"


#Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')


def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

#Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')

def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"




# Execute only if file is run by python interpreter
if __name__ == '__main__':
	# Reload server when code changes
    app.debug = True
    # Run local server with the application
    # Listen on all public addresses
    app.run(host='0.0.0.0', port=5000)