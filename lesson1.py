import requests

url = 'https://api.thecatapi.com/v1/images/search?limit=10'

def main():
    #Скачивание 10 котят
    response = requests.get(url).json()


    url_cats = []
    for data in response:
        url_cats.append(data['url'])


    for i in range(10):
        file = open(f'cat{i}.gif', 'wb') #write types
        file.write(
            requests.get(url_cats[i]).content
            )
        file.close()



if __name__ == "__main__":
    main()




