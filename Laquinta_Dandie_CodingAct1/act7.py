def check_prefix(s, prefix):
    
    result = s.startswith(prefix)

    print(result)
    return result


check_prefix("Hello", "He")
check_prefix("Coding", "Con")
check_prefix("Nora", "Circum")