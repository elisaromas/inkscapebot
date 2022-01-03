# Script para gerar um arquivo PDF de cada página de um Ebook (PDF).


#inportando a biblioteca pyautogui para leitura de tela, screenshot e pixels
import pyautogui  
#inportando a biblioteca time para usar sleep após um clique no alvo
import time  
#inportando a biblioteca keyboard para verificar qual tecla está apertada para parar o loop
import keyboard  
#inportando api do windows para realizar click de forma mais rápida e eficaz.
#import win32api ,win32con  #pip install pypiwin32

pag = 1 # variável
#começar da primeira página

#pyautogui.PAUSE = 2   #a cada 2 segundos executa o comando
#while True:
while keyboard.is_pressed('c')==False:  # Aperte a Tecla 'c' para parar a execução do script

#    pyautogui.alert ('O código está sendo executado. Não mexa no Computdor!') # Exibe caixa de alerta ao executar o script
    pyautogui.PAUSE = 0.5  # pausa de meio segundo a cada ação (comando)
        #Abrir inkscape
    pyautogui.press ('winleft') # pressione a tecla do windows 'winleft'
    pyautogui.write ('inkscape')  # escreva 'inkscape'
    pyautogui.press ('enter')  # pressione a tecla 'enter'
    time.sleep (20) # espere 20 segundos
        #Abrir Documento
    pyautogui.moveTo (x=40, y=58)  # mouse é movido para a coordenada correspondente
    pyautogui.click (x=40, y=58)  # click do mouse no botão do menu para Abrir Documento
    time.sleep (4) # espere 4 segundos
        #Clicar no arquivo pra abrir
    pyautogui.moveTo (x=365, y=149)  # mouse é movido para a coordenada correspondente
    pyautogui.doubleClick (365,149) # click do mouse no arquivo do Ebook pra abrir
    time.sleep (2) # espere 2 segundos
        #Configuração de importação de PDF
    pyautogui.moveTo (x=516, y=262) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=516, y=262) # click do mouse em 'Importacao Poppler/Cairo'
    time.sleep (2) # espere 2 segundos
        #Selecionar pagina
    pyautogui.moveTo (x=640, y=173) # mouse é movido para a coordenada correspondente
    pyautogui.doubleClick (x=640, y=173) # click do mouse em Selecionar a pagina
    
    pyautogui.write (str(pag)) # escrevendo o número da página do ebook. (a cada loop do script é ecrito o número da pagina correspondente do PDF, sendo que o pdf tem 545 paginas)
    #agora a pagina a ser acessada está em função da variável pag
    
    time.sleep (10) # espere 10 segundos
        #Clicar em OK
    pyautogui.moveTo (x=1021, y=591) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=1021, y=591)  # click the mouse em 'Ok'
    time.sleep (7) # espere 7 segundos
        #Clicar no menu em Arquivo
    pyautogui.moveTo (x=26, y=35) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=26, y=35)  # click do mouse no menu em Arquivo
    time.sleep (3) # espere 3 segundos
        #Clicar em SalvarComo
    pyautogui.moveTo (x=80, y=200) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=80, y=200)  # click do mouse em SalvarComo 
    time.sleep (3) # espere 3 segundos
        #Abrir a pasta ichingPaginasParaEditar
    pyautogui.moveTo (x=283, y=146) # mouse é movido para a coordenada correspondente
    pyautogui.doubleClick (x=283, y=146)   # click do mouse na pasta 'ichingPaginasParaEditar'
    time.sleep (3) # espere 3 segundos
        #Clicar em Tipo *de arquivo*
    pyautogui.moveTo (x=317, y=612) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=317, y=612)   # click do mouse em Tipo *de arquivo* 
    time.sleep (3) # espere 3 segundos
        #Clicar em *PDF*
    pyautogui.moveTo (x=296, y=542) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=296, y=542) # click do mouse na guia do 'Formato de Documento Portatil' (PDF) 
    time.sleep (3) # espere 3 segundos
        #Renomear o arquivo *PDF
    pyautogui.moveTo (x=291, y=583) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=291, y=583) # click do mouse no campo para digitar o nome do arquivo
    time.sleep (3) # espere 3 segundos
    
    pyautogui.write (str(pag)) # escrevendo nome do arquivo (cada nome deverá ter como nome o número da pagina correspondente do PDF, sendo que o pdf tem 545 paginas)
    #agora a pagina a ser acessada está em função da variável pag
    
    time.sleep (3) # espere 3 segundos
        #Salvar
    pyautogui.moveTo (x=1240, y=586) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=1240, y=586) # click do mouse no botão Salvar 
    time.sleep (4) # espere 4 segundos
        #Formato de Documento Portátil
    pyautogui.click('BTNOK.png') # Print do botão 'Ok' para ser clicado pelo pyautogui
    time.sleep (3) # espere 3 segundos
        #Fechar o inkscape
    pyautogui.moveTo (x=1338, y=8) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=1338, y=8) # click do mouse no botão de fechar no canto superior direito 
        #Fechar sem Salvar
    pyautogui.moveTo (x=510, y=422) # mouse é movido para a coordenada correspondente
    pyautogui.click (x=510, y=422) # click do mouse na janela em Fechar sem Salvar
    
    pag += 1 # incrementa pag para que na próxima iteração o bot acesse a página seguinte
    if pag == 546: #se pag for maior que o numero de paginas do ebook (545), então o laço while é finalizado
      break
    
    
        #Observação o inkscape é fechado sem salvar o arquivo porque o propósito é apenas gerar um aquivo '.pdf' de cada página para uma outra edição automática posterior em outro bot.
        #após a finalização de todas as páginas, outro bot irá editar cada página, e fazer o tratamento de design, usando diversos programas de editoração em sequencias e ordens.
        #programas de editoração: gimp, scribus.
        
