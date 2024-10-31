package restService.request;

public class NewTicketRequest {

    // Return an array of OrderItems 
    public String[] getItems(){
        return null;
    }

    // Return the order's ID
    public int getOrderID(){
        return -1;
    }

    // Return the ticket's table number if it is a dine-in order. Otherwise, return -1
    public int getTableNumber(){
        return -1;
    }

    // Return true if the order is a to-go order
    public boolean isTogo(){
        return false;
    }
}
