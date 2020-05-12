# Proiect Cloud Computing

Cristea Ionut-Bogdan
SIMPRE, anul 1
2020

## Descriere problema
    Aceasta aplicatie web utilizeaza doua servicii in cloud, prin intermediu a doua API REST (The Movie Database (TMDb) API si Studio API) pentru a lista o colectie cuprinzatoare de filme, impreuna cu cateva date despre acestea. Aplicatia
 prezinta si un link construit pe baza unor variabile ce returneaza locatiile cinematografelor dintr-un oras la alegere (in cadrul unei cautari pe google maps).

## API-uri utilizate
    The Movie Database (TMDb) API - https://developers.themoviedb.org/3/getting-started/introduction
                                  - platforma ce perminte accesul la o gama variata de informatii din domeniul cinematografiei, de la filme, seriale, actori etc
                                  - securitate realizata prin intermediul unei chei API ("API key")
                                  - proiectul utilizeaza endpoint-ul pentru listarea informatiilor despre filmele din categoria "Trending" pentru o anumita perioada de timp (acesta realizeaza deci o cerere HTTP de tip GET)
                                  - API-ul returneaza un fisier json in care se afla informatii sub forma unui dictionar ce contine elemente de tip sir de caractere
    Studio Ghibli API - https://ghibliapi.herokuapp.com/#
                      - aplicatie web ce ofera informatii despre filmele celebrului studio japonez de anime Ghibli 
                      - accesul la API este public
                      - prezenta aplicatie utilizeaza endpoint-ul ce listeaza filmele produse de studio, impreuna cu data lansarii acestora (realizeaza o cerere HTTP de tip GET)
                      - se returneaza un fisier json care contine informatii text cuprinse intr-un dictionar

## Descriere arhitectura

    Aplicatia web ruleaza in cadrul platformei App Engine de pe Google Cloud Platform. Partea de backend a fost dezvoltata in Python versiunea 3, partea de frontend a fost realizata in HTML. Aplicatia poate fi gasita la adresa:
        https://woven-plane-275813.ew.r.appspot.com

### Exemple de cereri si raspunsuri
    Cele doua API utilizate in proiect functioneaza in moduri similare:
        1.realizare cerere tip GET: pentru a putea realiza aceste cereri in Python, am utilizat cadrul web Flask;
            exemplu de cerere GET: requests.get(endpoint1)
        2. primire raspuns: raspunsul vine sub forma unui fisier json ce contine un dictionar cu informatiile cerute;
            exemplu de raspuns:
            
            ```Python
            {
                "id": "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
                "title": "My Neighbor Totoro",
                "description": "Two sisters ...",
                "director": "Hayao Miyazaki",
                "producer": "Hayao Miyazaki",
                "release_date": "1988",
                "rt_score": "93",
                ...
            }
            ```

### Metode HTTP
    Aplicatia realizeaza, in cadrul sau, doua metode HTTP de tipul GET, pentru a returna date de pe serverele sursa.

### Autentificare
    Utilizarea "The Movie Database (TMDb) API" a necesitat accesul la o cheie API, cheie primita gratuit in urma realizarii unui cont pe platforma.

