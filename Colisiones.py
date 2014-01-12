def choque(estado, x_p1_izq, x_p2_izq, x_p1_der, x_p2_der, borde_mapa):
	#VERSION BETA, POR AHORA SOLO CHEQUEA CUANDO HAY MOVIMEINTO LATERAL, NO CUANDO ESTAN SALTANDO.
	#esta funcion chequea si dos objetos tan chocando de acuerdo a sus coordenadas de los extremos de los sprites (de ahi los terminos "x_izq" e "x_der")
	#la gracia esta en que podrá chequear dependendiendo del pj q sea, y hacia donde se este moviendo, tbn revisa si esta al borde del mapa
	#necesitaremos tbn que las coordenadas x de cada sprite sean variables dinamicas (osea que en cada refresh se actualizen), de lo contrario esto no servirá)
	#su funcionamiento es simple, cada vez que un personaje x se mueva a y lado, se llama a la funcion de la forma "colisionador(camina_y_pj_x, ...)", si devuelve 0 hay choque, si no, via libre.)

	if estado = "camina_izq_pj_1":
		if x_p1_izq == x_p2_der or x_p1_izq == 0:
			return 0
		else:
			return 1

	elif estado = "camina_izq_pj_2" or x_p2_izq == 0:
		if x_p2_izq == x_p1_der:
			return 0
		else:
			return 1

	elif estado = "camina_der_pj_1":
		if x_p1_der == x_p2_izq or x_p1_der == borde_mapa:
			return 0
		else:
			return 1

	elif estado = "camina_der_pj_2":
		if x_p2_der == x_p1_izq or x_p2_der == borde_mapa:
			return 0
		else:
			return 1

#Ahora vienen los golpes. Mismo formato de arriba, solo que ahora si importan las coordenadas y.
#IMPORTANTE: YO ASUMO QUE SOLO HABRAN GOLPES CUANDO SE ESTA DE PIE, Y AGACHADO. Por tanto, dividiré la hitbox en tercios, y solo ocupare los tercios "del medio y de abajo". Cualquier cosa avisen.
#IMPORTANTE 2: AGREGO COMO VARIABLE EL QUE EL OTRO PERSONAJE PUEDA ESTAR DEFENDIENDO. De ahi explico.

def golpe_suave_parado(estado, defensa, x_p1_izq, x_p2_izq, x_p1_der, x_p2_der, y_p1_sup, y_p2_sup, y_p1_inf, y_p2_inf, borde_mapa):
	if estado == "pj1_izq":
		#se lee "pj 1 golpea por la izquierda"
		if (x_p1_izq - x_p2_der) < 10:
			#asumo que podran golpearse cuando haya cierta distancia entre ellos, no tiene por qué ser 10 (es arbitrario)
			for x in range((y_p1_sup + (y_p1_inf-y_p1_sup)*(1/3)), (y_p1_sup + (y_p1_inf-y_p1_sup)*(2/3))):
				#crea la hitbox del medio, ya que es un golpe "de pie"
				for y in range(y_p2_sup, y_p2_inf):
					if x == y:
						#revisa si el el sprite oponente esta en el rango del hitbox
						if defensa == "si":
							return "minimo"
							#el daño que se da, al golpear pero estar defendiendo, es el minimo posible (a decidir)
						else:
							return "maximo"
							#fue un golpe limpio, por lo que recibe el daño completo del golpe liviano (a decidir)
		else:
			return "nada"
			#golpe al aire, no genera daño

	elif estado == "pj1_der":
		if (x_p2_izq - x_p1_der) < 10:
			for x in range((y_p1_sup + (y_p1_inf-y_p1_sup)*(1/3)), (y_p1_sup + (y_p1_inf-y_p1_sup)*(2/3))):
				for y in range(y_p2_sup, y_p2_inf):
					if x == y:
						if defensa == "si":
							return "minimo"
						else:
							return "maximo"
		else:
			return "nada"


	elif estado == "pj2_izq":
		if (x_p2_izq - x_p1_der) < 10:
			for x in range((y_p2_sup + (y_p2_inf-y_p2_sup)*(1/3)), (y_p2_sup + (y_p2_inf-y_p2_sup)*(2/3))):
				for y in range(y_p1_sup, y_p1_inf):
					if x == y:
						if defensa == "si":
							return "minimo"
						else:
							return "maximo"
		else:
			return "nada"

	elif estado == "pj2_der":
		if (x_p1_izq - x_p2_der) < 10:
			for x in range((y_p2_sup + (y_p2_inf-y_p2_sup)*(1/3)), (y_p2_sup + (y_p2_inf-y_p2_sup)*(2/3))):
				for y in range(y_p1_sup, y_p1_inf):
					if x == y:
						if defensa == "si":
							return "minimo"
						else:
							return "maximo"
		else:
			return "nada"

	return "nada"
	#este nada esta porque si se llega al caso en que se revise si el sprite esta en la hitbox, y NO esta en la hitbox, automaticamente se sale de la funcion y llegará aqui