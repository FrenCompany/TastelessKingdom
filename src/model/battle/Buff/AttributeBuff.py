from .Buff import Buff


class AttributeBuff(Buff):
    def __init__(self, cooldown, buff_dict):
        super(AttributeBuff, self).__init__(cooldown)
        self.buff_dict = buff_dict

    def buff_multipliers(self, multipliers):
        for key in self.buff_dict:
            try:
                multipliers.mult[key] += self.buff_dict[key]
            except:
                multipliers.mult[key] = self.buff_dict[key]
        return multipliers
