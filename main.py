from jinja2 import Environment, PackageLoader, select_autoescape
from emails.email import send_mail

def main():
    email_id_sender = input("Enter Global SMTP Email ID: ")
    password = input("Enter Global SMTP Email Password: ")
    env = Environment(
        loader=PackageLoader("emails"),
        autoescape=select_autoescape()
    )
    
    stop = False
    while True: 
        name = input("Name: ")
        email = input("Email: ")
        certificate = input("Certificate URL [Google Drive Link]: ")
        
        template_select_error = True
        template_name = ""
        while template_select_error:
            template_type = input("""
                Select one of the following 3 Options
                1. The candidate is a winner [1st, 2nd, 3rd]
                2. The candidate is a finalist
                3. The candidate is a semi finalist\n""")

            if str(template_type) == "1":
                template_select_error = False
                template_name = "nonwinner.html"
            elif str(template_type) == "2":
                template_select_error = False
                template_name = "finalist.html"
            elif str(template_type) == "3":
                template_select_error = False
                template_name = "semifinalist.html"
            else:
                # User did not select one of 3 options
                print("Please select a valid option.")
        
        template = env.get_template(template_name)
        
        email_body = template.render(full_name = name, url = certificate)
        send_mail(to=email, body=email_body, email=email_id_sender, password=password)

        print("You just sent a " + template_name.strip(".html") + " email to: " + email)
        
        if stop == False:
            d = input("Continue: ")
            print(d)
            stop = d == "y"
            if stop:
                break


if __name__ == "__main__":
    main()