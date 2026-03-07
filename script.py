import time
import pandas as pd
import requests
import os

URl_api = "http://127.0.0.1:8000/usuarios"

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
planinlha_cadastos = os.path.join(diretorio_atual, "usuarios.csv")

def cadastrar_user():
    try:
        df = pd.read_csv(planinlha_cadastos)    
        print(f"Link estabelecido! inciando processo de cadastros!")

        for index, linha in df.iterrows():
            payload = {
                "nome": str(linha["nome"]),
                "email": str(linha["email"]).strip(),
                "senha": str(linha["senha"])[:50],
                "is_vip": str(linha["is_vip"]).upper(),
            }

            try:
                
                response = requests.post(URl_api, json=payload, timeout = 5)
                
                if response.status_code in [200, 201]:
                    print(f"Usuario {index+1} cadastrado\n"
                    f"Cadastros concluídos: {index+1}/{len(df)}")
                else:
                    print(f"Erro! Não foi possível realizar cadastro {index+1} ERRO {response.status_code}")
            
            except requests.exceptions.ConnectionError:

                print(f"Servidor FastAPI desligado")
        
        print("Processo de cadasto de usuários")    

    except FileNotFoundError:
        print(f"Arquivo '{planinlha_cadastos}' não econtrado, passe o caminho correto!")
    
    except Exception as execption:
        print(f"Erro inesperado encontrado {execption}")


cadastrar_user()