def primeiro_refrao():
    return [
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos",
        "E cantai como os filhos do Senhor",
    ]


def animalzinhos(animal, animais):
    return [
        f"Os animalzinhos subiram de dois em dois",
        f"Os animalzinhos subiram de dois em dois",
        f"{animal}",
        f"E {animais}, como os filhos do Senhor",
    ]


def primeiro_verso():
    return [
        "Deus disse a Noé: Constrói uma arca",
        "Deus disse a Noé: Constrói uma arca",
        "Que seja feita",
        "De madeira para os filhos do Senhor",
    ]


def segundo_refrao():
    return [
        "O Senhor tem muitos filhos",
        "Muitos filhos ele tem",
        "Eu sou um deles, você também",
        "Louvemos ao Senhor",
    ]

verso_atual = ""

def verso_formando(pequena_frase):
    global verso_atual
    verso_atual += " " + pequena_frase
    return verso_atual


def letra_musica():
    refrao = primeiro_refrao()
    animalzinhos1 = animalzinhos("O elefante", "os passarinhos")
    animalzinhos2 = animalzinhos("A minhoquinha", "os pinguins")
    animalzinhos3 = animalzinhos("O canguru", "o sapinho")
    verso = primeiro_verso()
    outro_refrao = segundo_refrao()

    verso_formado0 = verso_formando("Braço direito")
    verso_formado1 = verso_formando(", braço esquerdo")
    verso_formado2 = verso_formando(", perna direita")
    verso_formado3 = verso_formando(", perna esquerda")
    verso_formado4 = verso_formando(", balança a cabeça")
    verso_formado5 = verso_formando(", dá uma voltinha")
    verso_formado6 = verso_formando(", dá um pulinho")
    verso_formado7 = verso_formando("e abraça o irmão")

    musica = [
        {"tempo": 22000, "texto": refrao[0]},
        {"tempo": 25000, "texto": refrao[1]}, 
        {"tempo": 29000, "texto": refrao[2]}, 
        {"tempo": 32000, "texto": refrao[3]}, 
        {"tempo": 38000, "texto": animalzinhos1[0]},
        {"tempo": 41000, "texto": animalzinhos1[1]}, 
        {"tempo": 45000, "texto": animalzinhos1[2]},
        {"tempo": 47000, "texto": animalzinhos1[3]}, 
        {"tempo": 52000, "texto": animalzinhos2[0]},  
        {"tempo": 55000, "texto": animalzinhos2[1]},  
        {"tempo": 59000, "texto": animalzinhos2[2]},  
        {"tempo": 61000, "texto": animalzinhos2[3]},  
        {"tempo": 66000, "texto": animalzinhos3[0]},  
        {"tempo": 69000, "texto": animalzinhos3[1]},  
        {"tempo": 72000, "texto": animalzinhos3[2]},  
        {"tempo": 75000, "texto": animalzinhos3[3]},  
        {"tempo": 80000, "texto": verso[0]}, 
        {"tempo": 83000, "texto": verso[1]},  
        {"tempo": 86000, "texto": verso[2]},  
        {"tempo": 88000, "texto": verso[3]},  
        {"tempo": 93000, "texto": "Por isso...!"}, 
        {"tempo": 96000, "texto": refrao[0]},
        {"tempo": 99000, "texto": refrao[1]},  
        {"tempo": 102000, "texto": refrao[2]},  
        {"tempo": 105000, "texto": refrao[3]},  
        {"tempo": 111000, "texto": refrao[0]},  
        {"tempo": 114000, "texto": refrao[1]},  
        {"tempo": 118000, "texto": refrao[2]},  
        {"tempo": 120000, "texto": refrao[3]},  
        {"tempo": 126000, "texto": refrao[0]}, 
        {"tempo": 130000, "texto": refrao[1]}, 
        {"tempo": 133000, "texto": refrao[2]},
        {"tempo": 136000, "texto": refrao[3]},
        {"tempo": 139000, "texto": "E atenção agora, porque"},
        {"tempo": 140000, "texto": outro_refrao[0]},
        {"tempo": 143000, "texto": outro_refrao[1]},
        {"tempo": 147000, "texto": outro_refrao[2]},
        {"tempo": 151000, "texto": outro_refrao[3]},
        {"tempo": 153000, "texto": verso_formado0},
        {"tempo": 154000, "texto": outro_refrao[0]},
        {"tempo": 158000, "texto": outro_refrao[1]},
        {"tempo": 161000, "texto": outro_refrao[2]},
        {"tempo": 164000, "texto": outro_refrao[3]},
        {"tempo": 167000, "texto": verso_formado1},
        {"tempo": 169000, "texto": outro_refrao[0]},
        {"tempo": 172000, "texto": outro_refrao[1]},
        {"tempo": 176000, "texto": outro_refrao[2]},
        {"tempo": 179000, "texto": outro_refrao[3]},
        {"tempo": 182000, "texto": verso_formado2},
        {"tempo": 185000, "texto": outro_refrao[0]},
        {"tempo": 188000, "texto": outro_refrao[1]},
        {"tempo": 191000, "texto": outro_refrao[2]},
        {"tempo": 195000, "texto": outro_refrao[3]},
        {"tempo": 198000, "texto": verso_formado3},
        {"tempo": 202000, "texto": outro_refrao[0]},
        {"tempo": 205000, "texto": outro_refrao[1]},
        {"tempo": 208000, "texto": outro_refrao[2]},
        {"tempo": 211000, "texto": outro_refrao[3]},
        {"tempo": 214000, "texto": verso_formado4},
        {"tempo": 219000, "texto": outro_refrao[0]},
        {"tempo": 222000, "texto": outro_refrao[1]},
        {"tempo": 225000, "texto": outro_refrao[2]},
        {"tempo": 229000, "texto": outro_refrao[3]},
        {"tempo": 232000, "texto": verso_formado5},
        {"tempo": 237000, "texto": outro_refrao[0]},
        {"tempo": 240000, "texto": outro_refrao[1]},
        {"tempo": 243000, "texto": outro_refrao[2]},
        {"tempo": 246000, "texto": outro_refrao[3]},
        {"tempo": 249000, "texto": verso_formado6},
        {"tempo": 254000, "texto": outro_refrao[0]},
        {"tempo": 257000, "texto": outro_refrao[1]},
        {"tempo": 260000, "texto": outro_refrao[2]},
        {"tempo": 263000, "texto": outro_refrao[3]},
        {"tempo": 265000, "texto": verso_formado7},
    ]

    return musica
