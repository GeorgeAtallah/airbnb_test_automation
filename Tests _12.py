from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

#********************************************
#********************************************

#Test 2

#verify search criteria
search_criteria = driver.find_element_by_css_selector("button._b2fxuo:nth-child(2) > div:nth-child(2)")
search_criteria.click()

location_search_criteria = driver.find_element_by_css_selector("#bigsearch-query-detached-query")
print("Location correct? {}".format(location_search_criteria.get_attribute('value')==location_value))

check_in_search_criteria = driver.find_element_by_css_selector("div._j8gg2a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
print("Check in date correct? {}".format(check_in_search_criteria.text == (months_names[check_in_month-1]+" "+str(check_in_day))))

check_out_search_criteria = driver.find_element_by_css_selector("div._j8gg2a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
print("Check out date correct? {}".format(check_out_search_criteria.text == (months_names[check_out_month-1]+" "+str(check_out_day))))

guests_search_criteria = driver.find_element_by_css_selector("._37ivfdq")
guests_search_criteria.click()
print("No of searched adults correct? {}".format((my_adults==int(driver.find_element_by_css_selector("#stepper-adults > div:nth-child(2) > span:nth-child(2)").text[:-15]))))
print("No of searched children correct? {}".format((my_children==int(driver.find_element_by_css_selector("#stepper-children > div:nth-child(2) > span:nth-child(2)").text[:-17]))))
print("No of searched infants correct? {}".format((my_infants==int(driver.find_element_by_css_selector("#stepper-infants > div:nth-child(2) > span:nth-child(2)").text[:-16]))))

#checking if property can accomodate (can use 1 bed for 2 adults sometimes in case of spouses)
list_of_searched_properties = driver.find_elements_by_xpath("//div[@class='_kqh46o']")
props_with_less_beds=[]
props_with_enough_beds=[]
for i in range(0,len(list_of_searched_properties),2):
    num_of_beds = int(list_of_searched_properties[i].text.split('·')[2][:-5])
    if(int(math.ceil(0.5*my_adults))+my_children+my_infants) > num_of_beds:
        props_with_less_beds.append(list_of_searched_properties[i])
    else:
        props_with_enough_beds.append(list_of_searched_properties[i])
if len(props_with_less_beds) > 0:
    print("Not all properties can accomodate all guests")
else:
    print("All properties can accomodate all guests")

#updating number of bedrooms
#driver.find_element_by_css_selector("._10v3f8y9").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
WebDriverWait(driver, 10)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
WebDriverWait(driver, 10)
try:
    rooms_beds_button = driver.find_element_by_css_selector("#menuItemButton-rooms_and_beds > button:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
    rooms_beds_button.click()
except:
    more_filter_button = driver.find_element_by_css_selector("#menuItemButton-dynamicMoreFilters")
    more_filter_button.click()
    
more_bedrooms = driver.find_element_by_css_selector("#filterItem-rooms_and_beds-stepper-min_bedrooms-0 > button:nth-child(3)")
less_bedrooms = driver.find_element_by_css_selector("#filterItem-rooms_and_beds-stepper-min_bedrooms-0 > button:nth-child(1)")
my_bedrooms = 5

selected_bedrooms = int(driver.find_element_by_css_selector("#filterItem-rooms_and_beds-stepper-min_bedrooms-0 > div:nth-child(2) > span:nth-child(2)").text[:-17])
while my_bedrooms != selected_bedrooms and -1 < my_bedrooms < 17 :
    if my_bedrooms > selected_bedrooms:
        more_bedrooms.click()
    elif my_bedrooms < selected_bedrooms:
        less_bedrooms.click()
    selected_bedrooms = int(driver.find_element_by_css_selector("#filterItem-rooms_and_beds-stepper-min_bedrooms-0 > div:nth-child(2) > span:nth-child(2)").text[:-17])

WebDriverWait(driver, 20)

#Adding Pool to amenities
try:
    pool_check_box = driver.find_element_by_css_selector("#filterItem-facilities-checkbox-amenities-7")
except:
    more_filter_button = driver.find_element_by_css_selector("#menuItemButton-dynamicMoreFilters")
    more_filter_button.click()
    pool_check_box = driver.find_element_by_css_selector("#filterItem-facilities-checkbox-amenities-7") 

if pool_check_box.is_selected() is False:
    pool_check_box.click()
WebDriverWait(driver, 20)
if pool_check_box.is_selected():
    pass
else:
    pool_check_box.click()

WebDriverWait(driver, 20)  
driver.find_element_by_css_selector("._m095vcq").click()
WebDriverWait(driver, 20)

#driver.switch_to.window(driver.window_handles[0])
#Verifying number of bedrooms is reflected in search
props_with_less_bedrooms=[]
props_with_enough_bedrooms=[]

try:
    #list_of_searched_properties = driver.find_elements_by_class_name("_kqh46o")
    list_of_searched_properties = wait.until(EC.visibility_of_elements_located((By.CLASS_NAME, "_kqh46o")))
except:
    driver.refresh()
    WebDriverWait(driver, 50)
    list_of_searched_properties = driver.find_elements_by_css_selector("div._8s3ctt:nth-child(2) > div:nth-child(3) > div:nth-child(3)")


for i in range(0,len(list_of_searched_properties),2):
    num_of_bedrooms = int(list_of_searched_properties[i].text.split('·')[1][:-9])
    if my_bedrooms > num_of_beds:
        props_with_less_bedrooms.append(list_of_searched_properties[i])
    else:
        props_with_enough_bedrooms.append(list_of_searched_properties[i])
if len(props_with_less_beds) > 0:
    print("Not all properties have at least the number of selected bedrooms")
else:
    print("All properties have at least the number of selected bedrooms")
    
#Verifying first result has pool
driver.find_element_by_css_selector("div._8s3ctt:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
WebDriverWait(driver, 20)
driver.switch_to.window(driver.window_handles[1])
property_amenities = driver.find_elements_by_xpath("//div[@class='_1nlbjeu']")
has_pool = False
for i in range(0,len(property_amenities)):
    if "Pool" in property_amenities[i].text:
        has_pool = True
print("Property has pool? {}".format(has_pool))