from smtplib import SMTP
import os


def send_emails(title: str, msg: str):
    try:
        sender = os.getenv("EMAIL_ID", "")
        password = os.getenv("EMAIL_PWD", "")
        recievers = os.getenv("RECIEVERS", "").split(",")

        smtp_address = "smtp-mail.outlook.com"  # smtp 서버 주소
        smtp_port = 587  # smtp 포트 번호

        subject = title
        content = f"Subject: {subject}\n\n {msg}"

        server = SMTP(smtp_address, smtp_port)  # 메일 서버 연결
        server.starttls()  # TLS 보안 처리
        server.login(sender, password)  # 로그인
        server.sendmail(sender, recievers[0], content.encode("utf-8").strip())
        server.close()  # smtp 서버 연결을 종료합니다.

    except ValueError:
        print("email 전송 실패")
