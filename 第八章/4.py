# 随机出35份试卷， 且保留35份试卷的答案
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# capitals 是 国家：首都 的字典

capitals_item = list(capitals.items())
print(capitals_item)

def create_qz():
    for i in range(35):
        # 打乱次序
        random.shuffle(capitals_item)

        filename_qz = '第' + str(i) + '份试卷.txt'
        pf_qz = open(filename_qz, 'w')

        filename_aw = '第' + str(i) + '份答案.txt'
        pf_aw = open(filename_aw, 'w')

 
        for i in range(len(capitals_item)):
            pf_qz.write('%s. What is the capital of %s?\n' % (i, capitals_item[i][0]))
            # print('%s. What is the capital of %s?\n' % (i, capitals_item[i][0]))

            abcd = ['A','B','C','D']  
            random.shuffle(abcd)
            
            incorrent = []
            ansower_list = []

            for index in range(len(abcd)):
                if index == 0:
                    incorrent.append(i)
                    ansower_list.append('%s: %s' % (abcd[index], capitals_item[i][1]))
                    pf_aw.write('%s: %s' % (abcd[index], capitals_item[i][1])+ '\n')
                else:
                    ca_index = random.randint(0, 49)
                    while ca_index in incorrent:
                        ca_index = random.randint(0, 49)
                    incorrent.append(ca_index)
                    ansower_list.append('%s: %s' % (abcd[index], capitals_item[ca_index][1]))
            ansower_list.sort()
            # print('\n'.join(ansower_list))
            # print('')
            pf_qz.write('\n'.join(ansower_list) + '\n\n')

            
            
    pf_aw.close()
    pf_qz.close()

create_qz()