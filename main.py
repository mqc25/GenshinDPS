import artifact, character, weapon, combat_simulator

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
    # A4
    Diluc.DMG_Bonus += 0.2

    # Wolf R1 no proc
    WGS = weapon.Weapon("WGS", refinement_level=1, weapon_skill_proc=False)

    # 4CW 11 CR rolls 4 CD rolls
    artifact = artifact.Artfiact()
    artifact.give_art_main_stat(["CD", "ATK", "DMG_Bonus_Ele"])
    artifact.give_art_sub_stat(["CR", "CD"], [11, 4])
    artifact.give_art_set_bonus("CW", None)

    # raw Diluc
    stat = combat_simulator.final_stat_calculator(Diluc, WGS, artifact)
    print("no buff Diluc")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f}".format(stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM))

    # buffed Diluc with Aquila NO Benny T6
    stat = combat_simulator.final_stat_calculator(Diluc, WGS, artifact, using_NO=True, pyro_RES=True, benny_Buff=678, EM_Buff=200)
    print("buff Diluc with Aquila NO Benny T6, 200 EM from sucrose and 11 CR roll, 4 CD roll")
    print("BaseATK: {:.2f} ATK%: {:.2f} Total ATK: {:.2f} CR: {:.2f} CD: {:.2f} DMG_Bonus: {:.2f} EM: {:.2f}".format(stat.BaseATK, stat.ATK_percent, stat.ATK, stat.CR, stat.CD, stat.DMG_Bonus, stat.EM))

    # rotation of Diluc/XQ/Benny/Sucrose assume sucrose give 200 EM and c6 XQ  with 12s DPS duration
    total_dmg, sequence, vape = combat_simulator.dilucVapeRotation(Diluc, stat)
    print(sequence)
    print(total_dmg)
    print(vape)

    for dmg, sequence_name, is_vape in zip(total_dmg, sequence, vape):
        print("{} {:.2f} {}".format(sequence_name, dmg, is_vape))

    print("Total Dmg: {:.2f} DPS over 21s: {:.2f}".format(sum(total_dmg), sum(total_dmg)/12.))

