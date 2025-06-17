import argparse
  
def main():
    parser = argparse.ArgumentParser(description = "file sorter")
    
    parser.add_argument("-r", "--reverse", action = "store_true", help = "reverse sorter")
    parser.add_argument("-o", "--output", required = True, help = "Output of sorted lines")
    
    parser.add_argument("input_file")
    
    args = parser.parse_args()
  
    try:
        with open(args.input_file, "r", encoding="utf-8-sig") as infile:
            lines = [line.rstrip('\n') for line in infile.readlines()]
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied for file '{args.input_file}'.")
        return

    sorted_lines = sorted(lines, key=lambda x: int(x), reverse=args.reverse)

    try:
        with open(args.output, "w", encoding="utf-8") as outfile:
            for line in sorted_lines:
                outfile.write(line + '\n')
    except PermissionError:
        print(f"Error: Permission denied for output file '{args.output}'.")
        return

    print(f"sorted '{args.input_file}' saved to '{args.output}'"
          + (" (in reverse order)." if args.reverse else "."))

if __name__ == "__main__":
    main()