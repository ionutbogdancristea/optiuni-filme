# importam clasele Flask pentru rute si render pt templates
from flask import Flask, render_template
# librarie pentru a putea face cereri tip HTTP in Python:
import requests

# instantiem un proiect de tip Flask
app = Flask(__name__)  # name este o variabila ce reprezinta numele modulului

# API 1: www.themoviedb.org
# SCOP: obtinem informatii despre cele mai populare filme ale saptamanii

# elemente generale ale endpoint-ului
api_key1 = "fd5597902342cd7ba417f69939733b4f"
api_version1 = 3
api_base_url1 = "https://api.themoviedb.org/"+str(api_version1)

# specifice endpoint-ului de cautare in Trending
media_type = "movie"  # extragem doar filmele
time_window = "week"  # cele mai populare filme ale saptamanii
endpoint_path1 = "/trending/"+str(media_type)+"/"+str(time_window)
endpoint1 = str(api_base_url1)+str(endpoint_path1)+"?api_key="+str(api_key1)

# realizam cererea HTTP GET
r1 = requests.get(endpoint1)

# extragem datele despre filmele din trending care ne intereseaza
# daca cererea HTTP a fost efectuata cu success:
if r1.status_code in range(200, 299):
    data = r1.json()
    # avem de ales intre ['page', 'results', 'total_pages', 'total_results']
    # extragem doar informatiile legate de rezultat: 'results'
    results = data['results']
else:
    results = 'Cererea HTTP a intampinat o problema, verificati conexiunea la API'


# in continuare vrem sa afisam locatiile cinematografelor de un anume fel dintr-un oras dat
api_base_url2 = 'https://www.google.com/maps/search/?api=1&'
city = 'bucuresti'
favourite_cinema = 'cinemacity'
endpoint_path2 = 'query=cinema+'+str(city)+'+'+str(favourite_cinema)
endpoint2 = str(api_base_url2)+str(endpoint_path2)

# API2: https://ghibliapi.herokuapp.com
# Scop: obtinem o lista a unora din cele mai bune filme din categoria anime

api_base_url3 = 'https://ghibliapi.herokuapp.com'
endpoint_path3 = '/films'
endpoint3 = str(api_base_url3)+str(endpoint_path3)

r3 = requests.get(endpoint3)

if r3.status_code in range(200, 299):
    # data = r3.json()
    results3 = r3.json()  # data['title']
else:
    results3 = 'Cererea HTTP a intampinat o problema, verificati conexiunea la API'

# decorator ce gestioneaza conexiunea cu pagina - vom folosi o singura pagina
# folosim functia render pt a afisa pagina in format html
@app.route('/')
def mainpage():
    return render_template('home.html', results=results, city=city,
                           favourite_cinema=favourite_cinema,
                           endpoint2=endpoint2, results3=results3)


# daca aplicatia nu ruleaza pe un server va rula pe pc ul local
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
