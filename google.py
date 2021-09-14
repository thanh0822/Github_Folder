import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
t=Translator()
a=t.translate("Em đẹp quá ",src="vi",dest="en")
print(a)
