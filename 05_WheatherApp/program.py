import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
																			 'location, temperature, s_temperature, conditions, people_condition')
def main():
	print_the_header()
	x = True
	while x:
		city = input('\nВведіть українське місто (Львів, Київ, Одеса) або ви(х)ід: ')
		if city == 'х':
			break
		else:
			city = city.lower().strip()

			html = get_html_from_web(city)
			report = get_weather_from_html(html)

			print('{} зараз: {} \n \t {} \n{} \n \n {}'.format(report.location,
																												 report.temperature,
																												 report.s_temperature,
																												 report.conditions,
																												 report.people_condition))




def print_the_header():
	print('\n----------------------------')
	print('          Погоднік')
	print('----------------------------')
	print('-----pwr-by-sinoptik.ua-----')
	print('----------------------------')



def get_html_from_web(city):
	url = 'https://ua.sinoptik.ua/погода-{}'.format(city)
	response = requests.get(url)
	# print(response.status_code)
	# print(response.text[0:500])
	return response.text

def get_weather_from_html(html):
	# cityCss = 'div#header h1'
	# TempCss = 'div#blockDays .today-temp'
	# DescCss = 'div#blockDays .description'

	soup = bs4.BeautifulSoup(html, 'html.parser')
	loc = soup.find(id='header').find('h1').get_text()
	condition = soup.find(id='blockDays').find(class_='description').get_text()
	p_cond = soup.select_one('#bd1c>.oDescription>.rSide>.description').get_text()
	s_temp = soup.find(id='blockDays').find(class_='temperature').get_text()
	temp = soup.find(id='blockDays').find(class_='today-temp').get_text()

	loc = cleanup_text(loc)
	# loc = find_city(loc)
	cond = cleanup_text(condition)
	p_cond = cleanup_text(p_cond)
	s_temp = cleanup_text(s_temp)
	temp = cleanup_text(temp)
	# print(n_condition)
	# print('{} зараз: {} \n \t {} \n{}'.format(loc,temp,s_temp,condition))
	# return loc, temp, s_temp, condition
	report = WeatherReport(location=loc, temperature=temp, s_temperature=s_temp, conditions=cond, people_condition=p_cond )
	return report

def find_city(loc: str):
	parts = loc.split(' ')
	return parts[2].strip()


def cleanup_text(text: str):
	if not text:
		return text

	text = text.strip()
	return text

if __name__ == '__main__':
	main()




