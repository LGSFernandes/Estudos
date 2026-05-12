def notas (* notas, sit = False):

    """
        DocStrings:

            :param notas: Desempacotamento Das Notas Para Avaliação e Cálculos.
            :param sit: Mostra ou não a Situação Média da Turma.
            :return resultado: Retorna o Resultado para Personalização de Resposta.

    """

    resultado = dict()

    resultado['quantidade'] = len(notas)
    resultado['maior'] = max(notas)
    resultado['menor'] = min(notas)
    resultado['média'] = sum(notas) / len(notas)

    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'

    return resultado


lista = notas(5.5, 2.5, 8.5, sit = True)

for k, v in lista.items():
    print(f'A {k} é: {v}')