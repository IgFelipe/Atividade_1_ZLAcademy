codigo_peca1, numero_peca1, unitario1 = input().split()
codigo_peca1 = int(codigo_peca1)
numero_peca1 = int(numero_peca1)
unitario1 = float(unitario1)

codigo_peca2, numero_peca2,unitario2 = input().split()
codigo_peca2 = int(codigo_peca2)
numero_peca2 = int(numero_peca2)
unitario2 = float(unitario2)


total_pagar = (numero_peca1 *unitario1) + (numero_peca2 *unitario2)


print(f"VALOR A PAGAR: R$ {total_pagar:.2f}")