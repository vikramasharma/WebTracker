import requests
import html
from bs4 import BeautifulSoup



def stars_count(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    stars = soup.find("span", id= "repo-stars-counter-star")
    str = stars.text.strip()
    if 'k' in str:
        return int( float( str.split('k')[0] ) * 1000 )
    else:
        return int(str)


    
def get_contributors(url):
    c_url = url+ "/graphs/contributors"
    contributors = []
    c_resp = requests.get(c_url).content
    c_dom = BeautifulSoup(c_resp,'html.parser')
    c_list = c_dom.find_all("li", attrs= {"class":"contrib-person"})
    count = 0
    for c in c_list:
        if (count>=3):
            break
        contact = c.a.attrs['href']
        contributors.append(contact)
        count+=1
    print(c_list)
    return contributors


def get_list_repos():
    url = "https://github.com/vinta/awesome-python"
    resp = requests.get(url)
    resp_code = resp.status_code
    print (resp_code)
    if resp_code != 200:
        print("error")
        return
    html_content = resp.content
    dom = BeautifulSoup(html_content,'html.parser')
    biglist = dom.select("article ul li")
    filtered_repos = []
    for list in biglist:
        href_link = list.a.attrs["href"]
        if "github.com" in href_link:
            s_count = stars_count(href_link)
            if s_count>500:
                print(s_count + " Github stars")
                print(href_link)
                name = href_link[1:]
                contributors = get_contributors(href_link)
                filtered_repos.append({"label": name,
                "link": href_link, "contributors": contributors})

    print(filtered_repos)



if __name__ == "__main__":
    print("started scraping")
    get_list_repos()