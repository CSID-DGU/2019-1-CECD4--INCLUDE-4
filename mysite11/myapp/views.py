from django.shortcuts import render
from .forms import SigninForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Token, Tokenchange, tokensell, buytoken, TokenList, requesttoken, tokenwhitelist, TokenOrder, codecounting
from .forms import uploadForm
from django.db.models import Q


from .models import Company_info, Client_account,Client_info

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404 



from django.core.paginator import Paginator

import binascii
#get_object_or_404는 특정 조건의 객체를 불러오는데 사용하며, 
#만약 만족하는 객체가 없다면 404 에러가 뜨게된다.


User = get_user_model()

companycod = 10
accocode = 10
class MetamaskContract():
     def __init__(self,fromadd,toadd,abi,contractaddress,companyAccount,count):
        self.fromadd=fromadd
        self.toadd=toadd
        self.ABI=abi
        self.ContractAddress=contractaddress
        self.companyAccount=companyAccount
        self.Count=count

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def signin(request):
    if request.method == "GET":
        return render(request, 'myapp/login.html')
    
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
#authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
#만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.

        if u: #u에 특정 값이 있다면
            login(request, user=u) #u 객체로 로그인해라
            return render(request,'myapp/home.html')
        else:
            return render(request, 'myapp/login.html')

def signout(request):
    logout(request)
    return render(request,'myapp/home.html')
    
def mypage(request):
    return render(request, 'myapp/mypage.html')

def intro(request):
    return render(request, 'myapp/intro.html')

def funding(request):
    return render(request, 'myapp/info.html')

def join(request):
    return render(request, 'myapp/join.html')

def test(request):
    return render(request, 'myapp/menu_test.html')
def info(request,code):
    company=get_object_or_404(Company_info,Company_code=code)
    return render(request, 'myapp/info.html',{'q':company})

def input_bank(request, client_code):
    user = Client_info.objects.get(client_code=client_code)
    if request.method == 'POST':
        answer = request.POST['bank_select']
        account = 123456789
        Client_info.objects.filter(client_code=client_code).update(input_bank=answer)
        Client_info.objects.filter(client_code=client_code).update(input_account=account)
        if user.bankstatus == 0:
            Client_info.objects.filter(client_code=client_code).update(bankstatus=10)
        else :
            Client_info.objects.filter(client_code=client_code).update(bankstatus=11)
        return render(request, 'myapp/load.html')
    elif request.method == 'GET':
        login = Client_info.objects.get(client_code=client_code)
        context = {'login':login}
        return render(request, 'myapp/input_bank.html', context)
    
def output_bank(request, client_code):
    user = Client_info.objects.get(client_code=client_code)
    if request.method == 'POST':
        answer = request.POST['bank_select']
        account = request.POST['bank_account']

        Client_info.objects.filter(client_code=client_code).update(output_bank=answer)
        Client_info.objects.filter(client_code=client_code).update(output_account=account)
        if user.bankstatus == 0:
            Client_info.objects.filter(client_code=client_code).update(bankstatus=1)
        else :
            Client_info.objects.filter(client_code=client_code).update(bankstatus=11)
        return render(request, 'myapp/load.html')
    elif request.method == 'GET':
        login = Client_info.objects.get(client_code=client_code)
        context = {'login':login}
        return render(request, 'myapp/output_bank.html', context)

def load(request):
    return render(request, 'myapp/load.html')

def addwhlist(request,companycode):
    buyer_account = request.POST.get('buyer_account')
    client = Client_info.objects.get(MetamastAddress=buyer_account)
    add_client = tokenwhitelist(company_code=companycode, Client_code=client.client_code)
    add_client.save()

    company = TokenList.objects.get(compname=companycode)
    whlistaddress = company.wlistAddress
    context = {'whlistaddress':whlistaddress, 'addaccount':buyer_account}

    return render(request, 'myapp/addwhlist.html', context)

