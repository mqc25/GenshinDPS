import character, weapon, combat_simulator
from artifact import Artfiact


def runDilucVapeCal():
    Diluc = character.Diluc()
    # Wolf R1 no proc
    WGS = weapon.Weapon("WGS", refinement_level=1, weapon_skill_proc=False)

    # 4CW 11 CR rolls 4 CD rolls
    artifact = Artfiact()
    artifact.give_art_main_stat(["CD", "ATK", "DMG_Bonus_Ele"])
    artifact.give_art_sub_stat(["CR", "CD"], [11, 4])
    artifact.give_art_set_bonus("CW", None)

    # raw Diluc
    stat = combat_simulator.final_stat_calculator(Diluc, WGS, artifact)
    print("no buff Diluc")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f}".format(
        stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM))

    # buffed Diluc with Aquila NO Benny T6
    stat = combat_simulator.final_stat_calculator(Diluc, WGS, artifact, using_NO=True, pyro_RES=True, benny_Buff=678,
                                                  EM_Buff=200)
    print("buff Diluc with Aquila NO Benny T6, 200 EM from sucrose and 11 CR roll, 4 CD roll")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f}".format(
        stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM))

    # rotation of Diluc/XQ/Benny/Sucrose assume sucrose give 200 EM  with 15s rotation duration (12s Diluc, 3s support)
    total_dmg, sequence, vape = combat_simulator.dilucVapeRotation(Diluc, stat)
    print(sequence)
    print(total_dmg)
    print(vape)

    for dmg, sequence_name, is_vape in zip(total_dmg, sequence, vape):
        print("{} {:.2f} {}".format(sequence_name, dmg, is_vape))

    print("Total Dmg: {:.2f} DPS over 15s: {:.2f}".format(sum(total_dmg), sum(total_dmg) / 15.))

def runKkomiVapeCal():
    Kkomi = character.Kkomi()
    # Wolf R1 no proc
    DV = weapon.Weapon("DV", refinement_level=1, weapon_skill_proc=False)

    # 4CW 11 CR rolls 4 CD rolls
    artifact = Artfiact()
    artifact.give_art_main_stat(["Heal_Bonus", "HP", "DMG_Bonus_Ele"])
    artifact.give_art_sub_stat(["HP_percent", "EM"], [5, 10])
    artifact.give_art_set_bonus("WT", None)

    # raw Kkomi
    stat = combat_simulator.final_stat_calculator(Kkomi, DV, artifact)
    stat.CR = 0
    stat.Heal_Bonus += 0.25
    print("no buff Kkomi")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HealBonus: {:.2f} HP {:.2f} HP_percent {:.2f}".format(
        stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.Heal_Bonus, stat.HP, stat.HP_percent))

    # buffed Kkomi with Aquila NO Benny T8 + pyro res with XL + 200 EM sucrose
    stat = combat_simulator.final_stat_calculator(Kkomi, DV, artifact, using_NO=True, pyro_RES=True, benny_Buff=775,
                                                  EM_Buff=200)
    stat.CR = 0
    stat.Heal_Bonus += 0.25
    print("buff Kkomi with Aquila NO Benny T6, 200 EM from sucrose and 11 CR roll, 4 CD roll")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HealBonus: {:.2f} HP {:.2f} HP_percent {:.2f}".format(
            stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.Heal_Bonus,
            stat.HP, stat.HP_percent))

    stat = combat_simulator.final_stat_calculator(Kkomi, DV, artifact, using_NO=True, pyro_RES=True, benny_Buff=775,
                                                  EM_Buff=0)
    stat.Heal_Bonus += 0.25
    print("buff Kkomi with Aquila NO Benny T6, ZL and 11 CR roll, 4 CD roll")
    print(
        "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HealBonus: {:.2f} HP {:.2f} HP_percent {:.2f}".format(
            stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.Heal_Bonus,
            stat.HP, stat.HP_percent))

    total_dmg, sequence, vape = combat_simulator.KkomiCAVapeRotation(Kkomi, stat)
    print(sequence)
    print(total_dmg)
    print(vape)

    for dmg, sequence_name, is_vape in zip(total_dmg, sequence, vape):
        print("{} {:.2f} {}".format(sequence_name, dmg, is_vape))

    print("Total Dmg: {:.2f} DPS over 15s: {:.2f}".format(sum(total_dmg), sum(total_dmg) / 15.))

def runHTVapeComp(character, weapon, artifact, usingChongC2=False, usingNO=False, usingZL=False):
    pass

