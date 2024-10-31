package dataObject;
import dataObject.OrderItemDataObject;

// This class represents an instance of a Ticket. It will not contain any logic.
// Only edit this class in the event a new data field must be added.
public class TicketDataObject {

    // General data fields
    public int ticketID;
    public OrderItemDataObject[] elements;
    public String ticketTime;


    // To-go order specific data fields
    public boolean isTogo;
    public String togoName;

    // Dine-in specific data fields
    public int tableNumber;

    public TicketDataObject(int ticketId){
        this.ticketID = ticketId;
    }
}
