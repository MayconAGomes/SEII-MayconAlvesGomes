peso = input("Peso: ")
peso = float(peso)
unidade = input("(K)g ou (L)bs: ")
unidade = unidade.lower()
if unidade == "k":
    print("Peso em lbs: " + str(peso*2.205))
elif unidade == "l":
    print("Peso em kg: " + str(peso/2.205))
