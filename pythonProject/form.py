from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

# Paso 1: Realiza la solicitud HTTP y analiza el contenido con BeautifulSoup
content = requests.get(url="https://appbrewery.github.io/Zillow-Clone/").text
soup = BeautifulSoup(content, "html.parser")

# Encuentra todas las tarjetas de propiedades
listings = soup.find_all("div", class_="StyledPropertyCardDataWrapper")
links = []
addresses = []
prices = []

for listing in listings:
    # Extrae el enlace
    a_tag = listing.find("a")
    if a_tag and "href" in a_tag.attrs:
        links.append(a_tag["href"])

    # Extrae y limpia la dirección
    address_tag = listing.find("address")
    if address_tag:
        address = address_tag.string.strip()
        address = address.replace('|', '')
        addresses.append(address)

    # Extrae y limpia el precio
    span_tag = listing.find("span")
    if span_tag:
        price = span_tag.string
        if "+" in price:
            price = price.split('+')[0]
        else:
            price = price.split('/')[0]
        prices.append(price)

# Imprime los datos obtenidos para verificar
print("Links:", links)
print("Addresses:", addresses)
print("Prices:", prices)

# Paso 2: Inicializa el navegador
driver = webdriver.Chrome()

try:
    # Navegar a la URL del formulario
    driver.get("https://forms.gle/uAfmMWenijWf3DqE8")

    # Esperar a que la página cargue completamente
    time.sleep(2)  # Ajusta el tiempo según sea necesario

    index = 0
    while index < len(links):
        # Esperar a que los campos estén disponibles
        time.sleep(2)  # Ajusta el tiempo según sea necesario

        # Encontrar los campos de entrada para la primera pregunta (links)
        link_inputs = driver.find_elements(By.XPATH,
                                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        if index < len(links) and link_inputs:
            link_inputs[0].send_keys(links[index])

        # Encontrar los campos de entrada para la segunda pregunta (addresses)
        address_inputs = driver.find_elements(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        if index < len(addresses) and address_inputs:
            address_inputs[0].send_keys(addresses[index])

        # Encontrar los campos de entrada para la tercera pregunta (prices)
        price_inputs = driver.find_elements(By.XPATH,
                                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        if index < len(prices) and price_inputs:
            price_inputs[0].send_keys(str(prices[index]))

        # Opcional: esperar un poco antes de enviar
        time.sleep(2)  # Ajusta el tiempo según sea necesario

        # Encontrar y hacer clic en el botón de envío
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Enviar")]')
        submit_button.click()

        # Esperar a que la página cargue después del envío
        time.sleep(2)  # Ajusta el tiempo según sea necesario

        # Encontrar y hacer clic en el botón "Enviar otra respuesta" si hay más datos que enviar
        if index + 1 < len(links):
            try:
                resend_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                resend_button.click()
                # Esperar a que la página de nuevo formulario cargue
                time.sleep(2)  # Ajusta el tiempo según sea necesario
            except Exception as e:
                print("No se encontró el botón 'Enviar otra respuesta'.")
                break
        else:
            break

        index += 1

except Exception as e:
    # Imprime un mensaje de error si algo sale mal
    print(f"Error: {e}")
    print("El proceso no se llevó a cabo completamente porque el navegador se cerró inesperadamente.")

finally:
    # Cierra el navegador después de completar el proceso
    time.sleep(3)  # Opcional: Esperar para ver el resultado antes de cerrar
    driver.quit()
