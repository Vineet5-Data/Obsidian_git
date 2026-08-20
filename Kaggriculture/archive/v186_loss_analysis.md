======================================================================
a_v186: 880-880 (50.0%)
======================================================================
op                     US/win  US/loss  OPP/loss  loss-win opp-us(loss)
EAST                    117.7    120.5     119.1      +2.8         -1.3
WATER                   118.5    115.8     133.5      -2.7        +17.7
PLANT                    21.4     19.4      26.9      -2.0         +7.4
SOUTH                   110.8    112.3      97.0      +1.5        -15.3
mkt:BUY_SEED             12.5     11.2      14.3      -1.3         +3.1
PASS                     95.9     97.1      86.3      +1.2        -10.8
HARVEST                  51.3     50.1      57.5      -1.2         +7.4
DROP                     25.1     26.0       2.0      +1.0        -24.0
WEST                    146.3    147.3     155.1      +0.9         +7.8
COLLECT_FERTILIZER       47.4     46.8      45.6      -0.6         -1.2
mkt:SELL                 32.7     33.2      65.7      +0.5        +32.5
NORTH                   149.1    148.7     140.0      -0.4         -8.7
mkt:BUY_PRODUCT           8.4      8.7      11.2      +0.3         +2.6
DIG                       2.2      1.9       3.8      -0.3         +1.8
FERTILIZE                 6.7      6.4       9.7      -0.3         +3.3
CARE                     44.2     43.9      47.3      -0.2         +3.4
FEED                     42.8     42.9      47.3      +0.1         +4.4
PICKUP                   16.7     16.8      19.4      +0.1         +2.6
BUILD_PASTURE             1.8      1.8       2.2      -0.1         +0.4
mkt:BUY_ANIMAL            1.4      1.4       1.3      -0.0         -0.1
PLACE                     2.1      2.1       7.5      -0.0         +5.4
mkt:HIRE                 41.0     41.0      40.2      +0.0         -0.8

money delta by day, avg across 880 losses (negative = behind):
  day  5: money      +846  plants 9.0/19.0  animals 6.0/6.0
  day 10: money   -11,836  plants 43.3/27.4  animals 15.3/11.4
  day 15: money    -1,966  plants 54.9/52.7  animals 16.0/13.7
  day 20: money      +458  plants 48.1/57.9  animals 16.0/13.9
  day 25: money    -5,644  plants 45.2/54.4  animals 16.0/13.9

worst 10 losses:
  t_94142273_0         seed=1042155578   margin=   -41,653
  t_94134439_0         seed=1042155578   margin=   -32,504
  t_94174874_1         seed=28251350     margin=   -31,285
  t_94174874_1         seed=28251350     margin=   -31,265
  t_94142273_0         seed=1281505960   margin=   -30,764
  t_94135296_0         seed=28251350     margin=   -30,749
  t_94178232_0         seed=28251350     margin=   -30,367
  t_94178232_0         seed=28251350     margin=   -29,759
  t_94178228_1         seed=28251350     margin=   -29,138
  t_94142273_0         seed=1042155578   margin=   -28,820

