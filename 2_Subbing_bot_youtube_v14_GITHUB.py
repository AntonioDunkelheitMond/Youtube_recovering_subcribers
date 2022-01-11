#CREADO POR ANTONIO JUSTO
import pathlib
import time
from pathlib import Path
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc
import os
#CREADO POR ANTONIO JUSTO
def login_you(mail, password):
    URL = "https://youtube.com"
    driver.get(URL)
    time.sleep(1)
    log_in = driver.find_element_by_css_selector(".signin #button")
    log_in.click()
    input_gmail = driver.find_element_by_id("identifierId")
    time.sleep(1)
    input_gmail.send_keys(mail)
    weiter_button = driver.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d")
    time.sleep(1)
    weiter_button.click()
    time.sleep(1)
    input_pass = driver.find_element_by_css_selector("#password .whsOnd")
    time.sleep(1)
    input_pass.send_keys(password)
    weiter_button = driver.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d")
    time.sleep(1)
    weiter_button.click()
    time.sleep(3)

if __name__ == "__main__":

    print(f"Please provide your email and passowrd in order to log in your gmail account")
    email = input("Escribe tu gmail: / Type your email: (Ex: example@gmail.com)")
    contrase = input("Escribe tu contraseña: / Type your password:  ")
    driver = uc.Chrome()
    login_you(email, contrase)

path_file_subs = Path.cwd() / "Kanalliste_nuevo.txt"
# print(path_file_subs.exists())
Max_daily_subs = 75 # Maximum number of daily subbed channels
i = 0 # variable to keep track o
with path_file_subs.open(mode="r", encoding="UTF-8") as file_subs_og:
    content = file_subs_og.read()
    content_og = content.splitlines()
    content = content.splitlines()
    print(content)

    with open("Kanalliste_nuevo_remaining.txt", "w", encoding="UTF-8") as file_subs_remaining:

        for user in content_og:
            if i >= Max_daily_subs:
                break

            time.sleep(1)
            print(f"{user} \n", end="")
            user = user.replace(" ", "+")
            URL = f"https://www.youtube.com/results?search_query={user}" #&sp=EgIQAg%253D%253D
            driver.get(URL)
            time.sleep(1)

            user = user.replace("+", " ")

            search_name_sub_de = f"Abo für {user} beenden."
            search_name_sub_en = f"Unsubscribe from {user}"
            # En español se tiene el problema de que en el código existe un NBSP  o  space character that prevents
            # an automatic line break at its position,
            # cosa que no ocurre con los otros dos idiomas que he añadido, por lo que tras trastear
            # las diferencias en el código en español permiten hacer funcionar tambien en Español
            search_name_sub_es = f"Anular suscripción a&nbsp;{user}"
            page = driver.page_source

            #Contamos el numero de ocurrencias, que determinan si estamos o ya suscritos
            if (page.count(search_name_sub_de) >= 2) or (page.count(search_name_sub_en) >= 2) \
                    or (page.count(search_name_sub_es) + page.count(f"Anular suscripción a {user}.") >= 2):

                content.pop(0)
                print(f"++++++++++++++++++++++++++++++ALREADY SUBBED TO: {user}")
                continue
            else:
                try:
                    sub_button = driver.find_element_by_css_selector(
                        ".ytd-channel-renderer > .ytd-subscribe-button-renderer:nth-child(1)").click()
                    time.sleep(2)
                    driver.get(URL)
                    print(i)
                    i += 1
                    content.pop(0)
                    with open("file_subs_remaining_temp.txt", "w", encoding="UTF-8") as file_subs_remaining_temp:
                        file_subs_remaining_temp.write("\n".join(content))
                    continue
                except Exception:

                    print(f"IT WAS NOT POSSIBLE TO SUB TO:: {user}")

                    content.pop(0)
                    with open("Sub_failures.txt", "a", encoding="UTF-8") as fa:
                        fa.write(f"{user} \n")

                    with open("file_subs_remaining_temp.txt", "w", encoding="UTF-8") as file_subs_remaining_temp:
                        file_subs_remaining_temp.write("\n".join(content))
                    continue
        print(content)
        print(len(content))
        file_subs_remaining.write("\n".join(content))

file1 = Path.cwd() / "Kanalliste_nuevo_old.txt"
os.chdir(Path.cwd())
if file1.exists():
    os.remove(file1)
os.rename("Kanalliste_nuevo.txt", "Kanalliste_nuevo_old.txt")
os.rename("Kanalliste_nuevo_remaining.txt", "Kanalliste_nuevo.txt")


