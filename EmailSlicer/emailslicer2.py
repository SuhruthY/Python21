f_name = input("Enter File Name:")
if len(f_name) < 1: f_name = "mbox.txt"

emails =[]
# opening a file with hidden emails
with open(f_name, encoding = 'utf-8') as fh:
    lines = fh.readlines()
    for lin in lines:
        if lin.startswith('From'):
            words = lin.split()
            word = words[1]
            emails.append(word)

emails = list(set(emails))

for email in emails:
    # Get User-name and Domain-name
    user_name = email[: email.index("@")]
    domain_name = email[email.index("@") + 1 :]

    print("Your username is {} and domain name is {}".format(user_name, domain_name))
