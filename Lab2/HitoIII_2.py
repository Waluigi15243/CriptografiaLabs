from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
opts= Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")

Nombre=["Camilo"]
Apellido=["Omori"]
Email=[""] #Pagina de correo temporal --> https://correotemporal.org/
Password=["am0gus"]
NewPassword=["k1d4m0gus123"]

driver = webdriver.Chrome('./chromedriver.exe')

print("Registro de Usuario")
driver.get('https://pizzahobby.eu/login?create_account=1')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/section/div/div/div/section')))
imput_buton = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/footer/button')

sleep(2)
imput_nombre = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[2]/div[1]/input')

sleep(2)
imput_apellido = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[3]/div[1]/input')

sleep(2)
imput_checbox = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[7]/div[1]/span/input')

sleep(2)
imput_checbox2 = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[1]/div[1]/label[1]/span/input')

sleep(2)
imput_email = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[4]/div[1]/input')

sleep(2)
imput_pass = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[5]/div[1]/div/input')

sleep(2)
imput_nombre.send_keys(Nombre)
sleep(2)
imput_apellido.send_keys(Apellido)
sleep(2)
imput_checbox.click()
sleep(2)
imput_checbox2.click()
sleep(2)
imput_email.send_keys(Email)
sleep(2)
imput_pass.send_keys(Password)
sleep(2)
imput_buton.click()

WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/header/div[2]/div[1]/div')))
imput_buton = driver.find_element(By.XPATH,'/html/body/main/header/div[2]/div[1]/div/div[3]/div[1]/div/div/button/span')
sleep(2)
imput_buton.click()
sleep(2)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/header/div[2]/div[1]/div/div[3]/div[1]/div/div/ul')))
imput_buton = driver.find_element(By.XPATH,'/html/body/main/header/div[2]/div[1]/div/div[3]/div[1]/div/div/ul/li[2]/a')
sleep(2)
imput_buton.click()



sleep(10)
print("Contraseña Olvidada")
driver.get('https://pizzahobby.eu/password-recovery')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/section/div/div/div/section')))
imput_buton = driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/section/section/form/section/div/button[1]')
sleep(5)
imput_email = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/form/section/div/div/input')
sleep(2)
imput_email.send_keys(Email)
sleep(2)
imput_buton.click()









sleep(10)
print("Login")
driver.get('https://pizzahobby.eu/login')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[7]/form/div')))
imput_email= driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/section/div[1]/div[1]/input')
sleep(2)

imput_pass = driver.find_element(By.XPATH ,'/html/body/main/section/div/div/div/section/section/section/form/section/div[2]/div[1]/div/input')
sleep(2)

imput_buton = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/section/form/footer/button')
sleep(2)

imput_email.send_keys(Email)
sleep(2)

imput_pass.send_keys(Password)
sleep(2)

imput_buton.click()
sleep(2)
WebDriverWait(driver,5)


sleep(10)
print("Cambio Interno de Password")
driver.get('https://pizzahobby.eu/identity')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/section/div/div/div/section')))
imput_buton = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/form/footer/button')
sleep(2)

imput_pass = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/form/section/div[5]/div[1]/div/input')
sleep(2)

imput_newpass = driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/section/section/form/section/div[6]/div[1]/div/input')
sleep(2)

imput_pass.send_keys(Password)
sleep(2)
imput_newpass.send_keys(NewPassword)
sleep(2)
imput_buton.click()


sleep(4)

driver.close()
