#!python3
# encoding:utf-8


'''
우수운 별명만들기
'''


def main():
    '''
        - 두개의 tuple ( first , last )에서 random으로 text를 추출후 조합
        - 조합한 닉네임에 만족할때 까지 계속 생성 및 질의
   '''
    import random

    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("a name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
             'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
             'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
             'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
             'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
             '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
             'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
             'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
             "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
             'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
             'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
             "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:
        nickName = ' '.join([random.choice(name) for name in [first, last]])
        retry = input("'{}' is godd nickname ??".format(nickName.strip()))
        if retry.lower() == 'y':
            break


def pig_latin():
    '''
   피그라틴
    - 자음으로 시작하는 영단어의 자음을 끝으로 이동 어미에 "ay"를 추가
    - 모음으로 싲가하는 단어는 어미에 "way"만 추가하면된다.

    단어를 입력하면 색인과 분할을 통하여 피그라틴을 반환하는 프로그램을 작성하라
   '''

    func = lambda x, y: x + y
    moSound = ['a', 'e', 'i', 'o', 'u']
    while True:
        word = input('input word:')
        pig_word = word[1:] + func(word[0], 'ay') if word[0] not in moSound else word + func('w', 'ay')
        print('input word : {} , pig_word : {}'.format(word, pig_word))

        ip = input('retry y/n:')
        if ip == 'n': break


if __name__ == '__main__':
    pig_latin()
