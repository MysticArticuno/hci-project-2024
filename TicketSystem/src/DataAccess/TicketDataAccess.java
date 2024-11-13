package DataAccess;

import java.util.ArrayList;

import dataObject.TicketDataObject;

public class TicketDataAccess {
    
    private static ArrayList<TicketDataObject> tickets;

    public TicketDataAccess() {
        initialize();
    }

    private void initialize() {
        tickets = new ArrayList<TicketDataObject>();
    }

    public static TicketDataObject CreateTicket(TicketDataObject ticket){
        ticket.ticketID = getNextID();
        tickets.add(ticket);
        return ticket;
    }

    private static int getNextID() {
        return tickets.size()+1;
    }

}
