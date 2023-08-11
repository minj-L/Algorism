import heapq

data = [

 {'goods': 'pizza', 'price':120},

 {'goods': 'chicken', 'price':380},
 
 {'goods': 'Tacco', 'price':987},
 
 {'goods': 'pudding', 'price':402},
]

smallest = heapq.nlargest(3, data, key=lambda god: god['price'])
print(smallest)
