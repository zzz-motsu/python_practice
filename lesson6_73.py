import builtins

builtins.print()

ranking = {
    'A': 100,
    'B': 85,
    'c': 95
}

# for key in ranking:
#     print(key)

print(sorted(ranking, key=ranking.get, reverse=True))