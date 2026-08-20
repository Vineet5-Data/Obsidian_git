======================================================================
a_v206_wheat_mirror: 1040-720 (59.1%)
======================================================================
op                     US/win  US/loss  OPP/loss  loss-win opp-us(loss)
WATER                   118.5    116.4     133.8      -2.0        +17.4
EAST                    118.9    120.5     118.6      +1.6         -1.9
WEST                    144.7    146.2     154.0      +1.5         +7.9
PLANT                    22.5     21.4      26.9      -1.2         +5.6
SOUTH                   109.4    110.3      96.8      +0.9        -13.6
mkt:BUY_SEED             12.8     12.1      14.2      -0.7         +2.1
PASS                     94.9     95.4      87.9      +0.5         -7.5
FERTILIZE                 6.5      6.0       9.6      -0.5         +3.6
HARVEST                  52.4     52.0      57.4      -0.4         +5.5
DIG                       2.1      1.8       3.7      -0.3         +1.9
COLLECT_FERTILIZER       47.3     47.1      45.7      -0.2         -1.4
DROP                     24.4     24.6       2.0      +0.2        -22.5
PICKUP                   16.3     16.5      19.5      +0.1         +3.0
NORTH                   150.3    150.2     139.8      -0.1        -10.4
mkt:SELL                 32.0     31.9      65.1      -0.1        +33.1
CARE                     44.4     44.4      47.3      -0.1         +2.9
FEED                     43.3     43.2      47.2      -0.1         +4.0
BUILD_PASTURE             1.8      1.8       2.2      -0.1         +0.4
mkt:BUY_PRODUCT           7.5      7.6      11.4      +0.1         +3.8
PLACE                     2.1      2.1       7.5      +0.0         +5.4
mkt:HIRE                 41.0     41.0      40.2      +0.0         -0.8
mkt:BUY_ANIMAL            1.5      1.5       1.3      -0.0         -0.2

money delta by day, avg across 720 losses (negative = behind):
  day  5: money      +971  plants 9.4/18.9  animals 6.0/6.0
  day 10: money   -11,281  plants 43.1/27.4  animals 15.7/11.3
  day 15: money    -2,443  plants 52.8/52.8  animals 16.0/13.6
  day 20: money    +1,364  plants 47.5/57.8  animals 16.0/13.9
  day 25: money    -5,031  plants 45.9/54.5  animals 16.2/13.9

worst 10 losses:
  t_94139792_1         seed=1161830769   margin=   -36,457
  t_94173916_0         seed=1281505960   margin=   -32,082
  t_94134439_0         seed=1281505960   margin=   -31,660
  t_94139792_1         seed=28251350     margin=   -30,956
  t_94178201_1         seed=1788458074   margin=   -29,196
  t_94178201_1         seed=1788458074   margin=   -29,196
  t_94194055_0         seed=1788458074   margin=   -28,700
  t_94194055_0         seed=1788458074   margin=   -28,700
  t_94178232_0         seed=535203464    margin=   -27,873
  t_94138728_0         seed=1549107692   margin=   -27,675

