# GenshinDPS

## Instruction
Run the main python file

## Hu Tao Vape setup
Comp: ZL/CY(C2)/XQ(withNO)/HT

Rotation: ZL E -> CY E Q -> XQ Q E E -> HT E Q 6xN1C

DPS time: 9s

Rotation time: 17s (XQ Q cd)

Weapon: Homa R1

Sets:

| Set                         | ATK  | HP    | EM  | CR | CD  | Pyro |
|-----------------------------|------|-------|-----|----|-----|------|
| 4CW-EMsand-14CR-1CD-5HP     | 2932 | 27314 | 187 | 82 | 161 | 102  |
| 4CW-HPsand-14CR-1CD-5EM     | 3150 | 30689 | 99  | 82 | 161 | 102  |
| 4Red-EMsand-14CR-1CD-5HP    | 3060 | 27314 | 187 | 82 | 161 | 80   |
| 4Red-HPsand-14CR-1CD-5EM    | 3278 | 30689 | 99  | 82 | 161 | 80   |
| CW_WT-HPsand-14CR-1CD-5EM   | 3150 | 30689 | 179 | 82 | 161 | 95   |
| CW_Totm-EMsand-14CR-1CD-5EM | 2883 | 26552 | 285 | 82 | 161 | 95   |

DPS:

|            | Melt-Vape? | 4CW-EMsand | 4CW-HPsand | 4Red-EMsand | 4Red-HPsand | CW_WT-HPsand | Homa-CW_Totm-EMsand |
|------------|------------|------------|------------|-------------|-------------|--------------|---------------------|
| Q_hit_melt | True       | 116395     | 112827     | 97009       | 92615       | 107140       | 109721              |
| NA1        | True       | 11577      | 11222      | 12335       | 11776       | 10657        | 10913               |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| NA1        | False      | 5223       | 5612       | 6194        | 6635        | 5403         | 4945                |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| NA1        | False      | 5223       | 5612       | 6194        | 6635        | 5403         | 4945                |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| NA1        | True       | 11577      | 11222      | 12335       | 11776       | 10657        | 4945                |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| NA1        | False      | 5223       | 5612       | 6194        | 6635        | 5403         | 10913               |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| NA1        | False      | 5223       | 5612       | 6194        | 6635        | 5403         | 4945                |
| CA         | True       | 33572      | 32543      | 35771       | 34150       | 30903        | 31647               |
| 2xBlossom  | True       | 32015      | 31034      | 26683       | 25474       | 29470        | 30180               |
| Total      |            | 393898     | 384019     | 387769      | 373092      | 364960       | 371398              |
| DPS        |            | 23170      | 22589      | 22809       | 21946       | 21468        | 21846               |

## Diluc Vape Setup
Diluc only dmg calculate for Diluc/XQ/Benny/Sucrose comp over 15s rotation (3s for support)

Diluc lvl 90, 6/6/6 Talent with WGS R1 no skill proc, 4 CW with CD/Pyro/ATK, 11 CR rolls, 4 CD rolls

Benny has Aquila with T6 Q give 678 flat ATK and NO set

Sucrose give 200 EM and VV shred

| Buff status                | BaseATK | ATK% | ATK  | CR | CD  | DMG_Bonus | EM  |
|----------------------------|---------|------|------|----|-----|-----------|-----|
| No buff                    | 943     | 116  | 2350 | 66 | 139 | 62        | 0   |
| With team buff + resonance | 943     | 161  | 3452 | 66 | 139 | 62        | 200 |

Res multiplier: 1.15 Def multiplier: 0.49

Vape multiplier: 2.25 Enemy multiplier: 0.56

| ATK Sequence | DMG       | Vape?         |
|--------------|-----------|---------------|
| Q initial    | 38387.30  | True          |
| Q_DoT (4hit) | 20035.15  | False         |
| NA1          | 19624.42  | True          |
| E1           | 19892.34  | True          |
| NA1          | 20434.90  | False         |
| E2           | 21416.05  | True          |
| NA1          | 21245.38  | False         |
| E3           | 29435.23  | True          |
| NA1          | 22055.86  | True          |
| NA2          | 9593.04   | False         |
| NA3          | 10816.83  | False         |
| NA4          | 32945.07  | True          |
| Total        | 265881.55 | DPS: 17725.44 |
