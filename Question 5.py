import re

def find_pattern_occurrences(text):
    pattern = re.compile(r'C\w+jeb')
    matches = pattern.findall(text)
    return len(matches)

# Example usage:
text_to_search = "This is a sample text with a Cexamplejeb and another Cpatternjeb within it."
result = find_pattern_occurrences(text_to_search)
print(f"Number of occurrences: {result}")
