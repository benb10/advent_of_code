def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        in_sq_brackets = False
        strs_in_brackets = []
        strs_out_of_brackets = []

        for i in range(len(line)):
            char = line[i]

            if char == "[":
                in_sq_brackets = True

            if char == "]":
                in_sq_brackets = False

            sub_str = line[i : i + 3]
            if len(sub_str) != 3:
                continue
            if not sub_str.isalpha():
                continue

            is_aba = sub_str == sub_str[::-1] and sub_str[0] != sub_str[1]

            if is_aba:
                if in_sq_brackets:
                    strs_in_brackets.append(sub_str)
                else:
                    strs_out_of_brackets.append(sub_str)

        is_ssl = False
        for aba in strs_in_brackets:
            for bab in strs_out_of_brackets:
                if aba[0] == bab[1] and aba[1] == bab[0]:
                    is_ssl = True
                    break

        if is_ssl:
            total += 1

    return total
