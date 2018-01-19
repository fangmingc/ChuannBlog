## selenium
- 测试工具，模拟浏览器的正常访问。
	- 人工测试过于浪费人力和时间
	- 爬虫中使用它主要是为了解决requests无法直接执行JavaScript代码的问题
- selenium本质是通过驱动浏览器，完全模拟浏览器的操作，比如跳转、输入、点击、下拉等，来拿到网页渲染之后的结果，可支持多种浏览器

	```python
	from selenium import webdriver
	browser=webdriver.Chrome()
	browser=webdriver.Firefox()
	browser=webdriver.PhantomJS()
	browser=webdriver.Safari()
	browser=webdriver.Edge() 
	```
### 安装	
- `pip3 install selenium`
- selenium驱动浏览器需要特殊的组件，这里以chrome为例，需要下载chromedriver
	- 注意：版本需要和已安装的chrome版本相匹配，否则易出错
	- 下载chromdriver.exe放到python安装路径的scripts目录中
	- 国内镜像网站地址：http://npm.taobao.org/mirrors/chromedriver/
	- 最新的版本去官网找:https://sites.google.com/a/chromium.org/chromedriver/downloads
- 验证安装

	```python
	C:\Users\Administrator>python3
	Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from selenium import webdriver
	>>> driver=webdriver.Chrome() #弹出浏览器
	>>> driver.get('https://www.baidu.com')
	>>> driver.page_source
	```
- 注意：
	- selenium3默认支持的webdriver是Firfox，而Firefox需要安装geckodriver
	- 下载链接：https://github.com/mozilla/geckodriver/releases

#### 无界面浏览器
- 下载phantomjs，解压后把phantomjs.exe所在的bin目录放到环境变量
- 下载链接：http://phantomjs.org/download.html
- 验证安装
	
	```python
	C:\Users\Administrator>phantomjs
	phantomjs> console.log('egon gaga')
	egon gaga
	undefined
	phantomjs> ^C
	C:\Users\Administrator>python3
	Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from selenium import webdriver
	>>> driver=webdriver.PhantomJS() #无界面浏览器
	>>> driver.get('https://www.baidu.com')
	>>> driver.page_source
	```

### 基本使用
```python
from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time

browser = webdriver.Chrome()

try:
    """显式等待"""
    # browser.get('https://www.baidu.com')
    #
    # input_tag = browser.find_element_by_id('kw')
    # input_tag.send_keys('美女')  # python2中输入中文错误，字符串前加个u
    # input_tag.send_keys(Keys.ENTER)  # 输入回车
    #
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))  # 等到id为content_left的元素加载完毕,最多等10秒
    #
    # # print(browser.page_source)
    # print(browser.current_url)
    # print(browser.get_cookies())

    """隐式等待"""
    # browser.get("https://www.taobao.com/")
    # browser.implicitly_wait(3)
    #
    # input_tag = browser.find_element_by_id("q")
    # input_tag.send_keys("三体")
    # input_tag.send_keys(Keys.ENTER)
    #
    # time.sleep(3)

    """普通选择器"""
    # browser.get("https://www.baidu.com")

    # 取单个标签
    # tag = browser.find_element(By.CLASS_NAME, "s_ipt")
    # tag = browser.find_element_by_class_name("s_ipt")
    # tag = browser.find_element_by_id("kw")
    # tag = browser.find_element_by_name("wd")
    # tag = browser.find_element_by_css_selector(".quickdelete-wrap input")
    # tag.send_keys("三体")

    # tag = browser.find_element_by_link_text("贴吧")
    # tag = browser.find_element_by_partial_link_text("贴")
    # tag.click()

    # tag = browser.find_element_by_tag_name("body")
    # print(tag.tag_name)
    # 以上选择器使用find_elements_by_xxx表示获取所有符合的标签，返回列表

    """xpath选择器"""
    # browser.get("https://doc.scrapy.org/en/latest/_static/selectors-sample1.html")

    # tags = browser.find_elements_by_xpath('//a')
    # for tag in tags:
    #     print(tag.tag_name, tag.text, tag.get_attribute("href"))

    # tags = browser.find_elements_by_xpath("//a[3]/img")
    # for tag in tags:
    #     print(tag.tag_name, tag.text, tag.get_attribute("src"))

    browser.get("https://www.baidu.com")
    div_tag = browser.find_element_by_name("tj_briicon")
    q = div_tag.get_attribute("style")
    print(q, type(q))

    time.sleep(2)

finally:
    browser.quit()
```

#### 等待元素加载
- selenium只是模拟浏览器的行为，而浏览器解析页面是需要时间的（执行css，js），一些元素可能需要过一段时间才能加载出来，为了保证能查找到元素，必须等待
- 显式等待
	- 必须指定等待的标签
	- wait = WebDriverwait(driver, 10)
- 隐式等待
	- 等待所有元素被加载完毕
	- driver.implicitly_wait(3)

#### 选择器
- 普通选择器
	- 见代码
- xpath，按照文档树结构查找，chrome检查元素在elements界面右键某元素可以copy出该元素的xpath路径
	- /单斜杠表示绝对路径寻找，只寻找一层
		- /表示从文档树顶级开始，该级下只有html标签
		- /html，表示html标签，该级下有head和body两个标签
	- //，双斜杠表示从下属层级寻找，找到为止，不限层级
	- 其余见代码


