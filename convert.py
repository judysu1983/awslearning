import csv

def get_language(name):
	try:
		start = name.index('(')
		end = name.index(')')
		return name[start+1:end]
	except ValueError:
		return ''

def no_lang_name(name):
	try:
		start = name.index('(')
		end = name.index(')')
		return name[0:start].strip()
	except ValueError:
		return name.strip()

course_by_id = {}
courses_by_norm_name = {}

with open('export-0329-PartnerDIG.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile, delimiter='|')

	for row in reader:
		course_name = row['name']
		course_id = row['idcourse']
		course_language = row['lang_code']
		norm_name = no_lang_name(course_name)
		course_by_id[course_id] = row
	
		if norm_name not in courses_by_norm_name:
			courses_by_norm_name[norm_name] = {}

		courses_by_norm_name[norm_name][course_language] = course_id

	#print(courses_by_norm_name['Amazon DynamoDB Service Introduction'])
	#print(courses_by_norm_name['AWS Cloud Development Kit'])

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
	fieldnames = ['skillbuilder_id','duration_in_seconds', 'tc_product_domain','code', 'skill_level', 'training_category', 'paid_content_flag', 'content_version','name',
	'english', 'french', 'german', 'indonesian', 'italian', 'japanese', 'korean', 'portuguese-br', 'simplified_chinese', 'spanish', 'spanish_latam', 'traditional_chinese', 'thai','vietnamese']

	writer = csv.DictWriter(csvfile, delimiter='|', fieldnames=fieldnames)
	writer.writeheader()

	no_english_count = 0;
	for name_norm in courses_by_norm_name:

		courses = courses_by_norm_name[name_norm]

		if 'english' not in courses:
			no_english_count += 1
			print(str(no_english_count) + ': no english course found for ' + name_norm)
			continue

		new_row = {}
		new_row['skillbuilder_id'] = course_by_id[courses['english']]['skillbuilder_id']
		new_row['duration_in_seconds'] = course_by_id[courses['english']]['duration_in_seconds']
		new_row['tc_product_domain'] = course_by_id[courses['english']]['tc_product_domain']
		new_row['code'] = course_by_id[courses['english']]['code']
		new_row['skill_level'] = course_by_id[courses['english']]['skill_level']
		new_row['training_category'] = course_by_id[courses['english']]['training_category']
		new_row['paid_content_flag'] = course_by_id[courses['english']]['paid_content_flag']
		new_row['content_version'] = course_by_id[courses['english']]['content_version']
		new_row['name'] = name_norm

		new_row['english'] = courses['english']

		if 'french' in courses:
			new_row['french'] = courses['french']
		else:
			new_row['french'] = ''

		if 'german' in courses:
			new_row['german'] = courses['german']
		else:
			new_row['german'] = ''

		if 'indonesian' in courses:
			new_row['indonesian'] = courses['indonesian']
		else:
			new_row['indonesian'] = ''

		if 'italian' in courses:
			new_row['italian'] = courses['italian']
		else:
			new_row['italian'] = ''

		if 'japanese' in courses:
			new_row['japanese'] = courses['japanese']
		else:
			new_row['japanese'] = ''

		if 'korean' in courses:
			new_row['korean'] = courses['korean']
		else:
			new_row['korean'] = ''

		if 'portuguese-br' in courses:
			new_row['portuguese-br'] = courses['portuguese-br']
		else:
			new_row['portuguese-br'] = ''

		if 'simplified_chinese' in courses:
			new_row['simplified_chinese'] = courses['simplified_chinese']
		else:
			new_row['simplified_chinese'] = ''

		if 'spanish' in courses:
			new_row['spanish'] = courses['spanish']
		else:
			new_row['spanish'] = ''

		if 'spanish_latam' in courses:
			new_row['spanish_latam'] = courses['spanish_latam']
		else:
			new_row['spanish_latam'] = ''

		if 'traditional_chinese' in courses:
			new_row['traditional_chinese'] = courses['traditional_chinese']
		else:
			new_row['traditional_chinese'] = ''

		if 'thai' in courses:
			new_row['thai'] = courses['thai']
		else:
			new_row['thai'] = ''

		if 'vietnamese' in courses:
			new_row['vietnamese'] = courses['vietnamese']
		else:
			new_row['vietnamese'] = ''

		writer.writerow(new_row)

