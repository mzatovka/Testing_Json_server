Расписать инструкцию каким образом развернуть проект через докер пошаговая инструкция

# Testing JSON Server

Проект представляет собой mock REST API сервер на базе **JSON Server**, предназначенный для тестирования API.

В проекте используется Docker для запуска JSON Server в изолированном контейнере.

## Технологии

* **Node.js 20 Alpine**
* **JSON Server**
* **Docker**
* **REST API**
* **JSON**

---

# Запуск проекта через Docker

## 1. Установить Docker

Перед запуском проекта необходимо установить **Docker Desktop**.

После установки запустите Docker Desktop и убедитесь, что Docker работает.

Проверить установку можно командой:

```bash
docker --version
```

Например:

```text
Docker version 28.x.x
```

Также можно проверить работу Docker:

```bash
docker run hello-world
```

Если команда выполнилась успешно, Docker готов к работе.

---

## 2. Клонировать репозиторий

Откройте терминал и выполните:

```bash
git clone https://github.com/mzatovka/Testing_Json_server.git
```

После клонирования перейдите в директорию проекта:

```bash
cd Testing_Json_server
```

---

## 3. Проверить структуру проекта

В проекте должны находиться Dockerfile и файл с тестовыми данными:

```text
Testing_Json_server/
│
├── Dockerfile
├── fixtures/
│   └── db.json
├── public/
├── src/
├── tests/
├── views/
├── package.json
└── README.md
```

`Dockerfile` содержит инструкции для создания Docker image.

В проекте Dockerfile настроен следующим образом:

* используется `node:20-alpine`;
* рабочая директория контейнера — `/app`;
* устанавливается `json-server`;
* используется порт `3000`;
* сервер запускается с файлом `fixtures/db.json`.

---

# 4. Создать Docker Image

Находясь в корневой директории проекта, выполните:

```bash
docker build -t testing-json-server .
```

### Что происходит?

Docker читает `Dockerfile` и создаёт на его основе image.

Команда:

```bash
docker build -t testing-json-server .
```

где:

* `docker build` — создание Docker image;
* `-t testing-json-server` — имя создаваемого image;
* `.` — текущая директория, в которой находится `Dockerfile`.

После успешного выполнения можно проверить созданный image:

```bash
docker images
```

В списке должен появиться:

```text
testing-json-server
```

---

# 5. Запустить Docker Container

После создания image необходимо запустить контейнер:

```bash
docker run -d --name testing-json-server -p 3000:3000 testing-json-server
```

### Что означает команда?

```bash
docker run
```

Создаёт и запускает контейнер.

```bash
-d
```

Запускает контейнер в фоновом режиме.

```bash
--name testing-json-server
```

Задаёт имя контейнера.

```bash
-p 3000:3000
```

Пробрасывает порт:

```text
порт компьютера : порт контейнера
```

То есть:

```text
localhost:3000 → container:3000
```

```bash
testing-json-server
```

Имя Docker image, из которого создаётся контейнер.

Docker официально использует формат `docker run [OPTIONS] IMAGE`, а параметр `-p` используется для публикации порта контейнера на хост-машину.

---

# 6. Проверить запущенный контейнер

Для проверки выполните:

```bash
docker ps
```

В списке должен отображаться контейнер:

```text
testing-json-server
```

Также можно проверить состояние контейнера:

```bash
docker ps -a
```

Команда `docker ps -a` показывает также остановленные контейнеры.

---

# 7. Проверить работу JSON Server

После запуска контейнера JSON Server должен быть доступен по адресу:

```text
http://localhost:3000
```

Откройте этот адрес в браузере.

API использует данные из файла:

```text
fixtures/db.json
```

Для проверки API можно обратиться к endpoint из базы данных, например:

```text
http://localhost:3000/users
```

> Название endpoint зависит от структуры файла `fixtures/db.json`.

---

# 8. Проверить API через браузер или Postman

Для проверки API можно использовать:

* браузер;
* Postman;
* Swagger/другой API-клиент;
* автоматизированные API-тесты.

Например:

```http
GET http://localhost:3000/users
```

Если endpoint `users` присутствует в `fixtures/db.json`, сервер должен вернуть данные в формате JSON.

---

# 9. Посмотреть логи Docker Container

Если сервер не запускается или API не отвечает, сначала рекомендуется посмотреть логи:

```bash
docker logs testing-json-server
```

Для просмотра логов в режиме реального времени:

```bash
docker logs -f testing-json-server
```