def tokenregis(request):
    is_in = Client_account.objects.filter(Cli_code = request.user.client_code)
    if is_in:
        return render(request,'myapp/cantregist.html')

    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            co = Company_info.objects.all().last()
            aco = Client_account.objects.all().last()
            comcode = ""
            if co:
             cod = co.Company_code
             code = int(cod) + 1
             stcode = str(code)
             while len(stcode) < 6:
                stcode = '0' + stcode
             a = Company_info(Company_name = form.data['compname'], Company_code = stcode,information = form.data['introduce'], photo = form.files['image'], President_Email = form.data['preemail'])
             a.save()
             comcode = stcode
            else:
             a = Company_info(Company_name = form.data['compname'], Company_code = "000000",information = form.data['introduce'], photo = form.files['image'], President_Email = form.data['preemail'])
             a.save()  
             comcode = "000000"

            if aco:
                cod = aco.Account_code
                code = int(cod) + 1
                stcode = str(code)
                while len(stcode) < 6:
                 stcode = '0' + stcode
                a = Client_account(Account_code = stcode,Cli_code = Client_info.objects.get(username = request.user).client_code,Company_code = comcode, Quota = 0)
                a.save()
            else:
                a = Client_account(Account_code = "000000",Cli_code = Client_info.objects.get(username = request.user).client_code,Company_code = comcode, Quota = 0)
                a.save()
            c = TokenOrder(tokenname = form.data['tokenname'], quota = form.data['quota'], metamaskaddress = request.user.MetamastAddress, initial = form.data['initial'], state = '0', divide = float(form.data['divide'])) 
            c.save()
            d = TokenList(tokenname =form.data['tokenname'],compname = comcode, companyAccount= request.user.MetamastAddress, CUR_price = form.data['price'] )
            d.save()
           
            return render(request,'myapp/home.html')
    
    else:
        form = uploadForm()
        return render(request,'myapp/tokenregister.html',{'form':form})

def adminpage(request):
    print(request.user)
    if request.user.username == "er":
        state0 = TokenOrder.objects.filter(state = '0')
        state2 = TokenOrder.objects.filter(state = '2')
        context = {'state0':state0, 'state2':state2}
        return render(request,'myapp/adminpage.html', context)
    else:
        return render(request,'myapp/home.html')

def tokenbuying(request,code):
    #POST일 경우와 아닌 경우를 나눈다.
    if request.method == 'POST':
        #구매요청한 정보 db에 저장
        company_code2 = request.POST.get('company_code')
        one_tokenprice2 = request.POST.get('one_tokenprice')
        token_num2 = request.POST.get('token_num_label')
        buyeraccount2 = request.POST.get('buyeraccount')
        selleraccount2 = request.POST.get('selleraccount')
        sellertotaltoken2 = request.POST.get('sellertotaltoken')
        client_code = request.POST.get('Client_code')
        sell_code = request.POST.get('sell_code')
        tokenname = request.POST.get('tokenname')
        code_count = codecounting.objects.get(primarykey = 1)
        count = code_count.requestcount + int(1)
        codecounting.objects.filter(primarykey=1).update(requestcount=count)
        b = requesttoken(requestcode=count,one_tokenprice=one_tokenprice2, requesttoken_num=token_num2, 
        buyer_account=buyeraccount2, seller_account=selleraccount2, sellertotaltoken=sellertotaltoken2,
        company_code=company_code2, whlist_check=0, Client_code=client_code, sell_code=sell_code)
        b.save()

        #구매한 양만큼 유저의 krw를 감소한다.
        login_user = request.user
        login_krw = Client_info.objects.get(username=login_user.username)
        buykrw = float(token_num2) * float(one_tokenprice2)
        leftkrw = float(login_krw.KRW) - float(buykrw)
        Client_info.objects.filter(username=login_user.username).update(KRW=leftkrw)

        #판매자가 판매하고 있는 토큰에 대하여 대기 토큰 등록하고 판매 토큰을 줄이기
        tokensell_info = tokensell.objects.get(sell_code=sell_code) #판매 토큰에 대한 판매 정보 가져옴
        quota_tmp = float(tokensell_info.quota) - float(token_num2)
        standby_tmp = tokensell_info.standby + float(token_num2)
        tokensell.objects.filter(sell_code=sell_code).update(standby=standby_tmp, quota=quota_tmp)

        #구매자가 구매를 요청했을 때, tokenchange에서 바이어에 입력한다. #requestcode에 따라서 달라짐. 토큰양이 전체 양보다 작으면 tokenchange를 세분화한다.
        #Tokenchange.objects.filter(sell_code=sell_code).update(buyer=buyeraccount2)
        if(sellertotaltoken2 > token_num2):
            Tokenchange.objects.filter(sell_code = sell_code).delete()
            tokennum_tmp = float(sellertotaltoken2) - float(token_num2)
            change1 = Tokenchange(tokenname=tokenname, tokenprice=one_tokenprice2, quantity=tokennum_tmp, seller=selleraccount2, Approval=False, sell_code=sell_code)
            change1.save()
            change2 = Tokenchange(tokenname=tokenname, tokenprice=one_tokenprice2, quantity=token_num2, seller=selleraccount2, Approval=False, sell_code=sell_code,
            buyer= buyeraccount2, request_code=count)
            change2.save()
        
        return render(request, 'myapp/tokenbuyrequest.html')
    else :
        login_user=request.user
        login_userinfo=Client_info.objects.get(username=login_user.username)
        try:
            company=Company_info.objects.get(Company_code=code)
            company2 = company.Company_code
            token=TokenList.objects.get(compname=company2)
            tokenselling=tokensell.objects.filter(tokenname=token.tokenname)
        #buylist=get_object_or_404(buytoken,token_taker=company)
            context={'selllist':tokenselling,'loginuserinfo':login_userinfo, 'company':company, 'code':code}
        except TokenList.DoesNotExist:
            #raise Http404("%s의 토큰을 준비중입니다.앞으로의 미래를 기대해보세요!" % company.Company_name)
            return render(request, 'myapp/home.html')      
        return render(request, 'myapp/tokenbuying.html',context)

