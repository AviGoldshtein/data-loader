docker build -t avigoldshtein/python-app:latest .
docker push avigoldshtein/python-app:latest

oc apply -f mysql-secret.yaml
oc apply -f mysql-pvc.yaml
oc apply -f mysql-deployment.yaml
oc apply -f mysql-service.yaml

oc apply -f python-app-deployment.yaml
oc apply -f python-app-service.yaml
oc apply -f python-app-route.yaml

oc cp ./data_create.sql -n avigoldshtein-dev mysql-<pod-number>:/tmp/data_create.sql
oc cp ./data_insert.sql -n avigoldshtein-dev mysql-<pod-number>:/tmp/data_insert.sql

oc rsh -n avigoldshtein-dev mysql-<pod-number>
mysql -u avi -p mydb < /tmp/data_create.sql



