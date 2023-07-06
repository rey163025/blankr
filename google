import webbrowser


def google(web):
    while True:
        if web.startswith('https://'):
            path = 'open -a /Applications/Google\ Chrome.app  %s'
            webbrowser.get(path).open(web)
            break
        else:
            print('NOT URL')
            web = input()


google(input())
