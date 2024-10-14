<h1> Descrição</h1>
<ul>
  <li>Automação em python para o envio de receptores no SIGE.</li>
  <li>Está automação pode não funcionar se o sistema sofrer alguma atualização.</li>
  <li>Foi criada unicamente para a seleção dos receptores</li>
  <li>Não mecher no mouse durante a execução do programa pois a biblioteca pyautogui utiliza as coordenadas da tela para a seleção dos elementos da página</li>
</ul>

<code>
# Usar para encontrar a localização do mouse
#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
</code>
