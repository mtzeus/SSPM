import psutil
import tkinter as tk

# About #
# Desenvolvido por www.twitter.com/mtz_treze
# Melhorias são bem vindas.

# Configurações do monitor
FONT = ("Arial", 12)
BG_COLOR = "black" # 
FG_COLOR = "green" 
TRANSPARENCY = 0.7  # Valor de 0.0 (totalmente transparente) a 1.0 (totalmente opaco)

class PerformanceMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("SSPM") 
        self.root.geometry("90x60") 
        self.root.overrideredirect(True) #caso adcione # no inicio dessa linha irá adcionar a barra de título
        self.root.attributes("-topmost", True)  # Mantém o monitor no topo de outros aplicativos
        self.root.attributes("-alpha", TRANSPARENCY)  # Define a transparência da janela

        self.cpu_label = tk.Label(root, text="CPU: 0%", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
        self.cpu_label.pack(padx=5, pady=5)

        self.ram_label = tk.Label(root, text="RAM: 0%", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
        self.ram_label.pack(padx=5, pady=5)

        self.update()

    def update(self):
        cpu_percent = self.calculate_cpu_usage()
        ram_percent = self.calculate_ram_usage()

        self.cpu_label.config(text=f"CPU: {cpu_percent}%")
        self.ram_label.config(text=f"RAM: {ram_percent}%")

        self.root.after(1000, self.update)

    def calculate_cpu_usage(self):
        cpu_percent = psutil.cpu_percent()
        return round(cpu_percent, 2)

    def calculate_ram_usage(self):
        ram_percent = psutil.virtual_memory().percent
        return round(ram_percent, 2)

root = tk.Tk()
root.configure(bg=BG_COLOR)

monitor = PerformanceMonitor(root)

root.mainloop()
