import images
import pygame
# /////////////// Card Class


class Cards:
    def __init__(self, value, name, picture, dark_picture, large_picture, points):
        self.value = value
        self.name = name
        self.picture = picture
        self.dark_picture = dark_picture
        self.large_picture = large_picture
        self.points = points


# Create cards
Card1 = Cards(1, "Guard Dog", images.P1, images.D1, images.L1, 3.08)
Card2 = Cards(2, "Knight", images.P2, images.D2, images.L2, 1.8)
Card3 = Cards(3, "Lord", images.P3, images.D3, images.L3, 2.42)
Card4 = Cards(4, "Queen", images.P4, images.D4, images.L4, 3.24)
Card5 = Cards(5, "Mad King", images.P5, images.D5, images.L5, 7.8)

# Hands/Decks
p1_Hand = [Card1, Card2, Card3, Card4, Card5]
p2_Hand = [Card1, Card2, Card3, Card4, Card5]

