import turtle
import time
import random

# Ekranı ayarla
turtle_ekrani = turtle.Screen()
turtle_ekrani.bgcolor("light blue")
turtle_ekrani.title("Catch the Turtle")

# Kaplumbağayı oluştur
catchTheTurtle = turtle.Turtle()

catchTheTurtle.shape("turtle")
catchTheTurtle.color("green")
catchTheTurtle.shapesize(2, 2)  # Kaplumbağayı biraz büyüt
catchTheTurtle.penup()
catchTheTurtle.hideturtle()

# Skor ve zaman için turtle nesneleri
skor_turtle = turtle.Turtle()
skor_turtle.hideturtle()
skor_turtle.penup()
skor_turtle.goto(0, 260)

zaman_turtle = turtle.Turtle()
zaman_turtle.hideturtle()
zaman_turtle.penup()
zaman_turtle.goto(0, 230)

# Skor ve zaman değişkenleri
skor = 0
zaman = 30  # Geri sayım süresi (saniye)
oyun_devam_ediyor = True  # Oyunun devam edip etmediğini kontrol eder

# Skoru güncelleme fonksiyonu
def skor_guncelle():
    skor_turtle.clear()
    skor_turtle.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

# Zamanı güncelleme fonksiyonu
def zaman_guncelle():
    zaman_turtle.clear()
    zaman_turtle.write(f"Zaman: {zaman}", align="center", font=("Arial", 24, "normal"))

# Kaplumbağayı rastgele bir yere taşıma fonksiyonu
def rastgele_konum():
    if oyun_devam_ediyor:  # Oyun devam ediyorsa hareket et
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        catchTheTurtle.goto(x, y)
        catchTheTurtle.showturtle()
        turtle_ekrani.ontimer(rastgele_konum, 500)  # Her 0.5 saniyede bir hareket et

# Kaplumbağaya tıklandığında skoru artırma fonksiyonu
def tiklama_skor(x, y):
    global skor
    if oyun_devam_ediyor and catchTheTurtle.isvisible():  # Oyun devam ediyorsa ve kaplumbağa görünürse skor artır
        skor += 1
        skor_guncelle()
        catchTheTurtle.hideturtle()

# Geri sayım fonksiyonu
def geri_sayim():
    global zaman, oyun_devam_ediyor
    if zaman > 0:
        zaman -= 1
        zaman_guncelle()
        turtle_ekrani.ontimer(geri_sayim, 1000)  # Her 1 saniyede bir geri say
    else:
        oyun_devam_ediyor = False  # Oyunu durdur
        zaman_turtle.clear()
        zaman_turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
        catchTheTurtle.hideturtle()  # Kaplumbağayı gizle

# Oyunu başlat
skor_guncelle()
zaman_guncelle()
rastgele_konum()
catchTheTurtle.onclick(tiklama_skor)  # Kaplumbağaya tıklandığında skor artır
geri_sayim()

# Oyun ekranını açık tut
turtle.mainloop()