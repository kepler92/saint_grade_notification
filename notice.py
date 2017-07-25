# 이메일을 보내기 위한 smtplib 모듈을 import 한다
import smtplib

# 이메일에 이미지를 첨부하기 위한 모듈들을 import 한다
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

try:
    import __secret_key as secret_key
except:
    import secret_key


def sendMessage(address, message):
    # 이메일 메세지 컨테이너를 만든다
    msg = MIMEMultipart()
    msg['Subject'] = u'세인트 성적 알림'

    # me == 보내는 사람의 주소
    # family = 받는 사람들의 모든 주소

    me = secret_key.sender_email
    you = address

    msg['From'] = me
    #msg['To'] = COMMASPACE.join(family)  # join 함수로 받는 사람들의 주소를 합친다
    msg['To'] = you
    #msg.preamble = 'saint score arlam'

    msg.attach(MIMEText(u'새로운 과목의 성적이 등록되었습니다.<br>', 'html', _charset='utf-8'))
    msg.attach(MIMEText(message, 'html', _charset='utf-8'))

    # 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(secret_key.sender_id, secret_key.sender_pw)
    s.sendmail(me, you, msg.as_string())
    s.quit()


def sendMessageWithImage(address, image_path):
    # 이메일 메세지 컨테이너를 만든다
    msg = MIMEMultipart()
    msg['Subject'] = u'세인트 성적 알림'

    # me == 보내는 사람의 주소
    # family = 받는 사람들의 모든 주소

    me = secret_key.sender_email
    you = address

    msg['From'] = me
    #msg['To'] = COMMASPACE.join(family)  # join 함수로 받는 사람들의 주소를 합친다
    msg['To'] = you
    #msg.preamble = 'saint score arlam'

    # 전송하고자 하는 이미지 파일들이 모두 PNG 파일이라고 가정하자
    '''for file in pngfiles:
        # 바이너리 모드로 전송할 파일들을 연다.
        # MIMEImage 클래스가 자동으로 이미지의 타입을 알아낼 것이다.
        fp = open(file, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)
    '''

    msg.attach(MIMEText(u'새로운 과목의 성적이 등록되었습니다.<br>첨부 이미지를 확인하여 주세요.<br>', 'html', _charset='utf-8'))

    fp = open(image_path, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

    # 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(secret_key.sender_id, secret_key.sender_pw)
    s.sendmail(me, you, msg.as_string())
    s.quit()