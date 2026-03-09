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
                browser = p.chromium.launch_persistent_context('user_data', headless=False)
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
    tomorrow = today + timedelta(days=1)
    weekday = today.isoweekday()
    df = bot.data_processing()

    #Verificação de Processo para o Dia Seguinte.
    if not weekday >= 6:
        df_new_day = df[df['DATA'] == tomorrow]

        if not df_new_day.empty:

            for index, line in df_new_day.iterrows():
                
                menssage = (
                            f"*AVISO DE LICITAÇÃO  {tomorrow.strftime('%d/%m/%Y')}*\n\n"
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
            bot.auto_off('Boa tarde! Amanhã não temos pregão.')


auto = notification_process()
         