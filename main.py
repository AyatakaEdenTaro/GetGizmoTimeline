from selenium import webdriver
import time

#ドライバーの指定
driver = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')

# ページにアクセス
driver.get("https://www.gizmodo.jp/")
time.sleep(1)
get_timelines = driver.find_element_by_id("cxTimeline").find_elements_by_class_name("p-timeline-cardTitle")
for timeline in get_timelines:
    timeline_link = timeline.find_element_by_tag_name("a").get_attribute("href")
    print(timeline_link)

driver.close()
driver.quit()


