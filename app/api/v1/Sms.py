from app.libs.redprint import Redprint
from app.service.Sms.SmsService import SmsService

api = Redprint('sms')


@api.route('/verification/get', methods=['POST'])
def verification_code_get():
    """
    获取验证码
    """
    res = SmsService()
    return res.send()
