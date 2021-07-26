class Weapon:
    BaseATK = 0.
    HP_percent = 0.
    DEF_percent = 0.
    ATK_percent = 0.
    EM = 0.
    ER = 0.
    CR = 0.
    CD = 0.
    DMG_Bonus = 0.
    Heal_Bonus = 0.

    def __init__(self , weapon_name, refinement_level=1, weapon_skill_proc=False):
        if weapon_name == "WGS":
            self.BaseATK = 608.
            self.HP_percent = 0.
            self.DEF_percent = 0.
            # sub stat + sub skill 1 + weapon proc
            self.ATK_percent = 0.496 + 0.2 + (refinement_level - 1) * 0.05 + weapon_skill_proc * (
                        0.4 + (refinement_level - 1) * 0.01)
            self.EM = 0.
            self.ER = 0.
            self.CR = 0.
            self.CD = 0.
            self.DMG_Bonus = 0.
