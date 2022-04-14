n = int(input())
run = list(map(int, input().split()))

run.sort()
runner = max(run)
runnerup = run.index(runner)

print(run[runnerup-1])
