import requests
import html
from bs4 import BeautifulSoup


def get_list_feed():
    url = "https://www.feedtheai.com/industry-news/"
    resp = requests.get(url)
    resp_code = resp.status_code
    print (resp_code)
    if resp_code != 200:
        print("error")
        return
    html_content = resp.content
    dom = BeautifulSoup(html_content,'html.parser')
    biglist = dom.select("div.gh-content.gh-canvas div ul")
    print(biglist)
    filtered_repos = []
    for list in biglist:
        name = list.text.strip()
        if "seed" in name or "Seed" in name:
            href_link = list.a.attrs["href"]
            filtered_repos.append({'name': name, 'link':href_link})
        

    print(filtered_repos)

def get_list_neuron():
    url = "https://www.theneurondaily.com/"
    resp = requests.get(url)
    resp_code = resp.status_code
    print (resp_code)
    if resp_code != 200:
        print("error")
        return
    html_content = resp.content
    dom = BeautifulSoup(html_content,'html.parser')
    biglist = dom.find("div", attrs={"class":"flex flex-col divide-y sm:divide-none"})
    filtered_repos = []
    for list in biglist:
        href_link = list.a.attrs["href"]
        name = list.text.strip()
        filtered_repos.append({'name': name, 'link':href_link})


    print(filtered_repos)


    

def get_list_console():
    url = "https://console.dev/latest"
    resp = requests.get(url)
    resp_code = resp.status_code
    print (resp_code)
    if resp_code != 200:
        print("error")
        return
    html_content = resp.content
    dom = BeautifulSoup(html_content,'html.parser')
    biglist = dom.find("div", attrs={"class":"latest-newsletter-list"})
    filtered_repos = []
    for list in biglist:
        href_link = list.a.attrs["href"]
        name = list.text.strip()
        filtered_repos.append({'name': name, 'link':href_link})


    print(filtered_repos)



if __name__ == "__main__":
    print("started scraping")
    get_list_console()