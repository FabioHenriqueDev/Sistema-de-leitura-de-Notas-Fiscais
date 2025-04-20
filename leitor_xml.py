import xmltodict

def ler_xml_danfe(nota):
    
    documento = xmltodict.parse(nota)
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe'] # Acessando a base da nota fiscal

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF'] # Acessando valor total da nota fiscal

    cnpj_vendeu = dic_notafiscal['emit']['CNPJ'] # Acessando cnpj de quem vendeu
    nome_vendeu = dic_notafiscal['emit']['xNome']# Acessando nome de quem vendeu

    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']

    produtos = dic_notafiscal['det']
    lista_produtos = []

    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, f'R${valor_produto}'))

    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'nome_comprou': [nome_comprou],
        'cpf_comprou': [cpf_comprou],
        'lista_produtos': [lista_produtos]
    }

    return resposta