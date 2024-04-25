from requests import session
ss = session()

def convert_speech_text(file_path,api_key):
    file = {'file': open(file_path,'rb')}
    res = ss.post(url='https://transcribe.whisperapi.com',headers={'Authorization': f'Bearer {api_key}'},files=file).json()['text']
    return res




if __name__ == '__main__':
    api_key = 'LFHLTUXWNDLT1ENZNKLS5QW53TLN8XLN'
    file_path = 'audio.mp3'
    # results = convert_speech_text(file_path,api_key)
    # print(results)