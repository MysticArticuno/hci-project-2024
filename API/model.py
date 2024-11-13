class Ticket:
    def __init__(self):
        self.ticket_id = ""
        self.ticket_time = ""
        self.ticket_date = ""
        self.customer_name = ""
        self.customer_number = ""
        self.customer_email = ""
        self.table_number = ""
        self.server_name = ""
        self.guest_count = ""
        self.items = []

    
    # def __dict__(self):
    #     return {
    #         "ticket_id": self.ticket_id,
    #         "ticket_time": self.ticket_time,
    #         "ticket_date": self.ticket_date,
    #         "is_togo": self.is_togo,
    #         "customer_name": self.customer_name,
    #         "customer_number": self.customer_number,
    #         "customer_email": self.customer_email,
    #         "table_number": self.table_number,
    #         "server_name": self.server_name,
    #         "guest_count": self.guest_count,
    #         "items": self.items
    #     }

class OrderItem:
    def __init__(self):
        pass