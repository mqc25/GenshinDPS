import character, weapon
import artifact


class Stat:
    def __init__(self, stat):
        self.BaseATK = stat["BaseATK"]
        self.BaseDEF = stat["BaseDEF"]
        self.BaseHP = stat["BaseHP"]
        self.HP = stat["HP"]
        self.ATK = stat["ATK"]
        self.ATK_percent = stat["ATK_percent"]
        self.EM = stat["EM"]
        self.ER = stat["ER"]
        self.DMG_Bonus = stat["DMG_Bonus"]
        self.CR = stat["CR"]
        self.CD = stat["CD"]
        self.Heal_Bonus = stat["Heal_Bonus"]
        self.ICD_time = 2.5
        self.ICD_count = 3


def final_stat_calculator(character, weapon, artifact, using_NO=False, pyro_RES=False, cyro_RES=False, benny_Buff=0.,
                          EM_Buff=0., ER_Buff=0., CR_Buff=0., CD_Buff=0., DMG_Bonus_Buff=0.):
    stat = dict()

    BaseATK = character.BaseATK + weapon.BaseATK
    stat["BaseATK"] = BaseATK
    ATK_percent = character.ATK_percent + weapon.ATK_percent + artifact.ATK_percent + using_NO * 0.2 + pyro_RES * 0.25
    stat["ATK_percent"] = ATK_percent
    stat["ATK"] = BaseATK * (1 + ATK_percent) + artifact.ATK + benny_Buff

    BaseHP = character.BaseHP
    stat["BaseHP"] = BaseHP
    HP_percent = character.HP_percent + weapon.HP_percent + artifact.HP_percent
    stat["HP"] = BaseHP * (1 + HP_percent) + artifact.HP

    BaseDEF = character.BaseDEF
    stat["BaseDEF"] = BaseDEF
    DEF_percent = character.DEF_percent + weapon.DEF_percent + artifact.DEF_percent
    stat["DEF"] = BaseDEF * (1 + DEF_percent) + artifact.DEF

    stat["EM"] = character.EM + weapon.EM + artifact.EM + EM_Buff
    stat["ER"] = character.ER + weapon.ER + artifact.ER + ER_Buff
    stat["CR"] = character.CR + weapon.CR + artifact.CR + cyro_RES * 0.15 + CR_Buff
    stat["CD"] = character.CD + weapon.CD + artifact.CD + CD_Buff

    stat["DMG_Bonus"] = character.DMG_Bonus + weapon.DMG_Bonus + artifact.DMG_Bonus + DMG_Bonus_Buff
    stat["Heal_Bonus"] = character.Heal_Bonus + weapon.Heal_Bonus + artifact.Heal_Bonus

    return Stat(stat)


def final_enemy_modifier(your_level=90, enemy_level=100, enemy_RES=0.1, using_VV=False, using_ZL=False, extra_shred=0.,
                         def_shred=0.):
    total_shred = using_VV * 0.4 + using_ZL * 0.2 + extra_shred
    final_res = enemy_RES

    if total_shred > final_res:
        overshred = total_shred - final_res
        final_res = -(overshred / 2.0)

    res_modifier = 1.0 - final_res
    def_modifier = (your_level + 100) / ((1 - def_shred) * (enemy_level + 100) + your_level + 100)
    print("Res multiplier: %.2f Def multiplier: %.2f".format(res_modifier, def_modifier))

    return res_modifier * def_modifier


def calculate_dmg(stat, mv, enemy_multiplier, amp_multiplier=1.0):
    # ATK * DMG_Bonus * MV * Amp * Crit_multiplier * Enemy_multiplier (Res + DEF)
    dmg = stat.ATK * (1 + stat.DMG_Bonus) * mv * amp_multiplier * (1.0 + stat.CR * stat.CD) * enemy_multiplier
    return dmg


