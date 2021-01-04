# -*- coding: utf-8 -*-

import turtle
import random
import time
import os

altura = 1000
largura = 1000
janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("green")
janela.setup(width=largura, height=altura)
janela.tracer(0)

# Cabeça da cobra
ccobra = turtle.Turtle()
ccobra.speed(0)
ccobra.shape("square")
ccobra.color("white")
ccobra.penup()
ccobra.goto(0,0)

# Comida da cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# Corpo da cobra

corpo = []


# Placar
placar1 = 0
recorde = 0
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0,460)
placar.write("Placar: {}  Recorde: {}".format(placar1,recorde), align="center", font=("Courier",24,"normal"))
resposta = 1
velocidade = 0.045

# Funções


def main():
    global resposta, velocidade
    if resposta == 1:
        janela.update()
        x = ccobra.xcor()
        x += 10
        ccobra.setx(x)
    if resposta == 2:
        janela.update()
        x = ccobra.xcor()
        x -= 10
        ccobra.setx(x)
    if resposta == 3:
        janela.update()
        y = ccobra.ycor()
        y += 10
        ccobra.sety(y)
    if resposta == 4:
        janela.update()
        y = ccobra.ycor()
        y -= 10
        ccobra.sety(y)

def direita():
    global resposta
    if resposta != 2:
        resposta = 1
    else:
        resposta = resposta
def esquerda():
    global resposta
    if resposta != 1:
        resposta = 2
    else:
        resposta = resposta
def cima():
    global resposta
    if resposta != 4:
        resposta = 3
    else:
        resposta = resposta
def baixo():
    global resposta
    if resposta != 3:
        resposta = 4
    else:
        resposta = resposta

janela.listen()
janela.onkeypress(direita, "d")
janela.onkeypress(esquerda, "a")
janela.onkeypress(baixo, "s")
janela.onkeypress(cima, "w")
janela.onkeypress(direita, "Right")
janela.onkeypress(esquerda, "Left")
janela.onkeypress(baixo, "Down")
janela.onkeypress(cima, "Up")
# Main game loop

while True:
    janela.update()
    main()
    time.sleep(velocidade)
    if ccobra.xcor() == largura / 2 or ccobra.xcor() == (largura/2)*-1 or ccobra.ycor() == altura/2 or ccobra.ycor() == altura/2*-1:
        os.system("aplay perdeu.wav&")
        for c in corpo:
            c.goto(10001,10001)
        corpo.clear()
        ccobra.goto(0, 0)
        if placar1 > recorde:
            recorde = placar1
            placar1 = 0
            velocidade = 0.03
            placar.clear()
            placar.write("Placar: {}  Recorde: {}".format(placar1, recorde), align="center",
                         font=("Courier", 24, "normal"))
        else:
            placar1 = 0
            velocidade = 0.03
            placar.clear()
            placar.write("Placar: {}  Recorde: {}".format(placar1, recorde), align="center",
                         font=("Courier", 24, "normal"))
        time.sleep(2)
    if ccobra.distance(comida) < 20:
        os.system("aplay som.wav&")
        placar1 += 1
        placar.clear()
        placar.write("Placar: {}  Recorde: {}".format(placar1, recorde), align="center", font=("Courier", 24, "normal"))
        comida.setx(random.randint((largura/2-10)*-1,(largura/2 - 10)))
        comida.sety(random.randint((altura/2-10)*-1,(altura/2-10)))
        if velocidade > 0.0009:
            velocidade -= 0.0009

        # Cria um novo segmento do corpo
        pi = len(corpo) % 2
        if pi == 0:
            segmento = turtle.Turtle()
            segmento.speed(0)
            segmento.shape("circle")
            segmento.color("blue")
            segmento.penup()
            corpo.append(segmento)
        else:
            segmento = turtle.Turtle()
            segmento.speed(0)
            segmento.shape("circle")
            segmento.color("red")
            segmento.penup()
            corpo.append(segmento)
    # Move todos os segmentos menos o primeiro
    for p in range(len(corpo)-1,0,-1):
        x = corpo[p-1].xcor()
        y = corpo[p-1].ycor()
        corpo[p].goto(x,y)
    # Move o primeiro segmento
    if len(corpo) > 0:
        x = ccobra.xcor()
        y = ccobra.ycor()
        corpo[0].goto(x,y)
    for c, n in enumerate(corpo):
        if c > 0:
            if n.distance(ccobra) <10:
                os.system("aplay perdeu.wav&")
                for c in corpo:
                    c.goto(10001, 10001)
                corpo.clear()
                ccobra.goto(0, 0)
                if placar1 > recorde:
                    recorde = placar1
                    placar1 = 0
                    velocidade = 0.03
                    placar.clear()
                    placar.write("Placar: {}  Recorde: {}".format(placar1, recorde), align="center",
                                 font=("Courier", 24, "normal"))
                else:
                    placar1 = 0
                    velocidade = 0.03
                    placar.clear()
                    placar.write("Placar: {}  Recorde: {}".format(placar1, recorde), align="center",
                                 font=("Courier", 24, "normal"))
                time.sleep(2)
janela.mainloop()