def dbtest(request):
    return render(request, 'myapp/dbtest.html')

def list(request):
    company=Company_info.objects
    candidates=Company_info.objects.all()
    paginator=Paginator(candidates,6)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    context= {'company':company,'posts':posts}
    return render(request, 'myapp/list.html',context)

def signup(request):
    if request.method == "GET":
        return render(request, 'myapp/signup.html' )
    
    
    elif request.method == "POST":
      
            if request.POST['password']==request.POST['password_check']:
           
                code=str(User.objects.count()).zfill(6)
                new_user=User.objects.create_user(username=request.POST['username'],
                password=request.POST['password'],
                client_code=code,
                MetamastAddress=request.POST['metamask'])

               
                new_user.save()
                return render(request,'myapp/home.html')      
            else:
                return render(request, 'myapp/signup.html',{ 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})#password와 password_check가 다를 것을 대비하여 error를 지정해준다.

    else:
        return render(request, 'myapp/signup.html')



def statechange(request,tokenname):
  
    mytoken = TokenOrder.objects.get(tokenname = tokenname)
    stat = int(mytoken.state) + 1
    strstat = str(stat)
    mytoken.state = strstat
    mytoken.save()
    
    context = {'mytoken':mytoken}

    return render(request,"myapp/statechange.html", context)

def statechangeuser(request,tokenname):

    mytoken = TokenOrder.objects.get(tokenname = tokenname)
    if int(mytoken.state) == 4:
        a = Token(tokenname = tokenname, person = request.user.client_code,quantity = mytoken.quota)
        a.save()
    stat = int(mytoken.state) + 1
    strstat = str(stat)
    mytoken.state = strstat
    mytoken.save()
   
    
    comptoken = TokenList.objects.get(tokenname = tokenname)
    context = {'mytoken':mytoken,'comptoken':comptoken}
   
        
    return render(request,"myapp/statechangeuser.html", context)

def register(request):
    if request.method == "GET":
        return render(request, 'myapp/register.html')

    elif request.method == "POST":
        code=str(Company_info.objects.count()).zfill(6)
        form=Company_info(Company_name=request.POST['name'],President_Email=request.POST['email'],Company_code=code)
        form.save()
        return render(request,'myapp/home.html')

def accountconnect(request):
    if request.method == "GET":
        candidates=Company_info.objects.all()
        context= {'candidates':candidates}
        
        return render(request,'myapp/accountconnect.html',context)


    elif request.method == "POST":
        ac_code=str(Client_account.objects.count()).zfill(6)
        Company=Company_info.objects.get(Company_code=str(request.POST.get('code')))
        if not Client_account.objects.filter(Cli_code=request.user.client_code):
            account=Client_account(Company_code=Company,Cli_code=request.user,Account_code=ac_code)
            account.save()
        return render(request,'myapp/accountconnect.html')

