email="sam_gourav88@hotmail.com"

if [[ $email =~ ^[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
echo "Valid email Id"
else
echo "InValid email Id"
fi