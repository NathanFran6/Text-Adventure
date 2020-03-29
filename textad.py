#! python3

#Waiting a little time before printing something
import time

#Start Functiuons

#Here's A Template Function
def chooseAnswer0():
    answer0=''
    while answer0.lower().strip() !='' and answer0.lower().strip() !='':
        answer0=input('''''')
        
    return answer0
#Input Vaildation to make sure they can't create a bug by typing something other than this.
def chooseAnswer():
    answer=''
    while answer.lower().strip() !='yes' and answer.lower().strip() !='no':
        answer = input('Would You like To Play (yes/no)')

    return answer
#Starting off 0 if choose yes
def chooseAnswer1():
    answer1=''
    while answer1.lower().strip() !='bike' and answer1.lower().strip() !='skateboard':
        answer1= input('''Ah! You are being chased by something! You need to go fast!\nShould you take the bike or the skateboard (bike/skateboard)''')

    return answer1
#Branches off 1 if choose Bike
def chooseAnswer11():
    answer11=''
    while answer11.lower().strip() !='right' and answer11.lower().strip() != 'left':
        answer11= input('''You see two paths. Quickly, you have to decide which path to go on! The left one is dark and looks like it goes down a cave. The right one goes up a hill and into sunlight.(left/right)''')

    return answer11
#Branches off 11 if choose right
def chooseAnswer112():
    answer112=''
    while answer112.lower().strip() !='pond' and answer112.lower().strip() !='path':
        answer112=input('''You head down the right path and up the hill and see a lagoon, with murky water. You also see the path continuing in a dark forest with weird sounds. Hurry! The thing is coming close! The pond looks like the btter option, as it has sunlight beyond the water. But looks and be decieving.(pond/path)''')
        
    return answer112
#Branches off 112 if choose path
def chooseAnswer1122():
    answer1122=''
    while answer1122.lower().strip() !='approach' and answer1122.lower().strip() !='continue':
        answer1122=input('''When  you enter the forest, you see a brightly colored bird, unlike any other you've seen, only in picture books. With purple and red feathers, and the head like all the colors just burst on top of it! It seems friendly, do you approach it? (approach/continue) ''')
        
    return answer1122
#Branches off 11 if choose left
def chooseAnswer111():
    answer111=''
    while answer111.lower().strip() !='graveyard' and answer111.lower().strip() !='shack':
        answer111=input('''You go down the path, and you see a graveyard with stones rolling over hills with what looks like miles on end. You need to hide somewhere, and the rough shrubbery is a perfect place to sneakily hide. But you also look to your left and see a run-down, dilapidated shack with a light coming out of it. You think someone might be in there to help you. Which one do you choose? (graveyard/shack)''')
        
    return answer111
#Branches off 111 if choose shack
def chooseAnswer1111():
    answer1111=''
    while answer1111.lower().strip() !='shovel' and answer1111.lower().strip() !='rope' and answer1111.lower().strip() !='both':
        answer1111=input('''You go into the shack, and see a single lightbulb, but no one in sight. You also see a table and two things on it. A shovel and a rope. They seem like they could help in someway. But you're not sure which one you should take. Hmmm...Wait...oh no, you hear the thing coming. Hurry up and choose! (rope/shovel) ''')
        
    return answer1111
#Branches off 1111 if choose shovel
def chooseAnswer11111():
    answer11111=''
    while answer11111.lower().strip() !='rocky' and answer11111.lower().strip() !='muddy':
        answer11111=input('''You grab the shovel, and hurry out of the shack, and see the mysterious thing. You use the shovel as a knife and hit the thing's leg. You can't get a clear look at their face, so you just run as the shovel won't hold them off for too long. Hurry! Should you take the rocky path with lots of roots and rocks, or the muddy path that is wet and murky.(rocky/muddy)''')
        
    return answer11111
#Branches off 11111 if choose rocky
def chooseAnswer0():
    answer0=''
    while answer0.lower().strip() !='' and answer0.lower().strip() !='':
        answer0=input('''''')
        
    return answer0
#Branches off 11111 if choose muddy
def chooseAnswer0():
    answer0=''
    while answer0.lower().strip() !='' and answer0.lower().strip() !='':
        answer0=input('''''')
        
    return answer0
#Branches off 1111 if choose rope
def chooseAnswer11112():
    answer11112=''
    while answer11112.lower().strip() !='talk' and answer11112.lower().strip() !='hill':
        answer11112=input('''You see it and tie the rope to its foot and rap it around a tree. Since it is tied up, you can decide to approachh it, or decide to run while you can.(talk/run''')
        
    return answer11112
#Branches off 11112 if choose talk
def chooseAnswer111121():
    answer111121=''
    while answer111121.lower().strip() !='undo' and answer111121.lower().strip() !='run':
        answer111121=input('''You start to undo the rope, but then you remember that looks can be decieving. Should you stop and go while you can, or should you give it a chance?(undo/run)''')
        
    return answer111121
#Branches off 111121 if chose Run
def chooseAnswer1111211():
    answer1111211=''
    while answer1111211.lower().strip() !='' and answer1111211.lower().strip() !='':
        answer1111211=input('''''')
        
    return answer1111211
#Branches off 1111 if choose hill
def chooseAnswer0():
    answer0=''
    while answer0.lower().strip() !='' and answer0.lower().strip() !='':
        answer0=input('''''')
        
    return answer0
#Branches off 111 if choose graveyard
def chooseAnswer1112():
    answer1112=''
    while answer1112.lower().strip() !='' and answer1112.lower().strip() !='':
        answer1112=input('''''')
        
    return answer1112
