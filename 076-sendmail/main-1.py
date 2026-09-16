# Wysyłka maila przez SMTP (Gmail) - wersja bez opakowania w funkcję (skrypt top-level).
import smtplib

# Dane wiadomości
mailFrom = "Your automation system"
mailTo = ["test@test.pl", "test10@test.pl"]  # Lista odbiorców
mailSubject = "Processing finished successfully"
mailBody = """Marsz, marsz, Dąbrowski,
Z ziemi włoskiej do Polski.
Za twoim przewodem
Złączym się z narodem.
Przejdziem Wisłę, przejdziem Wartę,
Będziem Polakami.
Dał nam przykład Bonaparte,
Jak zwyciężać mamy."""

message = f"""From: {mailFrom}
To: {", ".join(mailTo)}
Subject: {mailSubject}

{mailBody}
"""

# Dane logowania do serwera SMTP
user = "test@test.pl"
password = "***********"

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print("Wiadomość została wysłana.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")  # Obsługa błędu
finally:
    print("Koniec obsługi błędu.")  # Blok 'finally' wykonuje się zawsze
