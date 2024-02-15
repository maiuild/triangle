from tkinter import *
from tkinter import messagebox
import tkinter.font as font
class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Täisnurkse kolmnurga kalkulaator GUI')

        # Vidinate kirjastiil
        self.default_font = font.Font(family='Verdana', size=12)

        # Loome kaks frame't
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # Vidinate loomine
        (self.entry_base, self.entry_height, self.btn_calculate, self.text_box) = self.create_frame_widgets()

        self.bind('<Return>', self.controller.calculate_button_pressed)  # Enter klahvi vajutus aktiveerib Arvuta nupu
        self.bind('<Escape>', self.on_close)  # Esc nupu vajutusel alustab väljumist
        self.protocol('WM_DELETE_WINDOW', self.on_close)

        # Aseta aken ekraani keskele
        self.center_window()
    def center_window(self):
        self.update_idletasks()
        width = 580
        height = 280
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    def create_top_frame(self):
        frame = Frame(self, bg='blanchedalmond', height=15)     # Ülesande pildil oli vastava värv- blanchedalmond
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='blanchedalmond')    # Ülesande pildil oli vastava värv- blanchedalmond
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self):
        # Sisestusväljad

        lbl_info = Label(self.top_frame, text='Kolmnurga alus', bg='blanchedalmond', font=self.default_font)
        lbl_info.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        lbl_info2 = Label(self.top_frame, text='Kolmnurga kõrgus', bg='blanchedalmond', font=self.default_font)
        lbl_info2.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        entry_base = Entry(self.top_frame, font=self.default_font)
        entry_base.grid(row=0, column=1, padx=5, pady=5)

        entry_height = Entry(self.top_frame, font=self.default_font)
        entry_height.grid(row=1, column=1, padx=5, pady=5)

        # Arvutusnupp
        btn_calculate = Button(self.top_frame, text='    Arvuta     ', font=('Verdana', 12),
                               command=self.controller.calculate_button_pressed)
        btn_calculate.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky='ew')

        # Tektikast vastuste väljastamiseks.
        text_box = Text(self.bottom_frame, font=self.default_font)
        text_box.pack(expand=True, fill=BOTH, padx=10, pady=10)

        return entry_base, entry_height, btn_calculate, text_box
    def display_results(self, hypotenuse, perimeter, area, base, height):
        # Tulemused, mida on vaja tekstikasti lisada
        results_text = f'Alus: {base:.1f}\n'
        results_text += f'Kõrgus: {height:.1f}\n'
        results_text += f'Hüpotenuus: {hypotenuse:.1f}\n'
        results_text += f'Ümbermõõt: {perimeter:.1f}\n'
        results_text += f'Pindala: {area:.1f}\n'

        self.text_box.config(state='normal')  # Tekstikasti saab kirjutada
        self.text_box.delete('1.0', END)    # Kustutab eelneva teksti
        self.text_box.insert('insert', results_text + '\n')     # Lisab uued arvutatud väärtused
        self.text_box.config(state='disabled')  # Lukustab tekstikasti,  kasutaja ei saaks ise kasti kirjutada

    def on_close(self, event=None):
        # Kui akent üritatakse sulgeda
        if messagebox.askokcancel('Välju rakendusest', 'Kas soovid tõesti rakendusest väljuda?'):
            self.destroy()
    def show_error_message(self, message):
        messagebox.showerror('Viga', message)

