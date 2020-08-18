import pygame
import cards
import GUI
import images
import game
from random import randint

# /////TESTING
G1 = game.PlayGame()



# ///////////////////////////////////////////////// GAME LOOP

crashed = False


while not crashed:

    # Display P1 Cards
    count1 = 0
    for card in cards.p1_Hand:
        GUI.display_card_button(card,
                                ((GUI.width - len(cards.p1_Hand) * images.sizeSmall[0]) / 2 +
                                 count1 * images.sizeSmall[0],
                                 GUI.height - images.sizeSmall[1]),
                                (images.sizeSmall[0], images.sizeSmall[1]), G1)
        count1 += 1
    # Display P2 Cards
    count2 = 0
    for card in cards.p2_Hand:
        GUI.display_card_button(card,
                                ((GUI.width - len(cards.p2_Hand) * images.sizeSmall[0]) / 2 +
                                 count2 * images.sizeSmall[0], 0),
                                (images.sizeSmall[0], images.sizeSmall[1]), G1)
        count2 += 1

    # Display Selected Cards
    if G1.p1_selectedcard != "" and G1.p1_selectedcard != G1.p1_recentcard:
        GUI.display_Card(G1.p1_selectedcard, (200, 300))
    else:
        pygame.draw.rect(GUI.gameDisplay, images.color_maroon, (200, 300, images.sizeSmall[0], images.sizeSmall[1]))

    # Display Previous Card
    if G1.p1_recentcard != -1:
        GUI.display_Card(G1.p1_recentcard, (25, 300))

    if G1.p2_recentcard != -1:
        GUI.display_Card(G1.p2_recentcard, (1000, 300))

    GUI.pressed = False
    # EVENTS
    for event in pygame.event.get():
        # Quit/X
        if event.type == pygame.QUIT:
            crashed = True

        # Button Press
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y positions of the mouse click
            x, y = event.pos
            GUI.gameDisplay.fill(images.color_bg)
            GUI.pressed = True
            GUI.startButton(x, y, GUI.width/2-100, GUI.height/2-100, 200, 200, G1)
            GUI.restartButton(x, y, 1000, 400, 100, 50)

                         
        pygame.display.update()

pygame.quit()
quit()

