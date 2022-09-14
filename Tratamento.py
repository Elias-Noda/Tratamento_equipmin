import pandas as pd
import numpy as np
import glob


path = "Input_data/"
all_files = glob.glob(path + "*.csv")

li = [pd.read_csv(file,
                encoding='utf-8',
                sep=";",
                decimal=",",
                index_col=None,
                header=0) for file in all_files]
df = pd.concat(li, axis=0, ignore_index=True)


def tratamento(df):

    # Apagando as colunas irrelevantes
    df = df.drop(["DESCRIÇÃO_CONTRATO","DESCRIÇÃO_CONTRATADA",
            "DESCRIÇÃO_SERVIÇO","CARGO_EQUIPE_MÍNIMA",
            "CARGA_HORÁRIA_SEMANAL","EQUIPE_MÍNIMA_CONTRATADA",
            "TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_SP",
            "TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_OS_CLT",
            "TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_OS_TERCEIROS"], axis=1)

    # Removendo acentos dos nomes das colunas para evitar problemas
    df[["DESCRICAO_UNIDADE", "DESCRICAO_PERIODO",
        "TOTAL_CARGA_HORARIA_CONTRATADA", "AVALIACAO"]
        ] = df[["DESCRIÇÃO_UNIDADE", "DESCRIÇÃO_PERÍODO",
                "TOTAL_CARGA_HORÁRIA_CONTRATADA", "AVALIAÇÃO"]]

    df = df.drop(["DESCRIÇÃO_UNIDADE", "DESCRIÇÃO_PERÍODO",
        "TOTAL_CARGA_HORÁRIA_CONTRATADA", "AVALIAÇÃO"], axis=1)


    # Transformando os valores faltantes em zero
    df["TOTAL_CARGA_HORARIA_CONTRATADA"] = df["TOTAL_CARGA_HORARIA_CONTRATADA"].fillna(0)
    df["TOTAL_HORAS_APONTADAS"] = df["TOTAL_HORAS_APONTADAS"].fillna(0)
    df["TOTAL_CARGA_HORARIA_CONTRATADA"] = df["TOTAL_CARGA_HORARIA_CONTRATADA"].astype(np.float)
    df["TOTAL_HORAS_APONTADAS"] = df["TOTAL_HORAS_APONTADAS"].astype(np.float)

    # Criando uma coluna que mostra o quanto o apontado excede o contratado
    df["EXCEDENTE"] = df["AVALIACAO"]
    df["EXCEDENTE"][df["EXCEDENTE"] < 0] = 0

    # Criando uma coluna de que limita o excedente de apontada caso seja maior que a contratada
    df["TOTAL_APONTADA_SEM_EXCEDENTE"] = df["TOTAL_HORAS_APONTADAS"]
    for i in df["EXCEDENTE"]:
        if i > 0:
            df["TOTAL_APONTADA_SEM_EXCEDENTE"] = df["TOTAL_HORAS_APONTADAS"] - df["EXCEDENTE"]

    # Criando a coluna que calcula a porcentagem integral da apontada por contratada
    df["PORCENTAGEM_INTEGRAL"] = df["TOTAL_HORAS_APONTADAS"] / df["TOTAL_CARGA_HORARIA_CONTRATADA"]

    # Criando a coluna que calcula a porcentagem sem excedente da apontada por contratada
    df["PORCENTAGEM_SEM_EXCEDENTE"] = df["TOTAL_APONTADA_SEM_EXCEDENTE"] / df["TOTAL_CARGA_HORARIA_CONTRATADA"]

    # Removendo os valores nulos e inf causados por divisão com 0
    df["PORCENTAGEM_INTEGRAL"].replace([np.inf, -np.inf], "N/A", inplace=True)
    df["PORCENTAGEM_SEM_EXCEDENTE"] = df["PORCENTAGEM_SEM_EXCEDENTE"].fillna(0)

    # Colocando as colunas em ordem
    df = df.reindex(columns = ["DESCRICAO_UNIDADE", "DESCRICAO_PERIODO",
                    "TOTAL_HORAS_APONTADAS", "TOTAL_APONTADA_SEM_EXCEDENTE",
                    "TOTAL_CARGA_HORARIA_CONTRATADA", "AVALIACAO", "EXCEDENTE",
                    "PORCENTAGEM_INTEGRAL", "PORCENTAGEM_SEM_EXCEDENTE"])

    # Colocar aqui o nome que você quer para o arquivo tratado
    df.to_csv("Output_data/file.csv",
            encoding='utf-8',
            sep=';',
            decimal=".",
            index=False,
            header=True)

tratamento(df)