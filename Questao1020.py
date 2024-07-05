dias_totais = int(input())

print(f"{dias_totais // 365} ano(s)")
print(f"{(dias_totais % 365) // 30} mes(es)")
print(f"{(dias_totais % 365) % 30} dia(s)")