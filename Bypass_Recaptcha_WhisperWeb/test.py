from selenium.webdriver import Chrome , ChromeOptions , ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from requests import session
from os.path import abspath
_service = ChromeService('chromedriver.exe')
def setup_driver():
    options = ChromeOptions()
    options.add_argument('--proxy-server=127.0.0.1:40000')
    return Chrome(service=_service,options=options)


def get_audio_captcha(driver,file_name='test.mp3'):
    driver.get('https://www.google.com/recaptcha/api2/demo')
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@title="reCAPTCHA"]')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="recaptcha-anchor"]'))).click()
    driver.switch_to.default_content()
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[contains(@title,"expires")]')))
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="recaptcha-audio-button"]'))).click()
    audio_url = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="rc-audiochallenge-tdownload-link"]'))).get_attribute('href')
    audio_name = 'test.mp3'
    with open(audio_name,'wb') as file_audio:
        file_audio.write(session().get(audio_url).content)

def send_audio(driver,file_path='test.mp3'):
    driver.get('https://whisperapi.com/speech-to-text-free-tool')
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@type="file"]'))).send_keys(abspath(file_path))
    results = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/p'))).text
    source = driver.page_source
    results = source.split('<h3>Transcription Result:</h3><p>')[1].split('</p>')[0]
    print(results)
    with open('test.txt','w',encoding='utf-8') as file_source:
        file_source.write(str(driver.page_source))
        
if __name__ == '__main__':
    driver = setup_driver()
    # get_audio_captcha(driver)
    send_audio(driver)
    input("Enter to close")
    driver.close()    
