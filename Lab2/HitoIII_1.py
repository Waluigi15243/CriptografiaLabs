import _random
import email
from time import sleep
from tkinter import E, N, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")

Nombre = ["Camilo"]
Apellido = ["Omori"]
Email = [""] #Pagina de correo temporal --> https://temp-mail.org/es/change
Telefono = [""] #Inserte un numero telefonico
Password = ["am0gus"]
NewPassword = ["k1dam0gus"]


driver = webdriver.Chrome('./chromedriver.exe')

print("Registro de Usuario")
driver.get('https://www.dominospizza.cl/users/new')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[10]/div')))
imput_buton = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[2]/span/input')

sleep(2)
imput_nombre = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[2]/div[1]/input')

sleep(2)
imput_apellido = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[2]/div[2]/input')

sleep(2)
imput_telefono = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[3]/div[2]/div/div/input')

sleep(2)
imput_email = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[3]/div[1]/input')

sleep(2)
imput_pass = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[4]/div[1]/input')

sleep(2)
imput_confirmpass = driver.find_element(By.XPATH,'/html/body/div[10]/div/form/div[1]/div/div[4]/div[2]/input')

sleep(2)
imput_nombre.send_keys(Nombre)
sleep(2)
imput_apellido.send_keys(Apellido)
sleep(2)
imput_telefono.send_keys(Telefono)
sleep(2)
imput_email.send_keys(Email)
sleep(2)
imput_pass.send_keys(Password)
sleep(2)
imput_confirmpass.send_keys(Password)
sleep(2)
imput_buton.click()



sleep(10)
print("Contraseña Olvidada")
driver.get('https://www.dominospizza.cl/')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[6]/nav/ul')))
imput_buton = driver.find_element(By.XPATH, '/html/body/div[6]/nav/ul/span/li[1]/span')
sleep(2)
imput_buton.click()
sleep(2)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[7]/form/div')))
imput_buton = driver.find_element(By.XPATH, '/html/body/div[7]/form/div/div[3]/div[2]/div/div[3]/span/span')
sleep(2)
imput_buton.click()
sleep(5)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/form/div')))
imput_email = driver.find_element(By.XPATH,'/html/body/form/div/div[4]/div/div/div/input')
sleep(2)
imput_buton = driver.find_element(By.XPATH,'/html/body/form/div/div[5]/span/input')
sleep(2)
imput_email.send_keys(Email)
sleep(2)
imput_buton.click()









sleep(10)
print("Login")
driver.get('https://www.dominospizza.cl/')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[6]/nav/ul')))
imput_buton = driver.find_element(By.XPATH, '/html/body/div[6]/nav/ul/span/li[1]/span')
sleep(2)
imput_buton.click()
sleep(2)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[7]/form/div')))
imput_email= driver.find_element(By.XPATH,'/html/body/div[7]/form/div/div[3]/div[2]/div/div[1]/div/input')
sleep(2)

imput_pass = driver.find_element(By.XPATH ,'/html/body/div[7]/form/div/div[3]/div[2]/div/div[2]/div/input')
sleep(2)

imput_buton = driver.find_element(By.XPATH,'/html/body/div[7]/form/div/div[3]/div[3]/button')
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
driver.get('https://www.dominospizza.cl/users/edit')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[6]/nav/ul')))
imput_buton = driver.find_element(By.XPATH,'/html/body/div[6]/nav/ul/span/li[1]/a[1]')
sleep(5)
imput_buton.click()
sleep(2)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[10]/div[1]/ul')))
imput_buton = driver.find_element(By.XPATH,'/html/body/div[10]/div[1]/ul/li[2]/a')
sleep(2)

imput_buton.click()
sleep(2)

WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[10]/div[2]/form/div')))
imput_buton = driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/form/div/div[3]/div/div[2]/input')
sleep(2)

imput_newpass = driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/form/div/div[2]/div/div[5]/div/input')
sleep(2)

imput_confirmpass = driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/form/div/div[2]/div/div[6]/div/input')
sleep(2)

imput_newpass.send_keys(NewPassword)
sleep(2)
imput_confirmpass.send_keys(NewPassword)
sleep(2)
imput_buton.click()


sleep(4)
driver.close()
