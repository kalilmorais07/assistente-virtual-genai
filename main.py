import openai

openai.api_key = "SUA_CHAVE_OPENAI_AQUI"

def assistente_virtual(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente virtual bancário educado e claro."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content

print("🤖 Assistente Virtual Bancário")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Assistente: Até logo!")
        break
    resposta = assistente_virtual(pergunta)
    print("Assistente:", resposta)
