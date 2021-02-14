from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dateutil.relativedelta import relativedelta
import datetime
import math

def get_checkinout_left_pane_values():
#   wait.until(
#   EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._1lds9wb:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')))
    left_month_year = driver.find_element_by_css_selector("div._754zdu7 > div:nth-child(2) ._umpo2eg")
    return left_month_year.text.split(' ')

def get_checkinout_right_pane_values():
#    wait.until(
#    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div._1lds9wb:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'))
#     )    
    right_month_year = driver.find_element_by_css_selector("div._754zdu7 > div:nth-child(3) ._umpo2eg")
    return right_month_year.text.split(' ')
    
def click_next_month():
    next_month_button = driver.find_element_by_css_selector("._13tn83am").click()
    
def click_previous_month():
    previous_month_button = driver.find_element_by_css_selector("._nztsc8l").click()

def update_guests_list(glist):
    #updating adults
    glist[0] = int(driver.find_element_by_css_selector("div._3hmsj> div> div:nth-child(1) ._5afswi").text[:-15])
    #updating children
    glist[1] = int(driver.find_element_by_css_selector("div._3hmsj> div> div:nth-child(2) ._5afswi").text[:-17])
    #updating infants
    glist[2] = int(driver.find_element_by_css_selector("div._3hmsj> div> div:nth-child(3) ._5afswi").text[:-16])

months_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
full_months_names = ['January','February','March','April','May','June','July','August','September','October','November','December']

driver = Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.airbnb.com/")
wait = WebDriverWait(driver, 10)

#location elements
location_value = 'Rome, Italy'
location_xpath = '//*[@id="bigsearch-query-detached-query"]'

#check-in/check-out elements
check_in_field = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[1]/div/div/div[2]')
check_out_field = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[1]/div/header/div/div[2]/div[2]/div/div/div/form/div/div/div[3]/div[3]/div/div/div[2]')

#guests elements
guests_field = driver.find_element_by_class_name("_1yulsurh")
guests_field.click()
my_adults = 2
my_children = 1
my_infants = 0

#setting guests_list element 0 is adults, element 1 is children, element 2 is infants
guests_list=[0,0,0]

#setting dates
check_in_date = datetime.datetime.now()+ relativedelta(weeks=1)
check_out_date = datetime.datetime.now()+ relativedelta(weeks=2)

check_in_year = check_in_date.year
check_in_month = check_in_date.month
check_in_day = check_in_date.day

check_out_year = check_out_date.year
check_out_month = check_out_date.month
check_out_day = check_out_date.day

#setting location
WebDriverWait(driver, 10)
driver.find_element_by_css_selector("span._jo65ru:nth-child(3)").click()
WebDriverWait(driver,10)
inputLocation = driver.find_element_by_xpath(location_xpath)
inputLocation.clear()
inputLocation.send_keys(location_value)
WebDriverWait(driver,10)
driver.find_element_by_css_selector("span._jo65ru:nth-child(3)").click()
WebDriverWait(driver,10)
check_in_field.click()
WebDriverWait(driver,10)

#setting check in date
driver.find_element_by_css_selector("span._jo65ru:nth-child(3)").click()
WebDriverWait(driver, 10)
check_in_field.click()
wait = WebDriverWait(driver,10)
year_on_left = int(get_checkinout_left_pane_values()[1])
while check_in_year != year_on_left:
    if check_in_year > year_on_left:
        click_next_month()
    else :
        click_previous_month()
    print(get_checkinout_left_pane_values())
    year_on_left = int(get_checkinout_left_pane_values()[1])
    
    
month_on_left = full_months_names.index(str(get_checkinout_left_pane_values()[0]))
while (check_in_month-1) != month_on_left:
    if (check_in_month-1) > month_on_left:
        click_next_month()
    else :
        click_previous_month()
    month_on_left = full_months_names.index(get_checkinout_left_pane_values()[0])
    
