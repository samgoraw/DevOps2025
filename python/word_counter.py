import argparse

parser=argparse.ArgumentParser(description="Text File Word Counter")
parser.add_argument("filename",help="Path to the text file")
args = parser.parse_args()

try:

    with open(args.filename,"r", encoding = "utf-8") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

        print(f"Total number of words : {word_count}")

except FileNotFoundError:
        print(f"Error: The file '{args.filename}' was not found.")
except Exception as e:
        print(f"An unexpected error occurred : {e}")



## Run it mentioned as below
## py filename.py  (you can see validation error)
## py filename.py -h (you can description of arguments)
## py filename.py "sonam soni" 45 (pass name and age see the result)
## py filename.py "sonam soni" 45 --city Delhi (pass name and age with city)