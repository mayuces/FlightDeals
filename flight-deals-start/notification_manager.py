import smtplib
# your mail here
my_yahoo = "your mail here"
password = "your password here"


class NotificationManager:

    def send_emails(self, emails, message, link):
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_yahoo, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_yahoo,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8')
                )
