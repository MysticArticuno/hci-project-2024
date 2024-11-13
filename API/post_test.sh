curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
	"is_togo":"False",
	"customer_name":"",
	"customer_number":"",
	"customer_email":"",
	"table_number":"20",
	"server_name":"John Doe",
    "guest_count":"2",
	"items":[
		{"name": "Burger", "modifiers": ["Add Tomato", "Add Onion", "No Pickles"] },
		{"name": "Side Fries", "modifiers": ["No Salt"] },
		{"name": "Wings", "modifiers": ["Buffalo", "Ranch", "Celery"] },
		{"name": "Side Ranch", "modifiers": [] },
        {"name": "Side Ranch", "modifiers": [] }
    ]	
}' \
  http://localhost:5000/tickets/add
