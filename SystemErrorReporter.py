import logging
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Завантаження конфігурації
def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

# Налаштування логування
def setup_logging(log_file, log_level):
    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Відправлення повідомлення електронною поштою
def send_email(smtp_server, smtp_port, email, password, recipient_email, subject, message):
    try:
        # Налаштування SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)

        # Формування повідомлення
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Відправлення
        server.sendmail(email, recipient_email, msg.as_string())
        server.quit()
        logging.info(f"Email sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")

# Головна функція
def main():
    # Завантаження конфігурації
    config = load_config()
    email_settings = config["email_settings"]
    logging_settings = config["logging_settings"]

    # Налаштування логування
    setup_logging(logging_settings["log_file"], logging_settings["log_level"])

    # Симуляція помилок
    try:
        # Щось викликає помилку
        x = 1 / 0
    except ZeroDivisionError as e:
        error_message = f"Error occurred: {str(e)}"
        logging.error(error_message)

        # Відправлення email
        send_email(
            email_settings["smtp_server"],
            email_settings["smtp_port"],
            email_settings["email"],
            email_settings["password"],
            email_settings["recipient_email"],
            "System Error Alert",
            error_message
        )

if __name__ == "__main__":
    main()
