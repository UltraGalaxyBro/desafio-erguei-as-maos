def primeiro_refrao():
    return [
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos",
        "E cantai como os filhos do Senhor",
    ]


def animaizinhos(animal, animais):
    return [
        f"Os animaizinhos subiram de dois em dois",
        f"Os animaizinhos subiram de dois em dois",
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


def inicio_segunda_parte():
    return ["E atenção agora, porque"]


def segundo_refrao(movimento):
    base = [
        "O Senhor tem muitos filhos",
        "Muitos filhos ele tem",
        "Eu sou um deles, você também",
        "Louvemos ao Senhor",
    ]

    if movimento:
        base.append(", ".join(movimento))
    
    return base
