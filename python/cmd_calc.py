import argparse

parser=argparse.ArgumentParser(description="Command Line calculator")
parser.add_argument("num1", type=float, help="first agument")
parser.add_argument("operator", type=str, choices=["add","sub","mul"] ,help="Operator: add, sub, or mul")
parser.add_argument("num2",type=float,help="second argument")


args = parser.parse_args()

if args.operator == "add":
     result = args.num1 + args.num2
elif args.operator == "sub":
     result = args.num1 - args.num2
else:
     result = args.num1 * args.num2

print(f"Result of  {args.operator} between {args.num1} and {args.num2} is: {result}")

## Run it mentioned as below
## py filename.py  (you can see validation error)
## py filename.py -h (you can description of arguments)
## py filename.py "sonam soni" 45 (pass name and age see the result)
## py filename.py "sonam soni" 45 --city Delhi (pass name and age with city)

#num1,num2,operator
#result