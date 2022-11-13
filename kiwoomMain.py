import sys
from PyQt5.QtWidgets import *
import kiwoomAPI
from config import *

class kiwoonMain:
    def __init__(self):
        self.kiwoom = kiwoomAPI.kiwoomAPI()
    
# ========== #
    def Login(self):
        self.kiwoom.CommConnect()
        return self.kiwoom.login
    
    def Set_User_Name(self):
        user_name=self.kiwoom.GetLoginInfo("USER_NAME")
        return user_name
    
    def getLoginInfo(self):
        loginInfo = []
        loginInfo.append(self.kiwoom.GetLoginInfo("ACCOUNT_CNT"))
        loginInfo.append(self.kiwoom.GetLoginInfo("ACCLIST"))
        loginInfo.append(self.kiwoom.GetLoginInfo("USER_ID"))
        loginInfo.append(self.kiwoom.GetLoginInfo("USER_NAME"))
        loginInfo.append(self.kiwoom.GetLoginInfo("KEY_BSECGB"))
        loginInfo.append(self.kiwoom.GetLoginInfo("GetServerGubun"))
        
        return loginInfo
    
    def OPT10030(self):
        output_list={'OPT10030':['종목명','현재가','전일대비','등락률','거래량','거래금액'],}
        self.kiwoom.output_list=output_list['OPT10030']
        self.kiwoom.SetInputValue("시장구분","0")
        self.kiwoom.CommRqData("OPT10030","OPT10030",0,"0101")
        
        return self.kiwoom.ret_data['OPT10030']
    

    def OPT10031(self):
        output_list={'OPT10031':['종목명','현재가','전일대비','등락률','거래량','거래금액'],}
        self.kiwoom.output_list = output_list['OPT10031']

        self.kiwoom.SetInputValue("시장구분", "0")
        self.kiwoom.CommRqData("OPT10031", "OPT10031", 0, "0101")

        return self.kiwoom.ret_data['OPT10031']
    
    def OPT10032(self):
        self.kiwoom.output_list = output_list['OPT10032']

        self.kiwoom.SetInputValue("시장구분", "0")
        self.kiwoom.CommRqData("OPT10032", "OPT10032", 0, "0102")

        return self.kiwoom.ret_data['OPT10032']   
    
    def OPT10023(self):
        self.kiwoom.output_list = output_list['OPT10023']

        self.kiwoom.SetInputValue("시장구분", "0")
        self.kiwoom.SetInputValue("정렬구분"	,  "1");
        self.kiwoom.SetInputValue("시간구분"	,  "2");
        self.kiwoom.CommRqData("OPT10023", "OPT10023", 0, "0103")

        return self.kiwoom.ret_data['OPT10023']   
    
    def OPT10070(self):
        self.kiwoom.output_list = output_list['OPT10070']

        self.kiwoom.SetInputValue("종목코드", "005930")
        
        self.kiwoom.CommRqData("OPT10070", "OPT10070", 0, "0104")

        return self.kiwoom.ret_data['OPT10070'] 
    
# app = QApplication(sys.argv)
# api_con = kiwoonMain()

# result = api_con.OPT10031()
# print(result['Data'][0])

# result = api_con.OPT10032()
# print(result['Data'][0])

# result = api_con.OPT10023()
# print(result['Data'][0])

# result = api_con.OPT10070()
# print(result['Data'][0])
