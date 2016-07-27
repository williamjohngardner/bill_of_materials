from highton import Highton

high = Highton(
    api_key = 'c8b5caeec4d60694480e0a47ff92e8d1',
    user = 'williamjohngardner'
)

people = high.get_people()
companies = high.get_companies()

for person in people:
    print(person.first_name, person.last_name)

for company in companies:
    print(company.name)
