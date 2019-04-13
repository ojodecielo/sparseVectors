"""
**Serie 1 (Julia Schaeffer)**\n
In der Datei *abgabe.py* werden zwei Sparse-Vektoren vom User eingegeben und getestet. Der User hat zwei Moeglichkeiten:\n
- die Vektoren aus einer *csv*-Datei einzulesen\n
- oder manuell eingeben.\n
Im letzten Fall wird zuerst die Laenge des Vektors eingegeben (*int*), dann die Indizes der "nichtleeren" Stellen (*int*-Variablen, durch Komma getrennt) und anschliessend die entsprechenden Werte, die nicht gleich Null sind (*float*-Variablen, durch Komma getrennt).

Diese Angaben werden zuerst fuer den Vektor v1 eingetippt.
Folgendes gibt das Programm automatisch aus:\n
- den Vektor im Sparse-Format,\n
- die Maximumsnorm von v1,\n
- eine alternative Darstellung von v1 in Form von Tupeln, bestehend jeweils aus einem Index und dem entsprechenden Wert.\n
- v1 wird ausserdem als Vollvektor dargestellt.

Danach kann der User eine Skalarmultiplikation durchfuehren, indem er eine Zahl mit der Tastatur eingeben kann.

Nachher wird der User gefragt, ob er einen anderen Vektor (=v2) eingeben moechte.
Falls ja, so wird die Eingabe der Informationen analog durchgefuehrt, und die gleichen Ergebnisse werden herausgegeben.
Das Programm rechnet ausserdem die Summe und die Differenz dieser zwei Vektoren aus. 
Am Ende des Durchlaufs wird dem User wieder angeboten, eine Skalarmultiplikation mit v2 durchzufuehren.
Das Programm fragt nach einem Skalar und multipliziert den Vektor v2 mit dieser Zahl.

Beim Einlesen einer *csv*-Datei ueberprueft das Programm, ob der Dateiname korrekt eingegeben wurde, und weist ggf. darauf hin.\n
Im Falle der manuellen Eingabe wird ueberprueft, ob die Laenge des Vektors mit den Indizes uebereinstimmt, sowie ob genauso viele Indizes wie Werte eingegeben wurden. Auf Tippfehler wird hingewiesen.
"""