if __name__ == '__main__':
    HuTao = character.HuTao()

    # R1 Homa low HP
    Homa = weapon.Weapon("Homa", refinement_level=1, weapon_skill_proc=True)

    # Artifact with 15 crit roll and 5 EM roll
    # 4CW-HPsand 11 CR rolls 4 CD rolls for Homa
    CW_HP = Artfiact()
    CW_HP.give_art_main_stat(["CR", "HP", "DMG_Bonus_Ele"])
    CW_HP.give_art_sub_stat(["CR", "CD", "EM"], [14, 1, 5])
    CW_HP.give_art_set_bonus("CW", None)

    Homa_CW_HP_stat = combat_simulator.final_stat_calculator(HuTao, Homa, CW_HP, using_NO=True, pyro_RES=False, benny_Buff=0.,
                                                  EM_Buff=0)

    # 4CW-EMsand 11 CR rolls 4 CD rolls
    CW_EM = Artfiact()
    CW_EM.give_art_main_stat(["CR", "EM", "DMG_Bonus_Ele"])
    CW_EM.give_art_sub_stat(["CR", "CD", "HP_percent"], [14, 1, 5])
    CW_EM.give_art_set_bonus("CW", None)

    Homa_CW_EM_stat = combat_simulator.final_stat_calculator(HuTao, Homa, CW_EM, using_NO=True, pyro_RES=False, benny_Buff=0.,
                                                  EM_Buff=0)

    # 4Red-HPsand 11 CR rolls 4 CD rolls
    Red_HP = Artfiact()
    Red_HP.give_art_main_stat(["CR", "HP", "DMG_Bonus_Ele"])
    Red_HP.give_art_sub_stat(["CR", "CD", "EM"], [14, 1, 5])
    Red_HP.give_art_set_bonus("Red", None)

    Homa_Red_HP_stat = combat_simulator.final_stat_calculator(HuTao, Homa, Red_HP, using_NO=True, pyro_RES=False,
                                                             benny_Buff=0.,
                                                             EM_Buff=0)

    # 4Red-EMsand 11 CR rolls 4 CD rolls
    Red_EM = Artfiact()
    Red_EM.give_art_main_stat(["CR", "EM", "DMG_Bonus_Ele"])
    Red_EM.give_art_sub_stat(["CR", "CD", "HP_percent"], [14, 1, 5])
    Red_EM.give_art_set_bonus("Red", None)

    Homa_Red_EM_stat = combat_simulator.final_stat_calculator(HuTao, Homa, Red_EM, using_NO=True, pyro_RES=False,
                                                             benny_Buff=0.,
                                                             EM_Buff=0)

    # 2CW-2WT-HPsand 11 CR rolls 4 CD rolls for Homa
    CW_WT_HP = Artfiact()
    CW_WT_HP.give_art_main_stat(["CR", "HP", "DMG_Bonus_Ele"])
    CW_WT_HP.give_art_sub_stat(["CR", "CD", "EM"], [14, 1, 5])
    CW_WT_HP.give_art_set_bonus("CW", "WT")

    Homa_CW_WT_HP_stat = combat_simulator.final_stat_calculator(HuTao, Homa, CW_WT_HP, using_NO=True, pyro_RES=False,
                                                             benny_Buff=0.,
                                                             EM_Buff=0)

    # 2CW-2Totm-EMsand 11 CR rolls 4 CD rolls for Homa
    CW_TM_EM = Artfiact()
    CW_TM_EM.give_art_main_stat(["CR", "EM", "DMG_Bonus_Ele"])
    CW_TM_EM.give_art_sub_stat(["CR", "CD", "EM"], [14, 1, 5])
    CW_TM_EM.give_art_set_bonus("CW", "Totm")

    Homa_CW_TM_EM_stat = combat_simulator.final_stat_calculator(HuTao, Homa, CW_TM_EM, using_NO=True, pyro_RES=False,
                                                                benny_Buff=0.,
                                                                EM_Buff=0)

    # # HuTao-Homa-4CW-EMsand
    # stat = Homa_CW_EM_stat
    # stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    # stat.DMG_Bonus += 0.075
    # print("HuTao-Homa-4CW-EMsand low HP with E")
    # print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
    #     stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    # # HuTao-Homa-4CW-HPsand
    # stat = Homa_CW_HP_stat
    # stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    # stat.DMG_Bonus += 0.075
    # print("HuTao-Homa-4CW-HPsand low HP with E")
    # print(
    #     "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
    #         stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    # # HuTao-Homa-4Red-EMsand
    # stat = Homa_Red_EM_stat
    # stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    # print("HuTao-Homa-4Red-EMsand low HP with E")
    # print(
    #     "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
    #         stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    # # HuTao-Homa-4Red-HPsand
    # stat = Homa_Red_HP_stat
    # stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    # print("HuTao-Homa-4Red-HPsand low HP with E")
    # print(
    #     "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
    #         stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    # # HuTao-Homa-CW_WT-HPsand
    # stat = Homa_CW_WT_HP_stat
    # stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    # print("HuTao-Homa-CW_WT-HPsand low HP with E")
    # print(
    #     "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
    #         stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    # # # HuTao-Homa-CW_Totm-EMsand
    stat = Homa_CW_TM_EM_stat
    stat.ATK += stat.HP * (Homa.ATK_HP_scale + Homa.ATK_Low_HP_scale + HuTao.E_atk_buff[0])
    print("HuTao-Homa-CW_Totm-HPsand low HP with E")
    print(
        "BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f} HP: {:.2f}".format(
            stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM, stat.HP))

    ##CW
    ## rotation of ZL/CY/XQ/HT assume ZL is shield bot, CY has C2, XQ has NO and HT will melt the first Q instead of vape
    # total_dmg, sequence, vape, dps = combat_simulator.HuTaoVape(HuTao, stat, using_4_CW=True, using_ZL=True, usingC2Chong=True)
    # print(sequence)
    # print(total_dmg)
    # print(vape)
    # print(sum(total_dmg), dps)

    ##Red
    # # rotation of ZL/CY/XQ/HT assume ZL is shield bot, CY has C2, XQ has NO and HT will melt the first Q instead of vape
    # total_dmg, sequence, vape, dps = combat_simulator.HuTaoVape(HuTao, stat, using_4_Red=True, using_ZL=True, usingC2Chong=True)
    # print(sequence)
    # print(total_dmg)
    # print(vape)
    # print(sum(total_dmg), dps)

    # ##2-2
    # ## rotation of ZL/CY/XQ/HT assume ZL is shield bot, CY has C2, XQ has NO and HT will melt the first Q instead of vape
    total_dmg, sequence, vape, dps = combat_simulator.HuTaoVape(HuTao, stat,using_4_Red=False, using_ZL=True, usingC2Chong=True)
    print(sequence)
    print(total_dmg)
    print(vape)
    print(sum(total_dmg), dps)