def dilucVapeRotation(character, stat, using_c6_xq=True, using_4_CW=True, enemy_level=100, enemy_RES=0.1, using_VV=True,
                      using_ZL=False, extra_shred=0., def_shred=0., ):
    DPS_rotation_time = 12.0  # Benny Q duration
    total_rotation_time = 21.0  # XQ Q CD
    XQ_sword_pattern = [2, 3, 5] if using_c6_xq else [2, 3]
    XQ_sword_CD = 1.0

    vape_multiplier = 1.5 * (1. + (278 * stat.EM / (stat.EM + 1400.)) / 100. + using_4_CW * 0.15)
    enemy_multiplier = final_enemy_modifier(your_level=character.Level, enemy_level=enemy_level, enemy_RES=enemy_RES,
                                            using_VV=using_VV, using_ZL=using_ZL, extra_shred=extra_shred,
                                            def_shred=def_shred)

    print("Vape multiplier: %.2f Enemy multiplier: %.2f". format(vape_multiplier, enemy_multiplier))

    # start with 1 XQ sword status
    timer = 0.
    total_dmg = []
    sequence = []
    vape = []
    diluc_NA_sequence = 0
    enemy_element = "hydro"
    element_gauge = 1.0
    last_NA_ICD_frame = 0.
    ICD_counter = 0

    # Using ult and vape
    timer += character.Q_frame_count[0]
    # vape initial Q:
    Q_initial_dmg = calculate_dmg(stat, character.Q_damage[0], enemy_multiplier, vape_multiplier)
    total_dmg.append(Q_initial_dmg)
    sequence.append("Q initial dmg")
    vape.append(True)
    # 4 hit DoT Q:
    Q_DoT_dmg = 4 * calculate_dmg(stat, character.Q_damage[1], enemy_multiplier)
    total_dmg.append(Q_DoT_dmg)
    sequence.append("Q_DoT_dmg")
    vape.append(False)

    # NA-E-NA-E-NA-E with all 3 E vape and 1 NA vape:
    timer += 3 * character.NA_chain_framecount[0] + character.E_framecount[0] + character.E_framecount[1] + \
             character.E_framecount[2]
    # NA
    dmg = calculate_dmg(stat, character.NA_chain_damage[0], enemy_multiplier, vape_multiplier)
    total_dmg.append(dmg)
    sequence.append("NA1")
    vape.append(True)
    # E
    E_dmg = calculate_dmg(stat, character.E_damage[0], enemy_multiplier, vape_multiplier)
    stat.DMG_Bonus += 0.075 * using_4_CW
    total_dmg.append(E_dmg)
    sequence.append("E1")
    vape.append(True)
    # NA
    dmg = calculate_dmg(stat, character.NA_chain_damage[0], enemy_multiplier, vape_multiplier)
    total_dmg.append(dmg)
    sequence.append("NA1")
    vape.append(False)
    # E
    E_dmg = calculate_dmg(stat, character.E_damage[1], enemy_multiplier, vape_multiplier)
    stat.DMG_Bonus += 0.075 * using_4_CW
    total_dmg.append(E_dmg)
    sequence.append("E2")
    vape.append(True)
    # NA
    dmg = calculate_dmg(stat, character.NA_chain_damage[0], enemy_multiplier, vape_multiplier)
    total_dmg.append(dmg)
    sequence.append("NA1")
    vape.append(False)
    # E
    E_dmg = calculate_dmg(stat, character.E_damage[2], enemy_multiplier, vape_multiplier)
    stat.DMG_Bonus += 0.075 * using_4_CW
    total_dmg.append(E_dmg)
    sequence.append("E3")
    vape.append(True)

    last_NA_ICD_frame = 3 * character.NA_chain_framecount[0] + character.E_framecount[0] + character.E_framecount[1] + \
                        character.E_framecount[2]
    ICD_counter = 2
    diluc_NA_sequence = 0

    # NA till end
    while timer < DPS_rotation_time * 60:
        ICD_counter += 1
        diluc_NA_sequence += 1
        diluc_NA_sequence = diluc_NA_sequence % len(character.NA_chain_framecount)
        sequence_name = "NA" + str(diluc_NA_sequence + 1)
        is_vape = False
        if last_NA_ICD_frame >= 2.5 * 60:
            is_vape = True
            ICD_counter = 0
            last_NA_ICD_frame = 0
        elif ICD_counter > 2:
            is_vape = True
            ICD_counter = 0

        if is_vape:
            dmg = calculate_dmg(stat, character.NA_chain_damage[diluc_NA_sequence], enemy_multiplier, vape_multiplier)
        else:
            dmg = calculate_dmg(stat, character.NA_chain_damage[diluc_NA_sequence], enemy_multiplier)

        total_dmg.append(dmg)
        last_NA_ICD_frame += character.NA_chain_framecount[diluc_NA_sequence]
        timer += character.NA_chain_framecount[diluc_NA_sequence]
        sequence.append(sequence_name)
        vape.append(is_vape)

    return total_dmg, sequence, vape
