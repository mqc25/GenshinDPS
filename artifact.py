class Artfiact:
    HP_sub_avg = 254.
    DEF_sub_avg = 19.5
    ATK_sub_avg = 16.5
    HP_percent_sub_avg = 0.0498
    DEF_percent_sub_avg = 0.062
    ATK_percent_sub_avg = 0.0498
    EM_sub_avg = 19.75
    ER_sub_avg = 5.5
    CR_sub_avg = 0.033
    CD_sub_avg = 0.066

    HP_Main = 4780.
    ATK_Main = 311.
    HP_percent_Main = 0.466
    DEF_percent_Main = 0.583
    ATK_percent_Main = 0.466
    EM_Main = 187.
    ER_Main = 0.518
    DMG_Bonus_Ele_Main = 0.466
    DMG_Bonus_Phys_Main = 0.583
    CR_Main = 0.311
    CD_Main = 0.622
    HealingBonus_Main = 0.359

    HP = 0.
    DEF = 0.
    ATK = 0.
    HP_percent = 0.
    DEF_percent = 0.
    ATK_percent = 0.
    EM = 0.
    ER = 0.
    CR = 0.
    CD = 0.
    DMG_Bonus = 0.
    Heal_Bonus = 0.

    def __init__(self):
        return

    def give_sub_stat(self, sub_type, num_roll):
        if sub_type == "CR":
            self.CR += self.CR_sub_avg * num_roll
        elif sub_type == "CD":
            self.CD += self.CD_sub_avg * num_roll
        elif sub_type == "ER":
            self.ER += self.ER_sub_avg  * num_roll
        elif sub_type == "EM":
            self.EM += self.EM_sub_avg * num_roll
        elif sub_type == "HP":
            self.HP += self.HP_sub_avg * num_roll
        elif sub_type == "HP_percent":
            self.HP_percent += self.HP_percent_sub_avg * num_roll
        elif sub_type == "ATK":
            self.ATK += self.ATK_sub_avg * num_roll
        elif sub_type == "ATK_percent":
            self.ATK += self.ATK_percent_sub_avg * num_roll
        elif sub_type == "DEF":
            self.DEF_percent += self.DEF_sub_avg * num_roll
        elif sub_type == "DEF_percent":
            self.DEF_percent += self.DEF_percent_sub_avg * num_roll

    def give_main_stat(self, main_type):
        if main_type == "CR":
            self.CR += self.CR_Main
        elif main_type == "CD":
            self.CD += self.CD_Main
        elif main_type == "ER":
            self.ER += self.ER_Main
        elif main_type == "EM":
            self.EM += self.EM_Main
        elif main_type == "HP":
            self.HP_percent += self.HP_percent_Main
        elif main_type == "ATK":
            self.ATK_percent += self.ATK_percent_Main
        elif main_type == "DEF":
            self.DEF_percent += self.DEF_percent_Main
        elif main_type == "DMG_Bonus_Ele":
            self.DMG_Bonus += self.DMG_Bonus_Ele_Main
        elif main_type == "DMG_Bonus_Phys":
            self.DMG_Bonus += self.DMG_Bonus_Phys_Main
        elif main_type == "Heal_Bonus":
            self.Heal_Bonus += self.HealingBonus_Main

    def give_art_main_stat(self, main_types, include_feather_and_flower=True):
        for main_type in main_types:
            self.give_main_stat(main_type)

        if include_feather_and_flower:
            self.HP += self.HP_Main
            self.ATK += self.ATK_Main

    def give_art_sub_stat(self, sub_types, num_rolls):
        for sub_type, sub_roll in zip(sub_types, num_rolls):
            self.give_sub_stat(sub_type, sub_roll)

    def give_art_set_bonus(self, set1, set2):
        using_4_set = set2 is None

        if set1 == "CW":
            self.DMG_Bonus += 0.15
            if using_4_set:
                return

        elif set1 == "WT":
            self.EM += 80
            if using_4_set:
                return


