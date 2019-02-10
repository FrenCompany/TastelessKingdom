from src.model.battle.Buff import Buff


class CancelAttackBuff(Buff):
    def buff_reaction(self, reaction):
        reaction.cancelAttack()
        return reaction
