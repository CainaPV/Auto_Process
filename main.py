from playwright.sync_api import sync_playwright
import time
from datetime import timedelta, date
import pandas as pd
import shutil
import os

class Auto_Bot():

    @staticmethod
    def auto_notification(process):

        with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context('user_data', headless=False)
                page = browser.pages[0]
                page.goto("https://web.whatsapp.com/")
                selectors_list = ['input[aria-label*="Search"]', 'div[aria-label*="Search"]']
                group_field = None
                for sel in selectors_list:
                    try:
                         group_field = page.wait_for_selector(sel, timeout=60000)
                         if group_field:
                              break
                    except Exception:
                         continue     
                if group_field:
                     group_field.fill("Future")
                     selector_result = 'span[title="Future"]'
                     page.locator(selector_result).click()
                     selectors_message_list = ['div[aria-activedescendant][aria-autocomplete*="list"]', 'div[contenteditable*="true"]', 'div[data-tab="10"]', 'input[aria-activedescendant][aria-autocomplete="list"]']
                     message_field = None
                     for sel in selectors_message_list:
                          try:
                               message_field = page.wait_for_selector(sel, timeout=60000)
                               if message_field:
                                    break
                          except Exception:
                               continue
                if message_field:
                     message_field.fill(process)
                     time.sleep(5)
                     page.keyboard.press('Enter')
                     time.sleep(15)

    @staticmethod
    def auto_off(msg):

        with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context('user_data', headless=False)
                page = browser.pages[0]
                page.goto("https://web.whatsapp.com/")
                selectors_list = ['input[aria-label*="Search"]', 'div[aria-label*="Search"]']
                group_field = None
                for sel in selectors_list:
                    try:
                         group_field = page.wait_for_selector(sel, timeout=60000)
                         if group_field:
                              break
                    except Exception:
                         continue     
                if group_field:
                     group_field.fill("Future")
                     selector_result = 'span[title="Future"]'
                     page.locator(selector_result).click()
                     selectors_message_list = ['div[aria-activedescendant][aria-autocomplete*="list"]', 'div[contenteditable*="true"]', 'div[data-tab="10"]', 'input[aria-activedescendant][aria-autocomplete="list"]']
                     message_field = None
                     for sel in selectors_message_list:
                          try:
                               message_field = page.wait_for_selector(sel, timeout=60000)
                               if message_field:
                                    break
                          except Exception:
                               continue
                if message_field:
                     message_field.fill(msg)
                     time.sleep(5)
                     page.keyboard.press('Enter')
                     time.sleep(15)    
                                      

    @staticmethod
    def data_processing():
       
       path = r"C:\Users\caina\OneDrive\Área de Trabalho\Server\Arquivos\Licitacao\MAPA.xlsx"
       file_temp = 'mapa-temp.xlsx'
       copy_file = shutil.copy2(path,file_temp)   
       df = pd.read_excel(copy_file, sheet_name='2026')
       os.remove(file_temp) 
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
            msg = f"Boa tarde! Amanhã não temos pregão."
            bot.auto_off(msg)


if __name__ == "__main__":
    notification_process()
         