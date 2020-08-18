import pygame
import cards
import images
from random import randint

# /////////////////////////////////////////////WINDOW - SETTINGS

# create window
pygame.init()
width=1250
height=700
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(images.color_bg)

#  name - time
pygame.display.set_caption("GRAVITAS")
clock = pygame.time.Clock()
clock.tick(30)
pressed = False

# ///////////////////////////////////////////////////// Functions

def message(text, x , y, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def text_objects(text, font):
    textSurface = font.render(text, True, images.color_white)
    return textSurface, textSurface.get_rect()

def display_card_button(card, loc_card, size_card, game):
    # Mouse
    mouse = pygame.mouse.get_pos()
    #
    if loc_card[0] + size_card[0] > mouse[0] > loc_card[0] and loc_card[1] + size_card[1] > mouse[1] > loc_card[1]:
        global pressed
        if pressed == True:
            game.p1_selectedcard = card

        gameDisplay.blit(card.dark_picture, loc_card)
    else:
        gameDisplay.blit(card.picture, loc_card)


def display_Card(card, loc_card):
    gameDisplay.blit(card.picture, loc_card)


def startButton(x, y, xcoord, ycoord, bwidth, bheight, game):
    if xcoord + bwidth > x > xcoord and ycoord + bheight > y > ycoord:
        pygame.draw.rect(gameDisplay, images.color_maroon,(xcoord,ycoord,bwidth,bheight))
        global pressed

        if pressed == True:
            rndin = randint(0, len(cards.p2_Hand)-1)
            cpuCard = game.AIRUN()
            if game.p1_selectedcard != game.p1_recentcard:
                while cpuCard == game.p2_recentcard:
                    cpuCard = cards.p2_Hand[randint(0, len(cards.p2_Hand)-1)]
                game.determine(cpuCard)
                display_Card(game.p2_recentcard, (800,300))
                pressed == False
                cards.p2_Hand.sort(key=lambda x: x.value, reverse=False)
                cards.p1_Hand.sort(key=lambda x: x.value, reverse=False)
                game.checkwinner()
            else:
                message("Cannot play same cards twice in a row", width/2, height/2, 20)


    else:
        pygame.draw.rect(gameDisplay, images.color_red,(xcoord,ycoord,bwidth,bheight))


def restartButton(x, y, xcoord, ycoord, bwidth, bheight):
    if xcoord + bwidth > x > xcoord and ycoord + bheight > y > ycoord:
        pygame.draw.rect(gameDisplay, images.color_green,(xcoord,ycoord,bwidth,bheight))

        global pressed
        if pressed == True:
            cards.p1_Hand = [cards.Card1, cards.Card2, cards.Card3, cards.Card4, cards.Card5]
            cards.p2_Hand = [cards.Card1, cards.Card2, cards.Card3, cards.Card4, cards.Card5]
    else:
        pygame.draw.rect(gameDisplay, images.color_white,(xcoord,ycoord,bwidth,bheight))