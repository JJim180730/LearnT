
import time
from splinter.browser import Browser
from time import sleep
import traceback
from selenium.webdriver.chrome.service import Service
 
 
class Buy_Tickets(object):
    # 初始化
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.driver_name = 'chrome'   #'chrome'
        self.executable_path = 'C:\\Users\\larry\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\chromedriver.exe'
    # 登录
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('loginUserDTO.user_name', self.username)
        # sleep(1)
        self.driver.fill('userDTO.password', self.passwd)
        # sleep(1)
        
        #点击登录
        # self.driver.find_element_by_id('loginBtn').click()
        self.driver.find_by_id('loginSub').click()
        
       
        # 等待进入短信验证页面
        while True:
            # 判断是否需要进入短信验证页面
            if self.driver.is_text_present('短信验证登录'):
                # 输入手机号

                phone_number = input("请输入手机号码：")
                self.driver.fill('mobileNo', phone_number)

                # 点击获取验证码
                get_code_button = self.driver.find_by_id('getdynamicpassword')
                get_code_button.click()

                # 等待获取验证码
                time.sleep(5)  # 这里等待5秒，可根据实际情况调整等待时间

                # 获取手机验证码
                # 这里可以使用短信接口、邮件接口等方式获取验证码
                code = input('请输入手机验证码：')

                # 录入手机验证码
                self.driver.fill('dynamicpassword', code)

                # 确认验证
                confirm_button = self.driver.find_by_id('submitBtn')
                confirm_button.click()
                break

            time.sleep(1)

        # 登录成功后，可以进行后续操作，例如查询车票等
    # 买票
    def start_buy(self):
        my_service = Service()
        # browser = Browser('chrome',)
        self.driver = Browser(driver_name=self.driver_name,service = my_service)
        # self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(700, 500)
        self.login()
        self.driver.visit(self.ticket_url)
        try:
            print('开始购票...')
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        self.driver.find_by_text('预订')[self.order-1].click()
                        sleep(1.5)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        for i in self.driver.find_by_text('预订'):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            print('开始预订...')
            sleep(1)
            print('开始选择用户...')
            for p in self.passengers:
                self.driver.find_by_text(p).last.click()
                sleep(0.5)
                if p[-1] == ')':
                    self.driver.find_by_id('dialog_xsertcj_ok').click()
            print('提交订单...')
            sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            sleep(2)
            print('确认选座...')
            self.driver.find_by_id('qr_submit_id').click()
            print('预订成功...')
        except Exception as e:
            print(e)
 
 
 
 
if __name__ == '__main__':

    # 用户名
    username = input("请输入12306登录用户名：") #'larry_liang@outlook.com'
    # 密码
    password = input("请输入账号密码：") #'wangjing001'
    # 车次选择，0代表所有车次
    order = 0
    # 乘客名，比如passengers = ['王二狗', '王三狗']
    # 学生票需注明，注明方式为：passengers = ['王二狗(学生)', '王三狗']
    passengers = ['xxx', 'xxx']
    # 日期，格式为：'2018-01-20'
    dtime = 'xxxx-xx-xx'
    # 出发地(需填写cookie值)
    starts = '%u5357%u4EAC%2CNJH' #南京
    # 目的地(需填写cookie值)
    ends = '%u91D1%u534E%2CJBH' #金华
    Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()
