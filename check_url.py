import requests


# url에 '.com'이 포함되는 지 확인
def dot_come(url):
    if url[-4:] == ".com":
        return True
    else:
        return False

# url에 'https://'이 포함되는 지 확인


def check_http(url):
    if url[0:8] == "https://" or url[0:7] == "http://":
        return True
    else:
        return False


# URL이 유효한 값인 지 확인

def up_down():
    urls_to_check = input(
        "Welcome to IsItDown.py!\nPlease write a URLs you want to check. (separated by comma)\n")
    urls = urls_to_check.split(',')

    for i in urls:
        url = i.replace(' ', '').lower()
        if dot_come(url) == True:
            if check_http(url) == False:
                try:
                    r = requests.get("http://"+url)
                    if(r.status_code == 200):
                        print(f"http://{url} is up!")
                except:
                    print(f"http://{url} is down!")
            else:
                try:
                    r = requests.get(url)
                    if(r.status_code == 200):
                        print(f"http://{url} is up!")
                    else:
                        print(f"http://{url} is down!")
                except:
                    print(f"http://{url} is down!")
        else:
            print(f"{url} is not a valid URL.")


# 게임 시작


def start():
    restart = True
    while restart:
        restart = False
        ask = True
        up_down()

        while ask:
            ask = False
            replay = input("Do you want to start over? y/n ")
            if replay is "y":
                restart = True
            elif replay is "n":
                print("K, Bye!")
                break
            else:
                ask = True
                continue


start()
