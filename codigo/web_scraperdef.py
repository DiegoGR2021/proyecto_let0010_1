import chromedriver_autoinstaller
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

#PENSIONES
url = "https://www.spensiones.cl/apps/rentabilidad/getRentabilidad.php?tiprent=FP"

years = ["years", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006"]
months = ["months", 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
muestras_final = []


for i in range(1, 17):
    for j in range(1, 13):
        time.sleep(2)
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome() 
        driver.set_window_size(1024, 768) 
        driver.get(url)
        driver.save_screenshot("screen.png") 
        sbtn = driver.find_element(By.NAME, "btn")
        dropdown1 = driver.find_element(By.NAME, "aaaa")
        dropdown2 = driver.find_element(By.NAME, "mm")
        year = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr/td/select[1]/option["+str(i)+"]")
        month = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/form/table[1]/tbody/tr[2]/td/table/tbody/tr/td/select[2]/option["+str(j)+"]")
        dropdown1.click()
        year.click()
        dropdown2.click()
        month.click()
        sbtn.click()
        muestras = []

        source = driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        tablas = soup.find_all("table", class_ = "table table-striped table-hover table-bordered table-condensed")[1:]
        largo = len(tablas[0].find_all("td"))
        largoespec = len(tablas[2].find_all("td"))

        for m in range(0, largo, 5):
                dato = []
                dato.append(tablas[0].find_all("td")[m].get_text())
                print(dato)
                muestras.append(dato)

        # FONDO A
        for a in range(0, largo, 5):
            if tablas[0].find_all("td")[a+1].get_text().count("%") == 0:
                A = 0.0
            else:
                A = float(tablas[0].find_all("td")[a+1].get_text().strip("%").replace(',','.'))
            muestras[int(a/5)].append(A)
    
        # FONDO B
        for b in range(0, largo, 5):
            if tablas[1].find_all("td")[b+1].get_text().count("%") == 0:
                B = 0.0
            else:
                B = float(tablas[1].find_all("td")[b+1].get_text().strip("%").replace(',','.'))
            muestras[int(b/5)].append(B)
    
        # FONDO C CASO ESPECIAL
        for c in range(0, largoespec, 6):
            if tablas[2].find_all("td")[c+1].get_text().count("%") == 0:
                C = 0.0
            else:
                C = float(tablas[2].find_all("td")[c+1].get_text().strip("%").replace(',','.'))
            muestras[int(c/6)].append(C)

        # FONDO D
        for d in range(0, largo, 5):
            if tablas[3].find_all("td")[d+1].get_text().count("%") == 0:
                D = 0.0
            else:
                D = float(tablas[3].find_all("td")[d+1].get_text().strip("%").replace(',','.'))
            muestras[int(d/5)].append(D)

        # FONDO E CASO ESPECIAL
        for e in range(0, largoespec, 6):
            if tablas[4].find_all("td")[e+1].get_text().count("%") == 0:
                E = 0.0
            else:
                E = float(tablas[4].find_all("td")[e+1].get_text().strip("%").replace(',','.'))
            muestras[int(e/6)].append(E)
        
        for muestra in muestras:
            muestra.append(years[i])
            muestra.append(months[j])
            muestras_final.append(muestra)


for muestra in muestras_final:
    print(muestra)    

df = pd.DataFrame(muestras_final)
df.to_excel("30-11-2021_rentabilidad_afps.xlsx", index = False)