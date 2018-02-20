product = {}

def addProduct(productCode, quantity):
	if productCode in product:
		product[productCode] = product[productCode] + quantity
	else:
		product[productCode] = quantity

def removeProduct(productCode):
	if productCode in product:
		del product[productCode]

def showCart():
	for cart in product:
		print "{} ({})".format(cart, product[cart])

addProduct("Baju Merah Mantap", 1)
addProduct("Baju Merah Mantap", 1)
addProduct("Bukuku", 3)
removeProduct("Bukuku")
addProduct("Singlet Hijau", 1)
removeProduct("ProdukBohongan")
showCart()
