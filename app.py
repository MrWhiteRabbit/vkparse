import conf, vk_requests

file = open('post.txt', 'w')
user_domain = input('Введите id пользователя: ')

#создаем экземпляр api
api = vk_requests.create_api(app_id=conf.app_id, login=conf.login, password=conf.password)

#api_wall_get
#вытягиваем записи со стены, количество = count
awg = api.wall.get(
    domain=user_domain,
    count=100,
    timeout=10,
    )

#find and view likes for posts in awg
#разбираем массив awg, записываем в файл посты+лайки к ним
count=0
for post in awg['items']:
    get_items = awg.get('items')
    get_element = get_items[count]
    get_likes = get_element.get('likes')
    get_text = get_element.get('text')
    count_likes = get_likes.get('count')
    count+=1
    file.write('\n' + 'Пост:' + '\n' + 
            str(get_text) + '\n' + 
            'Лайков:' + '\n' + 
            str(count_likes) + '\n')

file.close()