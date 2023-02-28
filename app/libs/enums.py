from enum import Enum


class FileTypeEnum(Enum):
    TXT = 1
    PDF = 2
    PNG = 3
    JPG = 4
    JPEG = 5
    GIF = 6
    PPT = 7
    PPTX = 8
    DOC = 9
    DOCX = 10
    XLS = 11
    XLSX = 12
    CSV = 13
    MP3 = 14
    MP4 = 15


class SmsTemplateTypeEnum(Enum):
    测试 = {
        "sign_name": "阿里云短信测试",
        "sms_template_code": "SMS_154950909",
    }
    注册 = {
        "sign_name": "chaichai",
        "sms_template_code": "SMS_270945528"
    }
