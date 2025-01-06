from redis import StrictRedis

def send_notify(file_path: str,telegaram_id: str,) -> str | None:
    """Отправка сообщения"""
    return None

def subscribe_channel(channel_name: str):
    """Прослушка сооющений с канала"""
    # Пока редис использую 
    # TODO дополнить кафку
    try:
        client = StrictRedis(host='localhost', port=6379, password='root', username='root', db=0)
        pubsub = client.pubsub()
        pubsub.subscribe(channel_name)

        for message in pubsub.listen():
            if message['type'] == 'message':
                data = message['data'].decode('utf-8')

    except Exception as e:
        print("Ошибка подключения:", e)
    finally:
        client.close()
    
if __name__ == '__main__':
    channel_name = 'notify_channel'
    subscribe_channel(channel_name)
