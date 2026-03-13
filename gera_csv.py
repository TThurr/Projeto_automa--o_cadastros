import pandas as pd

dados_usuarios = {
    'nome': [
        'TESTE_A', 'TESTE_B', 'TESTE_C', 'TESTE_D', 'TESTE_E',
        'TESTE_F', 'TESTE_G', 'TESTE_H', 'TESTE_I', 'TESTE_J',
        'TESTE_K', 'TESTE_L', 'TESTE_M', 'TESTE_N', 'TESTE_O'
    ],
    'email': [
        'user_01@exemplo.com.br', 'user_02@exemplo.com.br', 'user_03@exemplo.com.br', 
        'user_04@exemplo.com.br', 'user_05@exemplo.com.br', 'user_06@exemplo.com.br', 
        'user_07@exemplo.com.br', 'user_08@exemplo.com.br', 'user_09@exemplo.com.br', 
        'user_10@exemplo.com.br', 'user_11@exemplo.com.br', 'user_12@exemplo.com.br', 
        'user_13@exemplo.com.br', 'user_14@exemplo.com.br', 'user_15@exemplo.com.br'
    ],

    'senha': [
        'DUMMY_1', 'DUMMY_2', 'DUMMY_3', 'DUMMY_4', 'DUMMY_5',
        'DUMMY_6', 'DUMMY_7', 'DUMMY_8', 'DUMMY_9', 'DUMMY_10',
        'DUMMY_11', 'DUMMY_12', 'DUMMY_13', 'DUMMY_14', 'DUMMY_15'
    ],
    'is_vip': [
        'S', 'N', 'S', 'N', 'S',
        'N', 'S', 'N', 'S', 'N',
        'S', 'N', 'S', 'N', 'S'
    ]
}

dados_itens = {
    'email_dono': [
        'user_01@exemplo.com.br', 'user_01@exemplo.com.br', 'user_01@exemplo.com.br', 
        'user_02@exemplo.com.br', 'user_03@exemplo.com.br', 'user_03@exemplo.com.br', 
        'user_03@exemplo.com.br', 'user_04@exemplo.com.br', 'user_05@exemplo.com.br', 
        'user_06@exemplo.com.br', 'user_07@exemplo.com.br', 'user_07@exemplo.com.br',
        'user_08@exemplo.com.br', 'user_09@exemplo.com.br', 'user_10@exemplo.com.br', 
        'user_11@exemplo.com.br', 'user_12@exemplo.com.br', 'user_13@exemplo.com.br', 
        'user_13@exemplo.com.br', 'user_14@exemplo.com.br', 'user_15@exemplo.com.br'
    ],
    'id_produto': [
        101, 105, 108, 202, 303, 305, 310, 404, 505, 601, 701, 705, 801, 901, 111, 222, 333, 444, 445, 555, 666
    ],
    'nome_produto': [
        'Cadeira Gamer', 'Mouse Pad', 'Headset RGB', 'Smart TV 55', 'Monitor Curvo', 'Teclado Mecanico',
        'Webcam 4K', 'Smartphone S23', 'Fone Bluetooth', 'Mochila Laptop', 'Placa de Video', 'Fonte 750W',
        'Impressora', 'SSD 1TB', 'Pendrive 64GB', 'Processador i7', 'Memoria RAM 16GB', 'Gabinete ATX',
        'Cabo HDMI 2.1', 'Suporte Monitor', 'Roteador WiFi 6'
    ],
    'valor': [
        1200.0, 80.0, 350.0, 3500.0, 1500.0, 400.0, 600.0, 4000.0, 250.0, 180.0, 2800.0, 500.0,
        900.0, 450.0, 45.0, 1900.0, 350.0, 400.0, 60.0, 150.0, 700.0
    ],
    'quantidade': [
        1, 6, 1, 1, 1, 5, 1, 1, 2, 1, 1, 1, 1, 3, 10, 1, 2, 1, 3, 1, 1
    ],
    'promocao_produto': [
        0.90, 1.0, 1.0, 0.95, 1.0, 0.85, 0.90, 0.90, 1.0, 1.0, 0.95, 1.0, 0.90, 1.0, 0.80, 0.95, 1.0, 0.90, 1.0, 1.0, 0.85
    ]
}

df_usuarios = pd.DataFrame(dados_usuarios)
df_itens = pd.DataFrame(dados_itens)

# Salvando os arquivos
df_usuarios.to_csv('usuarios.csv', index=False, encoding='utf-8')
df_itens.to_csv('itens_carrinho.csv', index=False, encoding='utf-8')

print("Arquivos de teste gerados com sucesso e sem dados sensíveis!")