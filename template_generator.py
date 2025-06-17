import sys

with open("preamble.txt") as f:
    preamble = f.read()
with open("problem.txt") as f:
    problem = f.read()
with open("enum_start.txt") as f:
    enum_start = f.read()
with open("enum_item.txt") as f:
    enum_item = f.read()
with open("enum_end.txt") as f:
    enum_end = f.read()
with open("postamble.txt") as f:
    postamble = f.read()
with open("newpage.txt") as f:
    newpage = f.read()

title_idx = min([idx for idx,val in enumerate(preamble) if (val == "}" and preamble[idx - 6:idx - 1] == "title")])

def parse(inp):
    course_name = "Math " + inp[0].upper()
    if inp[1][:2] == "hw":
        assignment_name = "Homework "+ inp[1][2:]
    else:
        assignment_name = " ".join([i.capitalize() for i in inp[1].replace("_", " ").split()])
    probs = inp[2].split("+")
    problem_lengths = []
    for i in probs:
        if i.isdigit():
            problem_lengths.append(int(i))
        else:
            mn = [int(j) for j in i.split("x")]
            for j in range(mn[0]):
                problem_lengths.append(mn[1])
    title = course_name + " " + assignment_name
    return title, problem_lengths

def problems(problem_lengths):
    problems = []
    for i in problem_lengths:
        if i == 1:
            problems.append(problem)
        else:
            problems.append(enum_problem(i))
    problems_string = ""
    for idx,val in enumerate(problems):
        problems_string += val
        if idx + 1 != len(problems):
            problems_string += "\n"
            problems_string += newpage
            problems_string += "\n"
    return problems_string

def enum_problem(n):
    problem = enum_start[:-1]
    for i in range(n):
        problem += "\n"
        problem += enum_item
    problem += enum_end
    return problem

def template(inp):
    title, problem_lengths = parse(inp)
    custom_preamble = preamble[:title_idx] + title + preamble[title_idx:]
    output = custom_preamble + "\n" + problems(problem_lengths) + "\n" + postamble
    return output

if __name__ == "__main__":
    print(template(sys.argv[1:]))
