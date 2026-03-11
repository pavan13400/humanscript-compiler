def generate_code(commands):

    code = []
    result_defined = False

    for cmd in commands:

        if cmd[0] == "create_list":
            code.append(f"nums = list(range({cmd[1]}, {cmd[2]}+1))")

        elif cmd[0] == "filter_even":
            code.append("nums = [x for x in nums if x % 2 == 0]")

        elif cmd[0] == "filter_odd":
            code.append("nums = [x for x in nums if x % 2 == 1]")

        elif cmd[0] == "sum":
            code.append("result = sum(nums)")
            result_defined = True

        elif cmd[0] == "average":
            code.append("result = sum(nums)/len(nums)")
            result_defined = True

        elif cmd[0] == "print":

            # automatically compute result if missing
            if not result_defined:
                code.append("result = sum(nums)")

            code.append("print(result)")

        elif cmd[0] == "print_list":
            code.append("print(nums)")

    return "\n".join(code)