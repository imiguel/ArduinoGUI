# -*- coding: utf-8 -*-
import wx
import webbrowser
import serial


#apagar esta linha quando tiver o sensor bluetooth
#serialPort = "/dev/cu.wchusbserial620"
#serialPort2 = "/dev/ttyusb0"

connectToArduino = serial.Serial("/dev/ttyUSB1", 9600)


#Mostra a janela quando se clica no "Sobre"
def aboutDialogMessage(self):
    dialog = wx.MessageDialog(self, "Programa para controlar RC Car\n \n"
                                    "Desenvolvido por: Miguel Rosa\n \n \n \n"
                                    "Todos os direitos reservados\n \n"
                                    "Mértola 2016",
                                    "RC Car Controller - Sobre", wx.OK)
    dialog.ShowModal()#Mostra a caixa de dialogo
    dialog.Destroy() #destroi a caixa de dialogo



#Abre a pagina do projecto no github
def openWebPageFromGitHub():
    #linkToPage = "https://github.com/imiguel/Arduino_RC_Car/wiki"
    linkToPage = "https://imiguel.github.io/Arduino_RC_Car"
    webbrowser.open_new(linkToPage)
    
    
#desligar o LED
def testeDoBotaoOn():
    print "BOTAO LED VERMELHO LIGADO"
    connectToArduino.write('30')


def testeDoBotaoOff():
    print "BOTAO LED VERMELHO DESLIGADO"
    connectToArduino.write('31')


def testeDoBotaoVerdeOn():
    print "BOTAO LED VERDE LIGADO"
    connectToArduino.write('32')


def testeDoBotaoVerdeOff():
    print "BOTAO LED VERDE DESLIGADO"
    connectToArduino.write('33')

def testeBuzzer():
    print "BUZZER PRESSIONADO"
    connectToArduino.write('34')
