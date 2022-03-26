import requests
import json
import pandas as pd


def conteudo():
    try:
        r = requests.get(
            'https://apiteams.goobee.com.br/api/publicavaga/vagas/SITE_CADMUS').content.decode('utf-8')
        resposta = json.loads(r)

        dataframe = []

        i = 0
        n_vagas = len(resposta)
        while i < n_vagas:
            data = {'Nome': {resposta[i]["name"]}, 'Local': resposta[i]['cidade_Regi_o__c'], 'Descrição': str(
                resposta[i]['descricao_da_vaga__c']).replace('<br>', '').replace('\n', '').replace('•', '')}
            dataframe.append(data)
            i += 1

        df = pd.DataFrame.from_dict(dataframe)
        df.to_excel('Vagas.xlsx', index=False)

    except Exception as error:
        raise error


if __name__ == "__main__":
    conteudo()