-- SERVICE TELEMETRY: ALL GAMES --

  days 0-14 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1497.7    54.5%     37.3%      162.5     10.62   98.0%      0.0%
    COLLECT_FERTILIZER        944.5    92.5%     41.0%      148.1      9.86   99.9%      0.0%
    FEED                     1653.4    86.0%     23.9%      152.2      9.88   97.3%      0.0%
    FERTILIZE                  33.9    94.7%     20.7%        2.6      0.17  100.0%      0.0%
    HARVEST                   692.4    66.6%     30.6%       64.1      4.26   99.7%      0.0%
    PLANT                    2435.1    65.9%     12.0%       82.0      5.47  100.0%      0.0%
    WATER                    4122.0    76.5%     27.5%      363.3     23.30   96.2%      0.0%
    movement turns/game-day: 114.34   PASS turns/game-day: 45.94
    animal cap ticks: EGG=0.60/day, MILK=2.22/day, WOOL=1.24/day
    crop expiry with held yield: STRAWBERRY=32.08/game, TOMATO=15.34/game

  days 15-19 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1480.1    25.0%     33.4%       64.4     11.69   90.7%      0.0%
    COLLECT_FERTILIZER       1040.1    41.4%     38.5%       77.5     15.14   97.6%      0.0%
    FEED                     1049.6    64.4%     15.9%       63.7     12.28   96.3%      0.0%
    FERTILIZE                 737.5    86.9%      6.8%       18.1      3.63  100.0%      0.0%
    HARVEST                  1670.4    49.5%     22.4%       84.6     16.71   98.7%      0.0%
    PLANT                    1442.0    24.4%     12.2%       21.7      4.34  100.0%      0.0%
    WATER                    3452.9    62.1%     26.2%      225.9     42.94   95.0%      0.0%
    movement turns/game-day: 165.88   PASS turns/game-day: 3.51
    animal cap ticks: EGG=0.04/day, MILK=1.92/day, WOOL=0.13/day
    crop expiry with held yield: CARROT=0.00/game, STRAWBERRY=480.80/game, TOMATO=92.27/game, WHEAT=0.02/game

  days 20-24 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1374.5    24.7%     32.5%       61.0     11.30   92.5%      0.0%
    COLLECT_FERTILIZER       1342.7    32.2%     31.1%       69.9     13.11   93.8%      0.0%
    FEED                     1013.8    63.8%     17.2%       65.2     12.70   97.4%      0.0%
    FERTILIZE                 965.2    86.2%      6.6%       22.2      4.43  100.0%      0.0%
    HARVEST                  2704.8    43.0%     25.9%      132.1     26.19   99.1%      0.0%
    PLANT                    1285.3    26.6%     19.3%       36.4      7.28  100.0%      0.0%
    WATER                    2876.6    60.3%     25.9%      202.2     38.17   94.4%      0.0%
    movement turns/game-day: 159.67   PASS turns/game-day: 1.13
    animal cap ticks: EGG=0.04/day, MILK=0.45/day, WOOL=0.26/day
    crop expiry with held yield: CARROT=0.03/game, MELON=0.03/game, STRAWBERRY=1032.66/game, TOMATO=114.31/game, WHEAT=0.21/game

  days 25-29 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      917.5    31.7%     38.1%       58.9     11.35   96.4%      0.0%
    COLLECT_FERTILIZER       1246.4    33.9%     35.5%       73.1     13.99   95.7%      0.1%
    FEED                      806.6    67.9%     19.7%       56.9     10.99   96.5%      0.0%
    FERTILIZE                 356.5    79.8%      5.8%        6.3      1.26  100.0%      0.0%
    HARVEST                  2070.5    63.2%     22.7%      126.9     25.16   99.5%      0.5%
    PLANT                     661.5    39.4%     22.3%       32.3      6.45  100.0%      0.0%
    WATER                    1600.5    77.0%     24.4%      127.4     23.53   92.3%      0.0%
    movement turns/game-day: 151.53   PASS turns/game-day: 6.08
    animal cap ticks: EGG=0.04/day, MILK=0.13/day, WOOL=0.05/day
    crop expiry with held yield: CARROT=0.01/game, STRAWBERRY=276.84/game, TOMATO=148.12/game, WHEAT=0.27/game

