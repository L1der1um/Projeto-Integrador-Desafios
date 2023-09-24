import tkinter as tk
import qrcode
from PIL import ImageTk

# Função para criar e exibir o código QR
def show_qr_code():
    url = "https://github.com/L1der1um/Projeto-Integrador-Desafios"
    qr = qrcode.QRCode(box_size=5,border=5)
    qr.add_data(url)
    img = qr.make_image(fill_color="black", back_color="white")

    # Exibir a imagem em uma janela tkinter
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.photo = img
    label.pack()

# Configuração da janela tkinter
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x300")

# Botão para criar e exibir o código QR
generate_button = tk.Button(root, text="Gerar QR Code", command=show_qr_code)
generate_button.pack()

root.mainloop()
