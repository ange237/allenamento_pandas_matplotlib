import pandas as pd
import matplotlib.pyplot as plt

#caricare il dataset
dataset = pd.read_csv('primo_passo_panda_matplotlib\data.csv')

#effettuare una prima ispezione del dataset
print(dataset.head())  #il metodo .head() di pandas per visualizzare le prime righe del dataset
print(dataset.describe()) # il metodo.describe() per avere un'idea delle statistiche principali dei dati

#Selezionare le colonne del dataset da analizzare
colonna1 = dataset['Id']
colonna2 = dataset['PetalLengthCm']

#Visualizzare un grafico a dispersione per vedere la relazione tra le due colonne
plt.scatter(colonna1, colonna2) #metodo .scatter() per creare il grafico a dispersione, impostando rispettivamente le etichette dell'asse x e y
plt.xlabel('Id') #asse delle x
plt.ylabel('PetalLengthCm') #asse delle y
plt.title('Grafico a dispersione') #titolo del grafico :Un grafico a dispersione ci permette di visualizzare la relazione tra due variabili continue.
plt.show() # mostriamo il grafico con il metodo .show()

#Calcolare il coefficiente di correlazione tra le due colonne:
#Il coefficiente di correlazione è un'indicazione della forza della relazione tra due variabili. Qui abbiamo utilizzato pandas e il suo metodo .corr() per calcolarlo tra le due colonne
corr_coeff = colonna1.corr(colonna2)
print("Il coefficiente di correlazione è:", corr_coeff)

#Creare un istogramma per analizzare la distribuzione dei valori nella colonna 1
#Un istogramma ci permette di visualizzare la distribuzione di una variabile continua. Utilizziamo il metodo .hist() di matplotlib per crearlo
plt.hist(colonna2, bins=10)
plt.xlabel('PetalLengthCm')
plt.ylabel('Conteggio')
plt.title('Istogramma')
plt.show()

#Creare un boxplot per visualizzare la distribuzione dei valori nella colonna 2:
#Così visualizziamo la distribuzione di una variabile continua e identifichiamo eventuali valori anomali.
#Ci serviamo di matplotlib e del suo metodo .boxplot() per creare il boxplot
plt.boxplot(colonna2)
plt.ylabel('PetalLengthCm')
plt.title('Boxplot')
plt.show()

#Creare un grafico a linee per vedere l'andamento dei valori della colonna 1 nel tempo
#Un grafico a linee ci permette di visualizzare l'andamento di una variabile continua nel tempo
colonna_data = dataset['PetalLengthCm']
plt.plot(colonna_data, colonna1)
plt.xlabel('tPetalLengthCmaa')
plt.ylabel('Id')
plt.title('Grafico a linee')
plt.show()

#Creare un grafico a barre per analizzare la distribuzione dei valori di una terza colonna
#Proseguiamo creando un grafico a barre con la funzione plt.bar()
colonna3 = dataset['PetalWidthCm']
plt.bar(colonna3.unique(), colonna3.value_counts()) #La funzione unique() restituisce tutti i valori unici presenti nella colonna 3 mentre value_counts() restituisce il conteggio di ciascun valore nella colonna
plt.xlabel('PetalWidthCm')
plt.ylabel('Conteggio')
plt.title('Grafico a barre')
plt.show()
