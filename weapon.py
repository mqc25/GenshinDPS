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

        elif weapon_name == "DV":
            self.BaseATK = 608.
            self.HP_percent = 0.496
            self.Heal_Bonus = 0.1

            self.DEF_percent = 0.
            self.ATK_percent = 0.
            self.EM = 0.
            self.ER = 0.
            self.CR = 0.
            self.CD = 0.
            self.DMG_Bonus = 0.

        elif weapon_name == "DM":
            self.BaseATK = 454.
            self.HP_percent = 0.
            self.Heal_Bonus = 0.
            self.DEF_percent = 0.
            self.ATK_percent = (0.24 + 0.06 * (refinement_level - 1)) if weapon_skill_proc else (0.16 + 0.04 * (refinement_level - 1))
            self.EM = 0.
            self.ER = 0.
            self.CR = 0.368
            self.CD = 0.
            self.DMG_Bonus = 0.

        elif weapon_name == "Homa":
            self.BaseATK = 608.
            self.HP_percent = 0.2 + 0.05 * (refinement_level - 1)
            self.Heal_Bonus = 0.
            self.DEF_percent = 0.
            self.ATK_percent = 0.
            self.EM = 0.
            self.ER = 0.
            self.CR = 0.
            self.CD = 0.662
            self.DMG_Bonus = 0.
            self.ATK_HP_scale = weapon_skill_proc * (0.008 + 0.002 * (refinement_level - 1))
            self.ATK_Low_HP_scale = weapon_skill_proc * (0.01 + 0.002 * (refinement_level - 1))

        elif weapon_name == "DB":
            self.BaseATK = 454.
            self.HP_percent = 0.
            self.Heal_Bonus = 0.
            self.DEF_percent = 0.
            self.ATK_percent = 0.
            self.EM = 221.
            self.ER = 0.
            self.CR = 0.
            self.CD = 0.
            self.DMG_Bonus = weapon_skill_proc * (0.2 + 0.04 * (refinement_level - 1))

        elif weapon_name == "TP":
            self.BaseATK = 608.
            self.HP_percent = 0.
            self.Heal_Bonus = 0.
            self.DEF_percent = 0.
            self.ATK_percent = 0.2 + (0.05 * (refinement_level - 1))
            self.EM = 0.
            self.ER = 0.
            self.CR = 0.
            self.CD = 0.662
            self.NA_Bonus = 0.4 + 0.1 * (refinement_level - 1)
