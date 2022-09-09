import random

contador = 0

atracoes = ['RODA GIGANTE', 'MONTANHA RUSSA', 'MONTANHA RUSSA AO CONTRARIO', 'SHOW DE MANOBRAS', 'KART', 'GIGA TOWER', 'TOBOAGUA','CARROSSEL', 
'SHOW GALINHA PINTADINHA', 'BARCO VIKING', 'CARRINHO BATE BATE', 'PEDALINHO', 'SHOW PATRULHA CANINA', 'ESPAÇO KIDS', 'LIMPEZA', 'PRAÇA DE ALIMENTAÇÃO', 'PORTARIA', 'SEGURANÇA']

setor = []

while contador < len(atracoes):
    letra = chr(random.randint(ord('A'), ord('G')))
    num = random.randint(1, 6)
    letra_num = f'{letra}{num}'
    setor.append(letra_num)
    contador += 1