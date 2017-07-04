# FootpatrolAPI
API for Footpatrol's mobile framework written in Python by Luke Davis ([@R8T3D](http://www.twitter.com/R8T3D))

## Features
  * Add products to cart

## Installation

FootpatrolAPI requires **Python 2.7**

#####  1. Install requirements
```sh
$ cd DIRECTORY_CONTAINING_FOOTPATROLAPI
$ pip install -r requirements.txt
```

#####  2. Set your cart_id
Edit the **main.py** file and set the cart_id variable to your CART ID. I can't tell you how to get this

#####  3. Run
```sh
$ cd DIRECTORY_CONTAINING_FOOTPATROLAPI
$ python main.py
```
#####  3. ATC
1. Fully close the Footpatrol mobile app on your phone.
2. Type in your desired PID.SIZE and then press enter.
3. Open the Footpatrol mobile app
4. The item should now be in your cart.

## Troubleshooting
1. The item isn't in my cart what happened?
    - Your cart id is incorrect
    - Your PID.SIZE is incorrect
    - The desired product is out of stock

2. How do I get the cart ID?
Vaguely, you need to view the network requests of your mobile device and get it from there.

3. What is the x-api-key?
The x-api-key allows you to change the script to work for other websites besides Footpatrol (but you need to do a bit more than just change that). I thought I'd make it a variable incase they ever change it.

## Todos

 * Web based GUI
 * Stock check
 * Auto-checkout

## License

MIT License (MIT)
