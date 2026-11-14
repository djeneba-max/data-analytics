contact_info = {
    "name": "Baba Ly",
    "address": "125 cloud Street",
    "city": "Newark",
    "state": "NJ",
    "zip": "07102"
}


print(f"""Mailing address:
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

del contact_info["name"]

ful_name = {
    "first name": "Baba",
    "last name": "Ly"
}

ful_name.update({"honorific": "Mr."})

contact_info.update(ful_name)

print(f"""Mailing address:
{contact_info['honorific']} {contact_info['first name']} {contact_info['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")