Для выхода из режима просмотра логов нажмите:

```text
Ctrl + C
```

---

# 10. Остановить Docker Container

Чтобы остановить сервер:

```bash
docker stop testing-json-server
```

После этого контейнер будет остановлен.

Проверить его состояние:

```bash
docker ps -a
```

---

# 11. Повторно запустить контейнер

Если контейнер уже создан, его не нужно создавать заново.

Достаточно выполнить:

```bash
docker start testing-json-server
```

После запуска сервер снова будет доступен:

```text
http://localhost:3000
```

---

# 12. Удалить Docker Container

Если контейнер больше не нужен:

```bash
docker rm testing-json-server
```

Если контейнер ещё запущен, сначала остановите его:

```bash
docker stop testing-json-server
```

Затем:

```bash
docker rm testing-json-server
```

---

# 13. Удалить Docker Image

Если необходимо полностью удалить созданный image:

```bash
docker rmi testing-json-server
```

Если контейнер, созданный из этого image, ещё существует, сначала удалите контейнер.

---

# Полный сценарий запуска

Если Docker уже установлен, полный запуск проекта можно выполнить следующими командами:

```bash
git clone https://github.com/mzatovka/Testing_Json_server.git
```

```bash
cd Testing_Json_server
```

```bash
docker build -t testing-json-server .
```

```bash
docker run -d --name testing-json-server -p 3000:3000 testing-json-server
```

После этого открыть:

```text
http://localhost:3000
```

---

# Полезные Docker команды

### Посмотреть запущенные контейнеры

```bash
docker ps
```

### Посмотреть все контейнеры

```bash
docker ps -a
```

### Посмотреть Docker images

```bash
docker images
```

### Посмотреть логи

```bash
docker logs testing-json-server
```

### Остановить сервер

```bash
docker stop testing-json-server
```

### Запустить сервер

```bash
docker start testing-json-server
```

### Удалить контейнер

```bash
docker rm testing-json-server
```

### Удалить image

```bash
docker rmi testing-json-server
```

# Testing JSON Server

Проект представляет собой mock REST API сервер на базе **JSON Server**, предназначенный для тестирования API.

В проекте используется Docker для запуска JSON Server в изолированном контейнере.

## Технологии

* **Node.js 20 Alpine**
* **JSON Server**
* **Docker**
* **REST API**
* **JSON**

---

# Запуск проекта через Docker

## 1. Установить Docker

Перед запуском проекта необходимо установить **Docker Desktop**.

После установки запустите Docker Desktop и убедитесь, что Docker работает.

Проверить установку можно командой:

```bash
docker --version
```

Например:

```text
Docker version 28.x.x
```

Также можно проверить работу Docker:

```bash
docker run hello-world
```

Если команда выполнилась успешно, Docker готов к работе.

---

## 2. Клонировать репозиторий

Откройте терминал и выполните:

```bash
git clone https://github.com/mzatovka/Testing_Json_server.git
```

После клонирования перейдите в директорию проекта:

```bash
cd Testing_Json_server
```

---

## 3. Проверить структуру проекта

В проекте должны находиться Dockerfile и файл с тестовыми данными:

```text
Testing_Json_server/
│
├── Dockerfile
├── fixtures/
│   └── db.json
├── public/
├── src/
├── tests/
├── views/
├── package.json
└── README.md
```

`Dockerfile` содержит инструкции для создания Docker image.

В проекте Dockerfile настроен следующим образом:

* используется `node:20-alpine`;
* рабочая директория контейнера — `/app`;
* устанавливается `json-server`;
* используется порт `3000`;
* сервер запускается с файлом `fixtures/db.json`.

---

# 4. Создать Docker Image

Находясь в корневой директории проекта, выполните:

```bash
docker build -t testing-json-server .
```

### Что происходит?

Docker читает `Dockerfile` и создаёт на его основе image.

Команда:

```bash
docker build -t testing-json-server .
```

где:

* `docker build` — создание Docker image;
* `-t testing-json-server` — имя создаваемого image;
* `.` — текущая директория, в которой находится `Dockerfile`.

После успешного выполнения можно проверить созданный image:

```bash
docker images
```

В списке должен появиться:

```text
testing-json-server
```

---

# 5. Запустить Docker Container

После создания image необходимо запустить контейнер:

```bash
docker run -d --name testing-json-server -p 3000:3000 testing-json-server
```

### Что означает команда?

```bash
docker run
```

