
user_dict = {'name': 'Dmitry',
             'id': 33112244,
             'surname': 'Yakovemko',
             'birthdate': '31.05.1990',
             'email': '@gmail.com',
             'phone': {'vodafone': '+390951111111'}}
level = 0

user_dict['level'] = level

word = 'a'.lower()

beginner = ['Family is close relatives',
            'He and his family are very funny',
            'You mought call me captain']
elementary = ["Fifteen men on the dead man's chest—" +
              " Yo-ho-ho,and a bottle of rum!",
              'I come from a large family- I have three' +
              ' brothers and two sisters',
              'I remember him looking round the cover' +
              'and whistling to himself as he did so, and' +
              'then breaking out in that old sea-song that' +
              'he sang so often afterwards']
pre_intermediate = ['Then he rapped on the door with a bit' +
                    'of stick like a handspike that he carried,' +
                    ' and when my father appeared, called roughly' +
                    'for a glass of rum',
                    'She values her job above her family',
                    'Much company, mate?']
intermediate = ['This, when it was brought to him, he drank slowly,' +
                'like a connoisseur, lingering on the taste and still' +
                'looking about him at the cliffs and up at our signboard',
                'My dad died when we were small so my mum raised the' +
                ' family on her own',
                'My father told him no, very little company,' +
                'the more was the pity']
upper_intermediate = ['And altogether I paid pretty dear for my monthly' +
                      'fourpenny piece, in the shape of' +
                      'these abominable fancies',
                      "Peter's success at college delighted his family",
                      'And indeed bad as his clothes were and coarsely' +
                      'as he spoke, he had none of the appearance of a' +
                      'man who sailed before the mast, but seemed like' +
                      'a mate or skipper accustomed to' +
                      'be obeyed or to strike']
advanced = ['Family it is a society of bees, consisting of worker bees,' +
            'a queen and drones',
            'Only in a small proportion of cases were referrals' +
            'made purely on grounds of existing illness in' +
            'patient or family',
            "At first we thought it was the want of company" +
            "of his own kind that made him ask this question," +
            "but at last we began to see he was desirous to avoid them."]
proficiency = ['Family is a group of animals, birds, consisting' +
               ' of a male,female and cubs,as well as a separate group' +
               ' of some animals or plants of the same species',
               'All day he hung round the cove or upon the' +
               ' cliffs with a brass telescope; all evening he' +
               'sat in a corner of the parlour next the fire and' +
               'drank rum and water very strong',
               'Dishes and spoons are not usually classified as' +
               'art works, and yet seem to belong to the same family']

sentence_list = [{"level": 0,
                  "text": beginner},
                 {"level": 1,
                  "text": elementary},
                 {"level": 2,
                  "text": pre_intermediate},
                 {"level": 3,
                  "text": intermediate},
                 {"level": 4,
                  "text": upper_intermediate},
                 {"level": 5,
                  "text": advanced},
                 {"level": 6,
                  "text": proficiency}]

message = {'user': user_dict,
           'message_text': word}


def find_by_level():
    for sentence in sentence_list:
        if message.get("user").get("level") == sentence.get("level"):
            return sentence

def filter_by_word(sentence):
    message_text = []
    for maches_word in sentence().get('text'):
        if message.get('message_text') in maches_word.lower():
            message_text.append(maches_word)
    return message_text

def merge_text():
    filtered_by_words = filter_by_word(find_by_level) 
    result_message = ""
    if not filtered_by_words:
        result_message = 'Not found'
    if len(filtered_by_words) >= 1:
        result_message = "...\n".join(filtered_by_words) 
    return result_message
