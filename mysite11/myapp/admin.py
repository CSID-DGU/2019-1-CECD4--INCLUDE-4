from django.contrib import admin
from myapp.models import Client_info,Company_info,Client_account
from .models import Token
from .models import Tokenchange
from .models import tokensell
from .models import TokenList
from .models import buytoken
from .models import requesttoken
from .models import tokenwhitelist
from .models import TokenOrder
from .models import codecounting

admin.site.register(Client_info)
admin.site.register(Company_info)
admin.site.register(Client_account)
admin.site.register(Token)
admin.site.register(Tokenchange)
admin.site.register(tokensell)
admin.site.register(TokenList)
admin.site.register(buytoken)
admin.site.register(requesttoken)
admin.site.register(tokenwhitelist)
admin.site.register(TokenOrder)
admin.site.register(codecounting)


#admin.site.register(Admin)
# Register your models here.
