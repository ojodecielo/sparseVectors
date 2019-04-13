"""
**Serie 1. Rechnen mit sparse-Vektoren (Julia Schaeffer)**\n
Abgabedatum: 6. November 2015
"""

class sparse(object):
    """
    Unter **class** werden die Eigenschaften eines sparse-Vektors definiert: \n
    - Laenge des Vektors als int-Variable\n
    - die Indizes der nichtleeren Stellen als Liste von int-Variablen\n
    - Liste der Werte, die ungleich Null sind, als Elemente eines geordneten Koerpers (z.B. als Gleitkommazahlen).\n
    """

    def __init__(self, laenge, index, wert):
	self.laenge = laenge              
	self.index = index                   
	self.wert = wert                      
    
    def maxNorm(self):                        
	"""
	Die Funktion *maxNorm* ermittelt die Maximumsnorm eines sparse-Vektors.\n
	- Eingabe: Sparse-Vektor\n
	- Ausgabe: Element eines geordneten Koerpers (z.B. eine Gleitkommazahl)\n
	"""
	import copy
	if self.index == []:
	    return 0.0
	else:
	    neue_werte = copy.deepcopy(self.wert)
	    null = neue_werte[0] - neue_werte[0]
	    for i in range(len(neue_werte)):
		if neue_werte[i] <= null:
		    neue_werte[i] = null-neue_werte[i]
	    maximum = neue_werte[0]
	    for i in range(len(neue_werte)):
		if maximum <= neue_werte[i]:
		    maximum = neue_werte[i]
	    return maximum

    def __add__(self, other):
	"""
	Die magic-Methode *__add__* addiert zwei sparse-Vektoren, falls sie gleich lang sind.\n
	- Eingabe: Zwei sparse-Vektoren\n
	- Ausgabe: Sparse-Vektor der Summe\n
	"""
	import copy
	if isinstance(other, sparse):
		if self.laenge == other.laenge:
			null = self.wert[0] - self.wert[0]
			index_sum = sorted(self.index + list((set(other.index)) - set(self.index)))
			wert_sum = []
			for i in index_sum:
				wert_sum.append(null)
			if len(self.index) == 0:
				wert_sum = other.wert
			elif len(other.index) == 0:
				wert_sum = self.wert
			else:
				list1 = copy.deepcopy(self.index)
				list2 = copy.deepcopy(other.index)
				j = 0
				k = 0
				m = 0
				for i in index_sum:
					if i in list1 and i in list2:
						j = list1.index(i)
						k = list2.index(i)
						m = index_sum.index(i)
						wert_sum[m] = self.wert[j] + other.wert[k]
					elif i in list1 and i not in list2:
						j = list1.index(i)
						m = index_sum.index(i)
						wert_sum[m] = self.wert[j]
					elif i in list2 and i not in list1:
						k = list2.index(i)
						m = index_sum.index(i)
						wert_sum[m] = other.wert[k]					
					else:
						print("Addition nicht moeglich, da die Vektoren unterschiedlich lang sind")
		return sparse(self.laenge, index_sum, wert_sum)
	else:
	    raise TypeError("Addition nicht moeglich, da mindestens einer der Vektoren kein sparse-Vektor ist")
	
    def __sub__(self, other):
	"""
	Die magic-Methode *__sub__* bildet die Differenz zweier sparse-Vektoren, falls sie gleich lang sind.\n
	- Eingabe: Zwei sparse-Vektoren\n
	- Ausgabe: Sparse-Vektor der Differenz\n
	"""
	import copy
	if isinstance(other, sparse):
		if self.laenge == other.laenge:
			null = self.wert[0] - self.wert[0]
			index_diff = sorted(self.index + list((set(other.index)) - set(self.index)))
			wert_diff = []
			for i in index_diff:
				wert_diff.append(null)
			if len(self.index) == 0:
				for i in wert_diff:
					wert_diff[i] = null - other.wert[i]
			elif len(other.index) == 0:
				wert_diff = self.wert
			else:
				list1 = copy.deepcopy(self.index)
				list2 = copy.deepcopy(other.index)
				j = 0
				k = 0
				m = 0
				for i in index_diff:
		   			if i in list1 and i in list2:
						j = list1.index(i)
						k = list2.index(i)
						m = index_diff.index(i)
						wert_diff[m] = self.wert[j] - other.wert[k]
					elif i in list1 and i not in list2:
						j = list1.index(i)
						m = index_diff.index(i)
						wert_diff[m] = self.wert[j]
					elif i in list2 and i not in list1:
						k = list2.index(i)
						m = index_diff.index(i)
						wert_diff[m] = null - other.wert[k]	
		else:
			print("Subtraktion nicht moeglich, da die Vektoren unterschiedlich lang sind")
		return sparse(self.laenge, index_diff, wert_diff)
	else:
	    raise TypeError("Subtraktion nicht moeglich, da mindestens einer der Vektoren kein sparse-Vektor ist")

    def iProd(self, other):
	"""
	Die Funktion *iProd* bildet das Skalarprodukt zweier sparse-Vektoren, falls sie gleich lang sind.\n
	- Eingabe: Zwei sparse-Vektoren\n
	- Ausgabe: Element eines geordneten Koerpers (z.B. eine Gleitkommazahl)\n
	"""
	import copy    
	if isinstance(other, sparse):
		if self.laenge == other.laenge:
			if self.index != [] or other.index != []:
				null = self.wert[0] - self.wert[0]
				produkt = null
				list1 = copy.deepcopy(self.index)
				list2 = copy.deepcopy(other.index)
				j = 0
				k = 0
				for i in self.index:
					if i in other.index:
						j = list1.index(i)
						k = list2.index(i)
						summand = self.wert[j] * other.wert[k]
					else:
						summand = null
					produkt = produkt + summand
			else:
				return 0.0
		else:
			print("Skalarprodukt kann nicht berechnet werden, da die Vektoren unterschiedlich lang sind")
		return produkt
	else:
		raise TypeError("Skalarprodukt kann nicht berechnet werden, weil mindestens einer der Vektoren kein sparse-Vektor ist")
		

  
    def sMult(self, x):
	"""
	Die Funktion *sMult* multipliziert einen sparse-Vektor mit einem Skalar.\n
	- Eingabe: Sparse-Vektor und ein Skalar\n
	- Ausgabe: Sparse-Vektor\n
	"""
	import copy
	neue_werte = copy.deepcopy(self.wert)
	for i in range(len(neue_werte)):
		neue_werte[i] = x * neue_werte[i]	
	return sparse(self.laenge, self.index, neue_werte)

   
    def umwandlung(self):
	"""
	Die Funktion *umwandlung* wandelt einen sparse-Vektor in eine Liste von Tupeln um mit je einem Index und dem entsprechenden Wert.\n
	- Eingabe: Sparse-Vektor\n
	- Ausgabe: Liste von Tupeln der Form *(Index, Wert)*. Hierbei ist Index eine int-Variable und Wert Element eines geordneten Koerpers, z.B. eine Gleitkommazahl.\n
	"""
	liste = []
	for i in range(len(self.index)):
		liste.append((self.index[i], self.wert[i]))
	return liste

    @staticmethod
    def readVektor(datei):
	"""
	Die Funktion *readVektor* stellt eine Methode zum Einlesen eines Sparse-Vektors aus einer csv-Datei.\n
	- Eingabe: csv-Datei\n
	- Ausgabe: Sparse-Vektor\n
	"""
	import csv
	with open(datei, 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		liste_index = []
		liste_wert = []
		laenge = 0
		row_count = 0
		for row in reader:
			if len(row) == 2:
				liste_index.append(int(row[0]))
				liste_wert.append(float(row[1]))
			else:
				if row[0] == 0:
					for row in reader:
						laenge = row[0]
				else:
					laenge = row[0]
	f.close()
	return sparse(laenge, liste_index, liste_wert)

   
    def __str__(self):
	"""
	Die magic-Methode *__str__* beschreibt die print-Funktion fuer die Sparse-Vektoren.\n
	- Eingabe: Sparse-Vektor\n
	- Ausgabe: Tupel mit Laenge, Liste der Indizes und Liste der Werte.\n
	"""
	return "(" + str(self.laenge) + ", " + str(self.index) + ", " + str(self.wert) + ")"

  
    def printFull(self):
	"""
	Die Funktion *printFull* stellt eine Methode zum Herausgeben des Vollvektors bereit.\n
	- Eingabe: Sparse-Vektor\n
	- Ausgabe: Liste mit Werten an jeder Stelle des sparse-Vektors, wobei die Werte Elemente eines geordneten Koerpers sind, z.B. Gleitkommazahlen.\n
	"""
	fullVektor = []
	n = 0
	for i in range(int(self.laenge)):
	    if i in self.index:
		fullVektor.append(self.wert[n]) 
		n += 1
	    else:
		fullVektor.append(0.0)
	return fullVektor