-- SERVICE TELEMETRY: ALL GAMES --

  days 0-14 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1519.3    54.2%     37.6%      162.4     10.58   97.7%      0.0%
    COLLECT_FERTILIZER        947.8    90.1%     42.2%      148.5      9.90   99.9%      0.0%
    FEED                     1648.1    87.0%     22.7%      150.3      9.76   97.4%      0.0%
    FERTILIZE                  62.5    95.2%     18.4%        4.3      0.29  100.0%      0.0%
    HARVEST                   646.1    70.3%     30.5%       58.6      3.88   99.3%      0.0%
    PLANT                    2400.4    67.0%     11.2%       75.7      5.05  100.0%      0.0%
    WATER                    4266.1    74.7%     27.0%      358.4     22.88   95.8%      0.0%
    movement turns/game-day: 113.68   PASS turns/game-day: 46.85
    animal cap ticks: EGG=0.27/day, MILK=2.42/day, WOOL=1.29/day
    crop expiry with held yield: STRAWBERRY=60.44/game, TOMATO=72.91/game

  days 15-19 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1500.6    24.3%     33.7%       62.8     11.28   89.9%      0.0%
    COLLECT_FERTILIZER       1072.4    40.2%     37.9%       76.7     14.90   97.1%      0.0%
    FEED                     1040.3    64.5%     15.6%       63.5     12.30   96.8%      0.0%
    FERTILIZE                 755.0    85.3%      5.8%       15.5      3.11  100.0%      0.0%
    HARVEST                  1589.5    48.4%     23.8%       81.4     16.07   98.7%      0.0%
    PLANT                    1680.6    21.6%     11.1%       20.3      4.07  100.0%      0.0%
    WATER                    3587.1    62.2%     25.9%      230.1     43.67   94.9%      0.0%
    movement turns/game-day: 167.23   PASS turns/game-day: 3.27
    animal cap ticks: EGG=0.04/day, MILK=1.12/day, WOOL=0.32/day
    crop expiry with held yield: CARROT=0.05/game, STRAWBERRY=386.02/game, TOMATO=107.57/game, WHEAT=0.06/game

  days 20-24 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1399.9    23.6%     33.2%       59.6     10.95   91.9%      0.0%
    COLLECT_FERTILIZER       1388.9    30.6%     31.0%       68.9     12.86   93.3%      0.0%
    FEED                     1023.8    62.6%     16.7%       63.9     12.46   97.5%      0.0%
    FERTILIZE                1070.5    83.0%      6.7%       23.9      4.78  100.0%      0.0%
    HARVEST                  2742.4    42.2%     26.0%      130.0     25.77   99.1%      0.0%
    PLANT                    1180.9    24.8%     19.9%       31.0      6.20  100.0%      0.0%
    WATER                    3033.6    59.4%     25.4%      201.4     38.06   94.5%      0.0%
    movement turns/game-day: 161.90   PASS turns/game-day: 1.09
    animal cap ticks: EGG=0.06/day, MILK=0.46/day, WOOL=0.27/day
    crop expiry with held yield: CARROT=0.01/game, MELON=0.04/game, STRAWBERRY=1042.11/game, TOMATO=168.97/game, WHEAT=0.13/game

  days 25-29 (telemetry games=1760)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      896.6    32.1%     38.7%       59.2     11.45   96.8%      0.0%
    COLLECT_FERTILIZER       1231.6    34.1%     35.7%       73.4     14.09   96.0%      0.0%
    FEED                      791.1    70.6%     18.8%       56.7     10.96   96.7%      0.0%
    FERTILIZE                 348.8    78.9%      6.6%        7.1      1.42  100.0%      0.0%
    HARVEST                  2053.3    64.9%     22.4%      125.6     24.85   99.4%      0.5%
    PLANT                     595.9    41.2%     23.5%       32.5      6.49  100.0%      0.0%
    WATER                    1562.5    76.3%     24.2%      124.5     23.03   92.5%      0.0%
    movement turns/game-day: 151.61   PASS turns/game-day: 5.70
    animal cap ticks: EGG=0.02/day, MILK=0.12/day, WOOL=0.08/day
    crop expiry with held yield: CARROT=0.01/game, MELON=0.01/game, STRAWBERRY=255.05/game, TOMATO=188.25/game, WHEAT=0.23/game