def search(request):
    if request.method == "GET":
        candidates=TokenList.objects.all()
        context= {'candidates':candidates}
        
        return render(request,'myapp/search.html',context)


    elif request.method == "POST":
       
        ac_code=TokenList.object.get(tokenname=Company_info.objects.get(request.POST.get('code')))
        info=tokensell.objects.get(tokenname=ac_code)
        info+=buytoken.objects.get(tokenname=ac_code)
        context= {'cols':cols}

        return render(request,'myapp/search.html',content)

def mypage(request): # 마이페이지 출력        

        b = tokenwhitelist()
        tokenlist = Token.objects.filter(person = request.user.client_code)
        transsel = Tokenchange.objects.filter(seller = request.user.MetamastAddress).exclude(request_code=0)
        transbuy = Tokenchange.objects.filter(buyer = request.user.MetamastAddress)
        tokenorder = TokenOrder.objects.filter(metamaskaddress = request.user.MetamastAddress)
        #TokenList = TokenList.objects.filter(tokenname = request)

        if transsel:

            for sel in transsel:
                cut = TokenList.objects.get(tokenname = sel.tokenname)
                rat = (cut.CUR_price - sel.tokenprice)/cut.CUR_price
                sel.rate = rat*100
                sel.save()

        if transbuy:

            for buy in transbuy:
                cut = TokenList.objects.get(tokenname = buy.tokenname)
                rat = (cut.CUR_price - buy.tokenprice)/cut.CUR_price
                buy.rate = rat*100
                buy.save()
        ccode = Client_info.objects.get(username = request.user).client_code
        compinfo = Client_account.objects.filter(Cli_code = ccode)
        if compinfo:
            comp = compinfo.first()
            code = comp.Company_code
            comptoken = TokenList.objects.filter(compname = code)
            requlist = requesttoken.objects.filter(company_code = code)
            whlist = tokenwhitelist.objects.filter(company_code = code)
            #whlist를 체크해서 리스트에 들어가 있으면, requesttoken에서 whlist_check 값을 1로 바꿔준다.
            requesttoken.objects.filter(Client_code__in=whlist).update(whlist_check='1')
            context = {'tokenlist':tokenlist,'transsel':transsel,'transbuy':transbuy, 'comptoken':comptoken, 'requlist':requlist, 'tokenorder':tokenorder, 'companycode':code, 'login':login}
        else: #투자만 하는 유저인 경우
            context = {'tokenlist':tokenlist,'transsel':transsel,'transbuy':transbuy,'tokenorder':tokenorder}
        return render(request, 'myapp/mypage.html',context)

def sell(request, tokenname): # 판매할 토큰을 판매자에게 보내기 위한 과정
    #판매하려는 양만큼 회사에게 돌려주고, db에 저장한다. 
        user = Token.objects.get(person = request.user.client_code)
        if (float(request.POST['number']) <= user.quantity):
            
            mad = Client_info.objects.get(username = request.user).MetamastAddress #유저의 메타마스크 주소
            token_num = request.POST['number']
            code_count = codecounting.objects.get(primarykey=1)
            count = code_count.tokensellcount + int(1)
            codecounting.objects.filter(primarykey=1).update(tokensellcount=count)
            a = tokensell(token_seller = request.user, tokenname = tokenname, quota = request.POST['number'], 
            price = request.POST['price'],metamask_account = mad, sell_code =count)
            a.save()
            quantity = user.quantity - float(token_num)
            if (quantity == 0):
               Token.objects.filter(person = request.user.client_code, tokenname=tokenname).delete()
            else :
                Token.objects.filter(person = request.user.client_code, tokenname=tokenname).update(quantity=quantity)


            #tokenchange에 값을 입력하여 판매 리스트에 등록한다.
            token_price = request.POST['price']
            selltoken = Tokenchange(tokenname=tokenname, tokenprice=token_price, quantity=token_num, seller=mad, Approval=False, sell_code=count)
            selltoken.save()

            #회사의 계정을 불러와 회사로 토큰을 보내도록 한다.
            tokenname_tmp = tokenname
            token_num = request.POST['number']
            candidate = TokenList.objects.get(tokenname = tokenname_tmp)
            context = {'tokencompany':candidate, 'quota':token_num}
            return render(request, 'myapp/sell.html', context)
        else:
            return render(request, 'myapp/mypage.html') #실패한 경우 페이지를 다시 돌아감 

