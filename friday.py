from playwright.sync_api import sync_playwright
import time
from datetime import timedelta, date
import pandas as pd
from main import Auto_Bot


#Verifica se hoje é sexta, se for, avisa se tem pregão na segunda.
def notification_process():

    bot = Auto_Bot()
    today = date.today()
    tomorrow = today + timedelta(days=1)
    weekday = today.isoweekday()
    df = bot.data_processing()
    
    if today.isoweekday() == 5:
         monday = today + timedelta(days=3)
         df_monday = df[df['DATA'] == monday]
         if not df_monday.empty:
              for index, line in df_monday.iterrows():
              
                menssage = (
                            f"*AVISO DE LICITAÇÃO  {monday.strftime('%d/%m/%Y')}*\n\n"
                            f"*PROCESSO: #**{line['#']}*\n"
                            f"*HORA:* {line['HORA'].strftime('%H:%Mh')}\n"
                            f"*FORMA DE COMPRA:* {line['MOD']}\n"
                            f"*CLIENTE:* {line['CLIENTE']}\n"
                            f"*OBJETO:* {line['OBJETO']}\n"
                            f"*VALOR:* R$ {line['R$']}\n"
                            f"*PORTAL:* {line['PORTAL']}\n"
                            f"*SITUAÇÃO:* {line['SITUAÇÃO']}"
                        )
                bot.auto_notification(menssage)
         else:
          msg=f"Boa tarde! Não temos pregão na segunda."
          bot.auto_off(msg)
            


auto = notification_process()
         