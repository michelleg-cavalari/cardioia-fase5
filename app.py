import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("WATSON_API_KEY")
url = os.getenv("WATSON_URL")
assistant_id = os.getenv("WATSON_ASSISTANT_ID")
environment_id = os.getenv("WATSON_ENVIRONMENT_ID")

authenticator = IAMAuthenticator(api_key)

assistant = AssistantV2(
    version="2024-08-25",
    authenticator=authenticator
)

assistant.set_service_url(url)

# Cria uma sessão com o Watson
session = assistant.create_session(
    assistant_id=assistant_id,
    environment_id=environment_id
).get_result()

session_id = session["session_id"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.json.get("mensagem", "")

    response = assistant.message(
        assistant_id=assistant_id,
        environment_id=environment_id,
        session_id=session_id,
        user_id="usuario_cardioia",
        input={
            "message_type": "text",
            "text": mensagem
        }
    ).get_result()

    respostas = []

    for item in response["output"]["generic"]:
        if item["response_type"] == "text":
            respostas.append(item["text"])

    return jsonify({
        "resposta": "\n".join(respostas)
    })


if __name__ == "__main__":
    app.run(debug=True)