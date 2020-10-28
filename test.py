# 作者    lishaoteng
# 时间    2020-10-28 15:13
# IDE   PyCharm
from selenium import webdriver
import time
# 指定驱动路径
driver = webdriver.Chrome("D:\python\chromedriver.exe")
# 需要打开的URL地址
url = "http://app.bjtitle.com/rui/bj-band.php?u=610819&t=3"
driver.get(url)
driver.find_element_by_id("team").click()
driver.switch_to.frame("layui-layer-iframe1")
driver.find_element_by_id("word").click()
word = driver.find_element_by_id("word")
word.send_keys("北京汽车集团有限公司团委")
time.sleep(1)
driver.find_element_by_id("btn-search").click()
time.sleep(1)
driver.find_element_by_class_name("team").click()
time.sleep(1)
driver.switch_to.defaultContent()
driver.find_element_by_class_name("btn").click()
time.sleep(1)
driver.quit()
# http: // app.bjtitle.com / rui / bj - band.php?u = 610819 & t = 3
# // *[ @ id = "word"]
# # word
# import org.openqa.selenium.By;
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.firefox.FirefoxDriver;
#
# public
#
#
# class FameStudy {
#
# public static void main(String[] args) {
# WebDriver dr = new FirefoxDriver();
# String url = "\\Your\\Path\\to\\main.html";
# dr.get(url);
#
# // 在default content定位id="id1"的div
# dr.findElement(By.id("id1"));
#
# // 此时，没有进入到id="frame"的frame中时，以下两句会报错
# dr.findElement(By.id("div1")); // 报错
# dr.findElement(By.id("input1")); // 报错
#
# // 进入id="frame"的frame中，定位id="div1"的div和id="input1"的输入框。
# dr.switchTo().frame("frame");
# dr.findElement(By.id("div1"));
# dr.findElement(By.id("input1"));
#
# // 此时，没有跳出frame，如果定位default content中的元素也会报错。
# dr.findElement(By.id("id1")); // 报错
#
# // 跳出frame, 进入default content;重新定位id="id1"的div
# dr.switchTo().defaultContent();
# dr.findElement(By.id("id1"));
# }
#
# }