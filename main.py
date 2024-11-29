import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://snusme.eu/'
    response = requests.get(url)
    print(response.status_code)
    #print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find_all("div", class_='flex-col')
    print([i.text for i in spoon])

    with open("page.txt", "a", encoding='UTF=8') as file:
        file.write(''.join([i.text for i in spoon]))
    #part = soup.find("div", class_="text-container",)
    #with open("page.txt", 'a', encoding='UTF-8') as file:
        #file.write(part.text)  


if __name__ == "__main__":
    main()
