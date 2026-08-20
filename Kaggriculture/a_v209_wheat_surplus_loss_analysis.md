======================================================================
a_v209_wheat_surplus: 1193-567 (67.8%)
======================================================================
op                     US/win  US/loss  OPP/loss  loss-win opp-us(loss)
PASS                    100.5     98.7      90.9      -1.8         -7.9
WEST                    144.2    145.4     147.0      +1.2         +1.6
SOUTH                   110.0    111.0      98.8      +1.0        -12.2
COLLECT_FERTILIZER       46.8     46.1      46.6      -0.7         +0.5
HARVEST                  49.7     50.4      57.6      +0.6         +7.2
WATER                   114.3    114.0     134.7      -0.4        +20.8
EAST                    121.3    121.7     117.8      +0.4         -3.8
FERTILIZE                 6.1      5.8       9.2      -0.3         +3.4
CARE                     43.7     43.5      48.3      -0.3         +4.9
NORTH                   149.6    149.8     137.9      +0.2        -11.9
FEED                     42.5     42.4      48.5      -0.1         +6.1
PLANT                    20.6     20.8      27.1      +0.1         +6.3
DROP                     24.5     24.4       2.0      -0.1        -22.4
mkt:BUY_SEED             12.1     12.0      14.2      -0.1         +2.1
BUILD_PASTURE             1.8      1.7       2.2      -0.1         +0.4
mkt:BUY_PRODUCT           7.7      7.7      12.1      +0.1         +4.3
DIG                       1.7      1.7       3.6      +0.1         +1.9
PLACE                     6.0      6.0       7.6      +0.0         +1.6
PICKUP                   16.3     16.3      20.1      -0.0         +3.9
mkt:SELL                 33.0     33.0      66.3      +0.0        +33.3
mkt:HIRE                 41.2     41.2      40.3      +0.0         -0.9
mkt:BUY_ANIMAL            1.3      1.3       1.4      +0.0         +0.0

money delta by day, avg across 567 losses (negative = behind):
  day  5: money      +968  plants 9.0/18.9  animals 6.0/6.0
  day 10: money   -11,636  plants 42.7/25.4  animals 15.6/10.9
  day 15: money      -589  plants 52.5/52.9  animals 16.0/13.6
  day 20: money    +3,338  plants 47.8/57.8  animals 16.0/14.3
  day 25: money    -2,223  plants 43.7/54.6  animals 16.2/14.2

worst 10 losses:
  t_94140675_1         seed=1042155578   margin=   -35,425
  t_94177280_1         seed=1788458074   margin=   -35,315
  t_94177280_0         seed=1788458074   margin=   -33,089
  t_94173433_0         seed=535203464    margin=   -32,230
  t_94140675_1         seed=28251350     margin=   -32,156
  t_94140675_1         seed=1281505960   margin=   -31,986
  t_94173433_0         seed=535203464    margin=   -31,877
  t_94140675_1         seed=28251350     margin=   -31,571
  t_94177280_1         seed=1788458074   margin=   -31,387
  t_94134439_1         seed=28251350     margin=   -31,232

