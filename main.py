import turtle
import random #rastgele konum üreterek kaplumbağa'nın konumunu rastgele belirlemek için kullandık

# Ekranı ayarla
turtle_ekrani = turtle.Screen()
turtle_ekrani.bgcolor("light blue")
turtle_ekrani.title("Catch the Turtle")

# Kaplumbağayı oluştur
catchTheTurtle = turtle.Turtle()#Nesne

catchTheTurtle.shape("turtle")
catchTheTurtle.color("green")
catchTheTurtle.shapesize(2, 2)  # Kaplumbağayı biraz büyüt
catchTheTurtle.penup() #kaplumbağa hareket ederken çizim yapmıyor bu sayede
catchTheTurtle.hideturtle() #Başlangıçta hideturtle() ile ekranda görünmüyor.

# Skor ve zaman için turtle nesneleri
skor_turtle = turtle.Turtle()#Nesne
skor_turtle.hideturtle()
skor_turtle.penup()
skor_turtle.goto(0, 260)

zaman_turtle = turtle.Turtle()#Nesne
zaman_turtle.hideturtle()
zaman_turtle.penup()
zaman_turtle.goto(0, 230)

# Yeniden başlatma butonu
restart_arrow = turtle.Turtle()
restart_arrow.hideturtle()
restart_arrow.penup()
restart_arrow.shape("arrow")
restart_arrow.color("red")
restart_arrow.shapesize(3, 3)
restart_arrow.goto(0, 0)

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
        catchTheTurtle.showturtle()#kaplumbağayı görünür hale getir
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
        restart_arrow.showturtle()  # Oku göster
        rotate_arrow()  # Döndürmeyi başlat


# Ok döndürme
def rotate_arrow():
    if not oyun_devam_ediyor:
        restart_arrow.right(10)
        turtle_ekrani.ontimer(rotate_arrow, 100)


# Oyunu sıfırla
def reset_game(x, y):
    global skor, zaman, oyun_devam_ediyor
    if not oyun_devam_ediyor:
        # Değişkenleri sıfırla
        skor = 0
        zaman = 30
        oyun_devam_ediyor = True

        # Görsel elemanları güncelle
        restart_arrow.hideturtle()
        zaman_turtle.clear()
        skor_guncelle()
        zaman_guncelle()

        # Oyun mekaniklerini yeniden başlat
        catchTheTurtle.onclick(tiklama_skor)
        rastgele_konum()
        geri_sayim()

# Oyunu başlat
skor_guncelle()
zaman_guncelle()
rastgele_konum()
catchTheTurtle.onclick(tiklama_skor)  # Kaplumbağaya tıklandığında skor artır
restart_arrow.onclick(reset_game)  # Ok tıklamasını bağla
geri_sayim()

# Oyun ekranını açık tut
turtle.mainloop()