import cards
import GUI
import random
import math


class PlayGame:
    def __init__(self):
        self.p1_score = 0
        self.p2_score = 0
        self.p1_recentcard = -1
        self.p2_recentcard = -1
        self.p1_selectedcard = ""
        self.p2_prev = ""

    def check_previous(self, p1_choice, p2_choice):
        if self.p1_recentcard != p1_choice and self.p2_recentcard != p2_choice:
            return True
        else:
            return False

    def determine(self, p2_selectedcard):
        self.p1_recentcard = self.p1_selectedcard
        self.p2_recentcard = p2_selectedcard

        # Tie
        if self.p1_selectedcard.value == p2_selectedcard.value:
            GUI.message("TIE", GUI.width/2, GUI.height/2, 20)

        # Player 1 wins except for 5v1
        elif self.p1_selectedcard.value > p2_selectedcard.value:
            if self.p1_selectedcard.value == 5 and p2_selectedcard.value == 1:
                cards.p2_Hand.append(self.p1_selectedcard)
                cards.p1_Hand.remove(self.p1_selectedcard)
                GUI.message("Player 2 wins", GUI.width/2, GUI.height/2, 20)
            else:
                cards.p1_Hand.append(p2_selectedcard)
                cards.p2_Hand.remove(p2_selectedcard)
                GUI.message("Player wins", GUI.width/2, GUI.height/2, 20)

        # Player 2 wins except for 1v5
        elif p2_selectedcard.value > self.p1_recentcard.value:
            if p2_selectedcard.value == 5 and self.p1_recentcard.value == 1:
                cards.p1_Hand.append(p2_selectedcard)   
                cards.p2_Hand.remove(p2_selectedcard)
                GUI.message("Player wins", GUI.width/2, GUI.height/2, 20)
            else:
                cards.p2_Hand.append(self.p1_selectedcard)
                cards.p1_Hand.remove(self.p1_selectedcard)
                GUI.message("Player 2 wins", GUI.width/2, GUI.height/2, 20)

    def checkwinner(self):
        if not cards.p2_Hand:
            GUI.message("PLAYER WINS GAME!", 500, 300, 30)
        if not cards.p1_Hand:
            GUI.message("Player 2 WINS GAME!", 500, 300, 30)


    def AI_Eval(self, Pcard, AIcard):
        # Tie
        if Pcard.value == AIcard.value:
            return 0

        # Player 1 wins except for 5v1
        elif Pcard.value > AIcard.value:
            if Pcard.value == 5 and AIcard.value == 1:
                return 2
            else:
                return 1

        # Player 2 wins except for 1v5
        elif AIcard.value > Pcard.value:
            if AIcard.value == 5 and Pcard.value == 1:
                return 1
            else:
                return 2




    # /////////////////////////////////////////////// SIMPLE AI

    def choiceValue(self, winner, Pcard, AIcard):

        #Tie
        if winner == 0:
            return 0
        #Player Wins
        elif winner == 1:
            if AIcard.value == 1:
                return -.7
            elif AIcard.value == 2:
                return -.5
            elif AIcard.value == 3:
                return -.75
            elif AIcard.value == 4:
                return -1
            elif AIcard.value == 5:
                return -1.25
        #AI
        elif winner == 2:
            if Pcard.value == 1:
                return .8
            elif Pcard.value == 2:
                return .5
            elif Pcard.value == 3:
                return .75
            elif Pcard.value == 4:
                return 1
            elif Pcard.value == 5:
                return 1.25

    def AIRUN(self):
        counterAI = 0
        AICardChoices = []
        AI_Ratings = []

        for aicard in cards.p2_Hand:
            if aicard != self.p2_recentcard:
                AI_Ratings.append(0)
                for pcard in cards.p1_Hand:
                    AIminirating = self.choiceValue(self.AI_Eval(pcard, aicard), pcard, aicard)
                    AI_Ratings[counterAI] += AIminirating
                counterAI +=1
                AICardChoices.append(aicard)


        #Previous Card Rules
        if self.p1_recentcard != "" and self.p2_prev != "":
            if self.p1_recentcard.value == 5 and self.p2_prev.value == 5:
                try:
                    return cards.Card4
                except:
                    print("No 4 in hand")
        # Choose Max Value Card
        AIindex = AI_Ratings.index(max(AI_Ratings))
        # Remove Max Value Card for Secondary Max
        AI_Ratings[AIindex] = -2
        # Second Max Value
        try:
            AIindex2 = AI_Ratings.index(max(AI_Ratings))
        except:
            AIindex2 = 0
        # Add Randomness
        randnum = random.randint(0, 50)
        if len(cards.p2_Hand) <= 5:
            x = 24
            print(x)
        else:
            x = 33
        if randnum < x:
            print("Good card", AICardChoices[AIindex].name)
            return AICardChoices[AIindex]
        elif 38 <= randnum <= 33:
            print("random card")
            return cards.p2_Hand[random.randint(0, len(cards.p2_Hand) - 1)]
        else:
            print("second best", AICardChoices[AIindex].name)
            return AICardChoices[AIindex2]