-- SERVICE TELEMETRY: ALL GAMES --

  days 0-14 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1499.7    54.1%     38.2%      162.3     10.63   98.3%      0.0%
    COLLECT_FERTILIZER        928.1    92.4%     41.4%      147.6      9.84  100.0%      0.0%
    FEED                     1687.2    86.7%     22.7%      151.2      9.84   97.7%      0.0%
    FERTILIZE                  31.2    95.3%     19.3%        2.3      0.15  100.0%      0.0%
    HARVEST                   667.6    67.5%     28.2%       62.3      4.14   99.6%      0.0%
    PLANT                    2437.1    69.2%     12.1%       81.6      5.44  100.0%      0.0%
    WATER                    4003.6    77.4%     27.8%      356.8     22.90   96.3%      0.0%
    movement turns/game-day: 114.42   PASS turns/game-day: 48.76
    animal cap ticks: EGG=0.35/day, MILK=2.32/day, WOOL=1.32/day
    crop expiry with held yield: STRAWBERRY=28.71/game, TOMATO=17.20/game

  days 15-19 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1492.2    25.3%     32.8%       64.2     11.59   90.2%      0.0%
    COLLECT_FERTILIZER       1029.0    42.4%     38.0%       77.6     15.17   97.7%      0.0%
    FEED                     1062.5    63.5%     15.3%       62.9     12.11   96.3%      0.0%
    FERTILIZE                 695.6    87.8%      6.3%       16.0      3.20  100.0%      0.0%
    HARVEST                  1612.7    49.1%     22.4%       82.8     16.33   98.7%      0.0%
    PLANT                    1445.0    26.1%     11.9%       22.2      4.44  100.0%      0.0%
    WATER                    3401.7    63.6%     26.3%      228.6     43.63   95.4%      0.0%
    movement turns/game-day: 166.55   PASS turns/game-day: 3.22
    animal cap ticks: EGG=0.04/day, MILK=1.82/day, WOOL=0.38/day
    crop expiry with held yield: STRAWBERRY=402.98/game, TOMATO=91.41/game, WHEAT=0.13/game

  days 20-24 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1447.7    22.7%     31.8%       58.0     10.61   91.4%      0.0%
    COLLECT_FERTILIZER       1436.4    30.9%     29.6%       67.6     12.53   92.7%      0.0%
    FEED                     1050.1    62.5%     15.7%       63.2     12.28   97.1%      0.0%
    FERTILIZE                1050.4    85.1%      6.3%       22.4      4.48  100.0%      0.0%
    HARVEST                  2758.0    42.0%     26.2%      128.7     25.49   99.0%      0.0%
    PLANT                    1371.6    23.5%     17.6%       29.3      5.87  100.0%      0.0%
    WATER                    2895.3    60.5%     25.8%      196.5     37.25   94.8%      0.0%
    movement turns/game-day: 163.96   PASS turns/game-day: 1.14
    animal cap ticks: EGG=0.04/day, MILK=0.59/day, WOOL=0.16/day
    crop expiry with held yield: CARROT=0.04/game, MELON=0.01/game, STRAWBERRY=1042.81/game, TOMATO=131.47/game, WHEAT=0.22/game

  days 25-29 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      911.4    32.3%     37.4%       58.5     11.33   96.7%      0.0%
    COLLECT_FERTILIZER       1225.0    34.9%     34.5%       73.1     14.06   96.2%      0.1%
    FEED                      801.4    70.2%     18.1%       56.6     10.98   97.1%      0.0%
    FERTILIZE                 347.3    82.1%      5.6%        6.4      1.28  100.0%      0.0%
    HARVEST                  1997.8    64.9%     22.0%      118.9     23.53   99.5%      0.5%
    PLANT                     741.3    40.1%     18.7%       29.5      5.89  100.0%      0.0%
    WATER                    1498.7    78.6%     23.2%      116.1     21.52   92.7%      0.0%
    movement turns/game-day: 153.31   PASS turns/game-day: 6.50
    animal cap ticks: EGG=0.01/day, MILK=0.22/day, WOOL=0.07/day
    crop expiry with held yield: CARROT=0.02/game, STRAWBERRY=243.47/game, TOMATO=165.49/game, WHEAT=0.42/game

