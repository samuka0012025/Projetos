import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.frame = ctk.CTkFrame(self, width=300, height=50, fg_color="#116", bg_color="#116")
        self.frame.pack()
        self.lb_title = ctk.CTkLabel(self.frame, text="Calculadora", font=('Roboto bold', 24), text_color="#fff")
        self.lb_title.place(x=80, y=10)

        self.span = ctk.CTkLabel(self, text="Esta é uma simples calculadora Baseado no Eval, \nnão utilize para produção, apenas na aprendizagem")
        self.span.pack( pady=6)

        self.entry = ctk.CTkEntry(self, width=250, font=('Roboto bold', 18))
        self.entry.pack(pady=20)

        self.result = ctk.CTkLabel(self, text="", text_color="teal", font=("Roboto bold", 20))
        self.result.pack()

        self.btn = ctk.CTkButton(self, width=250, text="Calcular".upper(), command=self.calcular)
        self.btn.pack(pady=20)
    
    def calcular(self):
        self.result.configure(text=str(eval(self.entry.get())))

app = App()
app.geometry("300x300")
app.title("Calculadora Simples")
app.resizable(False, False)
app.mainloop()
