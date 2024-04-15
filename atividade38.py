hora_inicio = int(input("Digite a hora de início da experiência em horas (0-23): "))
minuto_inicio = int(input("Digite os minutos de início da experiência (0-59): "))
segundo_inicio = int(input("Digite os segundos de início da experiência (0-59): "))
duracao_segundos = int(input("Digite a duração da experiência em segundos: "))

total_segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
total_segundos_fim = total_segundos_inicio + duracao_segundos

hora_fim = total_segundos_fim // 3600
minuto_fim = (total_segundos_fim % 3600) // 60
segundo_fim = (total_segundos_fim % 3600) % 60

print("O horário de término da experiência é:", hora_fim, "h:", minuto_fim, "m:", segundo_fim, "s")