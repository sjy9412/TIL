import webbrowser

def make_url(toke, method):
    return f'https://api.telegram.com/bot{token}/{method}'

def docs():
    webbrowser.open('https://telegram.com')
    return True