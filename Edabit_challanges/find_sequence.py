def seq_level(lst):
    lst = [lst[x] - lst[x-1] for x in range(1, len(lst))]
    if len(set(lst)) == 1: return "Linear"
    lst = [lst[x] - lst[x-1] for x in range(1, len(lst))]
    if len(set(lst)) == 1: return "Quadratic"
    lst = [lst[x] - lst[x-1] for x in range(1, len(lst))]
    if len(set(lst)) == 1: return "Cubic"

print(seq_level([1, 2, 3, 4, 5]),
      seq_level([2, 10, 26, 50, 82]),
      seq_level([-6, -4, 10, 42, 98, 184]))