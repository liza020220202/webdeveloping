import requests


def main():
    r = requests.get('https://httpbin.org/')
    print(f'{r.status_code=}\n'
          f'{r.content=}\n'
          f'{r.headers=}\n'
          f'{r.cookies}\n')
    with open('page.html', 'wb') as file:
        file.write(r.content)


def posts():
    data = {'key1': 1, 'key2': 2}
    r = requests.post('https://httpbin.org/post', data=data)
    print(f'{r.status_code=}\n'
          f'{r.content=}\n'
          f'{r.headers=}\n'
          f'{r.text=}\n')
    with open('response.txt', 'w') as file:
        file.write(r.text)


if __name__ == '__main__':
    posts()