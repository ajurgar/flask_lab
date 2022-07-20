from app import app
from flask import render_template
from models.customer_orders import orders



@app.route('/orders')
def index():
    return render_template('index.html', title = "My Orders", all_orders = orders)

@app.route('/orders/<index>')
def order(index):
    return render_template("order.html", title = "My Order", order = orders[int(index)])