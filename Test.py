def Golpe_Superior(poscicion_1, poscicion_2, altura_1, altura_2, defensa):
	if defensa == True:
		return 0
		#daño reducido por defensa
	else:
		if abs(poscicion_1 - poscicion_2) > 150:
			return 1
			#daño nulo
		else:
			for x in range((altura_1 + 200)/3, (altura_1 + 200)*2/3):
				for y in range(altura_2, altura_2 + 200:
					if x == y:
						return 2
						#golpe completo
			return 1


