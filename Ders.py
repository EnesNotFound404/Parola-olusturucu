import random
karakterler = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
parola_uzunlugu = int(input("Parolanın uzunluğunu girin: "))
parola = ""
for _ in range(parola_uzunlugu):
    parola += random.choice(karakterler)
print("Oluşturduğunuz parola: ", parola)






