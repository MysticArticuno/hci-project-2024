import datetime, json
from flask import jsonify
from model import Ticket

class TicketDataAccess:

        _tickets = []

        @staticmethod
        def _get_next_id(): # Private Method
            return len(TicketDataAccess._tickets)

        @staticmethod
        def get_ticket_by_id(id):
            for t in TicketDataAccess._tickets:
                if int(t.ticket_id) == int(id):
                    return t
            return None

        @staticmethod
        def get__filtered_ticket_by_id(id, station):
            for t in TicketDataAccess._tickets:
                if int(t.ticket_id) == int(id):
                    return t
            return None

        @staticmethod
        def get_all_tickets():
            return_tickets = []
            for t in TicketDataAccess._tickets:
                return_tickets.append(t.__dict__)
            return return_tickets

        @staticmethod
        def get_tickets_by_table_number(num):
            return_tickets = []
            for t in TicketDataAccess._tickets:
                if int(t.table_number) == int(num):
                    return_tickets.append(t.__dict__)
            return return_tickets

        @staticmethod
        def create_ticket(data):
            # Parse data coming from the POST request
            try:
                new_ticket = Ticket() # Create a new Ticket
                new_ticket.ticket_date = str(datetime.datetime.now().date()) # Give ticket a date
                new_ticket.ticket_time = str(datetime.datetime.now().strftime("%H:%M:%S")) # Give ticket a time
                is_togo = data["is_togo"] # Give the ticket object the correct fields
                if is_togo == True:
                    new_ticket.is_togo = True
                    new_ticket.customer_name = data["customer_name"]
                    new_ticket.customer_email = data["customer_email"]
                    new_ticket.customer_number = data["customer_number"]
                else:
                    new_ticket.is_togo = False
                    new_ticket.table_number = int(data["table_number"])
                    new_ticket.server_name = data["server_name"]
                    new_ticket.guest_count = int(data["guest_count"])
                new_ticket.items = data["items"] # Add Item List
        
            except KeyError: # In case of an invalid JSON field
                return None 

             # JSON data is okay, safe to create ticket
            new_ticket.ticket_id = TicketDataAccess._get_next_id() # Give ticket a unique ID
            TicketDataAccess._tickets.append(new_ticket) # Add ticket to internal array
            return new_ticket
            
class OrderItemDataAccess:

        _ITEM_JSON_LOCATION = "data/items.json"
        _CATEGORY_JSON_LOCATION = "data/categories.json"

        @staticmethod
        def _get_obj_from_json(name):
            with open(OrderItemDataAccess._ITEM_JSON_LOCATION) as f:
                data = json.load(f)
                for item in data:
                    if item["name"] == name:
                        return item

        @staticmethod
        def get_order_item_mods_by_name(name):
            item = OrderItemDataAccess._get_obj_from_json(name)
            return item

        @staticmethod
        def get_all_categories():
            with open(OrderItemDataAccess._CATEGORY_JSON_LOCATION) as f:
                data = json.load(f)
                return data

        @staticmethod
        def get_all_order_items_list():
            with open(OrderItemDataAccess._ITEM_JSON_LOCATION) as f:
                data = json.load(f)
                items = []
                for item in data:
                    items.append(item["name"])
                return items

