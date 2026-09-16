"""Wysyłka maila przez SMTP (Gmail) - funkcja SendInfoEmail przyjmuje dane logowania jako argumenty."""

import smtplib


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = f"""From: {mailFrom}
	To: {", ".join(mailTo)}
	Subject: {mailSubject}

	{mailBody}
	"""
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        return True
    except Exception as e:
        print(f"Wystąpił błąd: {e}")  # Obsługa błędu
        return False
    finally:
        print("Koniec obsługi błędu.")  # Blok 'finally' wykonuje się zawsze


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

# Dane logowania do serwera SMTP
user = "test@test.pl"
password = "***********"


SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