-- SERVICE TELEMETRY: LOSSES ONLY --

  days 0-14 (telemetry games=567)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1550.9    52.9%     38.1%      162.3     10.61   98.0%      0.0%
    COLLECT_FERTILIZER        929.7    92.5%     41.7%      148.0      9.86  100.0%      0.0%
    FEED                     1708.6    86.4%     22.3%      150.7      9.81   97.7%      0.0%
    FERTILIZE                  30.9    95.7%     20.2%        2.3      0.15  100.0%      0.0%
    HARVEST                   707.4    65.5%     28.2%       64.1      4.26   99.6%      0.0%
    PLANT                    2444.7    68.4%     12.2%       82.2      5.48  100.0%      0.0%
    WATER                    4020.3    77.9%     27.5%      358.1     23.01   96.4%      0.0%
    movement turns/game-day: 114.75   PASS turns/game-day: 48.23
    animal cap ticks: EGG=0.37/day, MILK=2.22/day, WOOL=1.34/day
    crop expiry with held yield: STRAWBERRY=29.34/game, TOMATO=17.43/game

  days 15-19 (telemetry games=567)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1525.4    24.9%     31.7%       63.5     11.39   89.7%      0.0%
    COLLECT_FERTILIZER       1050.0    42.9%     37.7%       77.3     15.06   97.4%      0.0%
    FEED                     1083.0    62.6%     15.1%       62.6     12.01   95.9%      0.0%
    FERTILIZE                 713.7    89.0%      6.1%       16.2      3.23  100.0%      0.0%
    HARVEST                  1676.8    48.4%     22.7%       84.5     16.62   98.4%      0.0%
    PLANT                    1426.5    24.6%     12.4%       21.4      4.27  100.0%      0.0%
    WATER                    3349.3    63.9%     26.4%      226.6     43.20   95.3%      0.0%
    movement turns/game-day: 167.09   PASS turns/game-day: 3.06
    animal cap ticks: EGG=0.03/day, MILK=1.30/day, WOOL=0.46/day
    crop expiry with held yield: STRAWBERRY=414.45/game, TOMATO=98.99/game, WHEAT=0.11/game

  days 20-24 (telemetry games=567)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1489.0    21.9%     30.8%       57.2     10.42   91.0%      0.0%
    COLLECT_FERTILIZER       1478.0    30.9%     29.1%       66.6     12.24   91.9%      0.0%
    FEED                     1091.2    60.4%     15.9%       63.1     12.17   96.4%      0.0%
    FERTILIZE                1050.5    88.4%      5.7%       21.2      4.23  100.0%      0.0%
    HARVEST                  2770.0    41.1%     27.0%      128.3     25.40   99.0%      0.0%
    PLANT                    1424.7    23.1%     17.9%       29.3      5.87  100.0%      0.0%
    WATER                    2790.9    61.6%     26.4%      195.1     37.04   94.9%      0.0%
    movement turns/game-day: 165.11   PASS turns/game-day: 1.13
    animal cap ticks: EGG=0.04/day, MILK=0.71/day, WOOL=0.13/day
    crop expiry with held yield: CARROT=0.02/game, MELON=0.02/game, STRAWBERRY=1024.43/game, TOMATO=113.34/game, WHEAT=0.14/game

  days 25-29 (telemetry games=567)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      924.4    32.5%     37.0%       58.7     11.35   96.7%      0.0%
    COLLECT_FERTILIZER       1261.6    33.1%     34.1%       70.5     13.47   95.5%      0.1%
    FEED                      814.8    69.1%     18.6%       56.8     11.03   97.1%      0.0%
    FERTILIZE                 355.5    84.8%      5.2%        6.0      1.21  100.0%      0.0%
    HARVEST                  2004.4    64.6%     22.1%      119.4     23.64   99.5%      0.5%
    PLANT                     723.4    40.7%     19.6%       30.5      6.09  100.0%      0.0%
    WATER                    1486.0    79.3%     23.4%      116.4     21.56   92.6%      0.0%
    movement turns/game-day: 153.89   PASS turns/game-day: 6.42
    animal cap ticks: EGG=0.01/day, MILK=0.20/day, WOOL=0.08/day
    crop expiry with held yield: STRAWBERRY=256.59/game, TOMATO=138.51/game, WHEAT=0.40/game

==============================================================================
a_v209_wheat_surplus: 1193-567 (67.8%)
==============================================================================

