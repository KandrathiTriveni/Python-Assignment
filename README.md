# RouteMobile Assignment

## Prerequisites
- Python 3.x
- RabbitMQ
- Erlang

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Flask Application

```bash
python app.py
```

## Run Consumer

```bash
python consumer.py
```

## POST API

**URL**

```
http://127.0.0.1:5000/items
```

**Method**

POST

**Body**

```json
{
    "item":"book"
}
```

**Response**

```
202 Accepted
```

## GET API

**URL**

```
http://127.0.0.1:5000/delay?delay_value=2
```

**Method**

GET

**Response**

```json
{
    "time_taken": 2.15
}
```