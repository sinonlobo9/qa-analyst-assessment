def remove_duplicates(items):
    seen = set()

    return [
        item
        for item in items
        if item not in seen and not seen.add(item)
    ]


if __name__ == "__main__":
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []

    values = [1, 2, 2, 3]
    assert remove_duplicates(values) == [1, 2, 3]
    assert values == [1, 2, 2, 3]

    print("All Part 1 tests passed successfully!")