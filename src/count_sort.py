from collections import Counter


def count_sort(in_string):
    """
    O(nlogn) solution for count sort string.
    """
    count = Counter(in_string)
    out_string = ""
    for letter, count in sorted(count.most_common(), key=lambda x: x[1] - 0.001 * ord(x[0]), reverse=True):
        out_string += letter

    return out_string


def count_sort_opt(in_string):
    sort_count = 255 * [0]
    for c in in_string:
        sort_count[ord(c)] += 1

    return ""


def general_test(in_string, expected_output, count_sort=count_sort):
    assert(count_sort(in_string) == expected_output)


if __name__ == "__main__":
    general_test("bbba", "ba")
    general_test("ba", "ab")
    general_test("eeaazzzz", "zae")
