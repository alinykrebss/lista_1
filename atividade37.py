segundos = int(input("Digite um valor inteiro em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = (segundos % 3600) % 60
print("O tempo em horas:minutos:segundos é:", horas, "h:", minutos, "m:", segundos_restantes, "s")