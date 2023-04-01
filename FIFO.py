import random

def randomise():   #funkcja generująca losowe dane
  random.seed(10)   #ziarno losowości - pozwala nam na wygenerowanie losowych danych, będą one takie same przy każdym uruchomieniu programu, ale wciąż w gruncie rzeczy losowe

  size = 100
  print("Size: " + str(size))
  pages = [random.randint(0, 10) for i in range(100)]   #przypisywanie wylosowanych wartości do listy 'pages'
  n = len(pages)

  return pages, n, size   #funkcja zwraca listę 'pages', n oraz size

def FIFO(pages, n, size):   #funkcja 'FIFO' przyjmuje listę 'pages', n oraz size
  page_hits = 0   #ustawiamy licznik trafien na zero
  page_faults = 0   #ustawiamy licznik błędów braku strony na zero
  queue = []   # w liście 'pages' będą przechowywane aktualne strony znajdujące się w pamięci

  plik = open("FIFO_data.txt", "a")   # procedura zapisu do plików wszystkich wylosowanych danych
  plik.write(str(pages))
  plik.write("\n")
  plik.close()

  for i in range(n):
    if pages[i] in queue:   # jeśli strona jest w już w ramkach pamięci, zwiększ trafienia o jeden
      page_hits += 1
    else:   # jeśli nie ma strony w ramkach:
      if len(queue) == size:   # jeśli długość aktualnej kolejki jest równa jej rozmiarowi
        queue.pop(0)   # usuń pierwszy element
        queue.append(pages[i])   # i zastąp go nowo przychodzącą stroną
        page_faults += 1   # zwiększ ilość błędów braku strony o jeden
      else:   # w przeciwnym wypadku (a może w zasadzie być tylko taki, w którym długość 'queue' będzie mniejsza od 'size'
        queue.append(pages[i])   # dopisz daną stronę do kolejki
        page_faults += 1   # i zwiększ ilość błędów braku strony o jeden
    print(queue)

  return page_hits, page_faults, n   # funkcja zwraca trafienia, błędy i 'n'

def display(page_hits, page_faults, n):   # funkcja do wyświetlania danych, są one tutaj też zapisywane do pliku
  print("Page Hits:" + str(page_hits))
  print("Page Faults:" + str(page_faults))
  HR = page_hits / n
  FR = page_faults / n
  print("Page hit rate: " + str(HR))
  print("Page fault rate: " + str(FR))

  plik = open("FIFO_data.txt", "a")
  plik.write("Page Hits: " + str(page_hits) + "\n")
  plik.write("Page Faults: " + str(page_faults) + "\n")
  plik.write("Page hit rate: " + str(HR) + "\n")
  plik.write("Page fault rate: " + str(FR) + "\n")
  plik.write("\n")
  plik.close()


pages, n, size = randomise()
page_hits, page_faults, n = FIFO(pages, n, size)
display(page_hits, page_faults, n)
