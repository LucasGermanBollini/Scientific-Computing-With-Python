def arithmetic_arranger(problems, show_answers=False):
    error = []
    #This is the legth checker
    if len(problems) > 5:
        error = 'Error: Too many problems.'
    #This is the operator checker
    if error == []:
        for i in problems:
            if error == []:
                if '*' in i or '/' in i:
                    error = "Error: Operator must be '+' or '-'."
    #This is the digits checker               
    if error == []:
        for i in problems:
            digits = i.split()
            for j in digits:
                if len(j) > 4:
                    error = 'Error: Numbers cannot be more than four digits.'
                try:
                    if j != '-' and j != '+':
                        int(j)
                except ValueError:
                    error = 'Error: Numbers must only contain digits.'
    #Then, if no conditional were activated, we start doing our convertion.
    #Print process:
    spaces_general = []
    if error == []:
        first_line = []
        count = 0
        space_between = 0
        for problem in problems:
            if len(problem.split()[0]) > len(problem.split()[2]):
                space_between = len(problem.split()[0]) + 2
            else:
                space_between = len(problem.split()[2]) + 2
            if count == 0:
                first_line.append(f" "*(space_between-len(problem.split()[0])) + problem.split()[0])
            else:
                first_line.append(f" "*(space_between-len(problem.split()[0])+4) + problem.split()[0])
            count += 1
        first_line = "".join(first_line)
        second_line = []
        count = 0
        for problem in problems:
            if len(problem.split()[0]) > len(problem.split()[2]):
                space_between = len(problem.split()[0]) + 2
            else:
                space_between = len(problem.split()[2]) + 2
            spaces_general.append(space_between)
            if count == 0:
                second_line.append(problem.split()[1]+f" "*(space_between-len(problem.split()[2])-1)+problem.split()[2])
            else:
                second_line.append(f" "*4 + problem.split()[1]+f" "*(space_between-len(problem.split()[2])-1)+problem.split()[2])
            count += 1    
        second_line = "".join(second_line)        
        third_line = []
        count = 0
        for problem in problems:
            if len(problem.split()[0]) > len(problem.split()[2]):
                space_between = len(problem.split()[0]) + 2
            else:
                space_between = len(problem.split()[2]) + 2
            if count == 0:
                third_line.append(f"-"*space_between)
            else:
                third_line.append(f" "*4+f"-"*space_between)
            count += 1    
        third_line = "".join(third_line)
        
    count = 0
    results_list = []
    space_start = 0
    if show_answers and error == []:
        for problem in problems:
            first_cal = int(problem.split()[0])
            second_cal = int(problem.split()[2])
            result = "None"
            if problem.split()[1] == '-':
                result = first_cal - second_cal
            else:
                result = first_cal + second_cal
            if count > 0:
                space_start = 4
            results_list.append(f" "*(space_start)+f" "*(spaces_general[count]-len(str(result)))+f"{result}")
            count += 1
        results_list = "".join(results_list)
        problems = first_line+"\n"+second_line+"\n"+third_line+"\n"+results_list
    if not show_answers and error == []:
        problems = first_line+"\n"+second_line+"\n"+third_line
    
    
    
    
    return problems if error == [] else error

print(f'\n{arithmetic_arranger(["1785 + 96","27 - 3", "5000 + 1700"],True)}')