-- SERVICE TELEMETRY: LOSSES ONLY --

  days 0-14 (telemetry games=880)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1543.2    53.6%     37.5%      162.1     10.55   97.7%      0.0%
    COLLECT_FERTILIZER        946.0    90.1%     42.1%      148.3      9.88   99.9%      0.0%
    FEED                     1648.0    86.5%     22.8%      150.0      9.76   97.5%      0.0%
    FERTILIZE                  62.3    96.0%     17.7%        4.2      0.28  100.0%      0.0%
    HARVEST                   651.1    70.1%     30.5%       58.6      3.88   99.3%      0.0%
    PLANT                    2362.3    67.1%     11.3%       75.4      5.02  100.0%      0.0%
    WATER                    4247.9    74.9%     27.0%      357.4     22.84   95.9%      0.0%
    movement turns/game-day: 113.48   PASS turns/game-day: 47.24
    animal cap ticks: EGG=0.28/day, MILK=2.46/day, WOOL=1.22/day
    crop expiry with held yield: STRAWBERRY=60.63/game, TOMATO=72.11/game

  days 15-19 (telemetry games=880)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1552.5    24.0%     33.0%       63.0     11.27   89.5%      0.0%
    COLLECT_FERTILIZER       1144.9    39.0%     36.8%       76.1     14.66   96.4%      0.0%
    FEED                     1037.7    65.2%     15.8%       64.2     12.41   96.7%      0.0%
    FERTILIZE                 779.5    86.7%      4.9%       13.7      2.73  100.0%      0.0%
    HARVEST                  1547.0    48.6%     24.5%       79.9     15.77   98.6%      0.0%
    PLANT                    1685.2    20.1%     10.9%       18.2      3.65  100.0%      0.0%
    WATER                    3540.6    62.7%     26.3%      227.9     43.33   95.1%      0.0%
    movement turns/game-day: 168.72   PASS turns/game-day: 3.15
    animal cap ticks: EGG=0.06/day, MILK=1.20/day, WOOL=0.28/day
    crop expiry with held yield: CARROT=0.09/game, STRAWBERRY=375.12/game, TOMATO=96.14/game, WHEAT=0.03/game

  days 20-24 (telemetry games=880)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                     1462.9    22.6%     32.9%       58.7     10.70   91.1%      0.0%
    COLLECT_FERTILIZER       1473.1    29.2%     29.9%       67.1     12.39   92.3%      0.0%
    FEED                     1029.1    62.1%     17.0%       63.8     12.44   97.5%      0.0%
    FERTILIZE                1122.2    84.5%      6.5%       24.5      4.90  100.0%      0.0%
    HARVEST                  2700.9    42.5%     26.8%      128.3     25.43   99.1%      0.0%
    PLANT                    1298.1    21.8%     18.5%       26.8      5.35  100.0%      0.0%
    WATER                    2975.8    59.7%     25.7%      196.8     37.20   94.5%      0.0%
    movement turns/game-day: 164.42   PASS turns/game-day: 1.12
    animal cap ticks: EGG=0.07/day, MILK=0.35/day, WOOL=0.27/day
    crop expiry with held yield: CARROT=0.01/game, MELON=0.01/game, STRAWBERRY=1038.58/game, TOMATO=164.62/game, WHEAT=0.08/game

  days 25-29 (telemetry games=880)
    operation             created/g   admit%   assign%  emitted/g  exec/day   exec%  unknown%
    CARE                      894.3    32.5%     38.3%       59.5     11.53   96.9%      0.0%
    COLLECT_FERTILIZER       1220.8    34.3%     35.7%       74.1     14.26   96.3%      0.0%
    FEED                      784.5    71.7%     18.9%       57.1     11.05   96.9%      0.0%
    FERTILIZE                 348.1    80.0%      6.9%        7.4      1.49  100.0%      0.0%
    HARVEST                  2020.8    66.2%     22.6%      124.2     24.57   99.4%      0.5%
    PLANT                     639.5    39.8%     22.8%       31.5      6.31  100.0%      0.0%
    WATER                    1516.4    77.3%     24.1%      122.1     22.62   92.6%      0.0%
    movement turns/game-day: 152.42   PASS turns/game-day: 5.61
    animal cap ticks: EGG=0.02/day, MILK=0.14/day, WOOL=0.05/day
    crop expiry with held yield: STRAWBERRY=248.47/game, TOMATO=189.58/game, WHEAT=0.23/game

==============================================================================
a_v186: 880-880 (50.0%)
==============================================================================

