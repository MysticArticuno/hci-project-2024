package dataObject;

// This class represents an instance of an OrderItem. It will not contain any logic.
// Only edit this class in the event a new data field must be added.
public class OrderItemDataObject {

    public String itemName;
    public String[] additionalModifiers;
    public String[] requiredModifiers;

    public OrderItemDataObject(String itemName, String[] modifiers){
        this.itemName = itemName;
        this.requiredModifiers = modifiers;
    }

    public OrderItemDataObject(String itemName){
        this.itemName = itemName;
        this.requiredModifiers = null;
    }
}
