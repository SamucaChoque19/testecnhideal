rodas = int(input("Qual a quantidade de rodas do veículo: "))
peso = float(input("Qual o peso em Kg do veículo: "))
pessoas = float(input("Quantas pessoas ocupam o veículo: "))

if rodas == 2 or rodas == 3:
    print("A categoria ideal para veículos com 2 ou 3 rodas é: A")
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("A categoria ideal para veículos apartir de 4 rodas e peso infeior a 3500 kg é: B")
elif rodas >= 4 and peso >= 3500 and peso <= 6000:
    print("A categoria ideal para veículos apartir de 4 rodas e peso entre 3500 e 6000 kg é: C")
elif rodas >= 4 and pessoas > 8:
    print("A categoria ideal para veículos apartir de 4 rodas e para mais de 8 passageiros é: D")
else:
    if rodas >= 4 and peso > 6000:
        print("A categoria ideal para veículos apartir de 4 rodas e peso superior a 6000 kg é: E")