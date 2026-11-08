from transformers import pipeline

tradutor = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr", device=-1)


def traduzir_texto(texto: str):
    if not texto.strip():
        raise ValueError("O texto não pode estar vazio.")

    limite = tradutor.model.config.max_position_embeddings
    paragrafos = texto.split("\n\n")
    traducoes = []

    for numero, paragrafo in enumerate(paragrafos, start=1):
        if not paragrafo.strip():
            continue
        tokens = tradutor.tokenizer.encode(paragrafo, add_special_tokens=True)
        if len(tokens) > limite:
            raise ValueError(
                f"O parágrafo {numero} ultrapassa o limite de {limite} tokens."
            )
        resultado = tradutor(paragrafo, max_new_tokens=500, truncation=False)

        traducoes.append(resultado[0]["translation_text"])

    return "\n\n".join(traducoes)