-- SERVICE TELEMETRY: LOSSES ONLY --

  days 0-14 (telemetry games=720)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1528.7    53.5%     37.6%      162.6     10.61   97.9%      0.0%
    COLLECT_FERTILIZER        945.3    92.4%     41.1%      148.0      9.86   99.9%      0.0%
    FEED                     1663.2    85.7%     23.7%      151.7      9.84   97.3%      0.0%
    FERTILIZE                  31.7    96.9%     20.3%        2.5      0.16  100.0%      0.0%
    HARVEST                   699.7    66.1%     30.9%       64.5      4.28   99.7%      0.0%
    PLANT                    2451.0    65.4%     12.1%       81.9      5.46  100.0%      0.0%
    WATER                    4083.9    77.1%     27.3%      362.0     23.21   96.2%      0.0%
    movement turns/game-day: 114.12   PASS turns/game-day: 46.33
    animal cap ticks: EGG=0.66/day, MILK=2.24/day, WOOL=1.14/day
    crop expiry with held yield: STRAWBERRY=32.24/game, TOMATO=12.40/game

  days 15-19 (telemetry games=720)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1539.3    24.8%     32.8%       64.7     11.67   90.1%      0.0%
    COLLECT_FERTILIZER       1099.7    40.4%     37.8%       77.0     14.91   96.9%      0.0%
    FEED                     1048.8    65.0%     15.9%       64.0     12.33   96.3%      0.0%
    FERTILIZE                 749.4    89.3%      5.8%       16.2      3.25  100.0%      0.0%
    HARVEST                  1656.3    49.3%     22.7%       84.2     16.60   98.6%      0.0%
    PLANT                    1453.1    23.1%     12.2%       20.7      4.13  100.0%      0.0%
    WATER                    3379.5    62.9%     26.8%      224.5     42.80   95.3%      0.0%
    movement turns/game-day: 167.14   PASS turns/game-day: 3.28
    animal cap ticks: EGG=0.05/day, MILK=1.74/day, WOOL=0.12/day
    crop expiry with held yield: CARROT=0.01/game, STRAWBERRY=469.63/game, TOMATO=71.50/game, WHEAT=0.01/game

  days 20-24 (telemetry games=720)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1461.6    23.0%     31.5%       59.7     10.92   91.4%      0.0%
    COLLECT_FERTILIZER       1442.0    30.9%     29.7%       68.5     12.71   92.8%      0.0%
    FEED                     1036.9    62.4%     17.3%       64.9     12.64   97.4%      0.0%
    FERTILIZE                1006.2    89.1%      6.2%       22.1      4.42  100.0%      0.0%
    HARVEST                  2683.2    43.0%     27.1%      131.4     26.04   99.1%      0.0%
    PLANT                    1432.5    23.2%     18.5%       32.2      6.45  100.0%      0.0%
    WATER                    2780.7    61.5%     26.3%      197.5     37.30   94.4%      0.0%
    movement turns/game-day: 162.26   PASS turns/game-day: 1.12
    animal cap ticks: EGG=0.05/day, MILK=0.34/day, WOOL=0.30/day
    crop expiry with held yield: MELON=0.06/game, STRAWBERRY=1029.32/game, TOMATO=99.69/game, WHEAT=0.07/game

  days 25-29 (telemetry games=720)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      914.3    31.6%     38.6%       59.8     11.54   96.6%      0.0%
    COLLECT_FERTILIZER       1240.8    34.4%     35.7%       74.2     14.23   95.9%      0.1%
    FEED                      805.2    68.0%     19.8%       57.5     11.11   96.6%      0.0%
    FERTILIZE                 353.8    83.1%      5.6%        6.2      1.24  100.0%      0.0%
    HARVEST                  2033.6    64.5%     22.8%      126.1     24.98   99.5%      0.5%
    PLANT                     703.7    38.6%     21.9%       32.3      6.47  100.0%      0.0%
    WATER                    1521.2    79.0%     24.5%      126.0     23.32   92.5%      0.0%
    movement turns/game-day: 152.50   PASS turns/game-day: 5.75
    animal cap ticks: EGG=0.04/day, MILK=0.10/day, WOOL=0.07/day
    crop expiry with held yield: STRAWBERRY=256.64/game, TOMATO=137.35/game, WHEAT=0.23/game

==============================================================================
a_v206_wheat_mirror: 1040-720 (59.1%)
==============================================================================

