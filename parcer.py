import requests
# from bs4 import BeautifulSoup


page = requests.get('https://teacherofrussia.ru/api/competitors?year=2023')
# soup = BeautifulSoup(page.text, 'html.parser')

for element in page.json():
    print(element['user']['full_name'])
    with open(f"photos/{element['avatar']['filename']}", "wb") as file:
        photo = requests.get(f"{element['avatar']['file_path']}")
        file.write(photo.content)

# all_links = soup.find_all('link')
# for link in all_links:
#    print(f'{link}\n\n')
# if __name__ == '__main__':
#     # for el in soup:
#     #     print(el)