-- ALL GAMES (n=1760) --
  net cash generated, day 0-19     us    +36,250.8   opp    +30,090.7   gap (opp-us)     -6,160.1   (n=1760)
  cash residual (should be ~0), day 0-19     us       +445.4   opp       -848.8   gap (opp-us)     -1,294.2   (n=1760)
    revenue (filled, exact):
      WOOL         us +12,897.18   opp  +7,350.85   gap  -5,546.33
      WHEAT        us  +1,166.35   opp  +5,843.44   gap  +4,677.09
      FERTILIZER   us +12,985.92   opp  +9,472.85   gap  -3,513.06
      MILK         us +15,840.39   opp +12,872.49   gap  -2,967.89
      MELON        us +13,876.27   opp +15,964.12   gap  +2,087.84
      EGG          us  +1,109.72   opp     +10.79   gap  -1,098.92
      TOMATO       us    +587.39   opp      +0.00   gap    -587.39
      STRAWBERRY   us  +7,010.23   opp  +7,544.04   gap    +533.80
      CARROT       us     +50.16   opp      +0.91   gap     -49.26
    avg realized price / unit (revenue/sold):
      TOMATO       us     +66.46   opp      +0.00   gap     -66.46
      WOOL         us    +168.52   opp    +128.69   gap     -39.84
      MELON        us    +162.87   opp    +199.19   gap     +36.32
      MILK         us    +179.47   opp    +160.06   gap     -19.41
      WHEAT        us     +35.81   opp     +43.20   gap      +7.39
      CARROT       us     +46.52   opp     +39.92   gap      -6.59
      FERTILIZER   us     +67.74   opp     +63.88   gap      -3.85
      EGG          us     +53.87   opp     +52.77   gap      -1.10
      STRAWBERRY   us    +198.69   opp    +199.28   gap      +0.59
    production (units, exact):
      WHEAT        us     +49.94   opp    +120.90   gap     +70.95
      FERTILIZER   us    +211.31   opp    +170.55   gap     -40.76
      WOOL         us     +79.62   opp     +57.46   gap     -22.16
      EGG          us     +20.60   opp      +0.20   gap     -20.39
      MELON        us     +92.30   opp     +80.53   gap     -11.77
      MILK         us     +89.77   opp     +80.54   gap      -9.24
      TOMATO       us      +8.84   opp      +0.00   gap      -8.84
      STRAWBERRY   us     +35.29   opp     +37.92   gap      +2.63
      CARROT       us      +1.08   opp      +0.02   gap      -1.06
    seed spend:
      STRAWBERRY   us  +3,015.45   opp  +3,830.68   gap    +815.23
      MELON        us  +1,762.45   opp  +1,229.09   gap    -533.36
      TOMATO       us    +534.94   opp      +3.98   gap    -530.97
      WHEAT        us    +378.23   opp    +738.07   gap    +359.84
      CARROT       us     +66.68   opp    +134.77   gap     +68.09
    animal spend:
      SHEEP        us  +2,770.45   opp  +3,795.45   gap  +1,025.00
      GOOSE        us    +578.35   opp      +3.41   gap    -574.94
      COW          us  +3,412.50   opp  +3,118.18   gap    -294.32
    buy_product spend (filled, exact):
      WHEAT        us  +8,189.38   opp  +9,414.79   gap  +1,225.41
  land spend, day 0-19     us     +3,000.0   opp     +4,317.0   gap (opp-us)     +1,317.0   (n=1760)
  wage spend, day 0-19     us     +5,119.0   opp     +3,232.2   gap (opp-us)     -1,886.8   (n=1760)
  feed actions (count), day 0-19     us       +213.4   opp       +203.9   gap (opp-us)         -9.6   (n=1760)
  fertilize actions (count), day 0-19     us        +19.5   opp        +21.8   gap (opp-us)         +2.4   (n=1760)
    crop tiles, end of window:
      WHEAT        us      +7.62   opp     +25.04   gap     +17.42
      TOMATO       us      +8.78   opp      +0.08   gap      -8.70
      STRAWBERRY   us     +29.91   opp     +33.60   gap      +3.69
      MELON        us      +3.82   opp      +0.36   gap      -3.46
      CARROT       us      +0.48   opp      +0.00   gap      -0.48
    herd, end of window:
      GOOSE        us      +1.93   opp      +0.01   gap      -1.92
      COW          us      +8.53   opp      +7.15   gap      -1.38
      SHEEP        us      +5.54   opp      +6.87   gap      +1.33
  net cash generated, day 20-24    us    +23,894.5   opp    +26,217.3   gap (opp-us)     +2,322.8   (n=1760)
  cash residual (should be ~0), day 20-24    us        +39.2   opp        -79.7   gap (opp-us)       -118.8   (n=1760)
    revenue (filled, exact):
      WHEAT        us    +667.07   opp  +9,506.87   gap  +8,839.81
      STRAWBERRY   us +14,125.74   opp +16,884.38   gap  +2,758.64
      TOMATO       us  +1,180.02   opp      +2.30   gap  -1,177.72
      EGG          us    +735.35   opp      +4.96   gap    -730.39
      MELON        us    +807.85   opp    +115.69   gap    -692.16
      FERTILIZER   us    +662.52   opp  +1,010.34   gap    +347.82
      WOOL         us  +3,269.79   opp  +2,977.55   gap    -292.24
      MILK         us  +6,339.55   opp  +6,178.19   gap    -161.36
      CARROT       us     +62.45   opp      +0.00   gap     -62.45
    avg realized price / unit (revenue/sold):
      WOOL         us    +165.64   opp     +93.84   gap     -71.80
      CARROT       us     +50.03   opp      +0.00   gap     -50.03
      MILK         us    +151.65   opp    +117.49   gap     -34.16
      STRAWBERRY   us    +166.39   opp    +156.17   gap     -10.22
      MELON        us     +51.77   opp     +56.14   gap      +4.37
      EGG          us     +57.73   opp     +54.52   gap      -3.21
      TOMATO       us     +74.09   opp     +71.04   gap      -3.05
      FERTILIZER   us     +25.66   opp     +23.69   gap      -1.97
      WHEAT        us     +48.64   opp     +49.68   gap      +1.03
    production (units, exact):
      WHEAT        us     +41.83   opp     +91.65   gap     +49.82
      STRAWBERRY   us     +85.44   opp    +109.25   gap     +23.81
      FERTILIZER   us     +56.88   opp     +78.13   gap     +21.26
      TOMATO       us     +15.93   opp      +0.32   gap     -15.61
      WOOL         us     +18.23   opp     +31.78   gap     +13.55
      EGG          us     +12.74   opp      +0.09   gap     -12.65
      MILK         us     +41.64   opp     +52.52   gap     +10.88
      MELON        us     +10.45   opp      +1.67   gap      -8.78
      CARROT       us      +1.25   opp      +0.00   gap      -1.25
    seed spend:
      CARROT       us      +1.62   opp     +42.73   gap     +41.10
      WHEAT        us    +338.78   opp    +322.39   gap     -16.39
      MELON        us      +0.18   opp      +0.00   gap      -0.18
    animal spend:
      SHEEP        us     +17.05   opp      +0.00   gap     -17.05
      GOOSE        us      +6.14   opp      +0.00   gap      -6.14
    buy_product spend (filled, exact):
      WHEAT        us  +1,672.90   opp  +8,393.74   gap  +6,720.84
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 20-24    us     +1,880.0   opp     +1,783.8   gap (opp-us)        -96.2   (n=1760)
  feed actions (count), day 20-24    us        +64.0   opp        +74.4   gap (opp-us)        +10.4   (n=1760)
  fertilize actions (count), day 20-24    us        +24.0   opp        +35.7   gap (opp-us)        +11.7   (n=1760)
    crop tiles, end of window:
      WHEAT        us     +18.73   opp     +24.36   gap      +5.63
      TOMATO       us      +5.57   opp      +0.01   gap      -5.56
      STRAWBERRY   us     +23.14   opp     +25.33   gap      +2.20
      CARROT       us      +0.04   opp      +1.88   gap      +1.84
      MELON        us      +0.29   opp      +0.00   gap      -0.29
    herd, end of window:
      GOOSE        us      +1.95   opp      +0.01   gap      -1.94
      COW          us      +8.53   opp      +7.13   gap      -1.40
      SHEEP        us      +5.58   opp      +6.84   gap      +1.27
  net cash generated, day 25-29    us    +21,638.5   opp    +23,630.6   gap (opp-us)     +1,992.0   (n=1760)
  cash residual (should be ~0), day 25-29    us        -75.4   opp        +30.5   gap (opp-us)       +105.9   (n=1760)
    revenue (filled, exact):
      WHEAT        us  +3,894.82   opp +13,403.70   gap  +9,508.89
      TOMATO       us  +3,157.13   opp     +25.47   gap  -3,131.66
      STRAWBERRY   us  +5,542.49   opp  +7,987.46   gap  +2,444.98
      EGG          us  +1,062.43   opp      +7.63   gap  -1,054.81
      WOOL         us  +2,999.50   opp  +3,785.21   gap    +785.71
      CARROT       us     +51.83   opp    +598.95   gap    +547.12
      MILK         us  +6,670.59   opp  +6,217.78   gap    -452.81
      FERTILIZER   us    +613.96   opp    +345.51   gap    -268.45
      MELON        us    +130.01   opp      +0.00   gap    -130.01
    avg realized price / unit (revenue/sold):
      MELON        us     +47.51   opp      +0.00   gap     -47.51
      CARROT       us     +86.06   opp     +53.99   gap     -32.07
      WOOL         us    +127.34   opp     +96.55   gap     -30.79
      MILK         us    +132.67   opp    +115.15   gap     -17.52
      TOMATO       us     +87.04   opp     +75.96   gap     -11.07
      STRAWBERRY   us    +108.87   opp    +116.18   gap      +7.31
      EGG          us     +60.80   opp     +56.87   gap      -3.93
      FERTILIZER   us      +7.27   opp      +7.69   gap      +0.42
      WHEAT        us     +51.36   opp     +51.55   gap      +0.19
    production (units, exact):
      WHEAT        us    +102.21   opp    +166.94   gap     +64.73
      TOMATO       us     +36.27   opp      +0.05   gap     -36.23
      FERTILIZER   us     +84.71   opp     +54.05   gap     -30.66
      EGG          us     +17.47   opp      +0.13   gap     -17.34
      STRAWBERRY   us     +50.35   opp     +67.59   gap     +17.24
      WOOL         us     +21.98   opp     +38.97   gap     +17.00
      CARROT       us      +0.60   opp     +11.18   gap     +10.58
      MILK         us     +48.93   opp     +54.11   gap      +5.18
      MELON        us      +0.79   opp      +0.00   gap      -0.79
    seed spend:
      CARROT       us     +10.68   opp     +48.18   gap     +37.50
      WHEAT        us    +266.93   opp    +265.57   gap      -1.36
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +728.08   opp  +7,467.61   gap  +6,739.53
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=1760)
  wage spend, day 25-29    us     +1,554.0   opp       +929.3   gap (opp-us)       -624.7   (n=1760)
  feed actions (count), day 25-29    us        +57.0   opp        +52.8   gap (opp-us)         -4.2   (n=1760)
  fertilize actions (count), day 25-29    us         +7.4   opp         +9.3   gap (opp-us)         +1.8   (n=1760)
    crop tiles, end of window:
      WHEAT        us      +2.00   opp      +0.81   gap      -1.19
      TOMATO       us      +0.81   opp      +0.01   gap      -0.80
      STRAWBERRY   us      +2.15   opp      +1.39   gap      -0.76
    herd, end of window:
      GOOSE        us      +1.95   opp      +0.01   gap      -1.94
      COW          us      +8.53   opp      +7.08   gap      -1.46
      SHEEP        us      +5.58   opp      +5.69   gap      +0.11