-- ALL GAMES (n=1760) --
  net cash generated, day 0-19     us    +37,578.2   opp    +29,632.0   gap (opp-us)     -7,946.2   (n=1760)
  cash residual (should be ~0), day 0-19     us       +437.7   opp       -832.9   gap (opp-us)     -1,270.5   (n=1760)
    revenue (filled, exact):
      WOOL         us +12,899.16   opp  +7,618.44   gap  -5,280.71
      WHEAT        us  +1,253.92   opp  +5,756.34   gap  +4,502.42
      FERTILIZER   us +12,944.85   opp  +9,442.08   gap  -3,502.77
      MILK         us +15,612.02   opp +12,557.67   gap  -3,054.35
      MELON        us +13,870.85   opp +15,848.14   gap  +1,977.30
      EGG          us  +1,427.86   opp     +10.71   gap  -1,417.16
      STRAWBERRY   us  +7,732.41   opp  +7,212.72   gap    -519.69
      TOMATO       us    +396.75   opp      +0.00   gap    -396.75
      CARROT       us      +9.07   opp      +0.97   gap      -8.09
    avg realized price / unit (revenue/sold):
      TOMATO       us     +69.17   opp      +0.00   gap     -69.17
      WOOL         us    +167.24   opp    +129.88   gap     -37.36
      MELON        us    +165.18   opp    +200.10   gap     +34.91
      MILK         us    +185.57   opp    +159.98   gap     -25.59
      WHEAT        us     +36.53   opp     +42.51   gap      +5.98
      FERTILIZER   us     +67.92   opp     +64.12   gap      -3.80
      STRAWBERRY   us    +191.56   opp    +194.63   gap      +3.08
      CARROT       us     +44.21   opp     +42.90   gap      -1.31
      EGG          us     +53.75   opp     +52.92   gap      -0.82
    production (units, exact):
      WHEAT        us     +68.85   opp    +122.02   gap     +53.17
      FERTILIZER   us    +211.12   opp    +169.52   gap     -41.59
      EGG          us     +26.57   opp      +0.20   gap     -26.36
      WOOL         us     +80.55   opp     +58.99   gap     -21.56
      MELON        us     +88.97   opp     +79.54   gap      -9.43
      MILK         us     +85.56   opp     +78.60   gap      -6.96
      TOMATO       us      +5.74   opp      +0.00   gap      -5.74
      STRAWBERRY   us     +40.38   opp     +37.12   gap      -3.26
      CARROT       us      +0.21   opp      +0.02   gap      -0.18
    seed spend:
      STRAWBERRY   us  +3,010.51   opp  +3,830.68   gap    +820.17
      MELON        us  +1,744.77   opp  +1,229.09   gap    -515.68
      TOMATO       us    +409.83   opp      +3.98   gap    -405.85
      WHEAT        us    +495.22   opp    +738.07   gap    +242.85
      CARROT       us     +49.72   opp    +134.77   gap     +85.06
    animal spend:
      SHEEP        us  +2,666.76   opp  +3,795.45   gap  +1,128.69
      GOOSE        us    +659.15   opp      +3.41   gap    -655.74
      COW          us  +3,387.73   opp  +3,118.18   gap    -269.55
    buy_product spend (filled, exact):
      WHEAT        us  +7,563.75   opp  +9,251.86   gap  +1,688.11
  land spend, day 0-19     us     +3,000.0   opp     +4,317.0   gap (opp-us)     +1,317.0   (n=1760)
  wage spend, day 0-19     us     +5,143.6   opp     +3,225.4   gap (opp-us)     -1,918.2   (n=1760)
  feed actions (count), day 0-19     us       +215.5   opp       +203.7   gap (opp-us)        -11.7   (n=1760)
  fertilize actions (count), day 0-19     us        +20.3   opp        +21.8   gap (opp-us)         +1.5   (n=1760)
    crop tiles, end of window:
      WHEAT        us      +9.37   opp     +25.00   gap     +15.64
      TOMATO       us      +6.82   opp      +0.08   gap      -6.74
      MELON        us      +3.94   opp      +0.36   gap      -3.58
      STRAWBERRY   us     +29.84   opp     +33.26   gap      +3.43
      CARROT       us      +0.24   opp      +0.00   gap      -0.24
    herd, end of window:
      GOOSE        us      +2.20   opp      +0.01   gap      -2.19
      SHEEP        us      +5.33   opp      +6.89   gap      +1.56
      COW          us      +8.47   opp      +7.04   gap      -1.43
  net cash generated, day 20-24    us    +22,198.9   opp    +24,244.0   gap (opp-us)     +2,045.1   (n=1760)
  cash residual (should be ~0), day 20-24    us         +7.4   opp        -50.0   gap (opp-us)        -57.4   (n=1760)
    revenue (filled, exact):
      WHEAT        us    +801.38   opp  +9,353.19   gap  +8,551.81
      STRAWBERRY   us +12,678.17   opp +15,681.32   gap  +3,003.15
      EGG          us    +879.75   opp      +5.02   gap    -874.73
      TOMATO       us    +862.77   opp      +2.43   gap    -860.34
      MILK         us  +6,512.96   opp  +5,763.23   gap    -749.72
      MELON        us    +886.67   opp    +141.32   gap    -745.36
      FERTILIZER   us    +684.43   opp  +1,017.13   gap    +332.70
      WOOL         us  +2,678.82   opp  +2,607.36   gap     -71.46
      CARROT       us     +38.85   opp      +0.00   gap     -38.85
    avg realized price / unit (revenue/sold):
      WOOL         us    +142.46   opp     +81.33   gap     -61.13
      CARROT       us     +55.55   opp      +0.00   gap     -55.55
      MILK         us    +160.10   opp    +117.17   gap     -42.93
      MELON        us     +55.32   opp     +68.14   gap     +12.82
      STRAWBERRY   us    +158.50   opp    +147.99   gap     -10.51
      TOMATO       us     +75.15   opp     +71.23   gap      -3.91
      FERTILIZER   us     +26.39   opp     +23.94   gap      -2.46
      EGG          us     +57.22   opp     +55.21   gap      -2.01
      WHEAT        us     +47.78   opp     +48.68   gap      +0.90
    production (units, exact):
      WHEAT        us     +49.29   opp     +92.32   gap     +43.03
      STRAWBERRY   us     +80.50   opp    +107.05   gap     +26.56
      FERTILIZER   us     +57.39   opp     +77.96   gap     +20.57
      EGG          us     +15.38   opp      +0.09   gap     -15.29
      WOOL         us     +16.88   opp     +32.13   gap     +15.25
      TOMATO       us     +11.48   opp      +0.35   gap     -11.13
      MELON        us     +12.52   opp      +1.73   gap     -10.78
      MILK         us     +41.26   opp     +49.12   gap      +7.87
      CARROT       us      +0.70   opp      +0.00   gap      -0.70
    seed spend:
      WHEAT        us    +382.62   opp    +322.39   gap     -60.24
      CARROT       us      +1.55   opp     +42.73   gap     +41.18
      MELON        us      +0.23   opp      +0.00   gap      -0.23
    animal spend:
      SHEEP        us     +63.64   opp      +0.00   gap     -63.64
      GOOSE        us      +1.53   opp      +0.00   gap      -1.53
    buy_product spend (filled, exact):
      WHEAT        us  +1,487.89   opp  +8,227.69   gap  +6,739.81
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 20-24    us     +1,880.0   opp     +1,784.1   gap (opp-us)        -95.9   (n=1760)
  feed actions (count), day 20-24    us        +65.3   opp        +74.4   gap (opp-us)         +9.0   (n=1760)
  fertilize actions (count), day 20-24    us        +22.3   opp        +35.7   gap (opp-us)        +13.4   (n=1760)
    crop tiles, end of window:
      STRAWBERRY   us     +20.07   opp     +25.20   gap      +5.13
      TOMATO       us      +4.62   opp      +0.01   gap      -4.61
      CARROT       us      +0.06   opp      +1.88   gap      +1.82
      WHEAT        us     +23.17   opp     +24.15   gap      +0.98
      MELON        us      +0.33   opp      +0.00   gap      -0.33
    herd, end of window:
      GOOSE        us      +2.20   opp      +0.01   gap      -2.19
      COW          us      +8.47   opp      +7.00   gap      -1.47
      SHEEP        us      +5.46   opp      +6.86   gap      +1.40
  net cash generated, day 25-29    us    +20,849.9   opp    +21,584.1   gap (opp-us)       +734.3   (n=1760)
  cash residual (should be ~0), day 25-29    us        -82.7   opp        +33.1   gap (opp-us)       +115.8   (n=1760)
    revenue (filled, exact):
      WHEAT        us  +4,164.74   opp +13,141.60   gap  +8,976.86
      TOMATO       us  +2,819.70   opp     +30.72   gap  -2,788.98
      STRAWBERRY   us  +4,986.89   opp  +7,120.52   gap  +2,133.63
      EGG          us  +1,255.88   opp      +7.73   gap  -1,248.15
      MILK         us  +6,713.98   opp  +5,652.33   gap  -1,061.65
      WOOL         us  +2,452.21   opp  +3,227.03   gap    +774.82
      CARROT       us     +80.91   opp    +649.97   gap    +569.06
      FERTILIZER   us    +659.29   opp    +339.05   gap    -320.24
      MELON        us    +150.80   opp      +0.00   gap    -150.80
    avg realized price / unit (revenue/sold):
      CARROT       us    +152.96   opp     +58.95   gap     -94.01
      MELON        us     +55.90   opp      +0.00   gap     -55.90
      WOOL         us    +108.08   opp     +82.20   gap     -25.89
      MILK         us    +135.85   opp    +111.84   gap     -24.02
      TOMATO       us     +93.12   opp     +86.37   gap      -6.75
      EGG          us     +60.46   opp     +57.67   gap      -2.80
      STRAWBERRY   us    +102.95   opp    +105.06   gap      +2.11
      WHEAT        us     +50.34   opp     +50.55   gap      +0.21
      FERTILIZER   us      +7.59   opp      +7.66   gap      +0.07
    production (units, exact):
      WHEAT        us    +109.88   opp    +166.92   gap     +57.04
      FERTILIZER   us     +84.10   opp     +53.39   gap     -30.71
      TOMATO       us     +30.28   opp      +0.04   gap     -30.24
      EGG          us     +20.77   opp      +0.13   gap     -20.64
      STRAWBERRY   us     +47.91   opp     +66.67   gap     +18.75
      WOOL         us     +21.19   opp     +39.01   gap     +17.82
      CARROT       us      +0.53   opp     +11.13   gap     +10.60
      MILK         us     +47.41   opp     +50.65   gap      +3.23
      MELON        us      +1.21   opp      +0.00   gap      -1.21
    seed spend:
      CARROT       us      +8.28   opp     +48.18   gap     +39.90
      WHEAT        us    +268.51   opp    +265.57   gap      -2.94
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +686.04   opp  +7,308.38   gap  +6,622.34
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 25-29    us     +1,554.4   opp       +929.6   gap (opp-us)       -624.8   (n=1760)
  feed actions (count), day 25-29    us        +57.3   opp        +52.8   gap (opp-us)         -4.5   (n=1760)
  fertilize actions (count), day 25-29    us         +6.6   opp         +9.3   gap (opp-us)         +2.7   (n=1760)
    crop tiles, end of window:
      STRAWBERRY   us      +2.54   opp      +1.39   gap      -1.15
      WHEAT        us      +1.66   opp      +0.81   gap      -0.86
      TOMATO       us      +0.31   opp      +0.01   gap      -0.30
    herd, end of window:
      GOOSE        us      +2.20   opp      +0.01   gap      -2.19
      COW          us      +8.47   opp      +6.92   gap      -1.54
      SHEEP        us      +5.46   opp      +5.72   gap      +0.26

