
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    response = ""

    if "desabafar" in incoming_msg:
        response = "Pode desabafar comigo. Estou aqui para ouvir."
    elif "frase" in incoming_msg:
        response = "Acredite: até as maiores árvores começaram como pequenas sementes."
    elif "respirar" in incoming_msg:
        response = "Vamos juntos: Inspire profundamente... expire lentamente..."
    else:
        response = "Oi! Eu sou o CoraBot. Envie 'desabafar', 'frase' ou 'respirar'."

    msg.body(response)
    return str(resp)
