import sys
from levenshtein import *

if __name__ == "__main__":
  try:
      osnova_arg = sys.argv[1:]
  except IndexError:
      print("Uporaba programa: python main.py <osnova>")
      sys.exit(1)

  with open('Vaja5B/vaja5b1.txt', 'r') as f:   
      lines = f.readlines()
      osnove = []
      izgovorjava = []
      for line in lines:
        line = line.split()
        osnove.append(line[0])
        izgovorjava.append(line[1:]) 
        
  osnova = osnova_arg
  najmanjsa_vrednost = []
  operacije = []
  for i in izgovorjava:
    vrednost, _, _ = levensthein_razdalja(i, osnova)
    najmanjsa_vrednost.append(vrednost)
  min_vrednost = min(najmanjsa_vrednost)
  min_indeks = najmanjsa_vrednost.index(min_vrednost)

  # Izpis sprememb in izris matrike
  _, matrika, path = levensthein_razdalja(izgovorjava[min_indeks], osnova, spremembe=True)
  print(f"Minimalno število sprememb je {min_vrednost} in najbližje razvrščeni vzorec je {osnove[min_indeks]}")

  rows = [i for i, j in path if i != 0 and j != 0]
  cols = [j for i, j in path if i != 0 and j != 0]

  # Matrika ničel enake velikosti kot osnovna matrika
  matrix = np.zeros((len(matrika), len(matrika[0])))
  plt.imshow(matrix, 'binary')

  # Označi najkrajšo pot
  plt.scatter(cols, rows, c='red', s=200, alpha=0.5)
  # Legenda
  for i in range(len(matrika)):
      for j in range(len(matrika[0])):
          plt.text(j, i, matrika[i][j], ha='center', va='center', color='black')
  for i, letter in enumerate(izgovorjava[min_indeks]):
      plt.text(-1.5, i+1, letter, va='center', fontsize=18)
  for i, letter in enumerate(osnova):
      plt.text(i+1, -1, letter, ha='center', va='center', fontsize=18)
  plt.xticks([])
  plt.yticks([])

  plt.show()
  sys.exit(0)