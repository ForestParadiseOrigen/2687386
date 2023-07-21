from flask import Flask

#Crear yo no se que

app = Flask(__name__)

#Crear ruta

@app.route('/')
def index():
    return 'Hola 2687386'


def paises():
    paises = [
                [
                    {
                        "nombre":"America",
                        "paises":[
                            "Colombia",
                            "Peru",
                            "Canada"
                            ]
                    }
                ],[
                    {
                        "nombre":"Europa",
                        "paises":[
                            "España",
                            "Rusia",
                            "Italia"
                            ]
                    }
                ],[
                    {
                        "nombre":"Asia",
                        "paises":[
                            "Japon",
                            "China",
                            "Armenia"
                            ]
                    }
                ]   
            ]
    
    contador_paises_america = 0
    for pais in paises[0][0].paises:
        contador_paises_america += 1
    print(contador_paises_america)
    
    user = 'Andres Cordoba'
    return render_template ('index.html',
                            user = user,
                            continentes = paises)