"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def first_alnum_substring(text: str) -> str:
    """Return all alphanumeric characters in text from the beginning up to the
    first non-alphanumeric character, or, if text does not contain any
    non-alphanumeric characters, up to the end of text."

    >>> first_alnum_substring('')
    ''
    >>> first_alnum_substring('IamIamIam')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!')
    'iamiamiam'
    >>> first_alnum_substring('IamIamIam!!andMore')
    'iamiamiam'
    >>> first_alnum_substring('$$$money')
    ''
    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'
    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []
    """
    
    b = ''
    result_mentions = []
    
    for a in range(len(text)):
        if text[a] == '@':
            b = first_alnum_substring(text[a + 1:])
            result_mentions.append(b)
    
    if result_mentions == ['']:
        return []
    
    return result_mentions

def extract_hashtags(text: str) -> List[str]:
    """Return a list of all hashtags in text, converted to lowercase, without
    duplicates included.
    
    >>> extract_hashtags('#qwe tweet #ASD hahahah #zxc')
    ['qwe', 'asd', 'zxc']
    >>> extract_hashtags('haha #Qwer hahaha #Qwer')
    ['qwer']
    >>> extract_hashtags('lalalala #qwe hahahha #qwe lalala #asd')
    ['qwe', 'asd']
    >>> extract_hashtags('#QWE lalala #qWe hehehehe #QWe')
    ['qwe']
    """
    
    c = ''
    result_hashtags = []
    
    for d in range(len(text)):
        if text[d] == '#':
            c = first_alnum_substring(text[d + 1:])
            if not c in result_hashtags:
                result_hashtags.append(c)
    
    if result_hashtags == ['']:
        return[]
    
    return result_hashtags
    
def find_words(text: str) -> List[str]:
    """Return the seperate words from the text.
    
    >>> find_words('#UofT Nick Frosst: Google Brain re-searcher by day, singer 
    @goodkidband by night!')
    ['nick', 'frosst', 'google',  'brain', 'researcher', 'by', 'day', 
    'singer', 'by', 'night']
    """
 
    e = ''
    new_text = ' ' + text + ' '
    result_wordslist = []
    g = ''
    h = 0
        
    for f in range(len(new_text) - 1):
        if new_text[f] == ' ':
            g = new_text[f + 1:]
            h = g.index(' ')
            e = g[:h]
            if e[0] != '@' and e[0] != '#':
                result_wordslist.append(first_alnum_substring(clean_word(e)))
    
    return result_wordslist

def count_words(text: str, words_times: Dict[str, int]) -> None:
    """Return the number of words in text. If a word is not the dictionary yet, 
    it should be added.
    
    >>> words = {'nick': 1, 'google': 1, 'by': 1}
    >>> count_words('#UofT Nick Frosst: Google Brain re-searcher by day, singer 
    @goodkidband by night!', words)
    >>> words
    {'nick': 2, 'google': 2, 'by': 3, 'frosst': 1, 'brain': 1, 'researcher': 1, 
    'day': 1, 'singer': 1, 'night': 1}
    """
    
    new_list = find_words(text)
    
    for i in range(len(new_list)):
        if new_list[i] in words_times:
            words_times[new_list[i]] = words_times[new_list[i]] + 1
        else:
            words_times[new_list[i]] = 1
    
def invert_dict(words_times: Dict[str, int]) -> Dict[int, List[str]]:
    """invert the keys and values of words_times.
    
    >>> invert_dict({'key': 2, 'words': 3, 'mind': 4, 'google': 3})
    {2: ['key'], 3: ['words', 'google'], 4: 'mind'}
    """
    
    result_dict = {}
    
    for words in words_times:
        times = words_times[words]
        
        if not (times in result_dict):
            result_dict[times] = [words]
        else:
            result_dict[times].append(words)
        
    return result_dict
            
   