#Branches Off 1 if choose skateboard
def chooseAnswer12():
    answer12=''
    while answer12.lower().strip() !='sleep' and answer12.lower().strip() != 'awake':
        answer12= input('''Quickly you hop on your skateboard, heading for woods.\nYou settle for the night in the woods.\nYou see the mysterious thing that is search for you.\nDo you sleep or stay awake?(awake/sleep)''')

    return answer12
#Bracnhes off 12 if choose awake
def chooseAnswer122():
    answer122=''
    while answer122.lower().strip() !='sing' and answer122.lower().strip() !='continue':
        answer122=input('''You start on your journey again, coming across a sound, music. You don't know where it's coming from, but it is your favorite song. Do you choose to continue or sing(continue/sing)''')
    return answer122
#Branches off of 122 if choose continue
def chooseAnswer1222():
    answer1222=''
    while answer1222.lower().strip() !='continue' and answer1222.lower().strip() !='stop':
        answer1222=input('''As you go along in the forest, you come across a big sign saying,"American Isles". It looks like a run down amusement park, rides, concessions, and all of the other normal sights. Do you stop and look around or continue on your way, fearing danger in there.(stop/continue)''')
    return answer1222
#Branches off 12221 if choose stop
def chooseAnswer12221():
    answer12221=''
    while answer12221.lower().strip() !='' and answer12221.lower().strip() !='':
        answer12221=input('''''')
    return answer12221
#Branches off 1222 if choose continue
def chooseAnswer12222():
    answer12222=''
    while answer12222.lower().strip() !='' and answer12222.lower().strip() !='':
        answer12222=input('''''')
    return answer12222
#End Functions
#Starts of the Paths and If,Elif,Else Statements
#I assigned varibles to each function to store the call and not repeat it for the elif statements.
print('Developed By Nathan Francis...')
time.sleep(2)
print('Story By Lucy Bolton and Nathan Francis...')
time.sleep(2)
print('_____')
answer0=chooseAnswer()
if answer0=='yes':
    answer1=chooseAnswer1()
    if answer1=='bike':
        answer11=chooseAnswer11()
        if answer11=='left':
            answer111=chooseAnswer111()
            if answer111=='shack':
                answer1111=chooseAnswer1111()
                if answer1111=='both':
                    print('Congraulations! By thinking outside the box, you chose the rope and the shovel to tie the thing to the tree and hit them with a shovel. YOU WON')
                elif answer1111=='shovel':
                    answer11111=chooseAnswer11111
                    if answer11111=='rocky':
                        print('TBD')
                    elif answer11111=='muddy':
                        print('TBD')
                elif answer1111=='rope':
                    thing2=input('You hear the mysterious thing outside as you pick up the rope. As you go outside, you can see the thing. What is it?')
                    print('A '+thing+'!')
                    answer11111=chooseAnswer11111()
                    if answer11111=='talk':
                        looks=input('You approach the '+thing2+' and look at it. What do you notice?')
                        print('''The '''+looks+thing2+''' raises it's head and you ask it why it is chasing you. The '''+things2+' responds...')
                        print('I was left on earth a long time ago, and that blue pearl you are holding in your hands is the only thing that can show me my way back home. Please just undo the rope and give me the pearl so I can go home...please...')
                        answer111121=chooseAnswer111121()
                        if answer111121=='undo':
                            print('But looks ARE decieving! As soon as he gets untied, he grabs you and captures you! GAME END') 
                    elif answer11111=='hill':
                        print('TBD')
            elif answer111=='graveyard':
                print('You go into the graveyard to hide and you see some spooky gravestones. What do they say?')
                grave1=input()
                print('Wow! What is the next one?')
                grave2=input()
                print('''That's spooky! What's the finally one''')
                grave3=input()
                print(grave1+' and '+grave2+' and '+grave3+'''.Woah!''')
                time.sleep(2)
                print('You stay in the graveyard all night. Even sleeping...')
                time.sleep(2)
                print('When you wake up, you continue through the graveyard. You evantually go back on your path to hide and get back to your home. Where is your home?')
                home=input()
                print('Ahh...'+home+'.Home sweet Home.')
        elif answer11=='right':
            answer112=chooseAnswer112()
            if answer112 =='path':
                answer1122=chooseAnswer1122
                if answer1122=='approach':
                    print('TBD')
                elif answer1122=='continue':
                    print('TBD')
            elif answer112=='pond':
                print('You swim down the lagoon, and it is peaceful.')
                time.sleep(2)
                print('''Wait...oh no! The current is getting stronger and you can't fight. You try, and try, and try , and then...''')
                time.sleep(3)
                print('GAME')
                time.sleep(2)
                print('END')
                answer0
    elif answer1=='skateboard':
        answer12=chooseAnswer12()
        if answer12=='awake':
            print('You see the mysertious thing that is following you. What is it?')
            thing1=input()#Allows them to name things that's following them
            print('You see a '+thing+'!')
            time.sleep(2)#Wait before continuing with Path
            answer122=chooseAnswer122()
            if answer122=='sing':
                song=input('You recognize the song. What song is it?')
                print('You hear '+song+'. What a beautiful song.')
                time.sleep(2)
                print('Wait, oh no, the '+thing+' heard you and found you! GAME END.')
                answer0
            elif answer122=='continue':
                answer1222=chooseAnswer1222()
                if answer1222=='continue':
                    print('TBD')
                elif answer1222=='stop':
                    print('TBD')
        elif answer12=='sleep':
            time.sleep(3)
            print('You awake from your sleep and wake up to the thing finding you! GAME END.')
            answer0
else:
    print('Too Bad!')
