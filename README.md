# Pizza Restaurants Code Challenge

For this code challenge, I worked with a Pizza Restaurant Domain.

I had to come up with a fully built Ract frontend application, so I can test if the API was working.

## Models

The Database contains three tables:
Restaurants, Pizzas and RestaurantPizza

## Relationships

A Restaurant has many Pizzas through RestaurantPizza

A Pizza has many Restaurants through RestaurantPizza

A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

## Validations

Add validations to the 'RestaurantPizza' model:

-must have a 'price' between 1 and 30