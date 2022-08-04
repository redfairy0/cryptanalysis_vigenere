### Взлом полиалфавитного шифра Виженера

#	Модифицированная функция поиска индекса совпадений

def IoM (text):
	Lx = 0
	n = len(text)
	for i in text:
		fi = text.count(i)
		p = (fi * (fi - 1))/(n * (n - 1))
		Lx += p**2
	return Lx

#	функция поиска индекса совпадений

def iom_lx (text):
	Lx = 0
	n = len(text)
	for i in range(26):
		ai = chr(i + 97)
		fi = text.count(ai)
		p = (fi * (fi - 1))
		Lx += p
	return Lx / (n * (n - 1))

#	Функция поиска индекса взаимных совпадений

def prob (text_x, text_y):
	mi = 0
	mx = len(text_x)
	my= len(text_y)
	for i in range(26):
	    fx = text_x.count(chr(i + 97))
	    fy = text_y.count(chr(i + 97))
	    mi += (fx * fy)
	return mi / (mx * my)


#	функция сдвига буквы алфавита на число вправо

def offset (text,s):
    ciph = ''
    for i in text:
        ciph += chr(((ord(i) + s - 97) % 26) + 97)
    return ciph

#	функция сдвига буквы алфавита на число влево

def reverse_offset (ciph,s):
    text = ''
    for i in ciph:
        text += chr(((ord(i) - s - 97) % 26) + 97)
    return text

#	функция подсчета индекса совпадений для строк

def prob_str (text_list, key_length, x_str):
	for i in range(key_length - 1):
		text_xy = text_list[i + 1]
		if x_str != i:
			print('Строка:', i + 1, 'Взаимный индекс', prob(text_list[0],text_list[i + 1]))
		else:
			print('Строка:', i + 1, 'Взаимный индекс -')

	return True




# Обозначим текст строкой
#text = 'dlcpmpcxuopjnsaeqcxxcnhccgpstrsslyjyzsjiejzlylirsgastfovukwdyvkepydiblcjosllerdmqdeyvfcbxgkvmerbwgbvbtsmyxhscibkqcdejmmnripnmqmxmcagdgflirgicxggzlcbejzlylircejlipdmqccqdikyrjiwusxaribkpnrezoxqkjrovqozcbejgspnwyxhqgmrmlccacbigxhgmerohziapsxgxkrrijoxrovmpxfogmbvcctmxhgxkyvtfkfcdmldlcmmnripdivd'
#text = 'helloworld'
#	искомый текст
#text = 'advertisementswanttopersuadeustobuyparticularproductshowdotheydoitletsimagineyourewatchingtvitsahoteveningyoufeelthirstyyouseeanadvertforarefreshingdrinkyouseepeoplelookingcoolandrelaxedyounoticethenameoftherefreshingdrinkbecauseyouthinkitcouldbeusefulforyoutosatisfyyourthirstadvertisersstudyhowpeoplelearnsothattheycanteachthemtorespondtotheiradvertisingtheywantustobeinterestedtotrysomethingandthentodoitagainthesearetheelementsoflearninginterestexperienceandrepetitionifanadvertcanachievethisitissuccessfulifanadvertworkswellthesametechniquecanbeusedtoadvertisedifferentthingssoforexampleinwinteriftheweatheriscoldandyouseeafamilyhavingawarmingcupofteaandfeelingcosyyoumaybeinterestedandnotethenameoftheteaherethesametechniqueisbeingusedaswiththecoolrefreshingdrinkifadvertisementsaretohelearnedthereisaneedforlotsofrepetitionbutadvertisershavetobecarefulbecausetoomuchrepetitioncanresultinconsumertirednessandthemessagemayfallondealearsconsumerslearntogeneralizefromwhattheyhavelearnedsoadvertiserssometimescopyahighlysuccessfulideathathasbeenwelllearnedbyconsumersforexamplethehighlysuccessfulwestonteacountryadvertisingfordifferentteahasledtodaewoocountryforautomobiledealersandcadburycountryforchocolatebars'
#	зашифрован ключом 'encrypt'
text = 'eqxvpibwrovlilanpkrdiieulysxyfvfzjrtntkgrnpntgpdwypvjfdphbvycnwsvvccilmzcxgcxcbwicltxpjzlvmzvvjywhxrxvlxgklqldtxpgjzphmclqlqtxeacuttkxsqiygxjegjfxgkqtzlzrshuvcexscnvjdhovpxadhpnpupteekguwdnrbvzatmlrprkthjgjvptyvruygczhekeiqxgnwjcnhygjzlzbxpqljsuihuvdjejbtpmjmsfckghyclqlpiameukysoievzqtkwfvlbnasjrvmeeiygrpclsgjrriailerlixepjkftfxbtvqehrqvfrwxmecuttkxvuzlvmlranycmyfvfztbrggichmiqvfrgrwbovrwbrtcebiaiavfbdbxnirgcmlruvygxxugvjtfiavjmueintegczmavvptlxrzgcgbiaevycwvrrvrxmmbpzdpgeqxvpiveactfxxzrvyghbxvujsrvifuwsabjnprbkxvgyfpzlarncrwxwnovrtvlakhstveadvshxhgqrbkxvgkjcsbjsgiccmxukeehlssqicmtqcnvgcpmavvpxyxugncpmlrtzqrhpqcebnhyfgvyutqvnpfpomairupkqvpxajissvvypghsgvjxgkpqjwnhyzcpztbrggichmiqcebchxrvycctqrqwrwxxrcycgxxugjybxxreylxjyrkjztbrtwjcstwjkkfiaipqfjgxjegjfxgkqtzlzbjnfmcgmmfgdccmwntvrdaiygrpcxhgjvptbwnpvcsysenfrhhjeggcibxvqezjmeqxvpibwrtjfpoigqscrtvrhljqxgnwjcihszwtfgxtrvzrxhrpceptlyyvzlrhrfwdcgmmegultlwnpurwxqrujyvxqnawyaesafvyaxeeutmclyzgiqaxeepkmvxrrtrjxsistfklaegvycnaeigccpkrrfjmpwzrtkghxvfufktmmzgjadicnjzewecfwtatlwswcgsxegjrrwtwogvllxpynvyggiqdpadgwhovphysegoybiprvycwbkunpqjvgrujdjearukmcminefscmvlcuttkxvuzlvysefzduxvrpkrttlnuccsmsqcvudhgbwergrjbtrsihqbdzjtwinnvphtrqerbqnvlefscmvlhfpraspqcyixfntj'

