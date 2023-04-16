import PySimpleGUI as sg
import qrcode as qr
import shutil
import os

counter = 0

layout = [
    [sg.Text("Coloque seu LINK", background_color='#FFFFFF', text_color='#000000'), sg.InputText(key="link")],
    [sg.Image(key="qrcode")],
    [sg.Button("Gerar", button_color='#000000'), sg.Button("Sair", button_color='#000000')]
]

current_path = os.getcwd()

qr_path = os.path.join("Códigos")
icon_path = os.path.join(current_path, "qrcode_scan_icon_136286.ico")

janela = sg.Window("Gerador de QRCODE", layout,icon=icon_path , background_color='#FFFFFF')

if not os.path.exists(qr_path):
    os.mkdir(qr_path)

while True:
    evento, valor = janela.read()

    if evento == sg.WIN_CLOSED or evento == "Sair":
        shutil.rmtree(qr_path)
        break

    if evento == "Gerar":
        link=valor["link"]
        codigo=qr.make(link)

        counter += 1

        name = f"code-{counter}.png"
        path = os.path.join(qr_path, name)

        codigo.save(path)
        janela["qrcode"].update(path)