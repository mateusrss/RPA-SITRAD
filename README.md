# RPA-SITRAD

Este projeto tem como objetivo automatizar a geração de relatórios no sistema SITRAD de temperatura e enviar o arquivo gerado (em formato PNG) automaticamente por e-mail. A automação foi implementada utilizando a biblioteca `pyautogui` para interação com a interface gráfica do sistema e um loop `for` para controlar o fluxo de execução. O envio de e-mail é feito automaticamente usando o protocolo SMTP, sem necessidade de interação manual.

Além disso, o script foi configurado para rodar automaticamente todos os dias às 23:55 utilizando uma ferramenta do Windows para agendamento de tarefas.

## Funcionalidades

- **Geração de Relatório**: O script interage automaticamente com o sistema SITRAD para gerar o relatório de temperatura.
- **Envio Automático de E-mail**: Após gerar o relatório em formato PNG, o arquivo é enviado automaticamente para o e-mail configurado no código, sem qualquer intervenção manual.
- **Agendamento de Execução**: O script foi agendado para ser executado automaticamente todos os dias às 23:55 utilizando a ferramenta de agendamento de tarefas do Windows.

## Como Usar

### Pré-requisitos

Antes de executar o projeto, você precisa garantir que as seguintes dependências estejam instaladas:

- **Python 3.x**
- **Bibliotecas Python**: Instale as dependências necessárias com o seguinte comando:

```bash
pip install pyautogui smtplib email

pip install pyautogui
