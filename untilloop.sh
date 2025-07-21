count=0

until [ $count -gt 5]; do
echo "Counter: $count"
((count++))
done