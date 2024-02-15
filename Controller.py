from tkinter import messagebox
from Model import Model
from View import View
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    def show_error(self, message):
        self.view.show_error_message(message)
    def calculate_button_pressed(self, event=None):
        try:
            base = float(self.view.entry_base.get())
            height = float(self.view.entry_height.get())
            # Kui sisestatakse nii alus kui kõrgus null negatiivsed arvud
            if base <= 0 and height <= 0:
                self.show_error('Kolmnurga alus ja kõrgus peavad olema positiivsed arvud.')
                return
            elif base <= 0:  # Kui alus on null või negatiivne arv
                self.show_error('Kolmnurga alus on vigane. Alus peab olema positiivne arv.')
                return
            elif height <= 0:   # Kui kõrgus on null või negatiivne arv
                self.show_error('Kolmnurga kõrgus vigane. Kõrgus peab olema positiivne arv.')
                return
            hypotenuse, perimeter, area = self.model.calculate_triangle_properties(base, height)
            self.view.display_results(hypotenuse, perimeter, area, base, height)

            # Puhastame sisestusväljad- ringi juhendi peal on ringi raadius eemaldatud, seega peab väljad puhastama
            self.view.entry_base.delete(0, 'end')
            self.view.entry_height.delete(0, 'end')
            # Fokusseerime esimesele sisestusväljale
            self.view.entry_base.focus()
        except ValueError:
            self.show_error('Sisestage palun arvulised väärtused kõikidesse väljadesse.')
    def run(self):
        self.view.mainloop()
    # Küsib üle, kas soovin rakendusest väljuda. Nagu ka tunnis tegime
    def on_close(self):
        if messagebox.askokcancel('Välju Rakendusest', 'Oled kindel, et soovid rakendusest väljuda?'):
            self.view.destroy()