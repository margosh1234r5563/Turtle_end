import math
import turtle as t

t.setup(600, 600)
t.pencolor("white")
t.pensize(1)


# square
def sqr(x, y, a):
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)


# triangle with two equal sides
def trng(x, y, d):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(135)
    t.forward(math.sqrt(d ** 2 + d ** 2))


# triangle with 90-degree angle
def trng_90(x, y, s):
    d = math.sqrt(2 * s * s)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(s)
    t.right(135)
    t.forward(d)
    t.right(135)
    t.forward(s)


# parallelogram
def prlm(x, y, m):
    e = math.sqrt(2 * m * m)
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(m)
    t.right(45)
    t.forward(e)
    t.right(135)
    t.forward(m)
    t.right(45)
    t.forward(e)
    t.right(135)


# rabbit
def rabbit():
    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng_90(-265, 205, 45)
    t.end_fill()

    t.right(270)
    t.fillcolor("#F72A49")
    t.begin_fill()
    trng_90(-220, 210, 45)
    t.end_fill()

    t.right(90)
    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng_90(-230, 160, 30)
    t.end_fill()

    t.left(180)
    t.fillcolor("#A050E3")
    t.begin_fill()
    trng_90(-225, 160, 23)
    t.end_fill()

    t.left(270)
    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(-215, 240, 23)
    t.end_fill()

    t.left(270)
    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(-245, 285, 20)
    t.end_fill()

    t.left(225)
    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng_90(-200, 205, 23)
    t.end_fill()
    t.left(45)


# fish
def fish():
    t.right(135)
    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng_90(75, 225, 40)
    t.end_fill()
    t.right(45)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng_90(41, 285, 55)
    t.end_fill()
    t.right(180)
    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng_90(41, 170, 55)
    t.end_fill()
    t.right(45)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(35, 228, 35)
    t.end_fill()
    t.right(45)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(-20, 228, 30)
    t.end_fill()
    t.right(180)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng_90(-45, 223, 25)
    t.end_fill()
    t.right(270)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng_90(-50, 198, 25)
    t.end_fill()
    t.left(90)


# chicken
def chckn():
    t.right(45)
    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng_90(255, 275, 27)
    t.end_fill()
    t.right(45)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(240, 255, 25)
    t.end_fill()

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng_90(210, 225, 55)
    t.end_fill()
    t.right(180)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng_90(205, 255, 55)
    t.end_fill()
    t.right(45)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(145, 255, 30)
    t.end_fill()

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng_90(176, 285, 40)
    t.end_fill()

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng_90(235, 190, 25)
    t.end_fill()
    t.right(135)


# right man
def rght_man():
    t.left(135)
    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(225, 70, 31)
    t.end_fill()
    t.right(135)

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng_90(225, 65, 55)
    t.end_fill()
    t.right(180)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng_90(220, 65, 55)
    t.end_fill()
    t.right(90)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng_90(280, -35, 25)
    t.end_fill()
    t.right(270)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng_90(225, -30, 35)
    t.end_fill()
    t.right(90)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(190, -55, 30)
    t.end_fill()
    t.right(270)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng_90(210, -65, 25)
    t.end_fill()
    t.left(90)


# cube that is made from different shapes
def yohuuuu():
    t.right(135)
    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng_90(-5, 0, 205)
    t.end_fill()
    t.right(180)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng_90(0, 2, 205)
    t.end_fill()
    t.right(180)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(-150, -150, 102)
    t.end_fill()
    t.right(90)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng_90(0, -1, 102)
    t.end_fill()
    t.right(225)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng_90(150, -150, 150)
    t.end_fill()
    t.right(225)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng_90(78, 75, 102)
    t.end_fill()
    t.left(270)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(4, 0, 100)
    t.end_fill()
    t.right(45)


# helicopter
def hlcpt():
    t.right(45)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng(30, -211, 55)
    t.end_fill()
    t.left(45)

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng(27, -289, 55)
    t.end_fill()
    t.left(135)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng(-32, -272, 27)
    t.end_fill()
    t.left(45)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng(-17, -253, 27)
    t.end_fill()
    t.left(225)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(-45, -240, 28)
    t.end_fill()
    t.right(180)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng(-37, -208, 45)
    t.end_fill()
    t.left(225)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(30, -208, 30)
    t.end_fill()
    t.right(45)


# sail
def sl():
    t.left(180)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng(-198, -173, 27)
    t.end_fill()

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng(-225, -175, 55)
    t.end_fill()
    t.left(180)

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng(-228, -193, 55)
    t.end_fill()

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng(-225, -256, 27)
    t.end_fill()
    t.right(45)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(-185, -256, 28)
    t.end_fill()
    t.right(270)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng(-184, -259, 40)
    t.end_fill()
    t.left(180)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(-216, -287, 28)
    t.end_fill()
    t.right(180)


# left man
def lft_man():
    t.right(135)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(-196, 93, 31)
    t.end_fill()
    t.right(135)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng(-227, 12, 55)
    t.end_fill()
    t.left(45)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(-230, 66, 28)
    t.end_fill()

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng(-209, 25, 55)
    t.end_fill()
    t.right(90)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng(-206, -10, 40)
    t.end_fill()
    t.left(45)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng(-209, -91, 27)
    t.end_fill()
    t.left(180)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng(-287, -50, 27)
    t.end_fill()
    t.left(135)


# spacecraft
def rckt():
    t.left(45)

    t.fillcolor("#EC66E7")
    t.begin_fill()
    trng(199, -128, 27)
    t.end_fill()
    t.right(180)

    t.fillcolor("#50BBE9")
    t.begin_fill()
    trng(198, -130, 40)
    t.end_fill()
    t.right(180)

    t.fillcolor("#FEDD12")
    t.begin_fill()
    trng(198, -133, 55)
    t.end_fill()
    t.left(45)

    t.fillcolor("#F72A49")
    t.begin_fill()
    trng(238, -252, 55)
    t.end_fill()
    t.right(45)

    t.fillcolor("#FF7C00")
    t.begin_fill()
    sqr(220, -238, 31)
    t.end_fill()
    t.left(90)

    t.fillcolor("#A050E3")
    t.begin_fill()
    trng(173, -239, 31)
    t.end_fill()
    t.left(45)

    t.fillcolor("#8ECC21")
    t.begin_fill()
    prlm(263, -283, 31)
    t.end_fill()
    t.right(135)


rabbit()
fish()
chckn()
rght_man()
rckt()
hlcpt()
sl()
lft_man()
yohuuuu()
