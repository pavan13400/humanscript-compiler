import re

def normalize(line):

    line = line.lower()

    # create numbers
    if "create" in line and "from" in line:
        nums = re.findall(r'\d+', line)
        if len(nums) >= 2:
            return f"Create list from {nums[0]} to {nums[1]}"

    # remove odd
    if "remove odd" in line:
        return "Filter odd"

    # remove even
    if "remove even" in line:
        return "Filter even"

    # show result
    if "show result" in line:
        return "Print result"

    # show numbers
    if "show numbers" in line:
        return "Print list"

    return line