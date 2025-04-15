# RPA-SITRAD

Este projeto tem como objetivo automatizar a geração de relatórios no sistema SITRAD de temperatura e enviar o arquivo gerado (em formato PNG) automaticamente por e-mail. A automação foi implementada utilizando a biblioteca `pyautogui` para interação com a interface gráfica do sistema e um loop `for` para controlar o fluxo de execução. O envio de e-mail é feito automaticamente usando o protocolo SMTP, sem necessidade de interação manual.

## Funcionalidades

- **Geração de Relatório**: O script interage automaticamente com o sistema SITRAD para gerar o relatório de temperatura.
- **Envio Automático de E-mail**: Após gerar o relatório em formato PNG, o arquivo é enviado automaticamente para o e-mail configurado no código, sem qualquer intervenção manual.
- 


Antes de executar o projeto, você precisa garantir que as seguintes dependências estejam instaladas:

- **Python 3.x**
- **Bibliotecas Python**: Instale as dependências necessárias com o seguinte comando:

```bash
pip install pyautogui
