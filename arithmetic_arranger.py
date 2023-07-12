def arithmetic_arranger(problems, show_answers=False):
    
    # Initializing string variables
    top_line = ""
    bot_line = ""
    dashes = ""
    answers_line = ""
    arranged_problems = ""
  
    # Da Rules
    if len(problems) > 5:
        return "Error: Too many problems."
      
    for problem in problems:
        first_operand, operator, second_operand = problem.split()
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Lines stuff
        max_len = max(len(first_operand), len(second_operand))
        
        top_line += first_operand.rjust(max_len + 2) + '    '
        
        bot_line += operator + ' ' + second_operand.rjust(max_len) + '    '
        
        dashes += '-' * (max_len + 2) + '    '
        
        # Calculations if True
        if show_answers:
            if operator == '+':
                answer = str(int(first_operand) + int(second_operand))
            
            else:
                answer = str(int(first_operand) - int(second_operand))
                
            answers_line += answer.rjust(max_len + 2) + '    '
            
    # Formatting the problems
    
    arranged_problems += top_line.rstrip() + '\n'
    arranged_problems += bot_line.rstrip() + '\n'
    arranged_problems += dashes.rstrip()
    
    if show_answers:
        arranged_problems += '\n' + answers_line.rstrip()
        
    return arranged_problems

    