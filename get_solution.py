import json
from pathlib import Path
from argparse import ArgumentParser


MAX_QUESTIONS = 160
QUESTIONS_DIR = Path("/home/iftakhar/Desktop/AlgoExpert/Coding Interview Questions/")
OUTPUT_DIR_PARENT = Path("/home/iftakhar/Desktop/Ubuntu migration/Projects/AlgoExpert-Questions/")

ARG_PARSER = ArgumentParser(description=f"Reads solution of sepcified question from \"{QUESTIONS_DIR}\" directory. And saves the solutions in solution.py file in respective directory.")
ARG_PARSER.add_argument('-q', type=int, help="A question number to get solutions for")


args = ARG_PARSER.parse_args()

def main():
    question_number = args.q
    if not 0<question_number<=MAX_QUESTIONS:
        print("Error: Invalid question number.")
        return
    question_dir_serial = f"{question_number}".rjust(3, '0')
    
    # Get question data file path to read solutions
    question_data_file = next(QUESTIONS_DIR.glob(f"{question_dir_serial}*/*_data.json"))

    # Prepare output file path to write read solutions
    solution_file_dir = next(OUTPUT_DIR_PARENT.glob(f"{question_dir_serial}*/"))
    solution_file_path = solution_file_dir / 'solutions.py'

    # Read solutions
    with open(question_data_file) as file:
        data = json.load(file)
        python_solutions = data['resources']['python']['solutions']
    
    # Write solutions
    with open(solution_file_path, 'w') as solutions:
        for idx, solution in enumerate(python_solutions):
            solutions.write(f"{'#'*60}\n# Solution {idx+1}\n")
            solutions.write(solution)
            if not idx+1==len(python_solutions):
                solutions.write(f"\n\n")

    # Success message
    print(f"Wrote {len(python_solutions)} solutions in \"{solution_file_path}\" file.")

if __name__=='__main__':
    main()
