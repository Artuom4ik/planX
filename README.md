# PlanX

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
___
#### Данный проект представляет из себя сервис по работе с ссылками и коллекциями ссылок. 
___
>### Запуск сервера с помощью docker-compose:
##### Для Windows
* Для того чтобы запустить, `docker-compose` на своем компьютере, вам потребуется установить [Docker Desktop](https://www.docker.com/products/docker-desktop/).
___
##### Для Linux
* Предварительные требования Для `linux` систем, для его выполнения вам потребуется следующее:

* Доступ к локальному компьютеру или серверу разработки `Ubuntu 20.04 (или выше)` от имени пользователя без привилегий root с привилегиями sudo. Если вы используете удаленный сервер, рекомендуется установить активный брандмауэр. Для настройки ознакомьтесь с документом [«Руководство по начальной настройке сервера Ubuntu 20.04»](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04).
* Система `Docker`, установленная на сервере или локальном компьютере в соответствии с шагами 1 и 2 документа [«Установка и использование Docker в Ubuntu 20.04»](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).

* После выполнения ряда требованний выполните команду для установки `docker-compose`:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Версию выбирайте сами. В ссылке указана 1.26.0

Затем необходимо задать правильные разрешения, чтобы сделать команду `docker-compose` исполняемой:

```
sudo chmod +x /usr/local/bin/docker-compose
```

Чтобы проверить успешность установки, запустите следующую команду:
```
docker-compose --version
```

Вывод будет выглядеть следующим образом:

```
Output
docker-compose version 1.26.0, build 8a1c60f6
```

___
>### Запуск сервера
##### Для Windows 
* Запустите программу `Docker Dosktop`.
* После запуска `Docker Desktop`, в консоле напишите команду:
```
docker-compose up --build
``` 
##### Для Linux:
* После успешной установки `docker-compose`, в консоли  напишите команду: 
```
docker-compose up --build
``` 
* После образ соберется в контейнер и сервер будет запущен.

>### Добавление данных
* Прежде чем вы захотите добавить свои ссылки либо коллекции, вам потребуется зарегестрироваться и аутентифицироваться.
* Для регистрации отправте `POST` на адрес `/accounts/register/` запрос с такими данными: 
```
{
    "email": "example@gmail.com",
    "password": "examplepassword"
}
```
* Далее вам нужно аутентифицироваться. Для этого отправте 'POST' запрос на адрес `accounts/login/`:
```
{
    "email": "example@gmail.com",
    "password": "examplepassword"
}
```
* После успешной аутентификации, можете добавлять свои ссылки и коллекции.

##### Работа с ссылками
* Для `просмотра` содержимого ссылки требуется отправить `GET` запрос по адресу:
```
127.0.0.1:8000/links/id/
```
- где `id` - это `id` ссылки

* Для `добавления` ссылки требуется отправить `POST` запрос с такими данными: 
```
{
    "link": "https://example.com"
}
```
* Для `удаления ` ссылки требуется отправить `DELETE` запрос с такими данными по адресу 
```
127.0.0.1:8000/links/id/
```
- где `id` - это `id` ссылки

* Для `изменения` ссылки требуется отправить `PUT` запрос по адресу 
```
127.0.0.1:8000/links/id/
```
С такими данными: 
```
{
    "title": "Example Website",
    "short_description": "This is an example website",
    "link": "https://www.example.com",
    "image": "example.jpg",
    "link_type": "website",
}
``` 
* Все эти поля не обязательные, можно передавать любые из этих

##### Работа с коллекциями
* Для `просмотра` содержимого коллекции требуется отправить `GET` запрос по адресу:
```
127.0.0.1:8000/collections/id/
```
- где `id` - это `id` ссылки

* Для `добавления` коллекции требуется отправить `POST` запрос по адресу:
```
127.0.0.1:8000/collections/
```
С такими данными: 
```
{
    "name": "Example Collection",
    "short_description": "Example",
    "links": [1, 3, 4]
}
```
- где поле `links` - поле содержащая список `id` ссылок отнсящихся к этой коллекции.

* Для `удаления ` коллекции требуется отправить `DELETE` запрос с такими данными по адресу 
```
127.0.0.1:8000/collections/id/
```
- где `id` - это `id` коллекции

* Для `изменения` коллекции требуется отправить `PUT` запрос по адресу 
```
127.0.0.1:8000/collections/id/
```
С такими данными: 
```
{
    "name": "Example Website",
    "short_description": "This is an example collection",
}
``` 
* Все эти поля не обязательные, можно передавать любые из этих

