# Aqui estamos importando um pacote interno no Python
# O pacote Datetime nos permite trabalhar com datas
from datetime import date, timedelta, datetime

hoje = date.today() # Este método do pacote nos retorna a data atual
print(hoje)

# Você também pode definir uma data específica

data_especifica = date(2023, 6, 26) # Neste caso é importante notar que o padrão americano é usado ano, mês e dia
print(data_especifica)

# Pegando partes separadas de datas

print(hoje.year)  # Mostra o ano
print(hoje.month) # Mostra o mês
print(hoje.day)   # Mostra o dia

hoje += timedelta(days=2)      # Aumenta dois dias na contagem
print(hoje)

hoje += timedelta(days=12)     # Se a soma ou subtração passarem o limite do mês
print(hoje)                    # A data é automaticamente atualizada

#########################################################################################
#Trabalhando com datas                                                                  #
#########################################################################################

agora = datetime.now()         # Pega o horário do momento

print(agora.hour)
print(agora.minute)
print(agora.second)

agora += timedelta(hours=5)    # Adiciona 5 horas ao tempo total

print(agora)

# Transformando uma data em String
string_data = hoje.strftime('%d-%m-%y')
print(string_data)

hoje += timedelta(days=10)
print(hoje)

hoje = datetime.strptime(string_data, '%d-%m-%y')
print(hoje)
