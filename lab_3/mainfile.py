import tkinter as tk  # так быстрее писать
from PIL import Image, ImageTk
import pygame

from lab_3.task import Button_task


#
def Click():
    Button_task(inputp, outputp)


Wait = 6000
window = tk.Tk()  # главное окно
window.title('Key_generat0r')
window.geometry("800x680")
#
# Тут музыка
pygame.mixer.init()  # Запуск mixer
pygame.mixer.music.load("musiclab.mp3")  # загрузка файла
pygame.mixer.music.set_volume(0.5)  # Громкость
pygame.mixer.music.play(-1)  # Зацикливание
#
# А тут фон
img1 = Image.open('background1.jpg')
img2 = Image.open('background3.jpg')
img3 = Image.open('background4.jpg')
images = [img1, img2, img3]
Current_img = 0
img = images[Current_img]
resized_img = img.resize((800, 680))  # задаем нужный размер
tk_img = ImageTk.PhotoImage(resized_img)  # для tkinter
img_back = tk.Label(window, image=tk_img)
img_back.place(x=0, y=0)


#
# Меняем фон
def Change_bg():
    global Current_img, tk_img
    Current_img = (Current_img + 1) % 3
    img = images[Current_img]
    resized_img = img.resize((800, 680))
    tk_img = ImageTk.PhotoImage(resized_img)
    img_back.config(image=tk_img)  # обновляем существующий фон
    window.after(Wait, Change_bg)  # перезапускаем таймер


#
#
inputp = tk.Entry(window, font=("Arial", 14), width=40)
inputp.place(x=50, y=100)  # Координаты окна ввода
#
generate_button = tk.Button(window, text="Generate", font=("Arial", 12), command=Click)
generate_button.place(x=500, y=100)
#
outputp = tk.Label(
    window, text="Key_generation", font=("Arial", 16)
)
outputp.place(x=50, y=250)
#
window.after(Wait, Change_bg)
window.mainloop()
