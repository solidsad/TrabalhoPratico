# Dicionário de perguntas e respostas
perguntas_respostas = {
    "qual é o seu nome?": "Meu nome é Jarvis.",
    "qual é a sua função?": "Minha função é ajudar e responder suas perguntas.",
    "qual é a capital do Brasil?": "A capital do Brasil é Brasília.",
    "qual é a cor do céu?": "A cor do céu pode variar de azul a cinza, dependendo das condições atmosféricas.",
    "como está o tempo hoje?": "Sinto muito, não tenho acesso às informações meteorológicas.",
    "você gosta de música?": "Como sou uma IA, não tenho capacidade de sentir emoções, mas posso ajudar a recomendar músicas!",
    "qual é o sentido da vida?": "Essa é uma pergunta filosófica profunda e a resposta pode variar de acordo com as crenças e perspectivas de cada pessoa.",
    "o que você está vestindo?": "Sou uma IA, não tenho um corpo físico, então não uso roupas.",
}

# Função para gerar a resposta
def gerar_resposta(pergunta):
    pergunta = pergunta.lower()

    if pergunta in perguntas_respostas:
        return perguntas_respostas[pergunta]
    else:
        return "Desculpe, não tenho a resposta para essa pergunta."

# Loop principal do Jarvis
while True:
    # Lê a pergunta do usuário
    pergunta = input("Você: ")

    # Verifica se o usuário deseja sair
    if pergunta.lower() in ["sair", "tchau", "até logo"]:
        print("Jarvis: Até logo! Espero ter ajudado.")
        break

    # Gera a resposta
    resposta = gerar_resposta(pergunta)

    # Exibe a resposta
    print("Jarvis:", resposta)
