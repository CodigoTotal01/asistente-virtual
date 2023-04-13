import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    # almacenar el recognizer en una variable
    r = sr.Recognizer()
    # config microphone - asignar econtexto a la clase

    with sr.Microphone() as origen:
        # tiempo de espera para escuchar
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion

        print('Ya puedes hablar causita')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)
        try:
            # buscar en google lo que halla buscado
            pedido = r.recognize_google(audio, language='es-mx')
            # prueba de que pudo ingresar
            print('Dijiste: ' + pedido)
            return pedido
        # por si no consige comprender el audio1
        except sr.UnknownValueError:
            print('ups, no te entendi, repitelo porfavor')
            return 'Sigo Esperarando ...'
        except sr.RequestError:
            print('ups, no te entendi, repitelo porfavor')
            return 'Sigo Esperarando ...'
        # Error inesperado
        except sr.RequestError:
            print('ups, algo salio mal, repitelo porfavor')
            return 'Sigo Esperarando ...'


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el moto de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'


def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.datetime.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)

    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miercoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }

    hablar(f"Hoy es: {calendario[dia_semana]}")

pedir_dia()
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos"
    hablar(hora)


def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    # Repasar esto
    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'

    hablar(f'Hola {momento}, soy Siro alegria, tu asistente del colca. Porfavor dime en que puedo ayudarte. Gaaaaa mano pipipi')


def pedir_cosas():
    saludo_inicial()
    comenzar = True
    while comenzar:
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break
pedir_cosas()
