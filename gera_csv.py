import pandas as pd

dados_usuarios = {
    'nome': [
        'Arthur Silva', 'Beatriz Souza', 'Carlos Oliveira', 'Daniela Lima', 'Eduardo Santos',
        'Fernanda Rocha', 'Gabriel Mendes', 'Helena Costa', 'Igor Martins', 'Julia Ferreira',
        'Kevin Souza', 'Larissa Lima', 'Marcos Paulo', 'Nathalia Dias', 'Otavio Luiz'
    ],
    'email': [
        'arthur@email.com', 'beasouza@provider.com', 'carlos.oli@web.com', 'dani_lima@site.com', 'edu_santos@email.com',
        'fer.rocha@mail.com', 'gabs.mendes@web.com', 'helena.c@provider.com', 'igor.martins@email.com', 'juju.f@site.com',
        'kevin.s@mail.com', 'lari.lima@web.com', 'marcos.p@email.com', 'nath.dias@provider.com', 'otavio.l@site.com'
    ],
    'senha': [
        'senha123', 'p@ssw0rd', 'admin789', 'dani2024', 'edu#123',
        'fer12345', 'gab@2026', 'helen@123', 'igor_pass', 'julia@321',
        'kevin#99', 'lari_2026', 'marcos@pwd', 'nath#456', 'otavio@789'
    ],
    'is_vip': [
        'S', 'N', 'S', 'N', 'S',
        'N', 'S', 'N', 'S', 'N',
        'S', 'N', 'S', 'N', 'S'
    ]
}

dados_itens = {
    'email_dono': [
        'arthur@email.com', 'arthur@email.com', 'arthur@email.com', 'beasouza@provider.com',
        'carlos.oli@web.com', 'carlos.oli@web.com', 'carlos.oli@web.com', 'dani_lima@site.com',
        'edu_santos@email.com', 'fer.rocha@mail.com', 'gabs.mendes@web.com', 'gabs.mendes@web.com',
        'helena.c@provider.com', 'igor.martins@email.com', 'juju.f@site.com', 'kevin.s@mail.com',
        'lari.lima@web.com', 'marcos.p@email.com', 'marcos.p@email.com', 'nath.dias@provider.com',
        'otavio.l@site.com'
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

df_usuarios.to_csv('usuarios.csv', index=False, encoding='utf-8')
df_itens.to_csv('itens_carrinho.csv', index=False, encoding='utf-8')
