food = input("Что вы хотите заказать: бургер, шаурма, хотдог: ")
if food == "бургер":
	value = input("сколько вам штук? ")
	inside = input("курица, мясо: ")
	temperature = input ("с подогревом или без подогрева?")
	coda = input ("кофе, чай, кола, вода")
	if coda == "":
		print (f"вы заказали {food} с {inside}, {value} шт ,{temperature}, клиент не выбрал напиток")
	else:
		print (f"вы заказали {food} с {inside},{value},{coda},")

elif food == "шаурма":
	value = input("сколько вам штук?")
	inside = input("курица или мясо ?")
	temperature = input (" с подогревом или без подогрева? ")
	coda = input("что будете пить: чай, кофе, колу, вода?")
	if coda == "":
		print (f"вы заказали {food} с {inside}, {value} шт , {temperature},клиент не выбрал напиток")
	else:
		print (f"вы заказали {food} с {inside},{value},{coda},")
	
elif food == "хотдог":
	value = input("сколько вам штук?")
	inside = input("курица или мясо?")
	temperature = input (" с подогревом или без подогрева? ")
	coda = input("что будете пить: кола, вода, чай, кофе? ")
	if coda == "":
		print (f"вы заказали {food} с {inside}, {value} шт , {temperature}, клиент не выбрал напиток")
	else:
		print (f"вы заказали {food} с {inside},{value},{coda},")
