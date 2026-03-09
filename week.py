from playwright.sync_api import sync_playwright
import time
from datetime import timedelta, date
import pandas as pd

class Auto_Bot():

    @staticmethod
    def auto_notification(process):

        with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context('user_data', headless=False)
                page = browser.pages[0]
                page.goto("https://web.whatsapp.com/")
                selector_search_group = 'div[contenteditable="true"]'
                page.wait_for_selector(selector_search_group, timeout=60000)
                page.locator(selector_search_group).click()
                page.locator(selector_search_group).fill("Future")
                page.keyboard.press('Enter')
                selector_chat = 'div[aria-activedescendant][aria-autocomplete="list"]'
                page.locator(selector_chat).fill(process)
                time.sleep(5)
                page.keyboard.press('Enter')
                time.sleep(5)

    @staticmethod
    def auto_off(msg):

        with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context('user_data', headless=True)
                page = browser.pages[0]
                page.goto("https://web.whatsapp.com/")
                selector_search_group = 'div[contenteditable="true"]'
                page.wait_for_selector(selector_search_group, timeout=60000)
                page.locator(selector_search_group).click()
                page.locator(selector_search_group).fill("Future")
                page.keyboard.press('Enter')
                selector_chat = 'div[aria-activedescendant][aria-autocomplete="list"]'
                page.locator(selector_chat).fill(msg)
                page.keyboard.press('Enter')
                time.sleep(10)            

    @staticmethod
    def data_processing():
       
       path = r"C:\Users\caina\OneDrive\Área de Trabalho\Server\Arquivos\Licitacao\MAPA.xlsx"
       df = pd.read_excel(path, sheet_name='2026')
       df = df[df['CLIENTE'].notna()]
       df['DATA'] = pd.to_datetime(df['DATA']).dt.date
       df['R$'] = df['R$'].fillna('S/ESTIMADO')
       df['SITUAÇÃO'] = df['SITUAÇÃO'].fillna('APTO')
       return df



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
              bot.auto_off(f"Bom dia! Não temos pregões para esta semana.")



auto = notification_process()
         
     







       








