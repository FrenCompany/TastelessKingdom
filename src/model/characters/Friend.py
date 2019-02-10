import random

class Greet:
    def run(self, npc, player):
        npc.changeState(Ask())
        print(npc.greeting)
class Ask:
    def run(self, npc, player):
        print(npc.ask)
        cond=True
        for ingrediente in npc.requisito:
            cond=cond and (ingrediente in player.inventory)
        if cond:
            npc.changeState(Receive())

class Receive:
    def run(self, npc, player):
        npc.changeState(Battle())
        print(npc.receive)
class Battle:
    def run(self,npc, player):
        print('Aqui iria la batalla')
        a = random.randint(1,2)
        if a==1:
            npc.changeState(Winner())
            print('Ganaste!')
        else:
            npc.changeState(Loser())
            print('Perdiste!')
class Winner:
    def run(self,npc, player):
        print(npc.win)

class Loser:
    def run(self,npc, player):
        print(npc.lose)


class Friend:
    def __init__(self, name, sprite, greeting, ask, receive, win, lose, requisito, player):
        self.name=name
        self.sprite=sprite
        self.state=Greet()
        self.player = player
        self.greeting=greeting
        self.ask=ask
        self.receive=receive
        self.win=win
        self.lose=lose
        self.requisito=requisito

    def interact(self):
        self.state.run(self, self.player)

    def changeState(self,new):
        self.state=new
