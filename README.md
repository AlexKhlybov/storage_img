# API приложениея для загрузки файлов

## Установка
Устанавливаем docker и docker-compose:
```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
usermod -aG docker $USER
```

Устанавливаем Pipenv:
```
pip3 install pipenv
```

Переходим в папку проекта:
```
cd storage_img
```

Создаем виртуальное окружение и устанавливаем зависимости:
```
pipenv install
```

Активируем виртуальное окружение:
```
pipenv shell
```

Копируем пример файла .env, после копирования, загляните в него, может быть вы захотите внести свои секреты:
```
cp example.env .env
```

Поднимаем базу данных в докер
```
docker-compose up -d
```

Запускаем сервер:
```
python3 main.py
```

## Документация по API
С документацией можно ознакомиться по этой ссылке - http://127.0.0.1:8000/docs/