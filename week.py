from playwright.sync_api import sync_playwright
import time
from datetime import timedelta, date
import pandas as pd
from main import Auto_Bot

bot = Auto_Bot()


def notification_process():
    
    bot = Auto_Bot()
    today = date.today()
    df = bot.data_processing()

    #Verifica se hoje é SEGUNDA, se for, vai avisar todos pregões que irão acontecer no meio da semana(SEGUNDA ATÉ SEXTA).
    if today.isoweekday() == 1:
         end_week = today + timedelta(days=4)
         df_week = df[(df['DATA'] >= today) & (df['DATA'] <= end_week)]
         if not df_week.empty:
              for index, line in df_week.iterrows():
              
                menssage = (
                                f"*AVISO DE LICITAÇÃO PARA ESTA SEMANA*\n\n"
                                f"*PROCESSO: #**{line['#']}*\n"
                                f"*DATA: {line['DATA'].strftime('%d/%m/%Y')}*\n"
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
        msg = f"Bom dia! Não temos pregões para esta semana."
        bot.auto_off(msg)



auto = notification_process()
         
     







       








