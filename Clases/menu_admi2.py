from tkinter import *
from ventana import *


def main():
 root = Tk()
 root.wm_title('Menu')
 app = Ventana(root) #objeto de la clase ventana, su parametro es root su frame principal
 app.mainloop()

if __name__ == '__main__':
  main()