def common_words(words_times: Dict[str, int], words_num: int) -> None:
    """Keep no more than words_number words in the words_times. If after 
    adding the number of tie words , the number is over words_number, 
    delet all tie words.
    
    >>> words = {'key': 2, 'words': 3, 'mind': 4, 'google': 3}
    >>> common_words(words, 1)
    >>> words
    {'mind': 4}
    >>> common_words(words, 3)
    >>> words
    {'words': 3, 'mind': 4, 'google': 3}
    >>> common_words(words, 2)
    >>> words
    {'mind': 4}
    """
    
    new_dict = invert_dict(words_times)
    h = []
    
    for j in new_dict:
        h.append(j)
    
    h.sort()
    h.reverse()
    
    m = 0
    n = []  #the list of words will in the new dict
    o = []  #the list of num whose words will in the new dict
    while m < len(h) and len(n) < words_num:
        n.extend(new_dict[h[m]])
        o.append(h[m])
        m = m + 1
    
    if len(n) > words_num:
        o.pop(-1)
    
    p = []
    for num in o:
        p.extend(new_dict[num])
    
    
    nnew_list = []
    for q in words_times:
        if q not in p:
            nnew_list.append(q)
    for it in nnew_list:
        del words_times[it]
         

def read_tweets(file_name: TextIO) -> Dict[str, List[tuple]]:
    """Return the context of file_name into dictionary. The key will be the user
    name and write other information in the list of tuple.
    """
    
    #find the username and manage them into str
    big_users = []
    users = []
    text_list1 = []
    text_list2 = []
    date_list1 = []
    date_list2 = []
    source_list2 = []
    favourite_list1 = []
    retweet_list2 = []
    source_list1 = []
    favourite_list2 = []
    retweet_list1 = []
    fline = 0
    index_b = 0
    index_a = 0
    text0 = ''
    tweets = {}
    tuple1 = ()
    tuple_list = []
    file_list = []
    
    for lines in file_name:
        file_list.append(lines)
    for line in range(len(file_list)):
        if len(file_list[line]) >= 2 and file_list[line][-2] == ':':
            big_users = file_list[line][:-2].lower()
            users.append(big_users)
            fline = line + 1
            while fline < len(file_list) and len(file_list[fline]) >= 2 and file_list[fline][-2] != ':':
                if file_list[fline][:13].isdigit():
                    date_list1.append(int(file_list[fline][0:14]))
                    index_b = file_list[fline][15:].index(',') + 15
                    index_a = file_list[fline][index_b + 1:].index(',') + index_b + 1
                    source_list1.append(file_list[fline][index_b + 1:index_a])
                    index_b = file_list[fline][index_a + 1:].index(',') + index_a + 1
                    favourite_list1.append(int(float(file_list[fline]
                                                     [index_a + 1:index_b])))
                    retweet_list1.append(int(float(file_list[fline]
                                                   [index_b + 1:])))
                    fline = fline + 1
                    while fline < len(file_list) and '<<<EOT' not in file_list[fline]:
                        text0 = text0 + file_list[fline].rstrip()
                        fline = fline + 1 
                    text_list1.append(text0)
                    text0 = ''
                fline = fline + 1
            text_list2.append(text_list1)
            text_list1 = []
            date_list2.append(date_list1)
            date_list1 = []
            source_list2.append(source_list1)
            source_list1 = []
            favourite_list2.append(favourite_list1)
            favourite_list1 = []
            retweet_list2.append(retweet_list1)
            retweet_list1 = []            
    for zz in range(len(users)):
        for xx in range(len(text_list2[zz])):
            tuple1 = (text_list2[zz][xx], date_list2[zz][xx], 
                      source_list2[zz][xx], favourite_list2[zz][xx], 
                      retweet_list2[zz][xx])
            tuple_list.append(tuple1)
        tweets[users[zz]] = tuple_list
        tuple_list = []
    
    return tweets
   
    
