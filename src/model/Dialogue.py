class Dialogue:
    def __init__(self,iftrue,iffalse,cond):
        self.iftrue=iftrue
        self.iffalse=iffalse
        self.cond=cond
        # a dialogue that shows up no matter what has a cond of True and iffalse ''
    def getDialogue(self):
        if self.cond:
            return self.iftrue
        else:
            return self.iffalse