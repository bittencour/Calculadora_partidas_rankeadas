def calcular_nivel_heroi(qtdVitorias, qtdDerrotas):
    saldoVitorias = qtdVitorias - qtdDerrotas

    if saldoVitorias <= 10:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Ferro"
    elif saldoVitorias <= 20:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Bronze"
    elif saldoVitorias <= 50:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Prata"
    elif saldoVitorias <= 80:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Ouro"
    elif saldoVitorias <= 90:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Diamante"
    elif saldoVitorias <= 100:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Lendário"
    else:
        return f"O Herói tem de saldo {saldoVitorias} e está no nível de Imortal"

qtdVitorias = int(input("Digite o número de vitórias do herói: "))
qtdDerrotas = int(input("Digite o número de derrotas do herói: "))

resultado = calcular_nivel_heroi(qtdVitorias, qtdDerrotas)
print(resultado)

