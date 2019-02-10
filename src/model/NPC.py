from Lib.copy import deepcopy
from src.model import Dialogue

class NPC:
    def __init__(self, name, dialogues, afterBattle):
        self.friend=False #maybe not necessary to set in init
        self.name=name #string (duh)
        self.dialogueState=0 (int)
        self.dialogues=dialogues #list of Dialogue objects
        self.afterBattleDialogue=afterBattle
        self.battleState=False
    def getName(self):
        return self.name

    def getFriend(self):
        return self.friend

    def getName(self):
        return self.name

    def getDialogue(self):
        if self.battleState==False:
            return self.dialogues[self.dialogueState].getDialogue()

        else:
            return self.afterBattleDialogue.getDialogue()

    def nextState(self):
        if self.dialogueState<len(self.dialogues):
            self.dialogueState+=1

    def setBattleState(self, didYouWin):
        self.battleState=True
        self.friend=didYouWin