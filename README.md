# Auto_Process 📊🤖

Sistema automatizado de verificação e notificação de pregões utilizando **Python**, **Playwright** e integração com o **Agendador de Tarefas do Windows**.

## 📋 Descrição do Projeto
O **Auto_Process** automatiza a leitura de planilhas Excel para identificar pregões agendados. O sistema resolve o problema comum de `PermissionError` (quando o arquivo está aberto por outro usuário) utilizando a biblioteca `shutil` para criar uma cópia em tempo real dos bits do arquivo, garantindo a execução sem interrupções.

A lógica é distribuída em três rotinas distintas para cobrir todo o ciclo semanal de monitoramento.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12.0**
* **Playwright**: Automação de notificações via navegador.
* **Pandas**: Tratamento e análise de dados das planilhas.
* **Shutil**: Manipulação de arquivos para evitar conflitos de leitura.
* **Openpyxl**: Engine de leitura para arquivos Excel.

## 🗂️ Estrutura de Arquivos e Agendamento
O projeto utiliza **Programação Orientada a Objetos (POO)**, onde os scripts secundários herdam as funcionalidades da classe base no `main.py`.

| Arquivo | Função Principal | Agendamento (Windows) |
| :--- | :--- | :--- |
| `main.py` | **Classe: Auto_Bot**. Verifica pregões para o dia seguinte. | Seg. a Qui. às 17:00 |
| `friday.py` | Herda `main.py`. Verifica pregões para a segunda-feira. | Sextas às 17:00 |
| `week.py` | Herda `main.py`. Mostra os pregões de toda a semana. | Segundas às 09:00 |

## ⚙️ Funcionalidades da Classe (main.py)
A classe principal (Auto_Bot) gerencia todo o fluxo de dados através de três métodos principais:

1. **`auto_notification(process)`**: 
   - Utiliza o Playwright para enviar as informações detalhadas do processo extraídas da planilha.
2. **`auto_off(msg)`**: 
   - Notifica o sistema/usuário quando não existem pregões agendados para o período.
3. **Tratamento de Dados e Cópia de Segurança**:
   - Utiliza `shutil` para copiar o arquivo Excel original.
   - Isso permite que o script acesse os dados em "tempo real", mesmo que alguém esteja editando a planilha no momento da execução.

## 🚀 Como Configurar
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/CainaPV/Auto_Process.git](https://github.com/CainaPV/Auto_Process.git)