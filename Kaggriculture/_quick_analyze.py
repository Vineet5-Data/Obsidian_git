import json, statistics

data = json.loads(open('.top_results.json').read())
by_replay = {}
for name, detail in data['details'].items():
    replay_id = name.rsplit('_', 1)[0]
    by_replay.setdefault(replay_id, []).append((name, detail))

ranked = []
for replay_id, entries in by_replay.items():
    total_w = sum(e[1]['wins'] for e in entries)
    total_l = sum(e[1]['losses'] for e in entries)
    worst = min(e[1]['minimum_margin'] for e in entries)
    mean = sum(e[1]['mean_margin'] for e in entries) / len(entries)
    all_margins = []
    for e in entries:
        all_margins.extend(e[1]['margins'])
    ranked.append((replay_id, total_w, total_l, worst, mean, all_margins))

ranked.sort(key=lambda x: x[3])

wins = data["wins"]
losses = data["losses"]
wr = data["win_rate"]*100
mm = data["mean_margin"]
print(f"Total: {wins}W-{losses}L ({wr:.1f}%)")
print(f"Mean margin: {mm:+,.0f}")
print(f"Worst single: {data['minimum_margin']:+,.0f}")
print(f"Best single: {data['maximum_margin']:+,.0f}")
print()
print("WORST 15 OPPONENTS (by worst margin):")
for r in ranked[:15]:
    rid, w, l, worst, mean, margins = r
    pct = w/(w+l)*100 if w+l else 0
    print(f"  {rid}: {w}W-{l}L ({pct:.0f}%) worst={worst:+,.0f} mean={mean:+,.0f}")

print()
print("UNBEATEN OPPONENTS:")
for r in ranked:
    if r[2] == 0:
        rid, w, l, worst, mean, margins = r
        print(f"  {rid}: {w}W-{l}L mean={mean:+,.0f}")

print()
all_margins = []
for r in ranked:
    all_margins.extend(r[5])

print("Margin distribution:")
buckets = [(-25000,-15000), (-15000,-10000), (-10000,-5000), (-5000,-2000), (-2000,0), (0,2000), (2000,5000), (5000,10000), (10000,20000)]
for lo, hi in buckets:
    count = sum(1 for m in all_margins if lo <= m < hi)
    pct = count/len(all_margins)*100
    bar = '#' * int(pct)
    print(f"  [{lo:>7,},{hi:>7,}): {count:>3} ({pct:>4.1f}%) {bar}")

# Identify patterns: do we lose more from one seat?
seat0_margins = []
seat1_margins = []
for name, detail in data['details'].items():
    seat = int(name.rsplit('_', 1)[1])
    for m in detail['margins']:
        if seat == 0:
            seat0_margins.append(m)
        else:
            seat1_margins.append(m)

print()
s0w = sum(1 for m in seat0_margins if m > 0)
s0l = sum(1 for m in seat0_margins if m < 0)
s1w = sum(1 for m in seat1_margins if m > 0)
s1l = sum(1 for m in seat1_margins if m < 0)
print(f"Seat analysis (opp extracted from seat X):")
print(f"  vs seat-0 opps: {s0w}W-{s0l}L ({s0w/(s0w+s0l)*100:.1f}%) mean={statistics.mean(seat0_margins):+,.0f}")
print(f"  vs seat-1 opps: {s1w}W-{s1l}L ({s1w/(s1w+s1l)*100:.1f}%) mean={statistics.mean(seat1_margins):+,.0f}")
