import random

def carregar_frases(caminho_arquivo="frases.txt"):
    """Carrega frases motivacionais de um arquivo texto."""
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]

def exibir_frase(frases):
    """Exibe uma frase aleatória."""
    frase = random.choice(frases)
    print(f"\n✨ Frase motivacional do dia:\n\n\"{frase}\"\n")

if __name__ == "__main__":
    frases = carregar_frases()
    exibir_frase(frases)
