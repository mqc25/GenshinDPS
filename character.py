import character


class Character:
    def __init__(self):
        self.NA_chain_framecount = None
        self.NA_chain_damage = None
        self.CA_framecount = None
        self.CA_damage = None
        self.E_framecount = None
        self.E_damage = None
        self.E_CD = None
        self.E_Duration = None
        self.Q_frame_count = None
        self.Q_damage = None
        self.Q_CD = None
        self.Q_Duration = None
        self.ElementType = None
        self.BaseATK = 0.
        self.ATK_percent = 0.
        self.BaseDEF = 0.
        self.DEF_percent = 0.
        self.CR = 0.05
        self.CD = 0.50
        self.EM = 0.
        self.DMG_Bonus = 0.
        self.ER = 100.
        self.BaseHP = 0.
        self.HP_percent = 0.
        self.Heal_Bonus = 0.
        self.Level = 90

class Diluc(Character):
    def __init__(self):
        Character.__init__(self)
        self.BaseATK = 335.
        self.BaseDEF = 784.
        self. BaseHP = 12981.
        self.CR += 0.242
        self.NA_chain_framecount = [24, 77, 115, 181]
        self.NA_chain_damage = [1.3038, 1.2738, 1.4363, 1.9475]
        self.E_framecount = [45, 52, 81]
        self.E_damage = [1.3216, 1.3664, 1.8064]
        self.E_CD = 10.
        self.Q_frame_count = [145]
        self.Q_damage = [2.866, 0.840]
        self.Q_CD = 12

class Kkomi(Character):
    def __init__(self):
        Character.__init__(self)
        self.BaseATK = 222.
        self.BaseDEF = 615.
        self.BaseHP = 11695.
        self.NA_chain_framecount = [25, 25, 50]
        self.NA_chain_damage = [1.094, 0.9846, 1.5089]
        self.CA_framecount = [90]
        self.CA_damage = [2.3731]
        self.Q_frame_count = [120]
        self.Q_damage = [0.1667, 0.0774, 0.1084]
        self.Q_CD = 18
        self.DMG_Bonus += 0.288

class HuTao(Character):
    def __init__(self, is_low_hp=True):
        Character.__init__(self)
        self.BaseATK = 106
        self.BaseDEF = 876
        self.BaseHP = 15552
        self.NA_chain_framecount = [13, 29, 54, 90, 134, 173]
        self.NA_chain_damage = [0.7406, 0.7622, 0.9643, 1.0368, 1.0716, 1.3578]
        self.CA_framecount = [65]
        self.CA_damage = [2.1476]
        self.E_framecount = [42]
        self.E_atk_buff = [0.0566]
        self.E_blossom = [1.024]
        self.Q_frame_count = [130]
        self.Q_damage = [5.5842 if is_low_hp else 4.4674]
        self.isLowHp = is_low_hp
        self.CD += 0.384
        if is_low_hp:
            self.DMG_Bonus += 0.33

class Yoimiya(Character):
    def __init__(self):
        Character.__init__(self)
        self.BaseATK = 323
        self.BaseDEF = 615
        self.BaseHP = 10164
        self.NA_chain_framecount = [27, 24, 37, 40, 57]
        self.NA_chain_damage = [0.6359*2, 1.2199, 1.6768, 0.8757*2, 1.997]
        self.E_framecount = [23]
        self.E_na_buff = [1.6174]
        self.Q_frame_count = [115]
        self.Q_damage = [2.2896, 2.196]
        self.CR += 0.242




