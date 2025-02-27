# py-tk-windows-notify-
Sistema de notificação parar Windows e outros sistemas que rodam tk py



# Sistema de Notificações TK com Pygame

Este repositório contém um sistema de notificações usando `tkinter` para interface gráfica e `pygame` para reproduzir sons. As notificações podem ser personalizadas com texto, ícones, sons e ações específicas ao clique do usuário.

## Instalação

### Requisitos

Para usar este sistema de notificações, você precisa ter o Python instalado na sua máquina. Além disso, as seguintes bibliotecas devem ser instaladas:

- `pygame` – para reproduzir sons.
- `Pillow` – para manipulação de imagens.
- `tkinter` – biblioteca gráfica para a interface (já incluída no Python, mas pode precisar de instalação separada em algumas distribuições).

### Passos para Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install pygame pillow
   ```

3. Agora você pode executar o script para usar o sistema de notificações. 

## Como Usar

O sistema de notificações é encapsulado na função `notifica()`. Aqui está como utilizá-la:

### Função `notifica()`

```python
notifica(txt, icon=None, sound=None, fg_rexcolor=None, toplevel=False, tempo=4000, callback=None)
```

#### Parâmetros:

- **`txt`**: (str) O texto que será exibido na notificação. **(Obrigatório)**.
- **`icon`**: (str) Caminho para a imagem do ícone (opcional).
- **`sound`**: (str) Tipo de som a ser tocado. Aceita os valores:
  - `"avaste"`: Som de notificação.
  - `"eroza"`: Som de erro.
  - `"atento"`: Som de alerta.
  - `"info"`: Som de informação.
  - **Caminho para arquivo MP3 personalizado**.
- **`fg_rexcolor`**: (str) Cor de fundo da notificação (em formato hexadecimal, como `#2E2E2E`).
- **`toplevel`**: (bool) Se `True`, cria uma janela `Toplevel`. Caso contrário, cria uma janela principal (`Tk`).
- **`tempo`**: (int) O tempo (em milissegundos) que a notificação ficará visível. O valor deve estar entre 500ms e 4000ms. O valor padrão é 4000ms.
- **`callback`**: (função) Função a ser chamada quando o usuário clicar fora dos primeiros 30px horizontais da notificação.

#### Exemplo de uso:

```python
def minha_acao():
    print("Você clicou na notificação!")

notifica("Mensagem de Teste", tempo=2000, callback=minha_acao)
```

Este exemplo irá exibir uma notificação com o texto `"Mensagem de Teste"` que ficará visível por 2 segundos. Se o usuário clicar fora dos primeiros 30px, a função `minha_acao` será chamada e a mensagem "Você clicou na notificação!" será exibida no terminal.

### Comportamento da Notificação:

1. **Tempo**: A notificação fica visível pelo tempo especificado em milissegundos. O mínimo é 500ms e o máximo é 4000ms.
2. **Fechamento**: Se o usuário clicar nos primeiros 30px horizontais da janela da notificação, ela será fechada automaticamente.
3. **Som**: O som será tocado quando a notificação for exibida, caso o parâmetro `sound` seja especificado.
4. **Imagem**: A notificação pode exibir um ícone, se o caminho para a imagem for fornecido no parâmetro `icon`.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

