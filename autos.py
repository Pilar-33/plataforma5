# María del Pilar Lévano Medina
autos = ["Ferrari", "VolksWagen", "Fiat", 
        "Lamborghini", "Tesla", "Honda"]

precios_autos = [10000000, 5000000, 500000, 
                9500000, 8000000, 1000000]

motos = ["Zanella", "Motomel", "Harley", "Honda"]
precios_motos = [100000, 250000, 2000000, 1000000]

def auto_mas_caro(autos, precios_autos):
    for i in range(len(precios_autos)):
        precio_maximo = precios_autos[0]
        marca_maxima = autos[0]
        if precios_autos[i] > precio_maximo:
            precio_maximo = precios_autos[i]
            marca_maxima = autos[i]
        return marca_maxima, precio_maximo
    

def moto_mas_barata(motos, precios_motos):
    for i in range(len(precios_motos)):
        precio_minimo = precios_motos[0]
        marca_minima = motos[0]
        if precios_motos[i] < precio_minimo:
            precio_minimo = precios_motos[i]
            marca_minima = motos[i]
        return marca_minima, precio_minimo
    
def marcas_autos_motos(autos, motos):
    marcas_comunes = []
    for marca_auto in autos:
        if marca_auto in motos:
            marcas_comunes.append(marca_auto)
    return marcas_comunes

