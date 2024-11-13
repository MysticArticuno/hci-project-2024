from flask import Flask, request, jsonify, abort

from data_access import TicketDataAccess, OrderItemDataAccess
from model import Ticket, OrderItem

ticket_data_access = TicketDataAccess()

app = Flask(__name__)

# GET Requests

@app.route("/")
def route_root():
    return "Hello! Server is Working!"

@app.get("/tickets")
def route_tickets():
    return ticket_data_access.get_all_tickets()

@app.get("/tickets/<ticket_id>")
def route_tickets_ticketid(ticket_id):
    return_ticket = ticket_data_access.get_ticket_by_id(ticket_id)
    if return_ticket == None:
        abort(400)
    else:
        return return_ticket.__dict__, 200

@app.get("/tickets/table/<table_number>")
def route_tickets_table(table_number):
    return ticket_data_access.get_tickets_by_table_number(table_number)

@app.get("/items")
def route_items():
    return OrderItemDataAccess.get_all_order_items_list()

@app.get("/categories")
def route_categories():
    return OrderItemDataAccess.get_all_categories()

@app.get("/items/<item_name>")
def route_items_itemname(item_name):
    item = OrderItemDataAccess.get_order_item_mods_by_name(item_name)
    if item == None:
        abort(400)
    else:
        return item

@app.get("/archive")
def route_archive():
    return TicketDataAccess.getArchivedTickets(item_name)

# POST Requests

@app.post("/tickets/add")
def route_add():
    data = request.get_json()
    if request.method != "POST":
        return 400
    # Create Ticket
    result = TicketDataAccess.create_ticket(data)
    if result == None:
        return 400
    else:
        return result.__dict__, 200

@app.post("/tickets/drop")
def route_drop():
    data = request.get_json()
    if request.method != "POST":
        return 400
    # Create Ticket
    result = TicketDataAccess.create_ticket(data)
    if result == None:
        return 400
    else:
        return result.__dict__, 200

