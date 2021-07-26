import character, weapon, combat_simulator
from artifact import Artfiact


def runDilucVapeCal():
    Diluc = character.Character()
    Diluc.BaseATK = 335.
    Diluc.BaseDEF = 784.
    Diluc.BaseHP = 12981.
    Diluc.CR += 0.242
    Diluc.NA_chain_framecount = [24, 77, 115, 181]
    Diluc.NA_chain_damage = [1.3038, 1.2738, 1.4363, 1.9475]
    Diluc.E_framecount = [45, 52, 81]
    Diluc.E_damage = [1.3216, 1.3664, 1.8064]
    Diluc.E_CD = 10.
    Diluc.Q_frame_count = [145]
    Diluc.Q_damage = [2.866, 0.840]
    Diluc.Q_CD = 12

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
    Kkomi = character.Character()
    Kkomi.BaseATK = 222.
    Kkomi.BaseDEF = 615.
    Kkomi.BaseHP = 11695.
    Kkomi.NA_chain_framecount = [25, 25, 50]
    Kkomi.NA_chain_damage = [1.094, 0.9846, 1.5089]
    Kkomi.CA_framecount = [90]
    Kkomi.CA_damage = [2.3731]
    Kkomi.Q_frame_count = [120]
    Kkomi.Q_damage = [0.1667, 0.0774, 0.1084]
    Kkomi.Q_CD = 18
    Kkomi.DMG_Bonus += 0.288

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

if __name__ == '__main__':
    runKkomiVapeCal()
