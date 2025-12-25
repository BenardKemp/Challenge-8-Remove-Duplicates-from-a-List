def remove_duplicates(items: list) -> list:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")

    result = []
    seen = set()

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

