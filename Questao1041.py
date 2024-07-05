x, y = map(float, input().split())


if x == 0 and y == 0:
    print("Origem")

elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")

else:
    quadrante = 1 if x > 0 and y > 0 else \
                2 if x < 0 and y > 0 else \
                3 if x < 0 and y < 0 else \
                4
    print(f"Q{quadrante}")