def finsell(request):
    return render(request, 'myapp/finsell.html')

def finapproval(request):
    return render(request, 'myapp/finapproval.html')


def send(request, requestcode): # 구매시 토큰을 전송하기 위한 과정
    #1.토큰의 시세를 변경해준다 2.판매자의 krw를 변경해준다 3.판매리스트에서 standby를 없애준다 4.구매자의 토큰소유 양을 변경해준다.
    # 평균가는 token_trans를 Product.objects.all().aggregate(Avg('price'))와 같은 형태로 계산한다.    

    #판매자의 krw변경
    trans = requesttoken.objects.get(requestcode = requestcode)
    seller = Client_info.objects.get(MetamastAddress = trans.seller_account)
    seller.KRW = seller.KRW + trans.one_tokenprice * trans.requesttoken_num
    seller.save()

    #판매리스트에서 대기 토큰 삭제
    tokenselling = tokensell.objects.get(sell_code=trans.sell_code)
    standby_tmp = tokenselling.standby
    standby_cal = standby_tmp - trans.requesttoken_num
    tokensell.objects.filter(sell_code=trans.sell_code).update(standby=standby_cal)

    if(tokenselling.standby == 0.0 and tokenselling.quota ==0.0): #토큰 판매가 대기도 없고, 0인 상태라면 삭제
        tokensell.objects.filter(sell_code=trans.sell_code).delete()

    #tokenchange에서 승인 완료로 변경해줌
    Tokenchange.objects.filter(sell_code=trans.sell_code, request_code=requestcode).update(Approval=True)

    #구매자의 토큰 소유 양 변경 및 거래 완료 시 거래요청에서 데이터 삭제
    company = Company_info.objects.get(Company_code = trans.company_code)
    token = TokenList.objects.get(compname = company.Company_code)
    buyer = Client_info.objects.get(MetamastAddress = trans.buyer_account)
    #st = Token.objects.filter(tokenname = token.tokenname) & Token.objects.filter(person = seller.client_code)
    st = Token.objects.filter(tokenname = token.tokenname)
    if st:
        st1 = st.get(person = request.user.client_code)
        st1.quantity -= trans.requesttoken_num
        st1.save()
        if st1.quantity == 0:
            st1.delete()
    bt = Token.objects.filter(person = buyer.client_code)

    if bt:
        bk = bt.filter(tokenname = token.tokenname)
        br = bk.first()
        br.quantity  = br.quantity + trans.requesttoken_num
        br.save()
    else:
        tok = Token(tokenname = token.tokenname, person = buyer.client_code, quantity = trans.requesttoken_num)
        tok.save()
    trans.delete() # 회사 마이페이지에서 승인 대기 내역 삭제
    candidates = TokenList.objects.get(tokenname = token.tokenname)
    
    add = candidates.companyAccount
    candidates={'seller':seller.MetamastAddress,'buyer':buyer.MetamastAddress,'ContractAddress':candidates.ContractAddress,'companyAccount':add,'tokennum':trans.requesttoken_num} # ABI가 없다고 함

    return render(request,'myapp/send.html', candidates)

def listToken(request):
    tokens = TokenList.objects.all()
    sell = tokensell.objects.all()
    buy = buytoken.objects.all()
    context = {'tokens':tokens, 'sell':sell,'buy':buy}
    return render(request,'myapp/listtoken.html', context)


def blockchain(request):
    candidates=Tokenchange.objects.all()
    tmp=u""
    for candidate in candidates:
        tmp+=str(candidate.tokenprice)+str(candidate.quantity)+candidate.seller+candidate.buyer+str(candidate.date)+candidate.T_type+str(candidate.Approval)
    

    tmp=tmp.encode('utf-8')
    tmp=binascii.hexlify(tmp)
    context={'a':tmp}

    

    return render(request, 'myapp/blockchain.html',context)
