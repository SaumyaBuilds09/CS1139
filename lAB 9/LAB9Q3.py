balls = input().split()

total_runs = 0
wickets = 0
boundaries = 0
runs_per_over = []
over_runs = 0
count = 0

for ball in balls:
    if ball == "W":
        wickets += 1
    else:
        runs = int(ball)
        total_runs += runs
        over_runs += runs

        if runs == 4 or runs == 6:
            boundaries += 1

    count += 1

    if count == 6:
        runs_per_over.append(over_runs)
        over_runs = 0
        count = 0

if count > 0:
    runs_per_over.append(over_runs)

print("Total Runs:", total_runs)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", runs_per_over)