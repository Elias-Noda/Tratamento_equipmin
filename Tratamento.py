import pandas as pd
import numpy as np
import glob

cols = ["DESCRIÇÃO_CONTRATO","DESCRIÇÃO_CONTRATADA","DESCRIÇÃO_UNIDADE",
        "DESCRIÇÃO_SERVIÇO","DESCRIÇÃO_PERÍODO","CARGO_EQUIPE_MÍNIMA",
        "CARGA_HORÁRIA_SEMANAL","EQUIPE_MÍNIMA_CONTRATADA","TOTAL_CARGA_HORÁRIA_CONTRATADA",
        "TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_SP","TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_OS_CLT",
        "TIPO_CONTRATAÇÃO_PREFEITURA_MUNICÍPIO_OS_TERCEIROS","TOTAL_HORAS_APONTADAS","AVALIAÇÃO"]

# Identificando o caminho dos arquivos em cada pasta
n = 1
while n < 24:
    if n == 1:
        path = "Input_data/R001-2014/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 2:
        path = "Input_data/R002-2014/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 3:
        path = "Input_data/R003-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 4:
        path = "Input_data/R004-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 5:
        path = "Input_data/R005-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 6:
        path = "Input_data/R006-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 7:
        path = "Input_data/R007-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 8:
        path = "Input_data/R008-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 9:
        path = "Input_data/R009-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 10:
        path = "Input_data/R010-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 11:
        path = "Input_data/R011-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 12:
        path = "Input_data/R012-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 13:
        path = "Input_data/R014-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 14:
        path = "Input_data/R015-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 15:
        path = "Input_data/R016-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 16:
        path = "Input_data/R0017-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 17:
        path = "Input_data/R018-2015/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 18:
        path = "Input_data/R019-2016/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 19:
        path = "Input_data/R020-2016/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 20:
        path = "Input_data/R021-2016/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 21:
        path = "Input_data/R022-2016/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 22:
        path = "Input_data/R023-2016/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)

    elif n == 23:
        path = "Input_data/R024-2020/"
        all_files = glob.glob(path + "*.csv")

        li = [pd.read_csv(file,
                        encoding='utf-8',
                        sep=";",
                        decimal=",",
                        index_col=None,
                        header=0) for file in all_files]
        df = pd.concat(li, axis=0, ignore_index=True) if len(li) > 0 else pd.DataFrame(columns = cols)


    # Definindo a função qde tratamento dos dados
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
        df["TOTAL_APONTADA_SEM_EXCEDENTE"] = df["TOTAL_APONTADA_SEM_EXCEDENTE"].astype(np.float)

        # Criando a coluna que calcula a porcentagem integral da apontada por contratada
        df["PORCENTAGEM_INTEGRAL"] = df["TOTAL_HORAS_APONTADAS"] / df["TOTAL_CARGA_HORARIA_CONTRATADA"]

        # Criando a coluna que calcula a porcentagem sem excedente da apontada por contratada
        df["PORCENTAGEM_SEM_EXCEDENTE"] = df["TOTAL_APONTADA_SEM_EXCEDENTE"] / df["TOTAL_CARGA_HORARIA_CONTRATADA"]

        # Removendo os valores nulos e inf causados por divisão com 0
        df["PORCENTAGEM_INTEGRAL"].replace([np.inf, -np.inf], "N/A", inplace=True)
        df["PORCENTAGEM_SEM_EXCEDENTE"] = df["PORCENTAGEM_SEM_EXCEDENTE"].fillna(0)

        # Adicionando a ID do contrato
        if n == 1:
            df["ID_CONTRATO"] = "R001-2014"
        elif n == 2:
            df["ID_CONTRATO"] = "R002-2014"
        elif n == 3:
            df["ID_CONTRATO"] = "R003-2015"
        elif n == 4:
            df["ID_CONTRATO"] = "R004-2015"
        elif n == 5:
            df["ID_CONTRATO"] = "R005-2015"
        elif n == 6:
            df["ID_CONTRATO"] = "R006-2015"
        elif n == 7:
            df["ID_CONTRATO"] = "R007-2015"
        elif n == 8:
            df["ID_CONTRATO"] = "R008-2015"
        elif n == 9:
            df["ID_CONTRATO"] = "R009-2015"
        elif n == 10:
            df["ID_CONTRATO"] = "R010-2015"
        elif n == 11:
            df["ID_CONTRATO"] = "R011-2015"
        elif n == 12:
            df["ID_CONTRATO"] = "R012-2015"
        elif n == 13:
            df["ID_CONTRATO"] = "R014-2015"
        elif n == 14:
            df["ID_CONTRATO"] = "R015-2015"
        elif n == 15:
            df["ID_CONTRATO"] = "R016-2015"
        elif n == 16:
            df["ID_CONTRATO"] = "R017-2015"
        elif n == 17:
            df["ID_CONTRATO"] = "R018-2015"
        elif n == 18:
            df["ID_CONTRATO"] = "R019-2016"
        elif n == 19:
            df["ID_CONTRATO"] = "R020-2016"
        elif n == 20:
            df["ID_CONTRATO"] = "R021-2016"
        elif n == 21:
            df["ID_CONTRATO"] = "R022-2016"
        elif n == 22:
            df["ID_CONTRATO"] = "R023-2016"
        elif n == 23:
            df["ID_CONTRATO"] = "R024-2020"
        
        # Colocando as colunas em ordem
        df = df.reindex(columns = ["ID_CONTRATO", "DESCRICAO_UNIDADE", "DESCRICAO_PERIODO",
                        "TOTAL_HORAS_APONTADAS", "TOTAL_APONTADA_SEM_EXCEDENTE",
                        "TOTAL_CARGA_HORARIA_CONTRATADA", "AVALIACAO", "EXCEDENTE",
                        "PORCENTAGEM_INTEGRAL", "PORCENTAGEM_SEM_EXCEDENTE"])

        # Exportando o arquivo depois de tratado
        if n == 1:
            df.to_csv("Output_data/R001-2014.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)

        elif n == 2:
            df.to_csv("Output_data/R002-2014.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)

        elif n == 3:
            df.to_csv("Output_data/R003-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 4:
            df.to_csv("Output_data/R004-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 5:
            df.to_csv("Output_data/R005-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 6:
            df.to_csv("Output_data/R006-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 7:
            df.to_csv("Output_data/R007-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 8:
            df.to_csv("Output_data/R008-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 9:
            df.to_csv("Output_data/R009-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 10:
            df.to_csv("Output_data/R010-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 11:
            df.to_csv("Output_data/R011-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 12:
            df.to_csv("Output_data/R012-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 13:
            df.to_csv("Output_data/R014-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 14:
            df.to_csv("Output_data/R015-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 15:
            df.to_csv("Output_data/R016-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 16:
            df.to_csv("Output_data/R017-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 17:
            df.to_csv("Output_data/R018-2015.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 18:
            df.to_csv("Output_data/R019-2016.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 19:
            df.to_csv("Output_data/R020-2016.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 20:
            df.to_csv("Output_data/R021-2016.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 21:
            df.to_csv("Output_data/R022-2016.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 22:
            df.to_csv("Output_data/R023-2016.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
        elif n == 23:
            df.to_csv("Output_data/R024-2020.csv",
                    encoding='utf-8',
                    sep=';',
                    decimal=".",
                    index=False,
                    header=True)
        
    # Chamando a função para tratar os dados
    tratamento(df)

    # Incrementando o indicador para ele refazer o processo com o próximo conjunto
    n += 1
