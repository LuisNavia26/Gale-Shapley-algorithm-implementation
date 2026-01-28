import argparse
import time
import solver
import Verifier

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    solve_parser = subparsers.add_parser("solve")
    solve_parser.add_argument("input_path")
    solve_parser.add_argument("-o", "--output")
    solve_parser.add_argument("-t", "--time", action="store_true")

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("input_path")
    verify_parser.add_argument("output_path")
    verify_parser.add_argument("-t", "--time", action="store_true")

    args = parser.parse_args()

    if args.command == "solve":
        input_text = open(args.input_path).read()
        problem = solver.input_parser(input_text)
        t0 = time.time()
        solution = solver.solver(problem)
        t1 = time.time()

        if args.output is None:
            print(solver.solution_formatter(solution))
            if args.time:
                print(f"Time taken: {t1 - t0}")
        else:
            if args.time:
                print(f"Time taken: {t1 - t0}")
            with open(args.output, "w") as f:
                f.write(solver.solution_formatter(solution))
    elif args.command == "verify":
        input_text = open(args.input_path).read()
        problem = solver.input_parser(input_text)
        parsed_output = Verifier.InputParser(open(args.output_path).read())
        hospital_dict = {hospital.index: hospital.preferences for hospital in problem.hospitals}
        student_dict = {student.index: student.preferences for student in problem.students}
        t0 = time.time()
        verifier = Verifier.Verifier(hospital_dict, student_dict, parsed_output)
        t1 = time.time()
        print(verifier)

        if args.time:
            print()
            print(f"Time taken: {t1 - t0}")

    
