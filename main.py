from bs4 import BeautifulSoup
import requests

# Written by Luke Davis (@R8T3D)
# Under the MIT license

# you need to change this to yours 
cart_id = 'YOUR CART ID'

# this shouldn't change, only have it as a variable just in case.
x_api_key = '5F9D749B65CD44479C1BA2AA21991925'

class FootpatrolAPI(object):
	def __init__(self):
		self.s = requests.Session()

		self.s.get("https://commerce.mesh.mx/stores/footpatrol/updates?version=2.0")
		self.s.get("https://commerce.mesh.mx/stores/footpatrol/nav?channel=iphone-app")
		self.s.get("https://commerce.mesh.mx/stores/footpatrol/deviceConfigurations/AppConfig")
		self.s.get("https://commerce.mesh.mx/stores/footpatrol/snippets/iphone-app?expand=content")
		self.s.get("https://commerce.mesh.mx/stores/footpatrol/carts/" + cart_id)

	def add_to_cart(self, pidsize):
		headers = {
		    'Host': 'commerce.mesh.mx',
		    'Content-Type': 'application/json',
		    'X-API-Key': x_api_key,
		    'Accept': '*/*',
		    'X-Debug': '1',
		    'Accept-Language': 'en-gb',
		    'User-Agent': 'FootPatrol/2.0 CFNetwork/808.3 Darwin/16.3.0',
		    'MESH-Commerce-Channel': 'iphone-app',
		}

		data = '{"quantity":1}'

		self.s.put('https://commerce.mesh.mx/stores/footpatrol/carts/' + cart_id + '/' + pidsize, headers=headers, data=data)

api = FootpatrolAPI()
api.add_to_cart(raw_input("PID.SIZE? "))
