def busqueda_Google(df,columnas,exacta):
    """
    Función que realiza un scrapping a una búsqueda exacta en Google (solo a la primera página). 
    
    Inputs:
            df ------> Dataframe
            columnas ------> Lista de columnas a realizarle la búsqueda
            exacta ------> Booleano que indica si la búsqueda a realizar es por palabra exacta o no
    
    Outputs:
            NO HAY. Se sobreescribe el dataframe creando una columna por cada columna a buscar.
            
    NOTA: La velocidad de ejecución es lenta dado la librería que se usa (para no ser bloqueado por Google)
    """
    options=Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-translate')
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Quitar para aumentar la velocidad
    options.add_experimental_option('useAutomationExtension', False) # Quitar para aumentar la velocidad
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    for col in columnas:
        for row in tqdm(df.itertuples(),total=df.shape[0]):
            liks = [] ; titles = []
            driver=webdriver.Chrome(options=options)
            caso = getattr(row,col)
            if exacta:
                url = f'https://www.google.com/search?q="{caso}"'
            else:
                url = f'https://www.google.com/search?q={caso}'
            url = url.strip().replace(" ","+")
            time.sleep(0.4) # Quitar para aumentar la velocidad
            driver.get(url)
            headings = driver.find_elements(By.XPATH,'//div[@class = "g"]')
            for heading in headings:
                title = heading.find_elements(By.TAG_NAME,'h3')
                links = heading.find_element(By.CSS_SELECTOR,'.yuRUbf>a').get_attribute("href")
                liks.append(links)
                for i in range(len(title)):
                    title[i] = title[i].text
                    titles.append(title[i])
            dic = dict(zip(titles,liks))
            driver.close()
            if len(headings)>0:
                df.loc[getattr(row,"Index"),f"Resultados_de_{col}"] = str(dic)