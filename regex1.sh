String="387-654-3212"

if [[ $String =~ ^[7-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
echo "Mobile pattern found"

else
 echo "No match found"

 fi
