#Добавляем образ clickhouse и postgreSQL в docker
docker pull yandex/clickhouse-server
docker pull postgres

#Создаем volume для clickhouse и postgreSQL
docker volume create clickhouse_vol
docker volume create postgres_vol


#Создаем сеть
docker network create project_net


#Поднимаем контейнер postgreSQL
docker run --rm -d --name postgres \
    -e POSTGRES_PASSWORD=admin123 \
    -e POSTGRES_USER=admin \
    -e POSTGRES_DB=hotels \
    -v postgres_vol:/var/lib/postgresql/data \
    --net=project_net \
    -p 5432:5432 \
    postgres:latest

#Поднимаем контейнер Clickhouse
docker run --rm -d --name clickhouse \
    -p 8123:8123 --ulimit nofile=262144:262144 \
    -v clickhouse_vol:/var/lib/clickhouse \
    yandex/clickhouse-server

#Подключаемся к ClickHouse с помощью DBeaver. Создаем таблицы

docker exec -it 5df26121ff11 /bin/bash



# Получение таблиц из сжатых tsv- 
# Скачивание и импортирование хитов из сжатого tsv-файла

#Обновим репозиторий
apt-get update

#Команда, которая удалит вольюмы - docker volume prune




#Установим curl
apt-get install curl

Получение таблиц из 
Скачивание и импортирование партиций hits:

curl -O https://datasets.clickhouse.com/hits/partitions/hits_v1.tar
tar xvf hits_v1.tar -C /var/lib/clickhouse # путь к папке с данными ClickHouse
# убедитесь, что установлены корректные права доступа на файлы
sudo service clickhouse-server restart
clickhouse-client --query "SELECT COUNT(*) FROM datasets.hits_v1"

Скачивание и импортирование партиций посещений:

curl -O https://datasets.clickhouse.com/visits/partitions/visits_v1.tar
tar xvf visits_v1.tar -C /var/lib/clickhouse # путь к папке с данными ClickHouse
# убедитесь, что установлены корректные права доступа на файлы
sudo service clickhouse-server restart
clickhouse-client --query "SELECT COUNT(*) FROM datasets.visits_v1"