-- LOSSES ONLY (n=880) --
  net cash generated, day 0-19     us    +35,553.1   opp    +33,535.0   gap (opp-us)     -2,018.0   (n=880)
  cash residual (should be ~0), day 0-19     us       +484.8   opp       -842.2   gap (opp-us)     -1,327.0   (n=880)
    revenue (filled, exact):
      WHEAT        us  +1,155.27   opp  +5,650.66   gap  +4,495.39
      WOOL         us +11,756.10   opp  +7,357.40   gap  -4,398.70
      FERTILIZER   us +13,004.90   opp  +9,533.46   gap  -3,471.44
      MELON        us +13,281.33   opp +16,728.49   gap  +3,447.16
      MILK         us +16,550.44   opp +13,941.33   gap  -2,609.11
      EGG          us  +1,225.32   opp      +8.89   gap  -1,216.43
      STRAWBERRY   us  +7,277.81   opp  +8,365.42   gap  +1,087.61
      TOMATO       us    +522.86   opp      +0.00   gap    -522.86
      CARROT       us     +45.64   opp      +1.36   gap     -44.28
    avg realized price / unit (revenue/sold):
      TOMATO       us     +65.64   opp      +0.00   gap     -65.64
      MELON        us    +159.63   opp    +199.82   gap     +40.19
      WOOL         us    +160.51   opp    +132.79   gap     -27.72
      MILK         us    +181.51   opp    +166.18   gap     -15.33
      WHEAT        us     +35.74   opp     +42.98   gap      +7.24
      CARROT       us     +46.17   opp     +39.97   gap      -6.20
      FERTILIZER   us     +67.46   opp     +63.79   gap      -3.66
      STRAWBERRY   us    +209.92   opp    +211.67   gap      +1.75
      EGG          us     +53.55   opp     +52.85   gap      -0.70
    production (units, exact):
      WHEAT        us     +49.40   opp    +119.12   gap     +69.72
      FERTILIZER   us    +210.40   opp    +171.37   gap     -39.03
      EGG          us     +22.88   opp      +0.17   gap     -22.71
      WOOL         us     +76.47   opp     +55.77   gap     -20.70
      MILK         us     +92.58   opp     +84.02   gap      -8.56
      TOMATO       us      +7.97   opp      +0.00   gap      -7.97
      MELON        us     +91.62   opp     +84.30   gap      -7.32
      STRAWBERRY   us     +34.67   opp     +39.59   gap      +4.92
      CARROT       us      +0.99   opp      +0.03   gap      -0.95
    seed spend:
      STRAWBERRY   us  +3,065.00   opp  +3,866.82   gap    +801.82
      MELON        us  +1,759.00   opp  +1,207.45   gap    -551.55
      TOMATO       us    +514.43   opp      +2.10   gap    -512.33
      WHEAT        us    +362.57   opp    +723.57   gap    +361.00
      CARROT       us     +60.52   opp    +146.23   gap     +85.70
    animal spend:
      SHEEP        us  +2,553.41   opp  +3,323.30   gap    +769.89
      GOOSE        us    +646.70   opp      +2.73   gap    -643.98
      COW          us  +3,495.00   opp  +3,296.82   gap    -198.18
    buy_product spend (filled, exact):
      WHEAT        us  +8,199.77   opp  +9,138.18   gap    +938.41
  land spend, day 0-19     us     +3,000.0   opp     +3,913.6   gap (opp-us)       +913.6   (n=880)
  wage spend, day 0-19     us     +5,125.4   opp     +3,273.4   gap (opp-us)     -1,852.1   (n=880)
  feed actions (count), day 0-19     us       +213.7   opp       +201.6   gap (opp-us)        -12.1   (n=880)
  fertilize actions (count), day 0-19     us        +17.5   opp        +21.7   gap (opp-us)         +4.2   (n=880)
    crop tiles, end of window:
      WHEAT        us      +6.91   opp     +24.79   gap     +17.88
      TOMATO       us      +8.41   opp      +0.04   gap      -8.36
      STRAWBERRY   us     +30.50   opp     +34.82   gap      +4.32
      MELON        us      +3.86   opp      +0.16   gap      -3.71
      CARROT       us      +0.28   opp      +0.00   gap      -0.28
    herd, end of window:
      GOOSE        us      +2.16   opp      +0.01   gap      -2.15
      SHEEP        us      +5.11   opp      +6.16   gap      +1.05
      COW          us      +8.74   opp      +7.78   gap      -0.96
  net cash generated, day 20-24    us    +24,680.8   opp    +31,897.0   gap (opp-us)     +7,216.2   (n=880)
  cash residual (should be ~0), day 20-24    us        +73.9   opp       -106.4   gap (opp-us)       -180.3   (n=880)
    revenue (filled, exact):
      WHEAT        us    +547.97   opp  +8,668.84   gap  +8,120.87
      STRAWBERRY   us +15,840.79   opp +20,744.73   gap  +4,903.95
      MILK         us  +6,332.74   opp  +7,599.80   gap  +1,267.06
      TOMATO       us  +1,046.65   opp      +1.91   gap  -1,044.73
      EGG          us    +769.57   opp      +3.93   gap    -765.64
      MELON        us    +688.45   opp     +88.07   gap    -600.38
      WOOL         us  +2,879.65   opp  +3,338.98   gap    +459.33
      FERTILIZER   us    +588.03   opp    +958.45   gap    +370.42
      CARROT       us     +32.14   opp      +0.00   gap     -32.14
    avg realized price / unit (revenue/sold):
      WOOL         us    +158.74   opp    +107.40   gap     -51.34
      CARROT       us     +46.37   opp      +0.00   gap     -46.37
      MELON        us     +43.24   opp     +85.26   gap     +42.02
      MILK         us    +145.34   opp    +124.18   gap     -21.16
      STRAWBERRY   us    +184.03   opp    +176.39   gap      -7.64
      EGG          us     +57.14   opp     +54.03   gap      -3.11
      TOMATO       us     +72.47   opp     +70.17   gap      -2.30
      FERTILIZER   us     +25.83   opp     +23.92   gap      -1.91
      WHEAT        us     +49.09   opp     +49.49   gap      +0.40
    production (units, exact):
      WHEAT        us     +37.87   opp     +91.31   gap     +53.44
      STRAWBERRY   us     +86.37   opp    +119.02   gap     +32.65
      FERTILIZER   us     +54.80   opp     +76.15   gap     +21.35
      MILK         us     +43.49   opp     +61.11   gap     +17.62
      WOOL         us     +16.44   opp     +31.18   gap     +14.74
      TOMATO       us     +14.44   opp      +0.14   gap     -14.30
      EGG          us     +13.47   opp      +0.07   gap     -13.39
      MELON        us     +10.21   opp      +0.45   gap      -9.76
      CARROT       us      +0.69   opp      +0.00   gap      -0.69
    seed spend:
      CARROT       us      +0.09   opp     +50.57   gap     +50.48
      WHEAT        us    +302.43   opp    +317.48   gap     +15.05
      MELON        us      +0.18   opp      +0.00   gap      -0.18
    animal spend:
      SHEEP        us     +12.50   opp      +0.00   gap     -12.50
      GOOSE        us      +3.41   opp      +0.00   gap      -3.41
    buy_product spend (filled, exact):
      WHEAT        us  +1,772.67   opp  +7,484.08   gap  +5,711.41
  land spend, day 20-24    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=880)
  wage spend, day 20-24    us     +1,880.0   opp     +1,762.0   gap (opp-us)       -118.0   (n=880)
  feed actions (count), day 20-24    us        +64.0   opp        +72.4   gap (opp-us)         +8.4   (n=880)
  fertilize actions (count), day 20-24    us        +24.5   opp        +36.2   gap (opp-us)        +11.7   (n=880)
    crop tiles, end of window:
      WHEAT        us     +17.22   opp     +24.60   gap      +7.39
      TOMATO       us      +5.52   opp      +0.01   gap      -5.51
      STRAWBERRY   us     +23.78   opp     +26.88   gap      +3.10
      CARROT       us      +0.00   opp      +2.11   gap      +2.11
      MELON        us      +0.10   opp      +0.00   gap      -0.10
    herd, end of window:
      GOOSE        us      +2.17   opp      +0.01   gap      -2.16
      SHEEP        us      +5.13   opp      +6.15   gap      +1.02
      COW          us      +8.74   opp      +7.78   gap      -0.96
  net cash generated, day 25-29    us    +21,626.5   opp    +27,425.7   gap (opp-us)     +5,799.2   (n=880)
  cash residual (should be ~0), day 25-29    us        -61.2   opp        +23.5   gap (opp-us)        +84.7   (n=880)
    revenue (filled, exact):
      WHEAT        us  +3,695.80   opp +13,254.15   gap  +9,558.35
      STRAWBERRY   us  +6,542.40   opp +10,171.56   gap  +3,629.17
      TOMATO       us  +2,886.26   opp     +12.91   gap  -2,873.35
      WOOL         us  +2,834.03   opp  +4,271.42   gap  +1,437.38
      EGG          us  +1,149.21   opp      +5.88   gap  -1,143.34
      MILK         us  +6,401.89   opp  +7,163.25   gap    +761.37
      CARROT       us      +6.93   opp    +673.95   gap    +667.02
      FERTILIZER   us    +634.54   opp    +374.21   gap    -260.33
      MELON        us     +67.10   opp      +0.00   gap     -67.10
    avg realized price / unit (revenue/sold):
      MELON        us     +29.00   opp      +0.00   gap     -29.00
      CARROT       us     +80.26   opp     +57.34   gap     -22.92
      STRAWBERRY   us    +124.35   opp    +133.61   gap      +9.27
      WOOL         us    +124.23   opp    +115.27   gap      -8.96
      MILK         us    +124.05   opp    +117.68   gap      -6.37
      TOMATO       us     +80.21   opp     +75.77   gap      -4.45
      EGG          us     +59.82   opp     +56.22   gap      -3.60
      FERTILIZER   us      +7.36   opp      +8.36   gap      +1.00
      WHEAT        us     +51.59   opp     +51.66   gap      +0.07
    production (units, exact):
      WHEAT        us     +95.96   opp    +167.97   gap     +72.01
      TOMATO       us     +35.98   opp      +0.06   gap     -35.92
      FERTILIZER   us     +86.35   opp     +53.54   gap     -32.80
      STRAWBERRY   us     +52.33   opp     +74.71   gap     +22.38
      EGG          us     +19.21   opp      +0.10   gap     -19.11
      WOOL         us     +21.29   opp     +36.76   gap     +15.48
      CARROT       us      +0.09   opp     +11.77   gap     +11.69
      MILK         us     +50.29   opp     +60.98   gap     +10.68
      MELON        us      -0.39   opp      +0.00   gap      +0.39
    seed spend:
      CARROT       us      +1.82   opp     +47.57   gap     +45.75
      WHEAT        us    +255.64   opp    +283.68   gap     +28.05
    animal spend:
    buy_product spend (filled, exact):
      WHEAT        us    +838.73   opp  +7,235.96   gap  +6,397.23
  land spend, day 25-29    us         +0.0   opp         +0.0   gap (opp-us)         +0.0   (n=880)
  wage spend, day 25-29    us     +1,556.7   opp       +911.0   gap (opp-us)       -645.7   (n=880)
  feed actions (count), day 25-29    us        +57.4   opp        +52.1   gap (opp-us)         -5.3   (n=880)
  fertilize actions (count), day 25-29    us         +7.8   opp         +8.8   gap (opp-us)         +1.0   (n=880)
    crop tiles, end of window:
      WHEAT        us      +2.29   opp      +0.80   gap      -1.49
      TOMATO       us      +0.82   opp      +0.01   gap      -0.80
      STRAWBERRY   us      +2.12   opp      +1.68   gap      -0.44
    herd, end of window:
      GOOSE        us      +2.17   opp      +0.01   gap      -2.16
      COW          us      +8.74   opp      +7.72   gap      -1.02
      SHEEP        us      +5.13   opp      +5.29   gap      +0.16