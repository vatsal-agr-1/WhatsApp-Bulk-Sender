from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from urllib import quote      #Uncomment line below to use python 2
#from urllib.parse import quote  #Uncomment line below to use python 3 




from time import sleep
# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()




#Enter the CSS Selector of the type feild from whatsapp web.

css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"


# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''

'''     


driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
#with open ('nuumbers.txt') as numbers_file:                    #uncomment these three three lines to read input from numbers.txt file
 #   for line in numbers_file:
  #  	line=line.strip()
    	if len (line)==10:								   		#skip numbers of length not equal to 10
    		phone.append(str(line))
# phone.extend(str(raw_input("Enter the comma separated list of numbers (Press enter to skip)\n")).split(','))

msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
driver.get("https://web.whatsapp.com")  # first call without delay in order to scan qr code
sleep(2)
for number in phone:
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    sleep(0)  # any delay is okay, even 0, but 3-5 seems appropriate
    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
    print ('Last Number '+ str(number))
print ("Done")
# driver.quit()                                                 #Close window using this.
