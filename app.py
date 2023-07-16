import requests
import html
from bs4 import BeautifulSoup


def gh_test():
    url = f"https://api.github.com/users/vikramasharma"
    user_data = requests.get(url).content
    print(user_data)


def stars_count(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    stars = soup.find("span", id="repo-stars-counter-star")
    str = stars.text.strip()
    if 'k' in str:
        return int(float(str.split('k')[0]) * 1000)
    else:
        return int(str)


def get_contributors(tag):
    url = f"https://api.github.com/repos/"
    c_url = url + tag + "/contributors?anon=1"
    contributors = []
    c_resp = requests.get(c_url).content
    count = 0
    print(c_resp)
    for c in c_resp:
        if (count >= 3):
            break
        #print(c)
        contributors.append(c["url"]) 
        #here we can add a part to scrape their other repos, see get_related_repos, filter by stars using star_count
        #get_related_repos(tag)
        count+=1
    #return contributors

    #print(contributors)
    #return contributors

    # c_dom = BeautifulSoup(c_resp, 'html.parser')
    # c_list = c_dom.find_all("li", attrs={"class": "contrib-person"})
    # count = 0
    # for c in c_list:
    #     if (count >= 3):
    #         break
    #     contact = c.a.attrs['href']
    #     contributors.append(contact)
    #     count += 1
    # # print(c_list)
    # return contributors


def get_related_repos(tag):
    t1 = tag.split("/")
    user = t1[1]
    url = f"https://api.github.com/users/"+user+"/repos"
    r_resp = requests.get(url).content
    projects = []
    for r in r_resp:
        stars = r["watchers_count"]
        if (stars>100):
            projects.append(r["html_url"] + stars + " stars")

    return projects




def get_list_repos():
    url = "https://github.com/vinta/awesome-python"
    resp = requests.get(url)
    resp_code = resp.status_code
    print(resp_code)
    if resp_code != 200:
        print("error")
        return
    html_content = resp.content
    dom = BeautifulSoup(html_content, 'html.parser')
    biglist = dom.select("article ul li")
    filtered_repos = []
    for list in biglist:
        href_link = list.a.attrs["href"]
        if "github.com" in href_link:
            s_count = stars_count(href_link)
            if s_count > 500:
                print(s_count, "stars")
                print(href_link)
                name = href_link[19:]
                print(name)
                contributors = get_contributors(name)
                filtered_repos.append({"label": name,
                                       "link": href_link, "contributors": contributors})

    # print(filtered_repos)


if __name__ == "__main__":
    print("started scraping")
    gh_test()
    get_list_repos()

