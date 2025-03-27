import tkinter as tk
from tkinter import messagebox
import random
from hangman_wortliste import wortList

class HangmanGame:
    
    def createGridBackground(self):
        """Kareli defter görünümü için yatay ve dikey çizgiler oluşturur."""
        spacing = 20  # Kareler arası mesafe
        # Yatay çizgiler
        for i in range(0, 1000, spacing):
            self.hangman_canvas.create_line(0, i, 1000, i, fill="lightgrey")
        # Dikey çizgiler
        for i in range(0, 1000, spacing):
            self.hangman_canvas.create_line(i, 0, i, 1000, fill="lightgrey")

    def createDisplayLabel(self):
        self.label_display = tk.Label(width=200, height=50)

    def __init__(self, root, wortList, lives, difficulty="medium"):
        self.root = root
        self.lives = lives
        self.difficulty = difficulty
        self.gesamtLebens = lives
        self.wort = random.choice(wortList)  # Rastgele bir kelime seçiliyor
        
        self.richtigerBuchstabe = []  # Doğru tahmin edilen harfler burada tutulacak
        self.gameOver = False  # Oyun bitti mi kontrolü için bir bayrak
        self.hints_used = 0  # Kullanılan ipucu sayısı

        self.label_lives = tk.Label(root, text=f"{self.lives} von {self.gesamtLebens} Leben übrig", font=("Cascadia Code", 14), fg="red")
        self.label_lives.pack(side=tk.TOP)  # Can göstergesi sabit bir yerde kalsın

        # Kareli defter arka planı
        self.hangman_canvas = tk.Canvas(root, width=600, height=600)
        self.hangman_canvas.pack()

        # Kareli defter çizgileri
        self.createGridBackground()

        # Kelimeyi ekranda göstermek için boşluklar oluşturuluyor
        self.display = ["_"] * len(self.wort)
        self.createDisplayLabel()
        
        # GUI elemanları
        self.label_wort = tk.Label(root, text=" ".join(self.display), font=("Cascadia Code", 24))
        self.label_wort.pack()

        self.sv_eingabe = tk.StringVar()
        self.sv_eingabe.trace_add("write", self.rateBuchstabe)
        self.entry_raten = tk.Entry(root, font=("Cascadia Code", 14), textvariable=self.sv_eingabe)
        self.entry_raten.pack()

        self.button_raten = tk.Button(root, text="Geben Sie bitte einen Buchstaben ein", command=self.rateBuchstabe)
        self.button_raten.pack()

        self.buchstaben = tk.Frame(root)
        self.buchstaben.pack()

        self.button_hint = tk.Button(root, text="Hinweis", command=self.useHint)
        self.button_hint.pack()

        # Harfleri gösteren etiketler
        self.letter_labels = {}
        self.createLetterLabels(root)

        self.updateHangmanCanvas()
  
    # Harf tahmin etme ve Canvas'ı güncelleme
    def rateBuchstabe(self, name, index, mode):

        erraten = self.entry_raten.get().lower()
        self.entry_raten.delete(0, tk.END)  # Giriş kutusunu temizle

        if len(erraten) != 1 or not erraten.isalpha():
            messagebox.showwarning("Ungültige Eingabe!", "Geben Sie bitte einen einzelnen Buchstaben ein.")
            return  # Geçersiz girdi
        if erraten in self.richtigerBuchstabe:
            messagebox.showinfo("Wiederholung!", f"Sie haben schon '{erraten}' eingegeben.")
            return  # Tekrar edilen harf

        self.richtigerBuchstabe.append(erraten)  # Harf doğru tahminler listesine ekleniyor

        if erraten in self.wort:
            self.updateDisplay(erraten)
        else:
            self.verlierLeben()

        # Kullanılan harfi güncelle
        self.updateLetterLabel(erraten)

        # Oyun kazanıldı mı kontrol edilir
        if self.istSpielGewonnen():
            self.gameOver = True
            messagebox.showinfo("Gewonnen :)", "Herzlichen Glückwunsch! Du hast das Wort erraten!")
            self.askReplay()
        elif self.istSpielVerloren():
            self.gameOver = True
            messagebox.showinfo("Verloren :(", f"Der richtige Wort war: '{self.wort}'")
            self.askReplay()

        self.updateHangmanCanvas()

    # Ekrandaki boşlukları günceller
    def updateDisplay(self, erraten):
        for position, buchstabe in enumerate(self.wort):
            if buchstabe == erraten:
                self.display[position] = buchstabe  # Doğru harfler yerleştiriliyor
        self.label_wort.config(text=" ".join(self.display))
        

    # Oyun kazanıldı mı kontrol eder
    def istSpielGewonnen(self):
        return "_" not in self.display

    # Oyun kaybedildi mi kontrol eder
    def istSpielVerloren(self):
        return self.lives == 0

    # Kullanıcının bir hayat kaybetmesini sağlar
    def verlierLeben(self):
        self.lives -= 1
        self.label_lives.config(text=f"{self.lives} von {self.gesamtLebens} Leben übrig")

    # def resetGesamtLeben(self):
    #     return self.

    # Oyunu sıfırlar ve yeniden başlatır
    def resetGame(self):
        
        self.wort = random.choice(wortList)
        self.display = ["_"] * len(self.wort)
        self.richtigerBuchstabe.clear()
        self.gameOver = False
        self.hints_used = 0
        self.label_wort.config(text=" ".join(self.display))
        self.resetLetterLabels()
        self.updateHangmanCanvas()
        

       # self.label_lives.config(text=f"{self.lives} von {self.gesamtLebens} Leben übrig")

        # Zorluk seviyesini tekrar seçme
        self.selectDifficulty()

    # Yeniden oynama isteği sorar
    def askReplay(self):
        antwort = messagebox.askyesno("Spiel beenden", "Möchten Sie nochmal spielen?")
        if antwort:
            self.resetGame()  # Oyunu sıfırla ve yeniden başlat
        else:
            self.root.quit()  # Oyunu sonlandır

    # Hangman aşamalarını GUI ile çizme
    def updateHangmanCanvas(self):
        self.hangman_canvas.delete("all")
        self.createGridBackground()  # Kareli defter arka planını tekrar çiz
        if self.difficulty == "einfach":
            if self.lives <= 4:
                self.hangman_canvas.create_oval(190,115,195,120,fill="black")   # sag göz
            
            if self.lives <= 3:
                self.hangman_canvas.create_oval(210,115,215,120, fill="black")  # sol göz
            
            if self.lives <= 2:
                self.hangman_canvas.create_arc(185, 130, 215, 150, start=0, extent=180, style=tk.ARC, width=2)  # agiz
            
            if self.lives <= 1:
                self.hangman_canvas.create_oval(195, 120, 205, 130, fill="red")  # Sol kulak
            
        # if self.lives <= 12:
                #self.hangman_canvas.create_oval(170, 120, 180, 130, fill="pink")  # Sol kulak

            #if self.lives <=11:
                #self.hangman_canvas.create_oval(220, 120, 230, 130, fill="pink")    # Sag kulak

            if self.lives <= 14:
                self.hangman_canvas.create_line(50, 350, 300, 350, width=2)  # Zemin
        
            if self.lives < 13:
                self.hangman_canvas.create_line(100, 350, 100, 50, width=2)  # Direk
            
            if self.lives <= 12:
                self.hangman_canvas.create_line(100, 50, 200, 50, width=2)  # Askı kolu
            
            if self.lives <= 11:
                self.hangman_canvas.create_line(200, 50, 200, 100, width=2)  # İp
        
            if self.lives <= 10:
                self.hangman_canvas.create_oval(175, 100, 225, 150, width=2)  # Kafa
        
            if self.lives <= 9:
                self.hangman_canvas.create_line(200, 150, 200, 250, width=2)  # Vücut
            
            if self.lives <= 8:
                self.hangman_canvas.create_line(200, 180, 170, 220, width=2)  # Sol kol
            
            if self.lives <= 7:
                self.hangman_canvas.create_line(200, 180, 230, 220, width=2)  # Sağ kol
            
            if self.lives <= 6:
                self.hangman_canvas.create_line(200, 250, 170, 300, width=2)  # Sol bacak
            
            if self.lives <= 5:
                self.hangman_canvas.create_line(200, 250, 230, 300, width=2)  # Sağ bacak
            
        elif self.difficulty == "mittel" or "schwer":
            if self.lives <= 10:
                self.hangman_canvas.create_line(50, 350, 300, 350, width=2)  # Zemin
        
            if self.lives < 9:
                self.hangman_canvas.create_line(100, 350, 100, 50, width=2)  # Direk
            
            if self.lives <= 8:
                self.hangman_canvas.create_line(100, 50, 200, 50, width=2)  # Askı kolu
            
            if self.lives <= 7:
                self.hangman_canvas.create_line(200, 50, 200, 100, width=2)  # İp
        
            if self.lives <= 6:
                self.hangman_canvas.create_oval(175, 100, 225, 150, width=2)  # Kafa
        
            if self.lives <= 5:
                self.hangman_canvas.create_line(200, 150, 200, 250, width=2)  # Vücut
            
            if self.lives <= 4:
                self.hangman_canvas.create_line(200, 180, 170, 220, width=2)  # Sol kol
            
            if self.lives <= 3:
                self.hangman_canvas.create_line(200, 180, 230, 220, width=2)  # Sağ kol
            
            if self.lives <= 2:
                self.hangman_canvas.create_line(200, 250, 170, 300, width=2)  # Sol bacak
            
            if self.lives <= 1:
                self.hangman_canvas.create_line(200, 250, 230, 300, width=2)  # Sağ bacak
        

        self.label_lives.config(text=f"{self.lives} von {self.gesamtLebens} Leben übrig")

    # İpucu kullanma fonksiyonu
    def useHint(self):
        if self.hints_used < 3:  # Maksimum 3 ipucu
            for buchstabe in self.wort:
                if buchstabe not in self.richtigerBuchstabe:
                    self.updateDisplay(buchstabe)
                    self.richtigerBuchstabe.append(buchstabe)
                    self.letter_labels[buchstabe].config(fg="green")
                    self.hints_used += 1
                    break
        else:
            messagebox.showinfo("!", "Max Hinweis!")

    # Harf etiketlerini oluşturma
    def createLetterLabels(self, root):
        """Alfabenin harflerini gösteren etiketleri oluşturur."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i, letter in enumerate(alphabet):
            label = tk.Label(self.buchstaben, text=letter, font=("Cascadia Code", 14))
            label.grid(row=i // 13, column=i % 13)
            self.letter_labels[letter] = label
 
    # Kullanılan harfi güncelleme
    def updateLetterLabel(self, letter):
        """Girilen harfin rengini değiştirir."""
        if letter in self.wort:
            self.letter_labels[letter].config(fg="green")  # Doğru tahmin yeşil
        else:
            self.letter_labels[letter].config(fg="red")  # Yanlis tahmin
    # Harf etiketlerini sıfırlama
    def resetLetterLabels(self):
        for label in self.letter_labels.values():
            label.config(fg="black")

    # Zorluk seviyesini seçme
    def selectDifficulty(self):
        difficulty_window = tk.Toplevel(self.root)
        difficulty_window.title("Spiel Modus")
        tk.Label(difficulty_window, text="Spiel Modus auswählen:", font=("Cascadia Code", 14)).pack()
        difficulty = tk.StringVar(value=self.difficulty)
        tk.Radiobutton(difficulty_window, text="einfach", variable=difficulty, value="einfach", font=("Cascadia Code", 12)).pack()
        tk.Radiobutton(difficulty_window, text="Mittle", variable=difficulty, value="mittle", font=("Cascadia Code", 12)).pack()
        tk.Radiobutton(difficulty_window, text="Schwer", variable=difficulty, value="schwer", font=("Cascadia Code", 12)).pack()

        def set_difficulty():
            self.difficulty = difficulty.get()
            if self.difficulty == "einfach":
                self.lives = 15
                self.gesamtLebens = 15
            elif self.difficulty == "schwer":
                self.lives = 5
                self.gesamtLebens = 5
            else:
                self.lives = 10
                self.gesamtLebens = 10
            self.label_lives.config(text=f"{self.lives} von {self.gesamtLebens} Leben übrig")
            difficulty_window.destroy()

        tk.Button(difficulty_window, text="Okay", command=set_difficulty, font=("Cascadia Code", 14)).pack()

def start_game():
    global root
    root = tk.Tk()
    root.title("Hangman Spiel")
    root.minsize(400, 600)
    root.maxsize(1200, 1200)
   
    # # Zorluk seviyesi seçimi
    difficulty = tk.StringVar(value="mittle")
    wahl_btn = tk.Button(root, text="Wählen Sie einen Schwierigkeitsgrad aus ", font=("Cascadia Code", 14))
    wahl_btn.pack()
    einfach_btn = tk.Radiobutton(root, text="Einfach", variable=difficulty, value="einfach", font=("Cascadia Code", 12))
    einfach_btn.pack()
    mittle_btn = tk.Radiobutton(root, text="Mittle", variable=difficulty, value="mittle", font=("Cascadia Code", 12))
    mittle_btn.pack()
    schwer_btn = tk.Radiobutton(root, text="Schwer", variable=difficulty, value="schwer", font=("Cascadia Code", 12))
    schwer_btn.pack()
    
    
    def start_hangman():
        
        if difficulty.get() == "einfach":
            lives = 15
        elif difficulty.get() == "schwer":
            lives = 5
        else:
            lives = 10
        game = HangmanGame(root, wortList, lives=lives, difficulty=difficulty.get())
        start_button.pack_forget() # Başlat butonunu gizle
        wahl_btn.pack_forget()
        einfach_btn.pack_forget()
        mittle_btn.pack_forget()
        schwer_btn.pack_forget()
        
    start_button = tk.Button(root, text="START", command=start_hangman, font=("Cascadia Code", 14))
    start_button.pack()


   


    root.mainloop()

start_game()
