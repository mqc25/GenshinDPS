# GenshinDPS

## Instruction
Run the main python file

## Setup
Diluc only dmg calculate for Diluc/XQ/Benny/Sucrose comp over 15s rotation (3s for support)

Diluc lvl 90, 6/6/6 Talent with WGS R1 no skill proc, 4 CW with CD/Pyro/ATK, 11 CR rolls, 4 CD rolls

Benny has Aquila with T6 Q and NO set

Sucrose give 200 EM and VV shred

| Buff status                | BaseATK | ATK% | ATK  | CR | CD  | DMG_Bonus | EM  |
|----------------------------|---------|------|------|----|-----|-----------|-----|
| No buff                    | 943     | 116  | 2350 | 66 | 139 | 82        | 0   |
| With team buff + resonance | 943     | 161  | 3452 | 66 | 139 | 82        | 200 |

Res multiplier: 1.15 Def multiplier: 0.49

Vape multiplier: 2.25 Enemy multiplier: 0.56

| ATK Sequence | DMG       | Vape?         |
|--------------|-----------|---------------|
| Q initial    | 43138.20  | True          |
| Q_DoT        | 22514.74  | False         |
| NA1          | 19624.42  | True          |
| E1           | 19892.34  | True          |
| NA1          | 20434.90  | False         |
| E2           | 21416.05  | True          |
| NA1          | 21245.38  | False         |
| E3           | 29435.23  | True          |
| NA1          | 22055.86  | True          |
| NA2          | 9593.04   | False         |
| NA3          | 24297.31  | True          |
| Total        | 253647.46 | DPS: 16909.83 |
