import re

def sort_emails():

    with open('./assets/potential-contacts.txt', 'r') as potential_contacts:
        contents = potential_contacts.read()
        emails = re.findall(r'\S+@\S+', contents)
        emails.sort()

        not_duplicated = []

        for y in emails:
            if y not in not_duplicated:
                not_duplicated.append(y)

        with open('./assets/emails.txt', 'w') as emails_file:
            for x in emails:
                emails_file.write(f'{x}\n')    



def sort_phone_numbers():
    with open('./assets/potential-contacts.txt', 'r') as potential_contacts:
        contents = potential_contacts.read()

        phones = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', contents)
        phones.sort()
        not_duplicated_numbers = []

        for x in phones:
            number = re.sub('[^0-9]+', '', x)
            number_format = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(number[:-1])) + number[-1]
            if len(number_format) < 12:
                number_format = '206' + number_format[2:]

            if number_format not in not_duplicated_numbers:
                not_duplicated_numbers.append(number_format)

        not_duplicated_numbers.sort()
        with open('./assets/phone-numbers.txt', 'w') as f:
            for i in not_duplicated_numbers:
                f.write(f'{i}\n')



if __name__ == '__main__':
   sort_emails()
   sort_phone_numbers()


