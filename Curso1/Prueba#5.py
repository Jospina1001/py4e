while True:
	score = input("Ingresa puntaje: ")
	s = float(score)
	if(s>=0):
		if(s<=1):
			if(s>=0.9):
				print("A")
				break
			elif(s>=0.8):
				print("B")
				break
			elif(s>=0.7):
				print("C")
				break
			elif(s>=0.6):
				print("D")
				break
			elif(s<0.6):
				print("F")
				break
		else:
			print("error")
print('done')
