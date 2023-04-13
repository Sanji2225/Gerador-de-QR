import PySimpleGUI as sg
import qrcode as qr
import os
import shutil
layout = [

    [sg.Text("Coloque seu LINK", background_color='#FFFFFF', text_color='#000000'), sg.InputText(key="link")],
    [sg.Image(key="qrcode")],
    [sg.Button("Gerar", button_color='#000000'),sg.Button("Novo", button_color='#000000'), sg.Button("Sair", button_color='#000000')]
]

janela = sg.Window("Gerador de QRCODE", layout,icon=r"C:\Users\PPGL\Pictures\Camera Roll\Gerador de QR\qrcode_scan_icon_136286.ico" , background_color='#FFFFFF')
directory = "qrcode"
parent_dir = r"C:\Users\Public\Documents"
path = os.path.join(parent_dir, directory)  
os.mkdir(path) 
while True:
    evento, valor = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Sair":
        shutil.rmtree(r"C:\Users\Public\Documents\qrcode")
        break
    if evento == "Gerar":
        link=valor["link"]
        codigo=qr.make(link)
        codigo.save(r"C:\Users\Public\Documents\qrcode\qrcode.png")
        janela["qrcode"].update(r"C:\Users\Public\Documents\qrcode\qrcode.png")
    if evento=="Novo":
        if os.path.exists(r"C:\Users\Public\Documents\qrcode\qrcode.png"):
            shutil.copy(r'C:\Users\Public\Documents\qrcode\qrcode.png', r"C:\Users\Public\Pictures", "qrcode1.png")
            os.remove(r"C:\Users\Public\Documents\qrcode\qrcode.png")
        janela["qrcode"].update()
        if evento == "Gerar":
            link=valor["link"]
            codigo=qr.make("link")
            codigo.save(r"C:\Users\Public\Documents\qrcode\qrcode.png")
            janela["qrcode"].update(r"C:\Users\Public\Documents\qrcode\qrcode.png")