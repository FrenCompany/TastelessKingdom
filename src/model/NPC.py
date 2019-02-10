from Lib.copy import deepcopy
from src.model import Dialogue

class NPC:
    def __init__(self, name, dialogues=[], afterBattle, animatedsprite):
        self.friend=False #maybe not necessary to set in init
        self.name=name #string (duh)
        self.dialogueState=0 (int)
        self.dialogues=dialogues #list of Dialogue objects
        self.afterBattleDialogue=afterBattle
        self.battleState=False
        self.sprite=animatedsprite
    def getName(self):
        return self.name

    def getFriend(self):
        return self.friend

    def getName(self):
        return self.name
    def setDialogue(self,nuevo):
        self.dialogues.append(nuevo)
    def getDialogue(self):
        if self.battleState==False:
            return self.dialogues[self.dialogueState].getDialogue()

        else:
            return self.afterBattleDialogue.getDialogue()

    def nextState(self):
        if self.dialogueState<len(self.dialogues) and self.dialogues[self.dialogueState].cond:
            self.dialogueState+=1

    def setBattleState(self, didYouWin):
        self.battleState=True
        self.friend=didYouWin