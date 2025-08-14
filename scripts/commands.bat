oc new-app mysql-persistent -p MYSQL_USER=Avi -p MYSQL_PASSWORD="1234" -p MYSQL_DATABASE=mydb -p MYSQL_ROOT_PASSWORD=rootpass
docker build -t mini_openshift:latest .