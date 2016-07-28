from highton import Highton

high = Highton(
    api_key = 'c8b5caeec4d60694480e0a47ff92e8d1',
    user = 'williamjohngardner'
)

sample_xml = "<person><first-name>William</first-name><last-name>Gardner</last-name><title>Principal</title><company-name>William John Gardner Design Studio</company-name><contact-data><email-addresses><email-address><address>bill@williamjohngardner.com</address></email-address></email-addresses><phone-numbers><phone-number><id>4433405272</id><number>4433405272</number></phone-number></phone-numbers><twitter-accounts><twitter-account><username>@williamjgardner</username><url>http://twitter.com/williamjgardner</url></twitter-account></twitter-accounts><web-addresses><web-address><id>214243865</id><url>http://www.williamjohngardner.com</url></web-address></web-addresses><addresses><address><street>PO Box 3098</street><city>Frederick</city><state>MD</state><zip>21705</zip><id>129411272</id><country>United States</country></address></addresses></contact-data></person>"


high.post_person(sample_xml)


people = high.get_people()
companies = high.get_companies()

for person in people:
    print(person.first_name, person.last_name)

for company in companies:
    print(company.name)

high.get_current_auth_user()
print(high.me)
