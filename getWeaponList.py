import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

if __name__ == "__main__":
    # Change this if needed
    wanted = ["Unlock","Craft"]
    
    options = Options()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)
    driver.get("https://wiki.teamfortress.com/wiki/Weapons")

    content = driver.find_element(By.CLASS_NAME,"mw-parser-output")
    tables = content.find_elements(By.CLASS_NAME,"grid")

    for table in tables:
        rows = table.find_elements(By.TAG_NAME,"tr")
        
        for row in rows:
            try:
                origin = row.find_element(By.TAG_NAME,"small").text
                itemHashName = row.find_element(By.TAG_NAME,"b").text
                if origin in wanted:
                    print(f"{itemHashName}")
                    with open("output.txt","a+") as f:
                        f.write('"'+itemHashName+'",')
            except:
                continue
