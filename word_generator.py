from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
d=webdriver.Chrome(options=options)
d.get("https://www.wordsdetail.com/6-letter-words/")
words=d.find_elements(By.CSS_SELECTOR, "ul li")
with open("words.csv","w") as file:
    file.write("")
with open("words.csv", "a") as file:
    for word in words:
        try:
            if len(word.text)==6:
                file.write(f"{word.text.lower()}\n")
        except:
            pass
    file.write("wordle")
d.quit()
