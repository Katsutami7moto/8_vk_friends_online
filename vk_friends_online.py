import vk
import getpass

APP_ID = 5667329


def get_user_login():
    login = input('Enter your login: ')
    return login


def get_user_password():
    password = getpass.getpass(prompt='Enter your password: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(online_friends):
    print('\nFriends online:\n')
    for friend in online_friends:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    current_login = get_user_login()
    current_password = get_user_password()
    try:
        friends_online = get_online_friends(current_login, current_password)
    except vk.exceptions.VkAuthError as error_message:
        print(error_message)
        exit(1)
    else:
        output_friends_to_console(friends_online)
        input()
