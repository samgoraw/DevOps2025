greet()
{

echo "Hello..!"

}
bye()
{

echo "Good bye!"
exit 0

}

while true; do
echo "Choose an option:"
echo "1) Great"
echo "2) Exit"
read -p "Enter your choice:" choice
case $choice in
1) greet ;;
2) bye ;;
*) echo "Invalid choice";;
esac
done
 