if __name__=="__main__":

	from sparse import sparse
	print("Dieses Programm rechnet mit sparse-Vektoren")

	branch = raw_input("Die Vektoren: \n\ta aus Datei einlesen \n\tb manuell eingeben\n ")
	ihre_datei = 0
	try:
		if branch == "a":
			try:
				ihre_datei = raw_input("Tippen Sie den Dateinamen ein. Die Datei soll sich im gleichen Ordner befinden: ")
				v1 = sparse.readVektor(ihre_datei)
				if len(v1.index) == len(v1.wert):
				    if v1.index[len(v1.index)-1] <= v1.laenge:
					print("Ihr sparse-Vektor v1 lautet: ")
					print v1
					print("Die Maximumsnorm von v1 ist: ")
					print sparse.maxNorm(v1)
					print("Alternative Darstellung von v1: ")
					print sparse.umwandlung(v1)
					print("Der Vollvektor v1 wird dargestellt als: ")
					print sparse.printFull(v1)
					if raw_input("Moechten Sie Multiplikation mit einem Skalar ausfuehren? (j/n) ")=="j":
					    x = input("Geben Sie eine Zahl ein: ")
					    print("Das Ergebnis der Multiplikation von v1 mit diesem Skalar: ")
					    print sparse.sMult(v1, x)
				    else:
					print("Die Laenge des Vektors stimmt nicht mit den Indizes ueberein")
				else:
				    print("Die Anzahl der Indizes soll der Anzahl der Werte entsprechen")
			except IOError:
				print("Die Datei existiert nicht in Ihrem Verzeichnis")
			if raw_input("Moechten Sie eine andere Datei einlesen? (j/n) ")=="j":
			    try:
				ihre_datei2 = raw_input("Tippen Sie den Dateinamen ein. Die Datei soll sich im gleichen Ordner befinden: ")
				v2 = sparse.readVektor(ihre_datei2)
				print("Ihr sparse-Vektor v2 lautet: ")
				print v2
				print("Die Maximumsnorm von v2 ist: ")
				print sparse.maxNorm(v2)
				print("Alternative Darstellung von v2: ")
				print sparse.umwandlung(v2)
				print("Der Vollvektor v2 wird dargestellt als: ")
				print sparse.printFull(v2)
				print("Die Summe zweier Vektoren ist: ")
				print v1 + v2
				print("Die Differenz zweier Vektoren ist: ")
				print v1 - v2
				print("Das Skalarprodukt zweier Vektoren betraegt: ")
				print sparse.iProd(v1, v2)
				if raw_input("Moechten Sie Multiplikation mit einem Skalar ausfuehren? (j/n) ")=="j":
				    x = input("Geben Sie eine Zahl ein: ")
				    print("Das Ergebnis der Multiplikation von v2 mit diesem Skalar: ")
				    print sparse.sMult(v2, x)
				    print("ENDE")
				else:
				    print("ENDE")
			    except IOError:
				print("Die Datei existiert nicht in Ihrem Verzeichnis")
			else:
			    print("Das Programm wurde abgebrochen")
		 
		elif branch == "b":
			laenge = int(input("Bitte geben Sie die Laenge Ihres sparse-Vektors ein (int): "))
			index_string = raw_input("Bitte geben Sie die Indizes Ihres sparse-Vektors ein, deren Eintraege nicht gleich Null sind, durch Komma getrennt (int): ")
			index = [int(e) if e.isdigit() else e for e in index_string.split(",")]
			wert_string = raw_input("Bitte geben Sie die Werte Ihres sparse-Vektors ein, die nicht gleich Null sind, durch Komma getrennt: ")
			wert = [float(e) for e in wert_string.split(",")]
			if len(index) == len(wert):
			    if laenge <= index[len(index)-1]:
				print("Die Laenge des Vektors stimmt nicht mit den Indizes ueberein. Ueberpruefen Sie Ihre Eingaben")
			    else:
				v1 = sparse(laenge, index, wert)
				print("Ihr sparse-Vektor v1 lautet: ")
				print v1
				print("Die Maximumsnorm von v1 ist: ")
				print sparse.maxNorm(v1)
				print("Alternative Darstellung von v1: ")
				print sparse.umwandlung(v1)
				print("Der Vollvektor v1 wird dargestellt als: ")
				print sparse.printFull(v1)
				if raw_input("Moechten Sie Multiplikation mit einem Skalar ausfuehren? (j/n) ")=="j":
					x = input("Geben Sie eine Zahl ein: ")
					print("Das Ergebnis der Multiplikation von v1 mit diesem Skalar: ")
					print sparse.sMult(v1, x)
			else:
			    print("Die Anzahl der Indizes soll der Anzahl der Werte entsprechen. Ueberpruefen Sie Ihre Eingaben")
			if raw_input("Moechten Sie einen anderen Vektor eingeben? (j/n) ")=="j":
				laenge2 = int(input("Bitte geben Sie die Laenge Ihres sparse-Vektors ein (int): "))
				index_string2 = raw_input("Bitte geben Sie die Indizes Ihres Sparse-Vektors ein, deren Eintraege nicht gleich Null sind, durch Komma getrennt (int): ")
				index2 = [int(e) if e.isdigit() else e for e in index_string2.split(",")]
				wert_string2 = raw_input("Bitte geben Sie die Werte Ihres sparse-Vektors ein, die nicht gleich Null sind, durch Komma getrennt: ")
				wert2 = [float(e) for e in wert_string2.split(",")]
				v2 = sparse(laenge2, index2, wert2)
				print("Ihr sparse-Vektor v2 lautet: ")
				print v2
				print("Die Maximumsnorm von v2 ist: ")
				print sparse.maxNorm(v2)
				print("Alternative Darstellung von v2: ")
				print sparse.umwandlung(v2)
				print("Der Vollvektor v2 wird dargestellt als: ")
				print sparse.printFull(v2)
				print("Die Summe zweier Vektoren ist: ")
				print v1 + v2
				print("Die Differenz zweier Vektoren ist: ")
				print v1 - v2
				print("Das Skalarprodukt zweier Vektoren betraegt: ")
				print sparse.iProd(v1, v2)
				if raw_input("Moechten Sie Multiplikation von v2 mit einem Skalar ausfuehren? (j/n) ")=="j":
				    x = input("Geben Sie eine Zahl ein: ")
				    print("Das Ergebnis der Multiplikation von v2 mit diesem Skalar: ")
				    print sparse.sMult(v2, x)
				    print("ENDE")
				else:
				    print("ENDE")
		else:
			print("Das Programm wurde abgebrochen")
	except IndexError:
		print("IndexError: Ueberpruefen Sie Ihre Eingaben!")
	except NameError:
		print("NameError: Ueberpruefen Sie Ihre Eingaben!")
	except SyntaxError:
		print("SyntaxError: Ueberpruefen Sie Ihre Eingaben!")
