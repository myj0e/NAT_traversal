echo "Use new log message or not"
echo "[0] New log files"
echo "[1] Old log files"
read -p "([1] for default):" YN
if [ "$YN" == "0" ]
then
    echo "############ GET UNSAFE USERNAMES ###########"
    sudo lastb > btmp.txt
fi

echo "############## GET LOCAL USERS ##############"
awk -F: '($3 >= 1000)' /etc/passwd | cut -d: -f1  > localusers.txt
    

echo "########## UNSAFE USERNAMES COUNTS ##########"
python username_count.py

echo "############## CHECK USERNAME ###############"
python check_username.py