days_of_month = driver.find_elements_by_css_selector("div._754zdu7 > div:nth-child(2) ._1eu9zfzy")
 
for i in range(0, len(days_of_month)):
    my_element = days_of_month[i]
    if int(my_element.text.strip()) == check_in_day:
        my_element.click()
        
#setting check out date
driver.find_element_by_css_selector("span._jo65ru:nth-child(3)").click()
check_out_field.click()
wait = WebDriverWait(driver, 10)
year_on_left = int(get_checkinout_left_pane_values()[1])
while check_out_year != year_on_left:
    if check_out_year > year_on_left:
        click_next_month()
    else :
        click_previous_month()
    year_on_left = int(get_checkinout_left_pane_values()[1])
    
    
month_on_left = full_months_names.index(str(get_checkinout_left_pane_values()[0]))
while (check_out_month-1) != month_on_left:
    if (check_out_month-1) > month_on_left:
        click_next_month()
    else :
        click_previous_month()
    month_on_left = full_months_names.index(get_checkinout_left_pane_values()[0])
    
days_of_month = driver.find_elements_by_css_selector("div._754zdu7 > div:nth-child(2) ._1eu9zfzy")
for i in range(0, len(days_of_month)):
    my_element = days_of_month[i]
    if int(my_element.text.strip()) == check_out_day:
        my_element.click()
        
#setting guests
driver.find_element_by_css_selector("span._jo65ru:nth-child(3)").click()
guests_field.click()
wait = WebDriverWait(driver, 10)
adults_minus = driver.find_elements_by_css_selector("#stepper-adults > button:nth-child(1)")[0]
adults_plus = driver.find_elements_by_css_selector("#stepper-adults > button:nth-child(3)")[0]
children_minus = driver.find_elements_by_css_selector("#stepper-children > button:nth-child(1)")[0]
children_plus = driver.find_elements_by_css_selector("#stepper-children > button:nth-child(3)")[0]
infants_minus = driver.find_elements_by_css_selector("#stepper-infants > button:nth-child(1)")[0]
infants_plus = driver.find_elements_by_css_selector("#stepper-infants > button:nth-child(3)")[0]
update_guests_list(guests_list)
while my_adults != guests_list[0] and -1 < my_adults < 17 :
    if my_adults > guests_list[0]:
        adults_plus.click()
    elif my_adults < guests_list[0]:
        adults_minus.click()
    update_guests_list(guests_list)
while my_children != guests_list[1] and -1 < my_children < 6 :
    if my_children > guests_list[1]:
        children_plus.click()
    elif my_children < guests_list[1]:
        children_minus.click()
    update_guests_list(guests_list)
while my_infants != guests_list[2] and -1 < my_infants < 6 :
    if my_infants > guests_list[2]:
        infants_plus.click()
    elif my_infants < guests_list[2]:
        infants_minus.click()
    update_guests_list(guests_list)
    
driver.find_element_by_css_selector("._1mzhry13").click()
wait = WebDriverWait(driver,10)
#********************************************
#********************************************

action = ActionChains(driver);
#first_result = driver.find_elements_by_xpath("//div[(@class='_e296pg')]")[1]
first_result = driver.find_elements_by_xpath("//div[(@itemprop='itemListElement')]")[0]
action.move_to_element(first_result).perform()
wait = WebDriverWait(driver,5)

map_highlight = driver.find_elements_by_xpath("//*[contains(@style, 'background-color: rgb(34, 34, 34);')]")

if len(map_highlight) == 1:
    print("Property highlighted on map succesfully.")
    
highlight_parent = map_highlight[0].find_element_by_xpath('..')
highlight_parent_parent = highlight_parent.find_element_by_xpath('..')

map_frame = driver.find_element_by_css_selector(".gm-style > iframe:nth-child(2)")
driver.switch_to.frame(highlight_parent_parent)

map_highlight[0].click()

driver.switch_to.default_content()