print('Длинна текста:',len(text))
print()
print('Текст:')
print()
print ('advertisementswanttopersuadeustobuyparticularproductshowdotheydoitletsimagineyourewatchingtvitsahoteveningyoufeelthirstyyouseeanadvertforarefreshingdrinkyouseepeoplelookingcoolandrelaxedyounoticethenameoftherefreshingdrinkbecauseyouthinkitcouldbeusefulforyoutosatisfyyourthirstadvertisersstudyhowpeoplelearnsothattheycanteachthemtorespondtotheiradvertisingtheywantustobeinterestedtotrysomethingandthentodoitagainthesearetheelementsoflearninginterestexperienceandrepetitionifanadvertcanachievethisitissuccessfulifanadvertworkswellthesametechniquecanbeusedtoadvertisedifferentthingssoforexampleinwinteriftheweatheriscoldandyouseeafamilyhavingawarmingcupofteaandfeelingcosyyoumaybeinterestedandnotethenameoftheteaherethesametechniqueisbeingusedaswiththecoolrefreshingdrinkifadvertisementsaretohelearnedthereisaneedforlotsofrepetitionbutadvertisershavetobecarefulbecausetoomuchrepetitioncanresultinconsumertirednessandthemessagemayfallondealearsconsumerslearntogeneralizefromwhattheyhavelearnedsoadvertiserssometimescopyahighlysuccessfulideathathasbeenwelllearnedbyconsumersforexamplethehighlysuccessfulwestonteacountryadvertisingfordifferentteahasledtodaewoocountryforautomobiledealersandcadburycountryforchocolatebars')
print()
print('Пусть будет ключ: encrypt')
print()
print('Шифротекст:')
print()
print (text)
print()

#	Поиск длинны ключа

iom_dict = {}
for t in range(len(text) // 2):
	siom = 0
	for i in range(t):
		xtext = text [i::t]
		if siom != IoM(xtext):
			siom += IoM(xtext) * (len(xtext)/t)
	iom_dict[siom] = t
	#	Вывод массива индексов совпадений для различных длинн ключа
	#print ('Длинна ключа = ', t, 'Индекс совпадений = ', siom)

#	Поиск длинны ключа по значению индекса совпадения
max_dict = max(iom_dict)
if iom_dict[max_dict] == 1:
	del iom_dict[max_dict]
max_dict = max(iom_dict)

#	Длинна ключа будет:
key_length = iom_dict[max_dict]
print('Длинна ключа = ', key_length)
print()
print()



###		Поиск ключа



#	Разбивка текста на строки зашифрованные отдельным символом ключа

text_list = []
for i in range(key_length):
	xi = text[i::key_length]
	text_list.append(xi)

#	Подсчёт и вывод индексов совпадений строк для проверки

#for i in range(key_length):
#	print(i,'-ая строка, ','Индекс совпадений = ', iom_lx(text_list[i]), 'Строка: ', text_list[i])
#	print()

print()


#	Поиск и вывод взаимных индексов совпадений строк

for i in range(key_length - 1):
	prob_str(text_list, key_length, i)
	print('\n')



input('Нажмите Enter для выхода\n')