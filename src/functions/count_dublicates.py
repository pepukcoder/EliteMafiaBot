from collections import Counter

def count_duplicates(arr: []):
    counter = Counter(arr)
    most_common = counter.most_common(1)

    if most_common:
        element, count = most_common[0]
        return count - 1, element  # Subtract 1 to exclude the original occurrence
    else:
        return 0, None