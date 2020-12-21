import requests
from urllib.parse import urljoin

TOKEN = 'insert_your_vk_token_here'
API_BASE_URL = 'https://api.vk.com/method/'
V = '5.21'


class VKApiUser:
    BASE_URL = API_BASE_URL
    USER_BASE_VK_PAGE = 'https://vk.com/id'

    def __create_method_url(self, method):
        return urljoin(self.BASE_URL, method)

    def __init__(self, vk_id, token=TOKEN, version=V):
        self.vk_id = vk_id
        self.token = token
        self.version = version

    def get_user_id(self):
        return self.vk_id

    def get_mutual_friends(self, other_friend):
        response = requests.get(self.__create_method_url('friends.getMutual'), params={
            'access_token': self.token,
            'v': self.version,
            'source_uid': self.vk_id,
            'target_uid': other_friend,
            })
        return response.json()

    def __str__(self):
        return f'{self.USER_BASE_VK_PAGE}{self.vk_id}'

    def __and__(self, other):
        return self.get_mutual_friends(other.get_user_id())


if __name__ == '__main__':
    vk_client = VKApiUser('insert_your_vk_user_id_here')
    user1 = VKApiUser('insert_user1_vk_id_here')
    user2 = VKApiUser('insert_user2_vk_id_here')
    print(f'ID общих друзей у меня и {user1}\n{vk_client.get_mutual_friends(user1.get_user_id())}\n')
    print(f'ID общих друзей у {user1} и {user2}\n {user1 & user2}')
    print(f'ID общих друзей у {vk_client} и {user2}\n {vk_client & user2}\n')
    print(f'ID общих друзей у {vk_client} и {user1}\n {vk_client & user1}\n')
    print(vk_client)
    print(user1)
    print(user2)

