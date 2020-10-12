# Get users email address
email = input("What is your email address?:").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@") + 1:]

print("Your username is {} and your domain name is {}".format(user_name, domain_name))
