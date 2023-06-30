def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Kullanıcıdan sıcaklık değeri alınması
sıcaklık = float(input("Sıcaklık değerini girin: "))

# Celsius'tan Fahrenheit'a dönüşüm
fahrenheit = celsius_to_fahrenheit(sıcaklık)
print(f"{sıcaklık} Celsius, {fahrenheit} Fahrenheit'a eşittir.")

# Fahrenheit'tan Celsius'a dönüşüm
celsius = fahrenheit_to_celsius(sıcaklık)
print(f"{sıcaklık} Fahrenheit, {celsius} Celsius'a eşittir.")
