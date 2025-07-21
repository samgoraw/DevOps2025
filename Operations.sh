firstName="Sam"
lastName="Gourav"

echo "Welcome $firstName $lastName"


num1=10
num2=90

sum="$(($num1+$num2))"

echo "Result: $sum"

echo "Result: $(($num2-$num1))"

read -p "Enter your name :" user_name
echo "Hello, $user_name"

echo "Script Name: $0"

echo "Number of arguments: $#"

echo "All arguments: $@"

echo "All arguments: $?"

echo "First arguments: $1"

