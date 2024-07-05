precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

codigo_item, quantidade = map(int, input().split())


if codigo_item in precos:
    preco_unitario =precos[codigo_item]
    valor_total = preco_unitario * quantidade

    print(f"Total: R$ {valor_total:.2f}")
else:
    
    print("Código de item inválido.")