-- ALL GAMES (n=1760) --
  net cash generated, day 0-19     us    +37,265.0   opp    +25,777.0   gap (opp-us)    -11,488.0   (n=1760)
  cash residual (should be ~0), day 0-19     us       +356.2   opp       -697.3   gap (opp-us)     -1,053.4   (n=1760)
    revenue (filled, exact):
      WOOL         us +11,987.13   opp  +7,081.60   gap  -4,905.53
      WHEAT        us  +1,218.84   opp  +5,785.24   gap  +4,566.40
      MILK         us +16,019.06   opp +11,776.45   gap  -4,242.61
      FERTILIZER   us +13,073.13   opp  +9,192.01   gap  -3,881.12
      EGG          us  +1,358.27   opp     +10.69   gap  -1,347.59
      STRAWBERRY   us  +7,021.25   opp  +6,313.44   gap    -707.81
      MELON        us +14,821.64   opp +14,371.80   gap    -449.85
      TOMATO       us    +393.94   opp      +0.00   gap    -393.94
      CARROT       us     +11.18   opp      +0.94   gap     -10.25
    avg realized price / unit (revenue/sold):
      TOMATO       us     +67.82   opp      +0.00   gap     -67.82
      WOOL         us    +162.85   opp    +128.81   gap     -34.04
      MELON        us    +175.25   opp    +209.17   gap     +33.91
      MILK         us    +183.92   opp    +160.40   gap     -23.52
      WHEAT        us     +36.18   opp     +42.74   gap      +6.55
      FERTILIZER   us     +68.20   opp     +64.47   gap      -3.73
      CARROT       us     +44.44   opp     +41.15   gap      -3.29
      EGG          us     +54.36   opp     +52.24   gap      -2.12
      STRAWBERRY   us    +202.50   opp    +201.68   gap      -0.82
    production (units, exact):
      WHEAT        us     +65.67   opp    +124.66   gap     +58.99
      FERTILIZER   us    +209.81   opp    +164.82   gap     -44.99
      EGG          us     +24.99   opp      +0.20   gap     -24.78
      WOOL         us     +78.07   opp     +55.31   gap     -22.76
      MELON        us     +88.64   opp     +68.87   gap     -19.76
      MILK         us     +89.03   opp     +73.50   gap     -15.53
      TOMATO       us      +5.81   opp      +0.00   gap      -5.81
      STRAWBERRY   us     +34.67   opp     +31.35   gap      -3.32
      CARROT       us      +0.25   opp      +0.02   gap      -0.23
    seed spend:
      STRAWBERRY   us  +2,971.25   opp  +3,830.68   gap    +859.43
      MELON        us  +1,820.95   opp  +1,229.09   gap    -591.86
      TOMATO       us    +425.80   opp      +3.98   gap    -421.82
      WHEAT        us    +489.15   opp    +738.07   gap    +248.92
      CARROT       us     +43.25   opp    +134.77   gap     +91.52
    animal spend:
      SHEEP        us  +2,596.02   opp  +3,795.45   gap  +1,199.43
      GOOSE        us    +665.11   opp      +3.41   gap    -661.70
      COW          us  +3,436.36   opp  +3,118.18   gap    -318.18
    buy_product spend (filled, exact):
      WHEAT        us  +7,605.51   opp  +9,222.24   gap  +1,616.73
  land spend, day 0-19     us     +3,000.0   opp     +4,228.4   gap (opp-us)     +1,228.4   (n=1760)
  wage spend, day 0-19     us     +5,229.8   opp     +3,148.1   gap (opp-us)     -2,081.7   (n=1760)
  feed actions (count), day 0-19     us       +213.6   opp       +203.4   gap (opp-us)        -10.2   (n=1760)
  fertilize actions (count), day 0-19     us        +17.9   opp        +21.8   gap (opp-us)         +3.9   (n=1760)
    crop tiles, end of window:
      WHEAT        us      +9.00   opp     +23.49   gap     +14.48
      TOMATO       us      +7.17   opp      +0.08   gap      -7.09
      MELON        us      +4.70   opp      +0.36   gap      -4.35
      STRAWBERRY   us     +29.23   opp     +31.09   gap      +1.86
      CARROT       us      +0.25   opp      +0.00   gap      -0.25
    herd, end of window:
      COW          us      +8.59   opp      +6.38   gap      -2.21
      GOOSE        us      +2.22   opp      +0.01   gap      -2.21
      SHEEP        us      +5.19   opp      +6.72   gap      +1.52
  net cash generated, day 20-24    us    +25,039.0   opp    +25,050.9   gap (opp-us)        +11.8   (n=1760)
  cash residual (should be ~0), day 20-24    us        +10.7   opp        -47.4   gap (opp-us)        -58.1   (n=1760)
    revenue (filled, exact):
      WHEAT        us    +752.02   opp  +9,423.53   gap  +8,671.51
      STRAWBERRY   us +14,645.81   opp +16,596.98   gap  +1,951.17
      MILK         us  +7,017.18   opp  +5,492.68   gap  -1,524.50
      MELON        us  +1,413.10   opp    +136.66   gap  -1,276.44
      EGG          us    +871.13   opp      +4.86   gap    -866.26
      TOMATO       us    +784.30   opp      +2.56   gap    -781.74
      FERTILIZER   us    +716.27   opp    +999.95   gap    +283.68
      WOOL         us  +2,633.90   opp  +2,765.58   gap    +131.68
      CARROT       us     +33.63   opp      +0.00   gap     -33.63
    avg realized price / unit (revenue/sold):
      WOOL         us    +156.79   opp     +91.23   gap     -65.55
      CARROT       us     +47.24   opp      +0.00   gap     -47.24
      MILK         us    +164.16   opp    +122.07   gap     -42.09
      STRAWBERRY   us    +178.61   opp    +169.03   gap      -9.58
      MELON        us     +71.06   opp     +64.62   gap      -6.44
      EGG          us     +58.20   opp     +53.51   gap      -4.69
      FERTILIZER   us     +27.14   opp     +24.55   gap      -2.59
      TOMATO       us     +74.28   opp     +75.17   gap      +0.89
      WHEAT        us     +48.31   opp     +49.13   gap      +0.82
    production (units, exact):
      WHEAT        us     +46.63   opp     +91.82   gap     +45.19
      FERTILIZER   us     +56.56   opp     +76.19   gap     +19.63
      WOOL         us     +13.99   opp     +30.37   gap     +16.38
      STRAWBERRY   us     +82.55   opp     +98.80   gap     +16.25
      MELON        us     +17.55   opp      +1.95   gap     -15.60
      EGG          us     +14.97   opp      +0.09   gap     -14.88
      TOMATO       us     +10.56   opp      +0.34   gap     -10.21
      MILK         us     +42.41   opp     +44.93   gap      +2.52
      CARROT       us      +0.71   opp      +0.00   gap      -0.71
    seed spend:
      CARROT       us      +1.20   opp     +42.73   gap     +41.52
      WHEAT        us    +334.33   opp    +322.39   gap     -11.94
    animal spend:
      SHEEP        us     +82.67   opp      +0.00   gap     -82.67
      GOOSE        us      +6.14   opp      +0.00   gap      -6.14
    buy_product spend (filled, exact):
      WHEAT        us  +1,513.22   opp  +8,272.30   gap  +6,759.08
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 20-24    us     +1,880.0   opp     +1,781.9   gap (opp-us)        -98.1   (n=1760)
  feed actions (count), day 20-24    us        +63.4   opp        +74.4   gap (opp-us)        +11.0   (n=1760)
  fertilize actions (count), day 20-24    us        +22.5   opp        +35.6   gap (opp-us)        +13.2   (n=1760)
    crop tiles, end of window:
      TOMATO       us      +5.16   opp      +0.01   gap      -5.15
      WHEAT        us     +18.55   opp     +23.05   gap      +4.51
      STRAWBERRY   us     +21.73   opp     +24.17   gap      +2.43
      CARROT       us      +0.06   opp      +1.89   gap      +1.83
      MELON        us      +0.64   opp      +0.00   gap      -0.64
    herd, end of window:
      COW          us      +8.59   opp      +6.36   gap      -2.23
      GOOSE        us      +2.24   opp      +0.01   gap      -2.23
      SHEEP        us      +5.36   opp      +6.70   gap      +1.35
  net cash generated, day 25-29    us    +22,803.8   opp    +23,902.9   gap (opp-us)     +1,099.1   (n=1760)
  cash residual (should be ~0), day 25-29    us        -75.0   opp        +36.0   gap (opp-us)       +111.0   (n=1760)
    revenue (filled, exact):
      WHEAT        us  +3,504.82   opp +13,285.54   gap  +9,780.72
      TOMATO       us  +2,822.07   opp     +30.80   gap  -2,791.27
      STRAWBERRY   us  +6,625.64   opp  +9,267.65   gap  +2,642.01
      MILK         us  +7,535.71   opp  +5,419.59   gap  -2,116.12
      EGG          us  +1,231.18   opp      +7.57   gap  -1,223.61
      WOOL         us  +2,611.61   opp  +3,631.57   gap  +1,019.96
      CARROT       us     +31.94   opp    +583.28   gap    +551.34
      FERTILIZER   us    +739.92   opp    +357.65   gap    -382.27
      MELON        us    +260.24   opp      +0.00   gap    -260.24
    avg realized price / unit (revenue/sold):
      MELON        us     +65.67   opp      +0.00   gap     -65.67
      WOOL         us    +121.19   opp     +94.66   gap     -26.53
      MILK         us    +144.66   opp    +119.63   gap     -25.03
      CARROT       us     +70.63   opp     +52.73   gap     -17.90
      EGG          us     +61.75   opp     +55.50   gap      -6.24
      STRAWBERRY   us    +134.04   opp    +137.31   gap      +3.27
      TOMATO       us     +86.92   opp     +86.60   gap      -0.33
      FERTILIZER   us      +8.49   opp      +8.71   gap      +0.23
      WHEAT        us     +51.14   opp     +51.26   gap      +0.13
    production (units, exact):
      WHEAT        us     +91.91   opp    +165.80   gap     +73.89
      FERTILIZER   us     +85.99   opp     +50.09   gap     -35.90
      TOMATO       us     +32.47   opp      +0.05   gap     -32.42
      EGG          us     +19.94   opp      +0.14   gap     -19.80
      WOOL         us     +19.90   opp     +38.12   gap     +18.22
      STRAWBERRY   us     +48.88   opp     +66.86   gap     +17.98
      CARROT       us      +0.45   opp     +11.11   gap     +10.66
      MILK         us     +50.49   opp     +45.42   gap      -5.07
      MELON        us      +2.24   opp      +0.00   gap      -2.24
    seed spend:
      CARROT       us      +5.91   opp     +48.18   gap     +42.27
      WHEAT        us    +246.73   opp    +265.57   gap     +18.84
    animal spend:
      GOOSE        us      +0.17   opp      +0.00   gap      -0.17
    buy_product spend (filled, exact):
      WHEAT        us    +821.01   opp  +7,401.55   gap  +6,580.55
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 25-29    us     +1,560.5   opp       +929.4   gap (opp-us)       -631.1   (n=1760)
  feed actions (count), day 25-29    us        +56.9   opp        +52.8   gap (opp-us)         -4.2   (n=1760)
  fertilize actions (count), day 25-29    us         +6.7   opp         +9.3   gap (opp-us)         +2.6   (n=1760)
    crop tiles, end of window:
      WHEAT        us      +1.73   opp      +0.78   gap      -0.95
      STRAWBERRY   us      +1.90   opp      +1.39   gap      -0.51
      TOMATO       us      +0.35   opp      +0.01   gap      -0.34
    herd, end of window:
      COW          us      +8.59   opp      +6.15   gap      -2.44
      GOOSE        us      +2.24   opp      +0.01   gap      -2.23
      SHEEP        us      +5.36   opp      +5.57   gap      +0.22

