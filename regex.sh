ip=192.168.1.1

if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
echo "Valid IP address"
else
echo "InValid IP address"
fi

String = "My number is 121345873 should match with some pattern 872832"

if [[ $String =~ [0-9]{8} ]]; then
echo "String contains 8 digit in row"
else
echo "No match found"
fi