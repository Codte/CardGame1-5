# ////////////////////////////////////////////// MINIMAX AI

def minimax_determine(self, h1, h2, handp, handai):
    # Tie
    if h1.value == h2.value:
        return
    # Player 1 wins except for 5v1
    elif h1.value > h2.value:
        if h1.value == 5 and h2.value == 1:
            handai.append(p1)
            handp.remove(self.p1_selectedcard)
        else:
            handp.append(p2_selectedcard)
            handai.p2_Hand.remove(p2_selectedcard)

    # Player 2 wins except for 1v5
    elif p2_selectedcard.value > self.p1_recentcard.value:
        if p2_selectedcard.value == 5 and self.p1_recentcard.value == 1:
            cards.p1_Hand.append(p2_selectedcard)
            cards.p2_Hand.remove(p2_selectedcard)
        else:
            cards.p2_Hand.append(self.p1_selectedcard)
            cards.p1_Hand.remove(self.p1_selectedcard)


def scoring(self):
    sumHandPoints = 0
    for card in cards.p2_Hand:
        sumHandPoints += card.points
    if len(cards.p2_Hand) == 10:
        return 50 + sumHandPoints
    return sumHandPoints


def isterminal_Node(self, hand):
    if len(hand) == 9:
        return True
    if len(hand) == 1:
        return True
    else:
        return False


def minimax(self, hand, depth, maximizingPlayer):
    isTerminal = self.isterminal_Node(hand)
    if depth == 0 or isTerminal:
        if len(cards.p2_Hand) >= 9:
            return 10000
        elif len(cards.p1_Hand) >= 9:
            return -10000
    if maximizingPlayer:
        value = -math.inf
        p2_Handcopy = cards.p2_Hand.copy()
        p1_Handcopy = cards.p1_Hand.copy()

        for aicard in p2_Handcopy:
            for pcard in p1_Handcopy:



