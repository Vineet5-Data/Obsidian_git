======================================================================
a_v207_jobboard: 707-1053 (40.2%)
======================================================================
op                     US/win  US/loss  OPP/loss  loss-win opp-us(loss)
PASS                    103.4    104.7      87.3      +1.3        -17.3
NORTH                   144.3    143.7     139.6      -0.6         -4.1
EAST                    107.4    106.8     119.0      -0.6        +12.2
WEST                    140.4    139.9     152.9      -0.5        +13.0
HARVEST                  57.9     58.3      57.4      +0.4         -0.9
SOUTH                    94.9     94.6      97.3      -0.3         +2.8
FEED                     43.6     43.8      47.7      +0.2         +3.9
DROP                     22.0     22.2       1.9      +0.2        -20.3
DIG                       2.9      2.8       3.6      -0.1         +0.8
COLLECT_FERTILIZER       49.9     49.8      45.9      -0.1         -3.9
CARE                     49.8     49.7      47.7      -0.1         -2.1
FERTILIZE                 8.2      8.3       9.4      +0.1         +1.2
PLANT                    25.9     26.0      27.0      +0.1         +1.0
WATER                   129.2    129.1     133.8      -0.1         +4.7
PICKUP                   16.3     16.3      19.6      +0.0         +3.3
mkt:BUY_ANIMAL            1.4      1.4       1.3      -0.0         -0.1
mkt:BUY_PRODUCT           8.8      8.8      11.4      +0.0         +2.6
mkt:HIRE                 41.0     41.0      40.2      -0.0         -0.9
PLACE                     2.1      2.1       7.6      -0.0         +5.5
mkt:SELL                 31.3     31.2      65.5      -0.0        +34.3
BUILD_PASTURE             1.8      1.8       2.2      -0.0         +0.4
mkt:BUY_SEED             15.5     15.5      14.3      -0.0         -1.1

money delta by day, avg across 1053 losses (negative = behind):
  day  5: money      +869  plants 9.0/19.0  animals 6.0/6.0
  day 10: money   -12,120  plants 42.8/27.3  animals 15.4/11.3
  day 15: money    -1,659  plants 55.3/53.4  animals 16.0/13.7
  day 20: money    -3,085  plants 56.0/58.6  animals 16.0/14.2
  day 25: money    -6,959  plants 54.3/54.5  animals 16.1/14.1

worst 10 losses:
  t_94174874_1         seed=1042155578   margin=   -42,310
  t_94177280_0         seed=1042155578   margin=   -42,013
  t_94135296_0         seed=1042155578   margin=   -41,328
  t_94142273_0         seed=1161830769   margin=   -40,417
  t_94178232_0         seed=1161830769   margin=   -40,263
  t_94142273_0         seed=535203464    margin=   -39,467
  t_94142273_0         seed=535203464    margin=   -39,373
  t_94177272_0         seed=1161830769   margin=   -39,205
  t_94177272_0         seed=1161830769   margin=   -39,009
  t_94178232_0         seed=1042155578   margin=   -38,727

-- SERVICE TELEMETRY: ALL GAMES --

  days 0-14 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1069.8    92.4%     27.2%      164.3     10.93   99.8%      0.0%
    COLLECT_FERTILIZER        953.4    95.3%     37.9%      148.4      9.89  100.0%      0.0%
    FEED                     1576.0    96.3%     21.0%      151.4      9.89   98.0%      0.0%
    FERTILIZE                  67.0    52.1%     34.4%        4.4      0.29  100.0%      0.0%
    HARVEST                   624.7    73.7%     28.1%       60.0      3.99   99.8%      0.0%
    PLANT                    2215.0    72.7%     11.5%       77.3      5.15  100.0%      0.0%
    WATER                    4297.5    60.6%     33.4%      364.4     23.32   96.0%      0.0%
    movement turns/game-day: 111.38   PASS turns/game-day: 48.24
    animal cap ticks: EGG=0.37/day, MILK=2.64/day, WOOL=1.32/day
    crop expiry with held yield: STRAWBERRY=66.82/game, TOMATO=61.41/game

  days 15-19 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      610.8    80.0%     22.2%       79.5     15.87   99.8%      0.0%
    COLLECT_FERTILIZER        566.3    85.3%     29.3%       79.7     15.92   99.8%      0.0%
    FEED                      988.0    89.6%     11.9%       64.8     12.48   96.4%      0.0%
    FERTILIZE                 564.2    51.3%     18.8%       23.1      4.61  100.0%      0.0%
    HARVEST                  1406.2    47.6%     23.5%       96.5     19.26   99.8%      0.0%
    PLANT                     541.7    51.4%     18.2%       34.7      6.94  100.0%      0.0%
    WATER                    3893.6    45.2%     31.9%      258.9     49.57   95.7%      0.0%
    movement turns/game-day: 147.78   PASS turns/game-day: 6.21
    animal cap ticks: EGG=0.06/day, MILK=2.06/day, WOOL=0.21/day
    crop expiry with held yield: CARROT=0.02/game, STRAWBERRY=460.46/game, TOMATO=89.11/game, WHEAT=0.16/game

  days 20-24 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      610.8    77.9%     24.4%       79.5     15.87   99.8%      0.0%
    COLLECT_FERTILIZER        598.0    79.3%     26.2%       79.6     15.89   99.8%      0.0%
    FEED                      937.2    86.3%     13.0%       66.9     13.09   97.8%      0.0%
    FERTILIZE                 848.3    48.9%     14.3%       26.6      5.32  100.0%      0.0%
    HARVEST                  2554.1    45.2%     23.6%      161.9     32.25   99.6%      0.0%
    PLANT                     342.4    53.1%     38.6%       54.0     10.81  100.0%      0.0%
    WATER                    3653.6    43.2%     29.5%      242.6     45.69   94.2%      0.0%
    movement turns/game-day: 135.45   PASS turns/game-day: 2.21
    animal cap ticks: EGG=0.01/day
    crop expiry with held yield: CARROT=0.12/game, STRAWBERRY=1015.44/game, TOMATO=184.91/game, WHEAT=0.23/game

  days 25-29 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      489.4    83.6%     27.6%       64.0     12.76   99.7%      0.0%
    COLLECT_FERTILIZER        611.9    84.6%     26.9%       80.0     15.97   99.8%      0.0%
    FEED                      723.1    90.3%     16.0%       57.3     11.11   97.0%      0.0%
    FERTILIZE                 290.8    51.7%     14.7%        9.9      1.98  100.0%      0.0%
    HARVEST                  2103.8    53.3%     24.8%      133.9     26.64   99.7%      0.2%
    PLANT                     216.5    46.5%     43.5%       35.8      7.16  100.0%      0.0%
    WATER                    1999.5    49.5%     30.1%      139.0     25.22   90.7%      0.0%
    movement turns/game-day: 138.61   PASS turns/game-day: 8.96
    animal cap ticks: EGG=0.06/day, WOOL=0.03/day
    crop expiry with held yield: MELON=0.01/game, STRAWBERRY=232.75/game, TOMATO=179.24/game, WHEAT=0.53/game

-- SERVICE TELEMETRY: LOSSES ONLY --

  days 0-14 (telemetry games=1053)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1067.7    92.4%     27.1%      164.2     10.93   99.8%      0.0%
    COLLECT_FERTILIZER        952.6    95.3%     37.9%      148.4      9.89  100.0%      0.0%
    FEED                     1573.5    96.4%     20.9%      151.4      9.89   98.0%      0.0%
    FERTILIZE                  66.7    51.9%     34.6%        4.4      0.29  100.0%      0.0%
    HARVEST                   627.6    73.5%     28.0%       60.1      4.00   99.8%      0.0%
    PLANT                    2196.5    72.8%     11.6%       77.3      5.15  100.0%      0.0%
    WATER                    4298.1    60.5%     33.3%      363.9     23.29   96.0%      0.0%
    movement turns/game-day: 111.22   PASS turns/game-day: 48.47
    animal cap ticks: EGG=0.35/day, MILK=2.67/day, WOOL=1.26/day
    crop expiry with held yield: STRAWBERRY=67.58/game, TOMATO=61.45/game

  days 15-19 (telemetry games=1053)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      612.1    80.0%     22.2%       79.5     15.86   99.7%      0.0%
    COLLECT_FERTILIZER        569.0    85.0%     29.1%       79.7     15.92   99.8%      0.0%
    FEED                      985.5    89.8%     12.2%       65.2     12.56   96.3%      0.0%
    FERTILIZE                 565.5    51.8%     18.4%       23.0      4.59  100.0%      0.0%
    HARVEST                  1400.4    47.4%     23.6%       96.5     19.26   99.8%      0.0%
    PLANT                     543.2    51.2%     18.3%       35.2      7.03  100.0%      0.0%
    WATER                    3889.3    45.2%     32.0%      259.8     49.77   95.8%      0.0%
    movement turns/game-day: 147.60   PASS turns/game-day: 6.06
    animal cap ticks: EGG=0.07/day, MILK=2.10/day, WOOL=0.21/day
    crop expiry with held yield: CARROT=0.03/game, STRAWBERRY=454.14/game, TOMATO=82.67/game, WHEAT=0.09/game

  days 20-24 (telemetry games=1053)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      610.7    77.8%     24.5%       79.4     15.84   99.8%      0.0%
    COLLECT_FERTILIZER        601.7    78.7%     25.8%       79.5     15.87   99.8%      0.0%
    FEED                      934.9    86.5%     13.1%       67.0     13.10   97.8%      0.0%
    FERTILIZE                 857.7    48.9%     14.3%       26.9      5.37  100.0%      0.0%
    HARVEST                  2583.0    45.0%     23.7%      163.7     32.62   99.6%      0.0%
    PLANT                     354.2    52.3%     38.0%       54.0     10.79  100.0%      0.0%
    WATER                    3662.0    43.1%     29.4%      243.2     45.77   94.1%      0.0%
    movement turns/game-day: 135.00   PASS turns/game-day: 2.27
    animal cap ticks: EGG=0.00/day
    crop expiry with held yield: CARROT=0.12/game, STRAWBERRY=1029.69/game, TOMATO=187.71/game, WHEAT=0.20/game

  days 25-29 (telemetry games=1053)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      487.8    83.8%     27.7%       63.9     12.75   99.7%      0.0%
    COLLECT_FERTILIZER        611.8    84.6%     26.8%       79.9     15.95   99.8%      0.0%
    FEED                      716.9    90.6%     16.3%       57.5     11.16   97.0%      0.0%
    FERTILIZE                 295.5    52.0%     14.5%       10.1      2.01  100.0%      0.0%
    HARVEST                  2101.5    53.4%     24.8%      133.4     26.54   99.7%      0.3%
    PLANT                     219.4    46.3%     43.1%       35.7      7.14  100.0%      0.0%
    WATER                    1987.7    49.7%     29.9%      138.0     25.04   90.7%      0.0%
    movement turns/game-day: 138.61   PASS turns/game-day: 9.17
    animal cap ticks: EGG=0.03/day, WOOL=0.02/day
    crop expiry with held yield: STRAWBERRY=225.78/game, TOMATO=180.89/game, WHEAT=0.55/game

==============================================================================
a_v207_jobboard: 707-1053 (40.2%)
==============================================================================

-- ALL GAMES (n=1760) --
  net cash generated, day 0-19     us    +33,465.5   opp    +30,968.5   gap (opp-us)     -2,497.0   (n=1760)
  cash residual (should be ~0), day 0-19     us       +469.0   opp       -876.1   gap (opp-us)     -1,345.0   (n=1760)
    revenue (filled, exact):
      WOOL         us +12,313.13   opp  +7,213.75   gap  -5,099.37
      WHEAT        us  +1,279.55   opp  +5,762.66   gap  +4,483.11
      MELON        us +12,406.06   opp +16,553.76   gap  +4,147.70
      FERTILIZER   us +12,715.77   opp  +9,508.86   gap  -3,206.91
      MILK         us +15,297.38   opp +13,183.14   gap  -2,114.24
      EGG          us  +1,260.76   opp     +10.39   gap  -1,250.36
      STRAWBERRY   us  +6,501.96   opp  +7,631.69   gap  +1,129.73
      TOMATO       us    +626.52   opp      +0.00   gap    -626.52
      CARROT       us    +149.41   opp      +0.90   gap    -148.51
    avg realized price / unit (revenue/sold):
      TOMATO       us     +66.55   opp      +0.00   gap     -66.55
      MELON        us    +171.42   opp    +203.44   gap     +32.02
      WOOL         us    +160.99   opp    +129.86   gap     -31.14
      MILK         us    +183.14   opp    +164.52   gap     -18.62
      WHEAT        us     +36.65   opp     +43.13   gap      +6.47
      CARROT       us     +44.85   opp     +39.40   gap      -5.45
      FERTILIZER   us     +68.95   opp     +64.06   gap      -4.89
      STRAWBERRY   us    +202.68   opp    +201.77   gap      -0.91
      EGG          us     +53.45   opp     +52.57   gap      -0.88
    production (units, exact):
      WHEAT        us     +59.92   opp    +119.87   gap     +59.95
      FERTILIZER   us    +211.56   opp    +170.73   gap     -40.83
      EGG          us     +23.59   opp      +0.20   gap     -23.39
      WOOL         us     +77.93   opp     +55.89   gap     -22.04
      TOMATO       us      +9.41   opp      +0.00   gap      -9.41
      MELON        us     +72.71   opp     +81.76   gap      +9.05
      STRAWBERRY   us     +32.08   opp     +37.89   gap      +5.81
      MILK         us     +84.09   opp     +80.24   gap      -3.85
      CARROT       us      +3.33   opp      +0.02   gap      -3.31
    seed spend:
      STRAWBERRY   us  +3,026.65   opp  +3,830.68   gap    +804.03
      MELON        us  +1,828.50   opp  +1,229.09   gap    -599.41
      TOMATO       us    +522.33   opp      +3.98   gap    -518.35
      WHEAT        us    +452.53   opp    +738.07   gap    +285.54
      CARROT       us    +102.85   opp    +134.77   gap     +31.92
    animal spend:
      SHEEP        us  +2,708.24   opp  +3,795.45   gap  +1,087.22
      GOOSE        us    +588.75   opp      +3.41   gap    -585.34
      COW          us  +3,448.41   opp  +3,118.18   gap    -330.23
    buy_product spend (filled, exact):
      WHEAT        us  +7,860.66   opp  +9,356.47   gap  +1,495.82
  land spend, day 0-19     us     +3,000.0   opp     +4,329.5   gap (opp-us)     +1,329.5   (n=1760)
  wage spend, day 0-19     us     +5,077.1   opp     +3,233.1   gap (opp-us)     -1,844.1   (n=1760)
  feed actions (count), day 0-19     us       +215.7   opp       +203.9   gap (opp-us)        -11.9   (n=1760)
  fertilize actions (count), day 0-19     us        +27.0   opp        +21.8   gap (opp-us)         -5.2   (n=1760)
    crop tiles, end of window:
      WHEAT        us     +11.49   opp     +25.11   gap     +13.62
      TOMATO       us      +8.54   opp      +0.08   gap      -8.47
      MELON        us      +4.76   opp      +0.35   gap      -4.40
      STRAWBERRY   us     +30.13   opp     +33.61   gap      +3.48
      CARROT       us      +1.90   opp      +0.00   gap      -1.90
    herd, end of window:
      GOOSE        us      +1.96   opp      +0.01   gap      -1.95
      SHEEP        us      +5.42   opp      +6.90   gap      +1.48
      COW          us      +8.62   opp      +7.17   gap      -1.45
  net cash generated, day 20-24    us    +24,723.4   opp    +27,644.5   gap (opp-us)     +2,921.0   (n=1760)
  cash residual (should be ~0), day 20-24    us        -23.5   opp        -12.6   gap (opp-us)        +10.8   (n=1760)
    revenue (filled, exact):
      WHEAT        us    +908.92   opp  +9,455.80   gap  +8,546.88
      STRAWBERRY   us +14,804.37   opp +17,254.72   gap  +2,450.36
      MILK         us  +5,656.97   opp  +6,882.76   gap  +1,225.80
      TOMATO       us  +1,170.81   opp      +2.21   gap  -1,168.60
      MELON        us  +1,202.76   opp    +171.71   gap  -1,031.05
      EGG          us    +845.50   opp      +4.93   gap    -840.58
      WOOL         us  +2,743.75   opp  +3,276.27   gap    +532.53
      CARROT       us    +238.16   opp      +0.00   gap    -238.16
      FERTILIZER   us    +919.54   opp  +1,022.61   gap    +103.06
    avg realized price / unit (revenue/sold):
      CARROT       us     +48.32   opp      +0.00   gap     -48.32
      WOOL         us    +141.58   opp    +102.37   gap     -39.21
      MILK         us    +158.54   opp    +133.70   gap     -24.84
      STRAWBERRY   us    +167.33   opp    +158.82   gap      -8.51
      MELON        us     +87.53   opp     +82.21   gap      -5.32
      TOMATO       us     +72.71   opp     +68.23   gap      -4.48
      FERTILIZER   us     +26.79   opp     +23.88   gap      -2.90
      EGG          us     +56.34   opp     +54.22   gap      -2.12
      WHEAT        us     +48.57   opp     +49.20   gap      +0.64
    production (units, exact):
      WHEAT        us     +57.72   opp     +92.76   gap     +35.04
      STRAWBERRY   us     +89.44   opp    +109.79   gap     +20.35
      TOMATO       us     +16.10   opp      +0.33   gap     -15.77
      MILK         us     +35.98   opp     +51.42   gap     +15.44
      EGG          us     +15.01   opp      +0.09   gap     -14.92
      WOOL         us     +18.58   opp     +32.06   gap     +13.48
      FERTILIZER   us     +65.09   opp     +78.28   gap     +13.19
      MELON        us     +13.47   opp      +1.70   gap     -11.77
      CARROT       us      +4.93   opp      +0.00   gap      -4.93
    seed spend:
      WHEAT        us    +551.68   opp    +322.39   gap    -229.29
      CARROT       us      +1.92   opp     +42.73   gap     +40.81
    animal spend:
      SHEEP        us     +26.70   opp      +0.00   gap     -26.70
      GOOSE        us     +12.78   opp      +0.00   gap     -12.78
    buy_product spend (filled, exact):
      WHEAT        us  +1,317.62   opp  +8,292.71   gap  +6,975.09
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 20-24    us     +1,880.0   opp     +1,781.3   gap (opp-us)        -98.7   (n=1760)
  feed actions (count), day 20-24    us        +67.0   opp        +74.4   gap (opp-us)         +7.3   (n=1760)
  fertilize actions (count), day 20-24    us        +26.7   opp        +35.6   gap (opp-us)         +8.9   (n=1760)
    crop tiles, end of window:
      TOMATO       us      +5.17   opp      +0.01   gap      -5.16
      STRAWBERRY   us     +23.06   opp     +25.36   gap      +2.30
      CARROT       us      +0.06   opp      +1.88   gap      +1.82
      MELON        us      +1.51   opp      +0.00   gap      -1.51
      WHEAT        us     +25.56   opp     +24.36   gap      -1.20
    herd, end of window:
      GOOSE        us      +2.00   opp      +0.01   gap      -1.99
      COW          us      +8.62   opp      +7.16   gap      -1.46
      SHEEP        us      +5.47   opp      +6.86   gap      +1.39
  net cash generated, day 25-29    us    +23,890.1   opp    +24,881.3   gap (opp-us)       +991.2   (n=1760)
  cash residual (should be ~0), day 25-29    us       -115.2   opp        +69.8   gap (opp-us)       +185.0   (n=1760)
    revenue (filled, exact):
      WHEAT        us  +4,384.89   opp +13,214.43   gap  +8,829.54
      TOMATO       us  +2,828.46   opp     +28.63   gap  -2,799.83
      STRAWBERRY   us  +5,694.19   opp  +7,976.04   gap  +2,281.85
      WOOL         us  +3,251.26   opp  +4,435.64   gap  +1,184.39
      EGG          us  +1,116.03   opp      +7.51   gap  -1,108.52
      MILK         us  +7,519.20   opp  +6,886.79   gap    -632.41
      MELON        us    +584.29   opp      +0.00   gap    -584.29
      CARROT       us    +132.60   opp    +641.86   gap    +509.27
      FERTILIZER   us    +586.41   opp    +338.27   gap    -248.14
    avg realized price / unit (revenue/sold):
      MELON        us     +83.67   opp      +0.00   gap     -83.67
      WOOL         us    +125.63   opp    +108.31   gap     -17.32
      MILK         us    +145.00   opp    +129.17   gap     -15.83
      CARROT       us     +66.41   opp     +58.07   gap      -8.35
      TOMATO       us     +85.70   opp     +83.16   gap      -2.53
      EGG          us     +59.33   opp     +57.00   gap      -2.33
      STRAWBERRY   us    +113.47   opp    +114.63   gap      +1.16
      FERTILIZER   us      +6.98   opp      +7.46   gap      +0.48
      WHEAT        us     +50.53   opp     +50.76   gap      +0.23
    production (units, exact):
      WHEAT        us    +120.25   opp    +167.76   gap     +47.51
      FERTILIZER   us     +90.15   opp     +54.41   gap     -35.74
      TOMATO       us     +33.01   opp      +0.05   gap     -32.96
      STRAWBERRY   us     +49.22   opp     +68.40   gap     +19.19
      EGG          us     +18.81   opp      +0.13   gap     -18.68
      WOOL         us     +25.24   opp     +40.72   gap     +15.49
      CARROT       us      +2.00   opp     +11.15   gap      +9.15
      MELON        us      +6.92   opp      +0.00   gap      -6.92
      MILK         us     +51.00   opp     +53.43   gap      +2.43
    seed spend:
      WHEAT        us    +330.98   opp    +265.57   gap     -65.41
      CARROT       us     +28.85   opp     +48.18   gap     +19.33
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +421.73   opp  +7,335.48   gap  +6,913.75
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 25-29    us     +1,540.9   opp       +928.8   gap (opp-us)       -612.1   (n=1760)
  feed actions (count), day 25-29    us        +57.6   opp        +52.7   gap (opp-us)         -4.8   (n=1760)
  fertilize actions (count), day 25-29    us        +10.3   opp         +9.3   gap (opp-us)         -1.0   (n=1760)
    crop tiles, end of window:
      STRAWBERRY   us      +2.31   opp      +1.40   gap      -0.91
      TOMATO       us      +0.65   opp      +0.01   gap      -0.63
      WHEAT        us      +0.35   opp      +0.81   gap      +0.45
    herd, end of window:
      GOOSE        us      +2.00   opp      +0.01   gap      -1.99
      COW          us      +8.62   opp      +7.12   gap      -1.50
      SHEEP        us      +5.47   opp      +5.70   gap      +0.23

