import turtle
import pygame
import threading

# Função para reproduzir a música
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('Music1.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Função para desenhar a flor
def draw_flower():
    tu = turtle.Turtle()
    tu.screen.bgcolor("black")
    tu.pensize(2)
    tu.color("green")
    tu.left(90)
    tu.backward(100)
    tu.speed(900)
    tu.shape("turtle")

    def tree(i):
        if i < 10:
            return
        else:
            tu.forward(i)
            tu.color("white")
            tu.circle(4)
            tu.color("green")
            tu.left(30)
            tree(3 * i / 4)
            tu.right(60)
            tree(3 * i / 4)
            tu.left(30)
            tu.backward(i)

    tree(100)
    pygame.mixer.music.stop()
    turtle.done()

# Executa a reprodução de música e o desenho da flor simultaneamente
music_thread = threading.Thread(target=play_music)
music_thread.start()

draw_flower()