class Cart:
	def __init__(self):
		self.product = {}
	def addProduct(self, productCode, quantity):
		if productCode in self.product:
			self.product[productCode] = self.product[productCode] + quantity
		else:
			self.product[productCode] = quantity

	def removeProduct(self, productCode):
		if productCode in self.product:
			del self.product[productCode]

	def showCart(self):
		for cart in self.product:
			print "{} ({})".format(cart, self.product[cart])

cart = Cart()
cart.addProduct("Baju Merah Mantap", 1)
cart.addProduct("Baju Merah Mantap", 1)
cart.addProduct("Bukuku", 3)
cart.removeProduct("Bukuku")
cart.addProduct("Singlet Hijau", 1)
cart.removeProduct("ProdukBohongan")
cart.showCart()