-- LOSSES ONLY (n=720) --
  net cash generated, day 0-19     us    +36,526.2   opp    +33,515.9   gap (opp-us)     -3,010.3   (n=720)
  cash residual (should be ~0), day 0-19     us       +442.5   opp       -806.6   gap (opp-us)     -1,249.1   (n=720)
    revenue (filled, exact):
      WHEAT        us  +1,291.04   opp  +5,695.08   gap  +4,404.04
      WOOL         us +11,342.71   opp  +7,639.90   gap  -3,702.80
      MELON        us +13,202.29   opp +16,688.70   gap  +3,486.41
      FERTILIZER   us +12,951.61   opp  +9,510.13   gap  -3,441.47
      MILK         us +16,352.99   opp +13,992.99   gap  -2,360.01
      EGG          us  +1,569.75   opp      +9.32   gap  -1,560.42
      TOMATO       us    +272.93   opp      +0.00   gap    -272.93
      STRAWBERRY   us  +7,947.62   opp  +8,052.00   gap    +104.38
      CARROT       us      +9.72   opp      +1.63   gap      -8.10
    avg realized price / unit (revenue/sold):
      TOMATO       us     +66.50   opp      +0.00   gap     -66.50
      MELON        us    +162.05   opp    +198.03   gap     +35.97
      WOOL         us    +156.17   opp    +132.53   gap     -23.64
      MILK         us    +187.09   opp    +169.47   gap     -17.62
      WHEAT        us     +36.79   opp     +42.37   gap      +5.58
      FERTILIZER   us     +67.73   opp     +64.00   gap      -3.73
      STRAWBERRY   us    +203.74   opp    +207.23   gap      +3.49
      EGG          us     +53.69   opp     +52.87   gap      -0.82
      CARROT       us     +42.70   opp     +41.89   gap      -0.80
    production (units, exact):
      WHEAT        us     +69.48   opp    +120.59   gap     +51.11
      FERTILIZER   us    +209.74   opp    +170.25   gap     -39.49
      EGG          us     +29.24   opp      +0.18   gap     -29.06
      WOOL         us     +75.47   opp     +58.01   gap     -17.46
      MILK         us     +88.46   opp     +82.68   gap      -5.78
      TOMATO       us      +4.10   opp      +0.00   gap      -4.10
      MELON        us     +87.10   opp     +84.80   gap      -2.30
      CARROT       us      +0.23   opp      +0.04   gap      -0.19
      STRAWBERRY   us     +39.01   opp     +38.93   gap      -0.08
    seed spend:
      STRAWBERRY   us  +3,055.56   opp  +3,823.33   gap    +767.78
      MELON        us  +1,719.44   opp  +1,239.11   gap    -480.33
      TOMATO       us    +367.57   opp      +3.12   gap    -364.44
      WHEAT        us    +498.35   opp    +726.64   gap    +228.29
      CARROT       us     +44.36   opp    +143.33   gap     +98.97
    animal spend:
      SHEEP        us  +2,365.97   opp  +3,320.83   gap    +954.86
      GOOSE        us    +739.58   opp      +2.92   gap    -736.67
      COW          us  +3,521.11   opp  +3,307.78   gap    -213.33
    buy_product spend (filled, exact):
      WHEAT        us  +7,517.48   opp  +9,095.54   gap  +1,578.07
  land spend, day 0-19     us     +3,000.0   opp     +3,944.4   gap (opp-us)       +944.4   (n=720)
  wage spend, day 0-19     us     +5,142.5   opp     +3,273.4   gap (opp-us)     -1,869.1   (n=720)
  feed actions (count), day 0-19     us       +215.2   opp       +201.5   gap (opp-us)        -13.7   (n=720)
  fertilize actions (count), day 0-19     us        +18.3   opp        +21.4   gap (opp-us)         +3.1   (n=720)
    crop tiles, end of window:
      WHEAT        us      +9.11   opp     +25.06   gap     +15.95
      TOMATO       us      +6.01   opp      +0.06   gap      -5.95
      STRAWBERRY   us     +30.33   opp     +34.46   gap      +4.13
      MELON        us      +3.98   opp      +0.24   gap      -3.74
      CARROT       us      +0.16   opp      +0.00   gap      -0.16
    herd, end of window:
      GOOSE        us      +2.47   opp      +0.01   gap      -2.46
      SHEEP        us      +4.73   opp      +6.11   gap      +1.38
      COW          us      +8.80   opp      +7.78   gap      -1.02
  net cash generated, day 20-24    us    +22,979.9   opp    +30,378.5   gap (opp-us)     +7,398.6   (n=720)
  cash residual (should be ~0), day 20-24    us        +24.6   opp        -58.7   gap (opp-us)        -83.3   (n=720)
    revenue (filled, exact):
      WHEAT        us    +716.68   opp  +8,797.29   gap  +8,080.61
      STRAWBERRY   us +14,740.99   opp +19,975.66   gap  +5,234.66
      MILK         us  +5,948.64   opp  +6,888.05   gap    +939.42
      EGG          us    +940.38   opp      +4.25   gap    -936.13
      WOOL         us  +2,508.00   opp  +3,198.31   gap    +690.31
      TOMATO       us    +641.50   opp      +2.52   gap    -638.98
      MELON        us    +724.03   opp    +156.54   gap    -567.49
      FERTILIZER   us    +631.95   opp    +964.69   gap    +332.74
      CARROT       us     +24.21   opp      +0.00   gap     -24.21
    avg realized price / unit (revenue/sold):
      MELON        us     +46.09   opp    +102.46   gap     +56.37
      CARROT       us     +54.14   opp      +0.00   gap     -54.14
      WOOL         us    +145.03   opp    +102.53   gap     -42.50
      MILK         us    +144.17   opp    +119.74   gap     -24.42
      STRAWBERRY   us    +179.34   opp    +172.40   gap      -6.94
      TOMATO       us     +73.02   opp     +67.26   gap      -5.77
      EGG          us     +57.14   opp     +54.64   gap      -2.49
      FERTILIZER   us     +26.44   opp     +24.11   gap      -2.33
      WHEAT        us     +47.78   opp     +48.45   gap      +0.67
    production (units, exact):
      WHEAT        us     +46.81   opp     +93.37   gap     +46.56
      STRAWBERRY   us     +82.85   opp    +117.15   gap     +34.30
      FERTILIZER   us     +56.13   opp     +75.98   gap     +19.85
      EGG          us     +16.46   opp      +0.08   gap     -16.38
      WOOL         us     +15.68   opp     +31.22   gap     +15.54
      MILK         us     +42.50   opp     +57.45   gap     +14.95
      MELON        us     +11.87   opp      +1.00   gap     -10.87
      TOMATO       us      +8.78   opp      +0.24   gap      -8.54
      CARROT       us      +0.45   opp      +0.00   gap      -0.45
    seed spend:
      CARROT       us      +0.06   opp     +49.28   gap     +49.22
      WHEAT        us    +350.39   opp    +321.50   gap     -28.89
    animal spend:
      SHEEP        us     +87.50   opp      +0.00   gap     -87.50
      GOOSE        us      +0.83   opp      +0.00   gap      -0.83
    buy_product spend (filled, exact):
      WHEAT        us  +1,553.10   opp  +7,526.45   gap  +5,973.35
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=720)
  wage spend, day 20-24    us     +1,880.0   opp     +1,770.3   gap (opp-us)       -109.7   (n=720)
  feed actions (count), day 20-24    us        +65.0   opp        +72.3   gap (opp-us)         +7.3   (n=720)
  fertilize actions (count), day 20-24    us        +22.3   opp        +36.1   gap (opp-us)        +13.8   (n=720)
    crop tiles, end of window:
      STRAWBERRY   us     +20.68   opp     +26.51   gap      +5.83
      TOMATO       us      +4.38   opp      +0.02   gap      -4.36
      WHEAT        us     +21.59   opp     +24.87   gap      +3.28
      CARROT       us      +0.00   opp      +2.13   gap      +2.13
      MELON        us      +0.17   opp      +0.00   gap      -0.17
    herd, end of window:
      GOOSE        us      +2.47   opp      +0.01   gap      -2.46
      SHEEP        us      +4.91   opp      +6.10   gap      +1.20
      COW          us      +8.80   opp      +7.77   gap      -1.03
  net cash generated, day 25-29    us    +20,391.6   opp    +25,509.5   gap (opp-us)     +5,117.9   (n=720)
  cash residual (should be ~0), day 25-29    us        -79.2   opp        +37.4   gap (opp-us)       +116.6   (n=720)
    revenue (filled, exact):
      WHEAT        us  +3,952.21   opp +12,896.30   gap  +8,944.09
      STRAWBERRY   us  +6,015.36   opp  +9,606.44   gap  +3,591.08
      TOMATO       us  +2,473.73   opp     +29.51   gap  -2,444.23
      WOOL         us  +2,570.93   opp  +4,247.31   gap  +1,676.38
      EGG          us  +1,416.15   opp      +6.30   gap  -1,409.86
      CARROT       us     +17.65   opp    +749.26   gap    +731.61
      FERTILIZER   us    +676.48   opp    +360.81   gap    -315.66
      MILK         us  +5,677.74   opp  +5,862.28   gap    +184.54
      MELON        us     +81.40   opp      +0.00   gap     -81.40
    avg realized price / unit (revenue/sold):
      MELON        us     +41.01   opp      +0.00   gap     -41.01
      CARROT       us     +90.78   opp     +60.84   gap     -29.94
      TOMATO       us     +86.76   opp    +111.81   gap     +25.06
      MILK         us    +113.84   opp    +101.55   gap     -12.29
      WOOL         us    +121.64   opp    +111.23   gap     -10.41
      STRAWBERRY   us    +119.94   opp    +126.65   gap      +6.71
      EGG          us     +60.28   opp     +56.67   gap      -3.60
      FERTILIZER   us      +7.55   opp      +8.10   gap      +0.55
      WHEAT        us     +50.34   opp     +50.43   gap      +0.10
    production (units, exact):
      WHEAT        us    +104.70   opp    +168.95   gap     +64.26
      FERTILIZER   us     +85.83   opp     +53.25   gap     -32.58
      TOMATO       us     +28.51   opp      +0.06   gap     -28.45
      STRAWBERRY   us     +49.50   opp     +74.57   gap     +25.07
      EGG          us     +23.49   opp      +0.11   gap     -23.38
      WOOL         us     +19.91   opp     +37.92   gap     +18.01
      CARROT       us      +0.19   opp     +12.34   gap     +12.15
      MILK         us     +47.59   opp     +57.79   gap     +10.20
      MELON        us      +0.19   opp      +0.00   gap      -0.19
    seed spend:
      CARROT       us      +3.83   opp     +52.22   gap     +48.39
      WHEAT        us    +253.82   opp    +274.74   gap     +20.92
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +751.35   opp  +6,969.55   gap  +6,218.20
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=720)
  wage spend, day 25-29    us     +1,560.2   opp       +914.8   gap (opp-us)       -645.5   (n=720)
  feed actions (count), day 25-29    us        +57.8   opp        +51.9   gap (opp-us)         -5.9   (n=720)
  fertilize actions (count), day 25-29    us         +6.5   opp         +8.8   gap (opp-us)         +2.3   (n=720)
    crop tiles, end of window:
      WHEAT        us      +2.15   opp      +0.75   gap      -1.40
      STRAWBERRY   us      +2.41   opp      +1.62   gap      -0.80
      TOMATO       us      +0.17   opp      +0.02   gap      -0.16
    herd, end of window:
      GOOSE        us      +2.47   opp      +0.01   gap      -2.46
      COW          us      +8.80   opp      +7.73   gap      -1.07
      SHEEP        us      +4.91   opp      +5.19   gap      +0.28