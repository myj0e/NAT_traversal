echo "############ GET UNSAFE USERNAMES ###########"
sudo lastb > btmp.txt

echo "########## UNSAFE USERNAMES COUNTS ##########"
python username_count.py

echo "############## CHECK USERNAME ###############"
python check_username.py