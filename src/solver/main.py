import argparse
import solver

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    solve_parser = subparsers.add_parser("solve")
    solve_parser.add_argument("input_path")
    solve_parser.add_argument("-o", "--output")
    solve_parser.add_argument("-t")

    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("input_path")
    verify_parser.add_argument("output_path")
    verify_parser.add_argument("-t")

    args = parser.parse_args()

    if args.command == "solve":
        input_text = open(args.input_path).read()
        problem = solver.input_parser(input_text)
        solution = solver.solver(problem)

        if args.output is None:
            print(solver.solution_formatter(solution))
        else:
            with open(args.output, "w") as f:
                f.write(solver.solution_formatter(solution))
    
