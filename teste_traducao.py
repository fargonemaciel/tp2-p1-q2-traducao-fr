from transformers import pipeline

tradutor = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr", device=-1)

texto_curto = "Hello, how are you?"

texto_longo = (
    "Technology can help students access educational materials "
    "and practice new skills. However, learning also requires "
    "clear explanations, regular practice, and support from teachers.\n\n"
    "A school is planning to introduce a digital platform. "
    "Before choosing the software, the team will talk to students "
    "and teachers to understand their needs. The first version "
    "will include short activities and simple progress reports.\n\n"
    "After a month, the school will evaluate the results. "
    "Teachers will identify difficulties and suggest improvements. "
    "The goal is to support learning without replacing personal "
    "interaction. The final decision will consider both the "
    "technical results and the experiences of the people involved."
)

textos = {"CURTO": texto_curto, "LONGO": texto_longo}

limite_entrada = tradutor.model.config.max_position_embeddings

for nome, texto in textos.items():
    tokens = tradutor.tokenizer.encode(texto, add_special_tokens=True)
    print(f"\nTESTE {nome}")
    print(f"Tokens de entrada: {len(tokens)}")
    print(f"Limite configurado no modelo: {limite_entrada}")

    resultado = tradutor(texto, max_new_tokens=500, truncation=False)

    print("TRADUÇÃO:")
    print(resultado[0]["translation_text"])

print("\nTRADUÇÃO POR PARÁGRAFOS:")

paragrafos = texto_longo.split("\n\n")

print(f"Quantidade de parágrafos: {len(paragrafos)}")

traducoes = []

for numero, paragrafo in enumerate(paragrafos, start=1):
    if not paragrafo.strip():
        continue

    resultado_paragrafo = tradutor(paragrafo, max_new_tokens=500, truncation=False)

    traducao = resultado_paragrafo[0]["translation_text"]
    traducoes.append(traducao)

    print(f"\nParágrafo {numero}:")
    print(traducao)

texto_traduzido = "\n\n".join(traducoes)

print("\nRESULTADO REUNIDO:")
print(texto_traduzido)
