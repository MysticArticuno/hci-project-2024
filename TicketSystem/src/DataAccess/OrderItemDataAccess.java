package DataAccess;

import java.util.HashMap;
import java.util.ArrayList;

import dataObject.OrderItemDataObject;

public class OrderItemDataAccess {
    
    private static HashMap<String, OrderItemDataObject> items;

    public OrderItemDataAccess() {
        initialize();
    }

    private void initialize() {
        items = new HashMap<String, OrderItemDataObject>();
        String[] defaultModifiers = {};

        // Some default values

        String[] RegularBurgerDefault = {"Medium"};
        items.put("RegularBurger", new OrderItemDataObject("1/2 Pound Burger", defaultModifiers));

        items.put("ChickenSandwich", new OrderItemDataObject("Crispy Chicken Sandwich", null));
        items.put("Wings", new OrderItemDataObject("Saucy Wings", null));
        items.put("SideFries", new OrderItemDataObject("Salted French Fries"));

        
    }

    public static OrderItemDataObject getOrderItemByName(String name) {
        return items.get(name);
    }

}