-- LOSSES ONLY (n=567) --
  net cash generated, day 0-19     us    +35,054.1   opp    +30,545.5   gap (opp-us)     -4,508.7   (n=567)
  cash residual (should be ~0), day 0-19     us       +379.7   opp       -550.6   gap (opp-us)       -930.3   (n=567)
    revenue (filled, exact):
      WHEAT        us  +1,303.99   opp  +6,325.27   gap  +5,021.28
      WOOL         us +12,894.03   opp  +8,740.42   gap  -4,153.62
      FERTILIZER   us +12,985.83   opp  +9,477.65   gap  -3,508.17
      MELON        us +13,426.08   opp +16,437.01   gap  +3,010.93
      EGG          us  +1,570.34   opp      +6.72   gap  -1,563.62
      MILK         us +13,670.35   opp +12,248.27   gap  -1,422.08
      TOMATO       us    +446.46   opp      +0.00   gap    -446.46
      STRAWBERRY   us  +7,238.60   opp  +7,154.51   gap     -84.10
      CARROT       us     +16.39   opp      +1.18   gap     -15.20
    avg realized price / unit (revenue/sold):
      TOMATO       us     +66.93   opp      +0.00   gap     -66.93
      MELON        us    +163.49   opp    +203.22   gap     +39.73
      WOOL         us    +164.89   opp    +140.28   gap     -24.61
      MILK         us    +167.91   opp    +148.98   gap     -18.92
      WHEAT        us     +36.46   opp     +42.88   gap      +6.42
      FERTILIZER   us     +67.87   opp     +63.64   gap      -4.23
      EGG          us     +53.99   opp     +50.11   gap      -3.89
      CARROT       us     +43.62   opp     +41.88   gap      -1.74
      STRAWBERRY   us    +204.82   opp    +205.83   gap      +1.01
    production (units, exact):
      WHEAT        us     +68.18   opp    +123.63   gap     +55.45
      FERTILIZER   us    +209.78   opp    +169.28   gap     -40.50
      EGG          us     +29.08   opp      +0.13   gap     -28.95
      WOOL         us     +81.93   opp     +62.51   gap     -19.43
      MELON        us     +87.77   opp     +81.06   gap      -6.71
      TOMATO       us      +6.67   opp      +0.00   gap      -6.67
      MILK         us     +83.76   opp     +82.36   gap      -1.40
      STRAWBERRY   us     +35.34   opp     +34.80   gap      -0.54
      CARROT       us      +0.38   opp      +0.03   gap      -0.35
    seed spend:
      STRAWBERRY   us  +3,016.93   opp  +3,680.60   gap    +663.67
      MELON        us  +1,739.26   opp  +1,307.09   gap    -432.17
      TOMATO       us    +399.29   opp      +7.05   gap    -392.24
      WHEAT        us    +507.09   opp    +754.89   gap    +247.80
      CARROT       us     +42.54   opp    +131.46   gap     +88.92
    animal spend:
      SHEEP        us  +2,653.44   opp  +3,708.11   gap  +1,054.67
      GOOSE        us    +773.54   opp      +2.12   gap    -771.43
      COW          us  +3,245.86   opp  +3,233.86   gap     -11.99
    buy_product spend (filled, exact):
      WHEAT        us  +7,510.38   opp  +9,767.55   gap  +2,257.17
  land spend, day 0-19     us     +3,000.0   opp     +4,537.9   gap (opp-us)     +1,537.9   (n=567)
  wage spend, day 0-19     us     +5,229.9   opp     +3,265.5   gap (opp-us)     -1,964.4   (n=567)
  feed actions (count), day 0-19     us       +212.7   opp       +205.0   gap (opp-us)         -7.8   (n=567)
  fertilize actions (count), day 0-19     us        +18.1   opp        +19.9   gap (opp-us)         +1.8   (n=567)
    crop tiles, end of window:
      WHEAT        us      +9.30   opp     +26.42   gap     +17.12
      TOMATO       us      +6.43   opp      +0.14   gap      -6.29
      STRAWBERRY   us     +29.78   opp     +33.32   gap      +3.53
      MELON        us      +3.80   opp      +0.31   gap      -3.49
      CARROT       us      +0.14   opp      +0.00   gap      -0.14
    herd, end of window:
      GOOSE        us      +2.58   opp      +0.01   gap      -2.57
      SHEEP        us      +5.31   opp      +6.99   gap      +1.68
      COW          us      +8.11   opp      +7.31   gap      -0.81
  net cash generated, day 20-24    us    +22,237.2   opp    +28,730.6   gap (opp-us)     +6,493.3   (n=567)
  cash residual (should be ~0), day 20-24    us         +0.8   opp        -35.1   gap (opp-us)        -35.8   (n=567)
    revenue (filled, exact):
      WHEAT        us    +803.21   opp +10,878.66   gap +10,075.44
      STRAWBERRY   us +14,539.25   opp +18,878.85   gap  +4,339.60
      EGG          us    +978.17   opp      +2.83   gap    -975.34
      WOOL         us  +3,166.41   opp  +4,094.65   gap    +928.24
      MILK         us  +4,517.00   opp  +5,337.61   gap    +820.60
      TOMATO       us    +695.43   opp      +1.56   gap    -693.87
      MELON        us    +673.36   opp    +205.51   gap    -467.85
      FERTILIZER   us    +691.10   opp    +997.16   gap    +306.06
      CARROT       us     +17.78   opp      +0.00   gap     -17.78
    avg realized price / unit (revenue/sold):
      MELON        us     +47.45   opp    +107.00   gap     +59.55
      CARROT       us     +46.23   opp      +0.00   gap     -46.23
      WOOL         us    +166.36   opp    +123.87   gap     -42.49
      MILK         us    +122.64   opp     +98.44   gap     -24.20
      EGG          us     +57.18   opp     +50.19   gap      -6.99
      STRAWBERRY   us    +176.45   opp    +173.32   gap      -3.13
      TOMATO       us     +70.63   opp     +73.67   gap      +3.04
      FERTILIZER   us     +25.07   opp     +22.61   gap      -2.46
      WHEAT        us     +47.96   opp     +48.59   gap      +0.63
    production (units, exact):
      WHEAT        us     +47.88   opp     +97.29   gap     +49.41
      STRAWBERRY   us     +82.81   opp    +109.35   gap     +26.54
      FERTILIZER   us     +56.51   opp     +78.61   gap     +22.10
      MILK         us     +36.11   opp     +54.08   gap     +17.97
      EGG          us     +17.11   opp      +0.06   gap     -17.05
      WOOL         us     +16.24   opp     +33.02   gap     +16.78
      TOMATO       us      +9.85   opp      +0.66   gap      -9.19
      MELON        us     +10.74   opp      +1.74   gap      -9.00
      CARROT       us      +0.38   opp      +0.00   gap      -0.38
    seed spend:
      CARROT       us      +0.00   opp     +43.39   gap     +43.39
      WHEAT        us    +330.71   opp    +330.12   gap      -0.58
    animal spend:
      SHEEP        us    +102.29   opp      +0.00   gap    -102.29
      GOOSE        us      +1.59   opp      +0.00   gap      -1.59
    buy_product spend (filled, exact):
      WHEAT        us  +1,529.14   opp  +9,546.77   gap  +8,017.63
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=567)
  wage spend, day 20-24    us     +1,880.0   opp     +1,781.0   gap (opp-us)        -99.0   (n=567)
  feed actions (count), day 20-24    us        +63.3   opp        +75.2   gap (opp-us)        +12.0   (n=567)
  fertilize actions (count), day 20-24    us        +21.2   opp        +34.8   gap (opp-us)        +13.6   (n=567)
    crop tiles, end of window:
      WHEAT        us     +18.83   opp     +25.47   gap      +6.63
      TOMATO       us      +4.51   opp      +0.01   gap      -4.50
      STRAWBERRY   us     +21.97   opp     +24.68   gap      +2.72
      CARROT       us      +0.00   opp      +2.18   gap      +2.18
      MELON        us      +0.32   opp      +0.00   gap      -0.32
    herd, end of window:
      GOOSE        us      +2.58   opp      +0.01   gap      -2.58
      SHEEP        us      +5.51   opp      +6.98   gap      +1.47
      COW          us      +8.11   opp      +7.27   gap      -0.84
  net cash generated, day 25-29    us    +19,727.2   opp    +26,185.6   gap (opp-us)     +6,458.4   (n=567)
  cash residual (should be ~0), day 25-29    us       -133.4   opp        +92.0   gap (opp-us)       +225.5   (n=567)
    revenue (filled, exact):
      WHEAT        us  +3,519.32   opp +13,151.65   gap  +9,632.33
      STRAWBERRY   us  +6,236.83   opp  +9,627.80   gap  +3,390.97
      WOOL         us  +3,236.73   opp  +5,582.00   gap  +2,345.27
      TOMATO       us  +2,322.31   opp     +63.59   gap  -2,258.72
      EGG          us  +1,410.97   opp      +4.37   gap  -1,406.60
      CARROT       us      +3.47   opp    +617.05   gap    +613.58
      MILK         us  +4,706.17   opp  +5,283.71   gap    +577.54
      FERTILIZER   us    +622.01   opp    +323.68   gap    -298.33
      MELON        us    +134.83   opp      +0.00   gap    -134.83
    avg realized price / unit (revenue/sold):
      MELON        us     +51.83   opp      +0.00   gap     -51.83
      WOOL         us    +144.46   opp    +133.15   gap     -11.31
      TOMATO       us     +82.26   opp     +91.28   gap      +9.02
      EGG          us     +60.19   opp     +51.67   gap      -8.52
      STRAWBERRY   us    +126.15   opp    +133.06   gap      +6.91
      MILK         us     +99.13   opp     +97.41   gap      -1.72
      FERTILIZER   us      +7.47   opp      +7.18   gap      -0.29
      CARROT       us     +54.61   opp     +54.87   gap      +0.26
      WHEAT        us     +50.63   opp     +50.66   gap      +0.03
    production (units, exact):
      WHEAT        us     +93.29   opp    +169.71   gap     +76.42
      TOMATO       us     +28.23   opp      +0.06   gap     -28.17
      FERTILIZER   us     +81.50   opp     +53.65   gap     -27.86
      EGG          us     +23.44   opp      +0.08   gap     -23.36
      STRAWBERRY   us     +49.04   opp     +71.95   gap     +22.91
      WOOL         us     +21.46   opp     +41.84   gap     +20.38
      CARROT       us      +0.06   opp     +11.29   gap     +11.23
      MILK         us     +45.85   opp     +54.31   gap      +8.46
      MELON        us      +0.40   opp      +0.00   gap      -0.40
    seed spend:
      CARROT       us      +0.99   opp     +45.82   gap     +44.83
      WHEAT        us    +250.92   opp    +252.43   gap      +1.52
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +783.08   opp  +7,156.51   gap  +6,373.44
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=567)
  wage spend, day 25-29    us     +1,563.9   opp       +921.5   gap (opp-us)       -642.4   (n=567)
  feed actions (count), day 25-29    us        +57.2   opp        +53.1   gap (opp-us)         -4.1   (n=567)
  fertilize actions (count), day 25-29    us         +6.3   opp         +8.7   gap (opp-us)         +2.3   (n=567)
    crop tiles, end of window:
      WHEAT        us      +1.84   opp      +0.55   gap      -1.29
      STRAWBERRY   us      +2.20   opp      +1.02   gap      -1.18
      TOMATO       us      +0.21   opp      +0.01   gap      -0.20
    herd, end of window:
      GOOSE        us      +2.58   opp      +0.01   gap      -2.58
      COW          us      +8.11   opp      +7.20   gap      -0.91
      SHEEP        us      +5.51   opp      +5.61   gap      +0.10