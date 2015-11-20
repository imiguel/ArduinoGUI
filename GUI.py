# -*- coding: utf-8 -*-l
import wx
import Methods
import serial


class mainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="RC Car Controller", size=(700,500))

        #Criar uma barra de menus e sub-menus
        menuBar = wx.MenuBar(0)

        #Sub-menu "Ficheiro"
        fileMenu = wx.Menu()
        btnMenuSair = wx.MenuItem(fileMenu, wx.ID_CLOSE, "Sair") #Botao
        fileMenu.AppendItem(btnMenuSair)
        menuBar.Append(fileMenu, "&Ficheiro")

        #sub-menu "Sobre"
        fileAbout = wx.Menu()
        btnMenuSobre = wx.MenuItem(fileAbout, wx.ID_HELP, "Sobre") #Botao
        fileAbout.AppendItem(btnMenuSobre)
        btnMenuWebsite = wx.MenuItem(fileAbout, wx.ID_HOME, "Pagina oficial") #Botao
        fileAbout.AppendItem(btnMenuWebsite)
        menuBar.Append(fileAbout, "&Sobre")
        
        #Adiciona a barra de menus
        self.SetMenuBar(menuBar)


        #Labels
        self.label = wx.StaticText(self, label="BOTÕES PARA O LED", pos=(5, 80), style=wx.ALIGN_LEFT)
        self.label = wx.StaticText(self, label="BOTÕES PARA O LED VERDE", pos=(500, 80), style=wx.ALIGN_RIGHT)



        ##Coloca os botoes
        buttonOn = wx.Button(self, pos=(20, 100), size=(100,25), id=wx.ID_ANY, label="LED ON")
        buttonOff = wx.Button(self, pos=(20, 130), size=(100,25), id=wx.ID_ANY, label="LED OFF")
        buttonBuzzer = wx.Button(self, pos=(20, 160), size=(100,25), id=wx.ID_ANY, label="BUZZER SUPER MARIO")
        buttonVerdeOn = wx.Button(self, pos=(530, 100), size=(130,25), id=wx.ID_ANY, label="LED GREEN ON")
        buttonVerdeOff = wx.Button(self, pos=(530, 130), size=(130,25), id=wx.ID_ANY, label="LED GREEN OFF")


        ##ESTES 4 botoes ESTAO CERTOS!!!
        '''buttonMoveUP = wx.Button(self, pos=(100, 180), size=(50, 50), id=wx.ID_ANY, label="UP")
        buttonMoveDOWN = wx.Button(self, pos=(100, 230), size=(50, 50), id=wx.ID_ANY, label="DOWN")
        buttonMoveLEFT = wx.Button(self, pos=(50, 230), size=(50, 50), id=wx.ID_ANY, label="LEFT")
        buttonMoveUP = wx.Button(self, pos=(150, 230), size=(50, 50), id=wx.ID_ANY, label="RIGHT") '''


        #adiciona os metodos aos botoes
        self.Bind(wx.EVT_MENU, self.btnMenuSair_onClick, btnMenuSair)
        self.Bind(wx.EVT_MENU, self.btnMenuSobre_onClick, btnMenuSobre)
        self.Bind(wx.EVT_MENU, self.btnMenuWebSite_onClick, btnMenuWebsite)
        buttonOn.Bind(wx.EVT_BUTTON, self.buttonOn_onClick)
        buttonOff.Bind(wx.EVT_BUTTON, self.buttonOff_onClick)
        buttonVerdeOn.Bind(wx.EVT_BUTTON, self.buttonVerdeOn_onClick)
        buttonVerdeOff.Bind(wx.EVT_BUTTON, self.buttonVerdeOff_onClick)
        buttonBuzzer.Bind(wx.EVT_BUTTON, self.buttonBuzzer_onClick)

        #mostra a janela
        self.Show(True)
        
        
        ##Metodos das accoes dos botoes
    def btnMenuSair_onClick(self, event):
        self.Close()

    def btnMenuSobre_onClick(self, event):
        Methods.aboutDialogMessage(self)

    def btnMenuWebSite_onClick(self, event):
        Methods.openWebPageFromGitHub()
        
    def buttonOn_onClick(self, event):
        Methods.testeDoBotaoOn()

    def buttonOff_onClick(self, event):
        Methods.testeDoBotaoOff()

    def buttonVerdeOn_onClick(self, event):
        Methods.testeDoBotaoVerdeOn()

    def buttonVerdeOff_onClick(self, event):
        Methods.testeDoBotaoVerdeOff()

    def buttonBuzzer_onClick(self, event):
        Methods.testeBuzzer()
        
        
        
# MAIN
if __name__ == "__main__":
    app = wx.App()
    frame = mainWindow(None, "RC Car Controller")
    app.MainLoop()
