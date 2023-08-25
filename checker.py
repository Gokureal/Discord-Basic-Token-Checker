from requests import get, post
from random import randint

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "rrror" in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Geçersiz'
    elif "errror" in str(response.content):
        return 'Phone Lock'
    else:
        return 'Geçerli'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                    print(f'Token: {token} geçerli')
                    checked.append(token)
                else:
                    print(f'Token: {token} geçersiz')
        if len(checked) > 0:
            save = input(f'{len(checked)} geçerli tokenler\nkaydedilsin mi? (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'tokenler {name}.txt kaydedildi')
        input('enter')
    except:
        input('txt açılamadı')
