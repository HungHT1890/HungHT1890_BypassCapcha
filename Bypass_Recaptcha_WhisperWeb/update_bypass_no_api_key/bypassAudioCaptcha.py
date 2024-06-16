
from time import sleep
from requests import session
from urllib3  import disable_warnings , exceptions
from os import path , makedirs
from traceback import print_exc
# from whisper import transcribe , load_model

disable_warnings(exceptions.InsecureRequestWarning)
ss = session()


def bypassCaptchaAudio(mp3_url,file_name):
    try:
        with open(f'{file_name}.mp3','wb') as file_mp3:
            file_mp3.write(ss.get(url=mp3_url).content)
            api = 'https://whisperapi.com/api/stt'
            file = {'file': open(f'{file_name}.mp3','rb')}
        results = ss.post(url=api,files=file).json()['text']
        return results
    except Exception as f:
        if __name__ == '__main__':
            print_exc()
        print_exc()
        return ''


if __name__ == '__main__':
    bypassCaptchaAudio('https://www.google.com/recaptcha/enterprise/payload/audio.mp3?p=06AFcWeA56kzBzYLpzh9SjNFoveaRXMBIar8Ay57MuGGTv0UQ5Wryxk7eohxz-i0KSveFi3Z6m_so5HTUdeXo2F1tDAcE8Cye3C5DFOSJb6uA_V7aK4oWCcyAJ66qYG7GWeBnTPNMrH666t5qLMSa2efz3J9eM3tUFaBS_dBi7mBB96dQRd5-rVhVIbZ7mzzCrNuGuhYKWUxyc&k=6Ldbp6saAAAAAAwuhsFeAysZKjR319pRcKUitPUO','htth')