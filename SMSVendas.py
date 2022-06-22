import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACcdd703ce4491490a196629b543af6a1c"
# Your Auth Token from twilio.com/console
auth_token  = "834a3fac8356ebd8b36122da099b8550"
client = Client(account_sid, auth_token)
# Pandas - integração do python com exel
# Openpyxl - integração do python com exel
# Twilio1 - integração do python com SMS
# Passo a passo de solução
# Abrir os seis arquivos em excell
lista_meses = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Para cada arquivo verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 45000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 45000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 45000,'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')
        message = client.messages.create(
            to="+5583996384873",
            from_="+13862591123",
            body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas:{vendas}')

        print(message.sid)

# Se for maior que 55 mil envia SMS com o nome, o mês e as vendas do vendedor
# Caso não seja maior que 55 mil: não fazer nada