### 自动登陆博客园-破解极验滑动验证码
```python
import time
import random

from PIL import Image

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # 键盘按键操作

browser = webdriver.Chrome()
browser.implicitly_wait(5)


class SVCR:
    """
    识别滑动验证码   极验验证

    obj = SVCR(driver)
    obj.run()
    """

    def __init__(self, driver):
        self.driver = driver

        self.tracks = None
        self.start_x = 57

        self._get_full_img = True
        self._img_before = None
        self._img_after = None

    def run(self):
        """执行识别流程"""
        # 1. 点击按钮开始验证
        self.click_start_btn()

        # 2. 判断验证类型并执行相应的验证方法
        if True:
            return self.auth_slide()
        else:
            pass

    def auth_slide(self):
        """滑动验证"""
        # 1. 获取验证图片
        self.get_images()
        # 2. 根据验证图片生成移动轨迹
        self.generate_tracks()
        # 3. 根据轨迹进行滑动验证
        self.do_slide_auth()

        # 4. 循环验证直到成功或超时失败
        return self.check_slide_auth()

    def click_start_btn(self, search_style="CLASS_NAME", search_content="geetest_radar_tip"):
        """找到开始按钮并点击"""
        btn = self.driver.find_element(getattr(By, search_style), search_content)
        btn.click()

    def generate_tracks(self):
        """
        根据验证图片生成移动轨迹

        策略：匀加速再匀减速，超过一些，再回调，左右小幅度震荡
        """
        distance = self.generate_distance()

        v = 0
        current = 0
        t = 0.2
        tracks = []

        # 正向滑动
        while current < distance + 10:
            if current < distance * 2 / 3:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            current += s
            tracks.append(round(s))
            v = v + a * t

        # 往回滑动
        current = 0
        while current < 13:
            if current < distance * 2 / 3:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            current += s
            tracks.append(-round(s))
            v = v + a * t

        # 最后修正
        tracks.extend([2, 2, -3, 2])

        self.tracks = tracks

    def generate_distance(self):
        """计算滑动距离"""
        threshold = 60

        for i in range(self.start_x, self._img_before.size[0]):
            for j in range(self._img_before.size[1]):
                rgb1 = self._img_before.load()[i, j]
                rgb2 = self._img_after.load()[i, j]
                res1 = abs(rgb1[0] - rgb2[0])
                res2 = abs(rgb1[1] - rgb2[1])
                res3 = abs(rgb1[2] - rgb2[2])
                if not (res1 < threshold and res2 < threshold and res3 < threshold):
                    return i - 7  # 经过测试，误差为大概为7

    def get_images(self):
        """获取验证图片"""
        # 1. 截取完整图片
        if self._get_full_img:
            time.sleep(2)       # 等待图片加载完毕
            self._img_before = self._get_img()

        # 2. 点击出现缺口图片
        slider_btn = self.driver.find_element_by_class_name("geetest_slider_button")
        slider_btn.click()

        # 3. 截取缺口图片
        time.sleep(2)           # 等待图片加载完毕
        self._img_after = self._get_img()

    def _get_img(self):
        """截取图片"""
        div_tag = self.driver.find_element_by_class_name("geetest_slicebg")

        # 计算截取图片大小
        img_pt = div_tag.location       # {'x': 296, 'y': 15}
        img_size = div_tag.size         # {'height': 159, 'width': 258}
        img_box = (img_pt["x"], img_pt["y"], img_pt["x"] + img_size["width"], img_pt["y"] + img_size["height"])

        # 保存当前浏览页面
        self.driver.save_screenshot("snap.png")

        # 截取目标图片
        img = Image.open("snap.png")
        obj = img.crop(img_box)
        obj.show()
        print(img_box)
        return obj

    def do_slide_auth(self):
        """根据轨迹进行滑动验证"""
        # 模拟人的滑动
        slider_btn = self.driver.find_element_by_class_name("geetest_slider_button")
        ActionChains(self.driver).click_and_hold(slider_btn).perform()
        for track in self.tracks:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        # 释放鼠标
        time.sleep(0.5)  # 0.5秒后释放鼠标
        ActionChains(self.driver).release().perform()

    def check_slide_auth(self):
        """循环验证直到成功或超时失败"""
        time.sleep(2)
        div_tag = self.driver.find_element_by_class_name("geetest_fullpage_click")
        if div_tag and "display: block" in div_tag.get_attribute("style"):
            self._get_full_img = False
            self.start_x = random.randint(57, 63)
            return self.auth_slide()
        else:
            return True

try:
    # 1. 打开登录页面
    browser.get("https://passport.cnblogs.com/user/signin")
    browser.set_window_size(1366, 768)  # 分辨率 1920*1080

    # 2. 填写用户名和密码
    time.sleep(random.uniform(0.2, 1))     # 模拟人反应时间
    uname_input = browser.find_element_by_id("input1")
    pwd_input = browser.find_element_by_id("input2")
    uname_input.send_keys("qqqqqqqq")
    pwd_input.send_keys("qqqqqqqqq")

    # 3. 点击登录
    time.sleep(random.uniform(0.5, 1))     # 模拟人反应时间
    submit_input = browser.find_element_by_id("signin")
    submit_input.click()

    # 4. 开始认证
    auth = SVCR(browser)
    time.sleep(2)
    if auth.run():
        print(111111)
    time.sleep(10)

finally:
    browser.quit()
```






