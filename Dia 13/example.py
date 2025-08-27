import speech_recognition as sr

def transformar_audio_en_texto():
    r = sr.Recognizer()

    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Empezó la grabación")

        audio = r.listen(origen)

        try:
            pedido = r.recognize_google(audio, language="es-CO")
            print("Dijiste: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Ups, no entendí")
            return "sigo esperando"

        except sr.RequestError:
            print("Ups, no te escucho")
            return "sigo esperando"

        except Exception as e:
            print(f"Ups, algo ha salido mal: {e}")
            return "sigo esperando"

transformar_audio_en_texto()