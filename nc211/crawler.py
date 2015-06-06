# -*- coding: utf-8 -*-
import requests
import csv
import re
import html5lib
import urllib2

from bs4 import BeautifulSoup

def nc211_spider(start_page, end_page):

    with open('links.csv', 'w') as csvfile:
        linkwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_NONE)
        linkheader = ["url", "name", "location", "addr1", "addr2", "city", "state", "zipcode", "phone", "services"]
        linkwriter.writerow(linkheader)

    with open('details.csv', 'w') as detailfile:
        detailwriter = csv.writer(detailfile, delimiter=',', escapechar='"', lineterminator='\n', quoting=csv.QUOTE_NONE)
        detailheader = ["name", "website", "description", "hours", "intake", "fees", "eligibility", "accessibility", "volunteer", "geoserved_cnty", "geoserved_muni", "services", "languages", "phones", "addresses", "contacts"]
        detailwriter.writerow(detailheader)

    with open('links.csv', 'a') as csvfile:
        linkwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
        page = start_page

        while page <= end_page:
            url = 'http://nc211.bowmansystems.com/index.php/component/cpx/index.php?option=com_cpx&task=search.query&advanced=true&search_history_id=-1&all=&any=&zipcode=&range=0&city=&county=&geo_zipcode=&geo_city=&geo_county=&volunteer_query=&wishlist_query=&code=&submit=Search&page=' + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, 'html5lib')
            for div in soup.findAll('div', attrs={'class': 'content'}):
                hlink = 'http://nc211.bowmansystems.com' + div.find('a')['href']
                name = div.find('a').contents[0].encode('utf-8')
                raw_location = div.find('p', attrs={'class': 'location'}).contents
                phone = raw_location.pop().strip()
                length = len(raw_location)
                if length == 0:
                    addr1 = ''
                    addr2 = ''
                    city = ''
                    state = ''
                    zipcode = ''
                elif length == 1:
                    location = ''.join([location.encode('utf-8').strip() for location in raw_location])
                    location = re.sub('<br/>', ', ', location)
                    location = location.strip()[:-1]
                    loc_list = [x.encode('utf-8').strip() for x in location.split(',')]
                    addr1 = loc_list[0]
                    addr2 = ''
                    city = ''
                    state = ''
                    zipcode = ''
                elif length == 2:
                    location = ''.join([location.encode('utf-8').strip() for location in raw_location])
                    location = re.sub('<br/>', ', ', location)
                    location = location.strip()[:-1]
                    loc_list = [x.encode('utf-8').strip() for x in location.split(',')]
                    zipcode = loc_list[-1][3:]
                    state = loc_list[-1][0:2]
                    new_list = loc_list.pop()
                    if len(loc_list) > 0:
                        city = loc_list[-1]
                    else:
                        city = ''
                    addr1 = ''
                    addr2 = ''
                else:
                    location = ''.join([location.encode('utf-8').strip() for location in raw_location])
                    location = re.sub('<br/>', ', ', location)
                    location = location.strip()[:-1]
                    location = re.sub("Chaplainâs", "Chaplain\'s", location)
                    location = re.sub("Patrickâs", "Patrick\'s", location)
                    location = re.sub("410 â 414", "410-414", location)
                    loc_list = [x.encode('utf-8').strip() for x in location.split(',')]
                    zipcode = loc_list[-1][3:]
                    state = loc_list[-1][0:2]
                    new_list = loc_list.pop()
                    city = loc_list[-1]
                    new_list = loc_list.pop()
		    if len(loc_list) > 0:
	                addr1 = loc_list[0]
                        new_list = loc_list.pop(0)
                        if len(loc_list) > 0:
                            addr2 = loc_list[0]
                        else:
                            addr2 = ''
                    else:
		        addr1 = ''
		        addr2 = ''
                services = div.find('p', attrs={'class': 'services'}).contents[0].string
                print(hlink)
                print(name)
                # print(location)
                # print("Addr1 = " + addr1)
                # print("Addr2 = " + addr2)
                # print("City = " + city)
                # print("State = " + state)
                # print("Zipcode = " + zipcode)
                # print("Phone = " + phone)
                # print(services.strip())
                output = [hlink, name, location, addr1, addr2, city, state, zipcode, phone, services.strip()]
                get_single_item_data(hlink)
                print ('*******************')
                linkwriter.writerow(output)
                location = ''
            print("PAGE=" + str(page))
            page += 1
        csvfile.close()

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    # item_name="BLANK"

    # First get the name
    item_name = soup.find('p', {'id': 'view_field_name_top'}).text.encode('utf-8')

    # print item_name
    if not item_name:
        item_name = ''
        # print("Name=BLANK")

    # First piece of info the website address
    if soup.find('p', {'id': 'view_field_url'}):
        website_name = soup.find('p', {'id': 'view_field_url'}).text.encode('utf-8')
    # print website_name
    else:
       website_name = ''
       # print("Website Name=BLANK")

    # Text description
    first_description = soup.find('p', {'id': 'view_field_description'})
    if first_description:
        raw_description = first_description.contents
        description = ''.join([description.encode('utf-8').strip() for description in raw_description])
        description = re.sub('<br/>', ', ', description)
        if not description:
            description = ''
            # print("Description=BLANK")
    else:
        description = ''
       # print("Description=BLANK")

    # Hours
    first_hours = soup.find('p', {'id': 'view_field_hours'})
    if first_hours:
        raw_hours = first_hours.contents
        hours = ''.join([hours.encode('utf-8').strip() for hours in raw_hours])
        hours = re.sub('<br/>', ', ', hours)
        if not hours:
            hours = ''
            # print("Hours=BLANK")
    else:
         hours = ''
         # print("Hours=BLANK")

    # Intake Process
    first_intake = soup.find('p', {'id': 'view_field_intakeProcedure'})
    if first_intake:
        raw_intake = first_intake.contents
        intake = ''.join([intake.encode('utf-8').strip() for intake in raw_intake])
        intake = re.sub('<br/>', ', ', intake)
        if not intake:
            intake = ''
            # print("Intake=BLANK")
    else:
         intake = ''
         # print("Intake=BLANK")

    # Program Fees
    first_fees = soup.find('p', {'id': 'view_field_programFees'})
    if first_fees:
        raw_fees = first_fees.contents
        fees = ''.join([fees.encode('utf-8').strip() for fees in raw_fees])
        fees = re.sub('<br/>', ', ', fees)
        if not fees:
            fees = ''
            # print("Fees=BLANK")
    else:
         fees = ''
         # print("Fees=BLANK")

    # Eligibility
    first_eligibility = soup.find('p', {'id': 'view_field_eligibility'})
    if first_eligibility:
        raw_eligibility = first_eligibility.contents
        eligibility = ''.join([eligibility.encode('utf-8').strip() for eligibility in raw_eligibility])
        eligibility = re.sub('<br/>', ', ', eligibility)
        if not eligibility:
            eligibility = ''
            # print("Eligibility=BLANK")
    else:
         eligibility = ''
         # print("Eligibility=BLANK")

    # Accessibility
    first_accessibility = soup.find('p', {'id': 'view_field_accessibility'})
    if first_accessibility:
        raw_accessibility = first_accessibility.contents
        accessibility = ''.join([accessibility.encode('utf-8').strip() for accessibility in raw_accessibility])
        accessibility = re.sub('<br/>', ', ', accessibility)
        if not accessibility:
            accessibility = ''
            # print("Accessibility=BLANK")
    else:
         accessibility = ''
         # print("Accessibility=BLANK")

    # Volunteer Opportunities
    first_volunteer = soup.find('p', {'id': 'view_field_volunteer'})
    if first_volunteer:
        raw_volunteer = first_volunteer.contents
        volunteer = ''.join([volunteer.encode('utf-8').strip() for volunteer in raw_volunteer])
        volunteer = re.sub('<br/>', ', ', volunteer)
        if not volunteer:
            volunteer = ''
            # print("Volunteer=BLANK")
    else:
         volunteer = ''
         # print("Volunteer=BLANK")

    # languages
    first_languages = soup.find('p', {'id': 'view_field_languages'})
    if first_languages:
        raw_languages = first_languages.contents
        languages = ''.join([languages.encode('utf-8').strip() for languages in raw_languages])
        languages = re.sub('<br/>', ', ', languages)
        if not languages:
            languages = ''
            # print("Volunteer=BLANK")
    else:
         languages = ''
         # print("Volunteer=BLANK")


    #
    #  SECOND Tab
    #

    source_code = requests.get(item_url + '&tab=2')
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    # Areas(geographies) served
    geoserved_cnty = ', '.join([p.text for p in soup.select('div#current_tab p span')])
    geoserved_cnty = geoserved_cnty[18:]
    geoserved_cnty = re.sub('\(NC\)', '', geoserved_cnty)
    geoserved_cnty = ' '.join(unique_list(geoserved_cnty.split()))
    geoserved_cnty = geoserved_cnty[3:]
    # print geoserved_cnty

    test = soup.findAll("div", {"class":"view_type_geoserved"})
    if test:
        # print "TRUE"
        # print soup.select("div.view_type_geoserved > table tr > td")
        geoserved_muni = ', '.join(td.get_text(strip=True) for td in soup.select("div.view_type_geoserved > table tr > td") if td.text)
        # print geoserved_muni
    else:
        geoserved_muni = ''
        # print "FALSE"

    #
    #  THIRD Tab
    #

    source_code = requests.get(item_url + '&tab=3')
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    # Primary Services
    first_services = soup.findAll('li', {'id': 'view_field_primaryServices'})

    services_lis = []
    for ul in first_services:
        for li in ul.findAll('p'):
            if li.find('ul'):
                break
            services_lis.append(li)

    services = ''.join([str(services.text.encode("utf-8")).strip() for services in services_lis])
    services = re.sub('\)', '), ', services)
    services = services[:-2]
    # print (services)

    #
    #  FOURTH Tab
    #

    url = item_url + '&tab=4'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    page.close()

    # print soup.prettify()
    if soup.find("p", id="view_field_phonesLabel"):
        phone_first = soup.find("p", id="view_field_phonesLabel")
        phone_list_raw = phone_first.find_next_sibling("div")

        phone_output = []
        for tr in phone_list_raw.findAll('tr'):
            stack = []
            for td in tr.findAll('td'):
                td = re.sub('<br/>', ', ', str(td), count=1)
                td = striphtml(td)
                # print type(td)
                stack.append('\'' + td + '\'')
            phone_output.append((','.join(stack)))

        phone_output = '"' + '","'.join(phone_output) + '"'
    else:
        phone_output = ''

    # print phone_output

    if soup.find("p", id="view_field_addressesLabel"):
        addr_first = soup.find("p", id="view_field_addressesLabel")
        addr_list_raw = addr_first.find_next_sibling("div")

        addr_output = []
        for tr in addr_list_raw.findAll('tr'):
             stack = []
             for td in tr.findAll('td'):
                 td = re.sub('<br/>', ', ', str(td), count=2)
                 td = striphtml(td)
                 # print type(td)
                 stack.append('\'' + td + '\'')
             addr_output.append((','.join(stack)))

        addr_output = '"' + '","'.join(addr_output) + '"'
    else:
        addr_output = ''

    # print addr_output

    if soup.find("p", id="view_field_contactsLabel"):
        contacts_first = soup.find("p", id="view_field_contactsLabel")
        contacts_list_raw = contacts_first.find_next_sibling("div")

        contacts_output = []
        for tr in contacts_list_raw.findAll('tr'):
             stack = []
             for td in tr.findAll('td'):
                 td = re.sub('<br/>', ' ', str(td), count=1)
                 td = re.sub('</p><p>', ', ', td)
                 td = striphtml(td)
                 # print type(td)
                 stack.append('\'' + td + '\'')
             contacts_output.append((','.join(stack)))

        contacts_output = '"' + '","'.join(contacts_output) + '"'
    else:
        contacts_output = ''

    # print contacts_output

    with open('details.csv', 'a') as detailfile:
        detailwriter = csv.writer(detailfile, delimiter=',', escapechar='"', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
        detailrow = [item_name, website_name, description, hours, intake, fees, eligibility, accessibility, volunteer, geoserved_cnty, geoserved_muni, services, languages, phone_output, addr_output, contacts_output]
        detailwriter.writerow(detailrow)


def plaintext(html):
    plain_text = html
    plain_text = re.sub('?<=font-size:1em">.*', '', plain_text)
    # plain_text = re.sub('#</li>#', '', plain_text)
    # plain_text = re.sub('#<(script|style)\b[^>]*>(.*?)</(script|style)>#is', '', plain_text)
    # plain_text = re.sub('#<br[^>]*?>#', " ", plain_text)

    return plain_text


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

def splitkeepsep(s, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[:-1] + elem] if elem == sep else acc + [elem], re.split("(%s)" % re.escape(sep), s), [])

nc211_spider(1846, 2049)