-- LOSSES ONLY (n=1053) --
  net cash generated, day 0-19     us    +33,131.3   opp    +34,384.2   gap (opp-us)     +1,252.9   (n=1053)
  cash residual (should be ~0), day 0-19     us       +506.4   opp       -875.6   gap (opp-us)     -1,382.1   (n=1053)
    revenue (filled, exact):
      MELON        us +11,816.68   opp +17,656.81   gap  +5,840.13
      WHEAT        us  +1,319.43   opp  +5,764.06   gap  +4,444.63
      WOOL         us +11,702.94   opp  +7,451.43   gap  -4,251.51
      FERTILIZER   us +12,710.66   opp  +9,574.72   gap  -3,135.94
      MILK         us +15,966.78   opp +14,358.99   gap  -1,607.79
      STRAWBERRY   us  +6,655.54   opp  +8,114.60   gap  +1,459.06
      EGG          us  +1,269.00   opp      +5.27   gap  -1,263.73
      TOMATO       us    +589.35   opp      +0.00   gap    -589.35
      CARROT       us    +146.19   opp      +1.36   gap    -144.83
    avg realized price / unit (revenue/sold):
      TOMATO       us     +66.27   opp      +0.00   gap     -66.27
      MELON        us    +165.54   opp    +198.66   gap     +33.12
      WOOL         us    +157.49   opp    +137.41   gap     -20.08
      MILK         us    +186.08   opp    +170.08   gap     -16.00
      WHEAT        us     +36.87   opp     +43.17   gap      +6.31
      FERTILIZER   us     +68.93   opp     +63.82   gap      -5.12
      CARROT       us     +44.08   opp     +39.78   gap      -4.31
      EGG          us     +53.28   opp     +52.38   gap      -0.90
      STRAWBERRY   us    +208.99   opp    +209.45   gap      +0.46
    production (units, exact):
      WHEAT        us     +61.75   opp    +118.64   gap     +56.89
      FERTILIZER   us    +211.39   opp    +170.88   gap     -40.51
      EGG          us     +23.82   opp      +0.10   gap     -23.72
      WOOL         us     +75.32   opp     +54.64   gap     -20.68
      MELON        us     +71.86   opp     +89.44   gap     +17.59
      TOMATO       us      +8.89   opp      +0.00   gap      -8.89
      STRAWBERRY   us     +31.85   opp     +38.83   gap      +6.98
      CARROT       us      +3.32   opp      +0.03   gap      -3.28
      MILK         us     +86.25   opp     +84.56   gap      -1.69
    seed spend:
      STRAWBERRY   us  +3,054.32   opp  +3,790.22   gap    +735.90
      TOMATO       us    +522.46   opp      +2.28   gap    -520.18
      MELON        us  +1,768.51   opp  +1,265.03   gap    -503.48
      WHEAT        us    +462.72   opp    +737.50   gap    +274.79
      CARROT       us    +101.44   opp    +145.91   gap     +44.46
    animal spend:
      SHEEP        us  +2,555.56   opp  +3,462.96   gap    +907.41
      GOOSE        us    +592.88   opp      +1.71   gap    -591.17
      COW          us  +3,565.05   opp  +3,269.90   gap    -295.16
    buy_product spend (filled, exact):
      WHEAT        us  +7,841.90   opp  +9,344.62   gap  +1,502.72
  land spend, day 0-19     us     +3,000.0   opp     +4,120.6   gap (opp-us)     +1,120.6   (n=1053)
  wage spend, day 0-19     us     +5,074.0   opp     +3,277.9   gap (opp-us)     -1,796.1   (n=1053)
  feed actions (count), day 0-19     us       +216.2   opp       +203.1   gap (opp-us)        -13.1   (n=1053)
  fertilize actions (count), day 0-19     us        +26.9   opp        +20.6   gap (opp-us)         -6.3   (n=1053)
    crop tiles, end of window:
      WHEAT        us     +11.97   opp     +25.89   gap     +13.93
      TOMATO       us      +8.56   opp      +0.05   gap      -8.51
      STRAWBERRY   us     +30.41   opp     +34.53   gap      +4.12
      MELON        us      +3.94   opp      +0.16   gap      -3.78
      CARROT       us      +1.90   opp      +0.00   gap      -1.90
    herd, end of window:
      GOOSE        us      +1.98   opp      +0.01   gap      -1.97
      SHEEP        us      +5.11   opp      +6.38   gap      +1.27
      COW          us      +8.91   opp      +7.77   gap      -1.14
  net cash generated, day 20-24    us    +25,933.2   opp    +32,299.7   gap (opp-us)     +6,366.5   (n=1053)
  cash residual (should be ~0), day 20-24    us        -11.7   opp        -16.3   gap (opp-us)         -4.5   (n=1053)
    revenue (filled, exact):
      WHEAT        us    +933.36   opp  +9,349.14   gap  +8,415.77
      STRAWBERRY   us +15,946.84   opp +19,641.32   gap  +3,694.48
      MILK         us  +6,010.07   opp  +8,441.99   gap  +2,431.92
      TOMATO       us  +1,162.94   opp      +2.17   gap  -1,160.76
      WOOL         us  +2,706.38   opp  +3,854.75   gap  +1,148.38
      EGG          us    +841.24   opp      +2.48   gap    -838.76
      MELON        us    +903.42   opp    +118.14   gap    -785.28
      CARROT       us    +230.93   opp      +0.00   gap    -230.93
      FERTILIZER   us    +898.02   opp    +986.83   gap     +88.81
    avg realized price / unit (revenue/sold):
      CARROT       us     +47.21   opp      +0.00   gap     -47.21
      MELON        us     +74.51   opp    +105.79   gap     +31.28
      MILK         us    +160.05   opp    +141.03   gap     -19.02
      WOOL         us    +140.95   opp    +122.36   gap     -18.58
      STRAWBERRY   us    +177.48   opp    +171.30   gap      -6.18
      FERTILIZER   us     +26.78   opp     +23.81   gap      -2.97
      TOMATO       us     +71.57   opp     +69.36   gap      -2.21
      EGG          us     +55.89   opp     +54.42   gap      -1.47
      WHEAT        us     +48.85   opp     +49.07   gap      +0.22
    production (units, exact):
      WHEAT        us     +59.45   opp     +95.24   gap     +35.80
      STRAWBERRY   us     +90.51   opp    +115.92   gap     +25.41
      MILK         us     +37.72   opp     +59.79   gap     +22.07
      TOMATO       us     +16.25   opp      +0.14   gap     -16.10
      EGG          us     +15.05   opp      +0.05   gap     -15.01
      WOOL         us     +18.87   opp     +31.46   gap     +12.60
      FERTILIZER   us     +64.98   opp     +77.13   gap     +12.14
      MELON        us     +11.67   opp      +0.55   gap     -11.12
      CARROT       us      +4.89   opp      +0.00   gap      -4.89
    seed spend:
      WHEAT        us    +550.98   opp    +317.16   gap    -233.82
      CARROT       us      +0.57   opp     +46.91   gap     +46.34
      MELON        us      +0.15   opp      +0.00   gap      -0.15
    animal spend:
      SHEEP        us     +28.02   opp      +0.00   gap     -28.02
      GOOSE        us      +5.13   opp      +0.00   gap      -5.13
    buy_product spend (filled, exact):
      WHEAT        us  +1,246.90   opp  +7,988.83   gap  +6,741.93
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1053)
  wage spend, day 20-24    us     +1,880.0   opp     +1,760.5   gap (opp-us)       -119.5   (n=1053)
  feed actions (count), day 20-24    us        +67.1   opp        +73.5   gap (opp-us)         +6.4   (n=1053)
  fertilize actions (count), day 20-24    us        +27.0   opp        +35.8   gap (opp-us)         +8.8   (n=1053)
    crop tiles, end of window:
      TOMATO       us      +5.21   opp      +0.02   gap      -5.20
      STRAWBERRY   us     +23.47   opp     +26.46   gap      +2.99
      CARROT       us      +0.00   opp      +2.10   gap      +2.10
      MELON        us      +1.07   opp      +0.00   gap      -1.07
      WHEAT        us     +25.63   opp     +24.76   gap      -0.87
    herd, end of window:
      GOOSE        us      +1.99   opp      +0.01   gap      -1.99
      SHEEP        us      +5.17   opp      +6.37   gap      +1.20
      COW          us      +8.91   opp      +7.76   gap      -1.16
  net cash generated, day 25-29    us    +24,023.1   opp    +28,142.2   gap (opp-us)     +4,119.2   (n=1053)
  cash residual (should be ~0), day 25-29    us       -119.0   opp        +80.6   gap (opp-us)       +199.6   (n=1053)
    revenue (filled, exact):
      WHEAT        us  +4,383.46   opp +13,175.08   gap  +8,791.62
      STRAWBERRY   us  +5,996.07   opp  +9,173.34   gap  +3,177.28
      TOMATO       us  +2,652.18   opp     +14.19   gap  -2,637.98
      WOOL         us  +3,347.08   opp  +5,205.14   gap  +1,858.06
      EGG          us  +1,103.61   opp      +3.67   gap  -1,099.93
      CARROT       us     +35.04   opp    +676.50   gap    +641.46
      MELON        us    +348.02   opp      +0.00   gap    -348.02
      MILK         us  +7,759.23   opp  +8,107.17   gap    +347.94
      FERTILIZER   us    +581.01   opp    +345.87   gap    -235.13
    avg realized price / unit (revenue/sold):
      MELON        us     +70.95   opp      +0.00   gap     -70.95
      CARROT       us     +80.56   opp     +59.07   gap     -21.49
      MILK         us    +142.97   opp    +133.45   gap      -9.52
      STRAWBERRY   us    +118.52   opp    +122.13   gap      +3.62
      WOOL         us    +131.52   opp    +128.45   gap      -3.06
      TOMATO       us     +80.33   opp     +78.25   gap      -2.08
      EGG          us     +58.71   opp     +56.88   gap      -1.83
      FERTILIZER   us      +6.86   opp      +7.59   gap      +0.73
      WHEAT        us     +50.60   opp     +50.77   gap      +0.18
    production (units, exact):
      WHEAT        us    +121.10   opp    +169.06   gap     +47.96
      FERTILIZER   us     +90.51   opp     +54.30   gap     -36.21
      TOMATO       us     +33.01   opp      +0.07   gap     -32.95
      STRAWBERRY   us     +49.93   opp     +73.82   gap     +23.89
      EGG          us     +18.80   opp      +0.06   gap     -18.73
      WOOL         us     +24.78   opp     +40.29   gap     +15.51
      CARROT       us      +0.43   opp     +11.47   gap     +11.04
      MILK         us     +53.66   opp     +60.81   gap      +7.15
      MELON        us      +4.88   opp      +0.00   gap      -4.88
    seed spend:
      WHEAT        us    +339.83   opp    +277.72   gap     -62.11
      CARROT       us      +8.21   opp     +45.98   gap     +37.78
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +412.51   opp  +7,244.92   gap  +6,832.41
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1053)
  wage spend, day 25-29    us     +1,541.1   opp       +909.6   gap (opp-us)       -631.5   (n=1053)
  feed actions (count), day 25-29    us        +57.8   opp        +52.4   gap (opp-us)         -5.4   (n=1053)
  fertilize actions (count), day 25-29    us        +10.4   opp         +8.8   gap (opp-us)         -1.6   (n=1053)
    crop tiles, end of window:
      STRAWBERRY   us      +2.20   opp      +1.48   gap      -0.72
      TOMATO       us      +0.67   opp      +0.02   gap      -0.65
      WHEAT        us      +0.37   opp      +0.73   gap      +0.36
    herd, end of window:
      GOOSE        us      +1.99   opp      +0.01   gap      -1.99
      COW          us      +8.91   opp      +7.72   gap      -1.19
      SHEEP        us      +5.17   opp      +5.32   gap      +0.16