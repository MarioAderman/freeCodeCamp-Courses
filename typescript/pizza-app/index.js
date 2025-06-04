const menu = [
    { name: "Margherita", price: 8.99 },
    { name: "Pepperoni", price: 9.99 },
    { name: "Hawaiian", price: 10.99 },
    { name: "Vegetarian", price: 11.99 }
]

const cashInRegister = 100
const orderQueue = []
const nextOrderId = 1

function addNewPizza(pizzaObj) {
    menu.push(pizzaObj)
}
 
function placeOrder(pizza) {
    const selectedPizza = menu.find(pizzaObj => pizzaObj.name === pizza)
    cashInRegister += selectedPizza.price
    newOrder = {
        id: nextOrderId++,
        pizza: selectedPizza,
        status: "ordered"
    }
    orderQueue.push(newOrder)
    return newOrder
}

function completeOrder(order) {
    const completeOrder = orderQueue.find(orderObj => orderObj.id === order.id)
    completeOrder.status = "completed"
    return completeOrder
}

addNewPizza({ name: "Cheese", price: 7.99 })
addNewPizza({ name: "BBQ Chicken", price: 8.99 })
addNewPizza({ name: "Meat Lovers", price: 10.99 })

placeOrder("Margherita")
completeOrder("1")

console.log("Menu:", menu)
console.log("Cash in register:", cashInRegister)
console.log("Order queue:", orderQueue)
