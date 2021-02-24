import email
import quopri
import re

if __name__ == "__main__":
    msg_html = None
    with open("../raw/2021-02-23_money-stuff.eml", "r") as eml:
        msg = email.message_from_file(eml)
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                msg_html = quopri.decodestring(part.as_string(), header=True)
    with open("../as_string/2021-02-23_money-stuff.html", "w") as file:
        msg_html_no_header = re.sub(r"^Content-Type:.*\nContent-Transfer-Encoding.*\n\n", "", msg_html.decode("utf-8"))
        file.write(msg_html_no_header)
