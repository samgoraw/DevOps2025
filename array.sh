names=("alex" "sam" "Kevin" "ashok" "Sally" "Dopi")

echo "First ele: ${names[0]}"
echo "Third element: ${names[4]}"

echo "Total Name: ${#names[@]}" //for all is @

names[1]="John Doe"
echo "Changed element :${names[1]}"


for name in "${names[@]}"; do
echo "$name"
done

## iterate and store all values in one variable and lastly print variable
## after completing the loop
result=''
for name in "${names[@]}"; do
result+="$name ,"
done
echo "$result"