Создаёт и запускает контейнер.

```bash
-d
```

Запускает контейнер в фоновом режиме.

```bash
--name testing-json-server
```

Задаёт имя контейнера.

```bash
-p 3000:3000
```

Пробрасывает порт:

```text
порт компьютера : порт контейнера
```

То есть:

```text
localhost:3000 → container:3000
```

```bash
testing-json-server
```

Имя Docker image, из которого создаётся контейнер.

Docker официально использует формат `docker run [OPTIONS] IMAGE`, а параметр `-p` используется для публикации порта контейнера на хост-машину.

---

# 6. Проверить запущенный контейнер

Для проверки выполните:

```bash
docker ps
```

В списке должен отображаться контейнер:

```text
testing-json-server
```

Также можно проверить состояние контейнера:

```bash
docker ps -a
```

Команда `docker ps -a` показывает также остановленные контейнеры.

---

# 7. Проверить работу JSON Server

После запуска контейнера JSON Server должен быть доступен по адресу:

```text
http://localhost:3000
```

Откройте этот адрес в браузере.

API использует данные из файла:

```text
fixtures/db.json
```

Для проверки API можно обратиться к endpoint из базы данных, например:

```text
http://localhost:3000/users
```

> Название endpoint зависит от структуры файла `fixtures/db.json`.

---

# 8. Проверить API через браузер или Postman

Для проверки API можно использовать:

* браузер;
* Postman;
* Swagger/другой API-клиент;
* автоматизированные API-тесты.

Например:

```http
GET http://localhost:3000/users
```

Если endpoint `users` присутствует в `fixtures/db.json`, сервер должен вернуть данные в формате JSON.

---

# 9. Посмотреть логи Docker Container

Если сервер не запускается или API не отвечает, сначала рекомендуется посмотреть логи:

```bash
docker logs testing-json-server
```

Для просмотра логов в режиме реального времени:

```bash
docker logs -f testing-json-server
```

Для выхода из режима просмотра логов нажмите:

```text
Ctrl + C
```

---

# 10. Остановить Docker Container

Чтобы остановить сервер:

```bash
docker stop testing-json-server
```

После этого контейнер будет остановлен.

Проверить его состояние:

```bash
docker ps -a
```

---

# 11. Повторно запустить контейнер

Если контейнер уже создан, его не нужно создавать заново.

Достаточно выполнить:

```bash
docker start testing-json-server
```

После запуска сервер снова будет доступен:

```text
http://localhost:3000
```

---

# 12. Удалить Docker Container

Если контейнер больше не нужен:

```bash
docker rm testing-json-server
```

Если контейнер ещё запущен, сначала остановите его:

```bash
docker stop testing-json-server
```

Затем:

```bash
docker rm testing-json-server
```

---

# 13. Удалить Docker Image

Если необходимо полностью удалить созданный image:

```bash
docker rmi testing-json-server
```

Если контейнер, созданный из этого image, ещё существует, сначала удалите контейнер.

---

# Полный сценарий запуска

Если Docker уже установлен, полный запуск проекта можно выполнить следующими командами:

```bash
git clone https://github.com/mzatovka/Testing_Json_server.git
```

```bash
cd Testing_Json_server
```

```bash
docker build -t testing-json-server .
```

```bash
docker run -d --name testing-json-server -p 3000:3000 testing-json-server
```

После этого открыть:

```text
http://localhost:3000
```

---

# Полезные Docker команды

### Посмотреть запущенные контейнеры

```bash
docker ps
```

### Посмотреть все контейнеры

```bash
docker ps -a
```

### Посмотреть Docker images

```bash
docker images
```

### Посмотреть логи

```bash
docker logs testing-json-server
```

### Остановить сервер

```bash
docker stop testing-json-server
```

### Запустить сервер

```bash
docker start testing-json-server
```

### Удалить контейнер

```bash
docker rm testing-json-server
```

### Удалить image

```bash
docker rmi testing-json-server
```

---

# Результат

После выполнения:

```bash
docker build -t testing-json-server .
```

и:

```bash
docker run -d --name testing-json-server -p 3000:3000 testing-json-server
```

JSON Server запускается внутри Docker-контейнера и становится доступен локально через:

```text
http://localhost:3000
```

Dockerfile проекта непосредственно задаёт запуск:

```text
json-server --watch fixtures/db.json --host 0.0.0.0 --port 3000
```

поэтому контейнер использует `fixtures/db.json` как источник mock API данных.


