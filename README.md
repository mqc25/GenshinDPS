# GenshinDPS

## Instruction
Run the main python file

## Yoi melt setup
- Comp: Yoi(C0)/Kazu(C2)/Benny(C5)/Diona(C6) assume all T10
- Rotation time: 18s
- DPS time: 10s
- Weapon: R1 Thunder Pulse
- Set: 4CW
- Stat after all team buff

| Set                         | ATK  | HP    | EM  | CR | CD  | Pyro |
|-----------------------------|------|-------|-----|----|-----|------|
| 4CW-ATKsand-9CD-6CR-5EM     | 3310 | 14944 | 498 | 80 | 176 | 61.6 |

DPS sequence:

| Sequence | Melt? | DMG    |
|----------|-------|--------|
| NA1      | True  | 50070  |
| NA2      | False | 22112  |
| NA3      | True  | 115209 |
| NA4      | False | 32252  |
| NA5      | True  | 139378 |
| NA1      | True  | 52080  |
| NA2      | False | 22993  |
| NA3      | True  | 119761 |
| NA4      | False | 33517  |
| NA5      | True  | 144799 |
| NA1      | True  | 54091  |
| NA2      | False | 23697  |
| NA3      | True  | 122492 |
| NA4      | False | 34023  |
| NA5      | True  | 145883 |
| NA1      | True  | 54091  |
| NA2      | False | 23697  |
| Total    | 1190153 | DPS: 66119 |

## Hu Tao Vape setup
Comp: ZL/CY(C2)/XQ(withNO)/HT

Rotation: ZL E -> CY E Q -> XQ Q E E -> HT E Q 6xN1C

DPS time: 9s

Rotation time: 17s (XQ Q cd)

Weapon: Homa R1

Sets:

| Set                         | ATK  | HP    | EM  | CR | CD  | Pyro |
|-----------------------------|------|-------|-----|----|-----|------|
| 4CW-EMsand-14CR-1CD-5HP     | 3205 | 27314 | 187 | 82 | 161 | 102  |
| 4CW-HPsand-14CR-1CD-5EM     | 3457 | 30689 | 99  | 82 | 161 | 102  |
| 4Red-EMsand-14CR-1CD-5HP    | 3334 | 27314 | 187 | 82 | 161 | 80   |
| 4Red-HPsand-14CR-1CD-5EM    | 3585 | 30689 | 99  | 82 | 161 | 80   |
| CW_WT-HPsand-14CR-1CD-5EM   | 3457 | 30689 | 179 | 82 | 161 | 95   |
| CW_Totm-EMsand-14CR-1CD-5EM | 3148 | 26552 | 285 | 82 | 161 | 95   |

DPS:

|            | Melt-Vape? | 4CW-EMsand | 4CW-HPsand | 4Red-EMsand | 4Red-HPsand | CW_WT-HPsand | Homa-CW_Totm-EMsand |
|------------|------------|------------|------------|-------------|-------------|--------------|---------------------|
| Q_hit_melt | True       | 127237     | 123818     | 105666      | 101283      | 117577       | 119826              |
| NA1        | True       | 12656      | 12316      | 13436       | 12879       | 11695        | 11918               |
| CA         | True       | 36700      | 35714      | 38963       | 37347       | 33913        | 34562               |
| NA1        | False      | 5710       | 6158       | 6747        | 7256        | 5930         | 5400                |
| CA         | True       | 36700      | 35714      | 38963       | 37347       | 33913        | 34562               |
| NA1        | False      | 5710       | 6158       | 6747        | 7256        | 5930         | 5400                |
| CA         | True       | 36700      | 35714      | 38963       | 37347       | 33913        | 34562               |
| NA1        | True       | 12656      | 12316      | 13436       | 12879       | 11695        | 5400                |
| CA         | True       | 36700      | 35714      | 38963       | 37347       | 33913        | 34562               |
| NA1        | False      | 5710       | 6158       | 6747        | 7256        | 5930         | 11918               |
| CA         | True       | 36700      | 35714      | 38963       | 34150       | 33913        | 34562               |
| NA1        | False      | 5710       | 6158       | 6747        | 7256        | 5930         | 5400                |
| CA         | True       | 33572      | 35714      | 38963       | 37347       | 33913        | 31647               |
| 2xBlossom  | True       | 34998      | 34057      | 29064       | 27859       | 32341        | 34562               |
| Total      |            | 430590     | 421429     | 422373      | 408013      | 400513       | 405603              |
| DPS        |            | 25328      | 24789      | 24845       | 24000       | 23559        | 23859               |

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
