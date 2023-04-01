import random

def randomise():   #funkcja generująca losowe dane
  random.seed(10)   #ziarno losowości - pozwala nam na wygenerowanie losowych danych, będą one takie same przy każdym uruchomieniu programu, ale wciąż w gruncie rzeczy losowe
  size = 100

  print("Size: " + str(size))
  pages = [random.randint(0, 10) for i in range(100)]   #przypisywanie wylosowanych wartości do listy 'pages'
  n = len(pages)

  return pages, n, size   #funkcja zwraca listę 'pages', n oraz size

def LRU(pages, n, size):   #funkcja 'FIFO' przyjmuje listę 'pages', n oraz size
  page_hits = 0   #ustawiamy licznik trafien na zero
  page_faults = 0   #ustawiamy licznik błędów braku strony na zero
  queue = []   # w liście 'pages' będą przechowywane aktualne strony znajdujące się w pamięci
  cache = {}   # pomocniczy słownik 'cache'

  plik = open("LRU_data.txt", "a")
  plik.write(str(pages))
  plik.write("\n")
  plik.close()

  for i in range(n):
    if pages[i] in queue:   # jeśli strona jest w kolejce
      page_hits += 1   # zwiększ ilość trafień o jeden
      index = queue.index(pages[i])   # znajdujemy odpowiedni indeks elementu
      queue.pop(index)   # usuwamy go z listy 'queue'
      queue.append(pages[i])   # dodajemy do listy 'queue' nowy element

    else:   # jeśli strony nie ma w kolejce
      queue.append(pages[i])  # dodaj ją do listy 'queue'
      page_faults += 1  # i zwiększ ilość błędów braku strony o jeden

      if len(queue) > size:   # jeśli długość kolejki jest większa od wielkości ramek
        del cache[queue.pop(0)]   # usuń pierwszy element z listy 'queue', usuwany jest też odpowiadający temu elementowi element z pomocnicznego słownika 'cache'

      cache[pages[i]] = True   # ustaw wartość na True dla kluczy, które są de facto ostatnio używanymi stronami
    print(queue)

  return page_hits, page_faults, n  # funkcja zwraca trafienia, błędy i 'n'


def display(page_hits, page_faults, n):   # funkcja do wyświetlania danych, są one tutaj też zapisywane do pliku
  print("Page Hits:" + str(page_hits))
  print("Page Faults:" + str(page_faults))
  HR = page_hits / n
  FR = page_faults / n
  print("Page hit rate: " + str(HR))
  print("Page fault rate: " + str(FR))

  plik = open("LRU_data.txt", "a")
  plik.write("Page Hits: " + str(page_hits) + "\n")
  plik.write("Page Faults: " + str(page_faults) + "\n")
  plik.write("Page hit rate: " + str(HR) + "\n")
  plik.write("Page fault rate: " + str(FR) + "\n")
  plik.write("\n")
  plik.close()

pages, n, size = randomise()
page_hits, page_faults, n = LRU(pages, n, size)
display(page_hits, page_faults, n)
