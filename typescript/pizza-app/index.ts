type Pizza = {
    id: number,
    name: string,
    price: number
}

type Order = {
    id: number,
    pizza: Pizza,
    status: "ordered" | "completed"
}

let cashInRegister = 100;
let orderQueue: Array<Order> = [];
let nextOrderId = 1;
let nextPizzaId = 1;

const menu: Pizza[]= [
    { id: nextPizzaId++, name: "Margherita", price: 8.99 },
    { id: nextPizzaId++, name: "Pepperoni", price: 9.99 },
    { id: nextPizzaId++, name: "Hawaiian", price: 10.99 },
    { id: nextPizzaId++, name: "Vegetarian", price: 11.99 }
];

function addNewPizza(pizzaObj: Omit<Pizza, "id">): void {
    const newPizza: Pizza = {
        id: nextPizzaId++,
        ...pizzaObj
    }
    menu.push(newPizza)
}
 
function placeOrder(pizza: string): Order | undefined {
    const selectedPizza = menu.find(pizzaObj => pizzaObj.name === pizza)
    if (!selectedPizza) {
        console.log(`${pizza} does not exist in the menu`)
        return
    }
    cashInRegister += selectedPizza.price
    const newOrder: Order = {
        id: nextOrderId++,
        pizza: selectedPizza,
        status: "ordered"
    }
    orderQueue.push(newOrder)
    return newOrder
}

function completeOrder(order: number): Order | undefined {
    const completeOrder = orderQueue.find(orderObj => orderObj.id === order)
    if(!completeOrder){
        console.log("Error")
        return
    }
    completeOrder.status = "completed"
    return completeOrder
}

export function getPizzaDetail(identifier: number | string): Pizza | undefined {
    if (typeof identifier === "string"){
        return menu.find(pizza => pizza.name.toLowerCase() === identifier.toLowerCase())
    } else { 
        return menu.find(pizza => pizza.id === identifier)
    }
}

addNewPizza({ name: "Cheese", price: 7.99 })
addNewPizza({ name: "BBQ Chicken", price: 8.99 })
addNewPizza({ name: "Meat Lovers", price: 10.99 })

placeOrder("Margherita")
completeOrder(1)

console.log("Menu:", menu)
console.log("Cash in register:", cashInRegister)
console.log("Order queue:", orderQueue)

getPizzaDetail(5)
getPizzaDetail("Meat Lovers")