def most_popular(tweets: Dict[str, List[tuple]], first_date: int, 
                 last_date: int) -> str:
    """Return the username of the most popular tweet which between the first 
    date and the last date. The first date and the last date are inclusive. If
    there is no tweet between the dates or the number of the favourable are tie,
    just return the string 'tie'.
    
    Precondition: first_date and last_date should be an int with 14 digits.
    
    >>> most_popular({'uoftcompsci': [('hahahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha', 20181105091933, 'Twitter for Android', 3, 8)]}, 
    20181031211000, 20181231091100)
    'uoft'
    >>> most_popular({'uoftcompsci': [('hahahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha', 20181105091933, 'Twitter for Android', 2, 8)]}, 
    20181031211000, 20181231091100)
    'tie'
    >>> most_popular({'uoftcompsci': [('hahahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha', 20181105091933, 'Twitter for Android', 2, 8)]}, 
    20181031211000, 20181106091100)
    'uoft'
    >>> most_popular({'uoftcompsci': [('hahahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha', 20181105091933, 'Twitter for Android', 2, 8)]}, 
    20180131211000, 20180106091100)
    'tie'
    """
    
    num1 = 0
    mostlove = []
    list1 = []
    list2 = []
    user1 = []
    favourite_user = []
    
    for r in tweets:
        for s in tweets[r]:
            if first_date <= s[1] <= last_date:
                num1 = s[3] + s[4]
                list1.append(num1)
        list1.sort()
        if len(list1) >= 1:
            list2.append(list1[-1])
        list1 = []
                
    if list2 == []:
        return 'tie'
    for u in range(len(list2)):
        if list2[u] == max(list2):
            mostlove.append(u)
    if len(mostlove) > 1:
        return 'tie'
    for v in tweets:
        user1.append(v)
    favourite_user = user1[mostlove[0]]
    return favourite_user              
        
def find_hashtags(tweets: Dict[str, List[tuple]], username: str) -> List[str]:   
    """Retrun the hashtags which the user use.
    
    >>> find_hashtags({'uoftcompsci': [('#hah ahaha #has', 20181103091833, 
    'Twitter for Android', 3, 1), ('hahaha #has', 20181107051833, 'Twitter for 
    Android', 7, 3)], 'uoft': [('haha #1', 20181105091933, 'Twitter for 
    Android', 3, 8)]}, 'uoftcompsci')
    ["#hah', '#has']    
    """
    #text2 = ''
    #num2 = 0
    tag = ''
    tag_list = []
    new_username = username.lower()
    
    tweets1 = tweets[new_username]
    for w in tweets1:
        tag = extract_hashtags(w[0])
        if tag[0] not in tag_list:
            tag_list.extend(tag)
        tag = ''
    
    return tag_list
              
    
def detect_author(tweets: Dict[str, List[tuple]], aim_word: str) -> str:
    """Retrun the more like username in the tweets dictionary who write about 
    the aim_word. If there are more that one person use the hashtag, return the
    string 'unknown'.
    
    >>> detect_author({'uoftcompsci': [('#hah ahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha #has', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha #1 lalala #hah', 20181105091933, 'Twitter for
    Android', 3, 8)]}, '#1 lala')
    'uoft'
    >>> detect_author({'uoftcompsci': [('#hah ahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha #has', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha #1 lalala #hah', 20181105091933, 'Twitter for
    Android', 3, 8)]}, '#3')
    'unknown'
    >>> detect_author({'uoftcompsci': [('#hah ahaha', 20181103091833, 'Twitter 
    for Android', 3, 1), ('hahaha #has', 20181107051833, 'Twitter for Android', 
    7, 3)], 'uoft': [('haha #1 lalala #hah', 20181105091933, 'Twitter for
    Android', 3, 8)]}, '#hah kjdfhi'
    'unknown'
    
    """
    
    aim_user = []
    text_tag = []
    find_tag = []
    
    text_tag.extend(extract_hashtags(aim_word))
    if len(text_tag) == 0:
        return 'unknown'
    
    for x in tweets:
        for y in text_tag:
            if y in find_hashtags(tweets, x):
                aim_user.append(x)
                find_tag.append(y)
        find_tag = []
        if x in aim_user and find_tag != text_tag:
            aim_user.remove(x)
    
    if len(aim_user) == 1:
        return aim_user[0]
    else:
        return 'unknown'
    
            

        
        

        
if __name__ == '__main__':
    pass

