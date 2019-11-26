from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django_countries.fields import CountryField

class Client_info(AbstractUser):
    client_code = models.CharField(primary_key=True, max_length = 6) # 6자리 고유 코드 부여
    cl_email = models.CharField(max_length = 10, blank = True) # emailfield로 변형
    cl_phone = models.CharField(max_length = 11, blank = True) # -없이 입력
    auth = models.BooleanField(default = False) 
    #country =  CountryField()# 나라 선택 가능하게 하면 좋을듯?
    passport = models.CharField(max_length = 10, blank = True)
    MetamastAddress=models.CharField(max_length = 200, blank = True)
    KRW = models.IntegerField(default=0)

class Company_info(models.Model) : # company information
    Company_code = models.CharField(primary_key= True,max_length= 6)
    Company_name = models.CharField(max_length = 100, blank = True)
    President_Email = models.EmailField()
    Address = models.CharField(max_length= 100, blank = True)
    information=models.CharField(max_length=5000,blank=True)
    photo = models.ImageField(upload_to='image',default='image/default.jpg')
    keyinfo = models.ImageField(upload_to='image',default='image/defaultinfo.jpg')

class TokenOrder(models.Model):
    tokenname = models.CharField(max_length=100)
    initial = models.CharField(max_length=100)
 #DIVIDE_CHOICE = (1,0.1,0.01,0.001,0.0001,0.00001,0.000001,0.0000001,0.00000001,0.000000001,0.0000000001,0.00000000001,0.00000000001,0.0000000000001,0.00000000000001,0.000000000000001,0.000000000000001,0.000000000000001)
    divide = models.FloatField(default = 1)
    quota = models.FloatField(default = 0)
    metamaskaddress = models.CharField(max_length=200)
  
    STATE_CHOICE = (('0','토큰 예약 대기'),('1','토큰 생성 완료'),('2','ABI대기'),('3','화이트 리스트 등록'),('4','토큰 최종 발행'),('5', '거래 중'),('6', 'else')) # state 값은 0,1,2,3 중 선택. 단계에 따라 달라지게 설정하면 됨
    state = models.CharField(max_length = 1, choices=STATE_CHOICE, null = True)
    
class Client_account(models.Model) : # 고객 - 회사 계약정보 N:N관계해소
     Account_code = models.CharField(primary_key = True, max_length=6)
     Cli_code = models.CharField(max_length = 100)
     Company_code = models.CharField(max_length = 100)
     Quota = models.FloatField(default=0) # 고객의 구매량

class Token_Trans(models.Model):
    Time = models.DateTimeField('date publised',primary_key = True)
    company_code = models.ForeignKey(Company_info, on_delete = models.CASCADE)
    price = models.FloatField(default=0)

class TokenList(models.Model): # 현재 발행된 토큰 리스트, 토큰 발행하고 이 디비에 저장해주길 바람wind
    
    tokenname = models.CharField(max_length=100, primary_key=True)
    #compname = models.CharField(max_length=100) # 회사명 외래키
    compname = models.CharField(max_length = 100) 
    CUR_price = models.FloatField(default = 0)
    ContractAddress = models.CharField(max_length=100, null = True)
  #  ABI = models.CharField(max_length=1000000, null = True)
    companyAccount = models.CharField(max_length=100, null = True)
    wlistAddress = models.CharField(max_length=100, null = True)
  #  wlistABI = models.CharField(max_length=1000000, null = True)

class Token(models.Model): # 토큰을 소유한 고객 리스트
    tokenname = models.CharField(max_length=100)
    person = models.CharField(max_length = 100)
    quantity = models.FloatField(default = 0) # 토큰의 양
   

class Tokenchange(models.Model): # 토큰 거래내역 저장
    tokenname = models.CharField(max_length = 100) # 토큰명
    tokenprice = models.FloatField(default = 0) # 실거래가
    quantity = models.FloatField(default = 0) #거래량
    seller = models.CharField(max_length = 100,null=True) # 토큰 판매자 
    buyer = models.CharField(max_length = 100, null = True) # 토큰 구매자 
    date = models.DateTimeField(auto_now_add=True) #거래일시
    T_type = models.CharField(max_length = 3, null = True) # CTP(회사와 고객 거래) or PTP(개인과 개인 거래)
    Approval = models.BooleanField(default = False)
    rate = models.FloatField(default = 0)
    sell_code = models.IntegerField(default=0)
    request_code = models.IntegerField(default=0)

class tokensell(models.Model):
    token_seller = models.ForeignKey(Client_info,on_delete = models.CASCADE)
    tokenname = models.CharField(max_length=100)
    quota = models.FloatField(default = 0)
    price = models.FloatField(default = 0)
    metamask_account = models.CharField(max_length = 200, blank = True)
    standby = models.FloatField(default=0)
    sell_code = models.IntegerField(default=0)

#현재 판매하고 있는 토큰에 대하여 구매자가 구매 대기하고 있는 양에 대해서...

class buytoken(models.Model):
    token_taker = models.ForeignKey(Client_info,on_delete = models.CASCADE)
    tokenname = models.CharField(max_length=100)
    quota = models.FloatField(default = 0)
    price = models.FloatField(default = 0)

class requesttoken(models.Model): #토큰을 사길 원하는 사람들에 대한 목록
    #company_code, 1토큰가격, 구매요청한토큰개수, 구매자계정, 판매자계정, 해당판매자가판매하고있는총토큰양에 대하여 저장
    requestcode = models.IntegerField(default=0) # 거래번호. view에서 디비 조정할 때 필요함
    one_tokenprice = models.FloatField(default = 0)
    requesttoken_num = models.FloatField(default = 0)
    buyer_account = models.CharField(max_length = 200, blank = True)
    seller_account = models.CharField(max_length = 200, blank = True) 
    sellertotaltoken = models.FloatField(default = 0)
    company_code = models.CharField(max_length= 10, null=True)
    whlist_check = models.IntegerField(default=0)
    Client_code = models.CharField(max_length=6, null=True)
    sell_code = models.IntegerField(default=0)

class tokenwhitelist(models.Model):
    company_code = models.CharField(max_length=10)
    Client_code = models.IntegerField(default=0)

class codecounting(models.Model):
    primarykey = models.IntegerField(primary_key=True, null=False, default=1)
    tokensellcount = models.IntegerField(default=0)
    requestcount = models.IntegerField(default=0)


# Create your models here.