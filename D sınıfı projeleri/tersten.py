"""
a = input("Bir kelime gir: ")

print(a[::-1])
"""
def tersten(value):
    output = []
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
        
    return ''.join(output)

text = input("Bir cümle girin: ")
print("Yazdığınız cümlenin tersten yazılışı: {}".format(tersten(text)))

