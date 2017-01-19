#INVENTORY
inventory = []

#HEALTH POINTS
hp = 100

#ENEMY HEALTH POINTS
leonahp = 100

def dorm():
    #BACKSTORY
    print("""Diana wakes up in her dorm room in the Solari temple. It has been her only home since the beginnings of her memory.
    \n***
    \nDiana had no memory of her long-dead parents, who died in a frigid storm on the unforgiving slopes of Mount Targon.
They had travelled from a distant land, drawn by dreams of a mountain they had never seen and the promise of
revelation. Exhaustion and blinding stormwinds overwhelmed them on the eastern slopes of the mountain, and there,
beneath cold, pitiless moonlight, Diana came into the world as her mother breathed her last.
Hunters from Solari temple found her the next day wrapped in bearskin and cradled in the arms of her dead father.
She was brought to the temple where she was presented to the sun. The girl with the sable hair was raised as one of
the Solari, a faith that dominated the lands around Mount Targon. Diana became an initiate, and was raised to
venerate the sun in all its aspects. She learned the legends of the sun and trained every day with the Ra-Horak,
the warrior templars of the Solari.""")
    print("""\nBut all was not well.
    \nThe Solari elders taught that all life came from the sun, and that the light of the
moon was false, offering no nourishment and crafting shadows in which only creatures of darkness found succor. Yet
Diana found moonlight entrancing and beautiful in a way the harsh sun glaring down the mountain could never match.
As the years went by, Diana found herself ever at odds with the elders and their teachings. She couldn't help but
question all she was told, always suspecting there was more that went unsaid in every teaching, as though what she
was being taught was willfully incomplete. As she grew, Diana's sense of isolation only became stronger as childhood
friends distanced themselves from the mordant, questioning girl who never quite fit in.""")
    print("""\n***
    \nDiana takes in her surroundings as these thoughts slipped from her mind.
    \nThe moon is full tonight. A cold draft wafts in through the open window to the left, brushing the loose strands of
her sable hair to one side.
    \nDiana stands up, the moon calling to her. She can see for miles out of the window, the aging stone tower in which
the dorms were built providing a great view of the neighboring forest as well as the nearby village precariously perched
on the slopes of Mount Targon.
    \n'The moonflowers should be in full bloom tonight,' Diana thinks. 'I cannot bear this temple anymore. I must find
freedom. I must find truth.'""")
    #OPTIONS
    print("\nDiana can go back to BED")
    print("Diana can climb through the WINDOW")
    choice = raw_input("What next? BED or WINDOW: ")
    choice = str.lower(choice)
    if choice == "window":
        print("\nDiana climbs through the window.")
        ledge()
    elif choice == "bed":
        print("\nDiana goes back to bed. Sleep overcomes her and her eyelids grow heavy. Soon there is nothing but blackness...")
        print("Game Over")
    else:
        print("Invalid command")
        dorm()

def ledge():
    #STORY
    print """\nDiana finds herself perched on a small ledge barely a foot across extending towards the left. It is a 100
foot drop to the bottom."""
    #OPTIONS
    choice = raw_input("\nWhat next? RIGHT, LEFT, or FORWARD: ")
    choice = str.lower(choice)
    if choice == "right":
        print("\nDiana fell to her death.")
        print("Game Over: Diana DIED")
    elif choice == "left":
        window()
    elif choice == "forward":
        print("\nDiana fell to her death.")
        print("Game Over: Diana DIED")
    else:
        print("\nInvalid command")
        ledge()

def window():
    #STORY
    print("""\nPressing against the cool stone, Diana shuffles towards the left. She moves slowly, but deliberately, ensuring
she doesn't interrupt the slumber of her fellow initiates.
As she gets to the third window, Diana jerks to a halt. The soft, flickering light of a candle casts the windowsill in a
golden glow. There are two tall shadows on the far wall of the room, one is talking animatedly while the other patiently listens.
Diana holds her breath. This is the room of one of the elders. Diana curses. What are they doing up this late?
Straining her ears, Diana pieces together the conversation. It is about her. The elders are furious with her heretical
tendencies. They are considering taking drastic action that may result in her death.""")
    #OPTIONS
    print("\nDiana can WALK past the window")
    print("Diana can crouch and SNEAK past the window")
    choice = raw_input("What next? WALK or SNEAK: ")
    choice = str.lower(choice)
    if choice == "walk":
        print("""\nDiana shuffles across the window, hoping the elders will not see her. The room suddenly falls silent
and the candle is extinguished. Diana's heart sinks. She suddenly feels a strong grip around her waist and is violently
yanked into the room.""")
        print("Game Over: Diana was CAUGHT")
    elif choice == "sneak":
        print("""\nDiana hunches down into a ball and shuffles across, making sure the top of her head stays well beneath
        the windowsill.""")
        ladder()
    else:
        print("\nInvalid command")
        window()

def ladder():
    #STORY
    print("""\nDiana finds an spindly wooden ladder lying on its side against the ledge.""")
    while inventory.count('LADDER') == 0:
        inventory.append('LADDER')
    print "\nA LADDER has been added into Diana's inventory. INVENTORY:", inventory
    #OPTIONS
    print("Diana can use the LADDER to climb down the tower")
    print("Diana can JUMP down the tower")
    choice = raw_input("What next? LADDER or JUMP: ")
    choice = str.lower(choice)
    if choice == "ladder":
        print("""\nDiana picks up the ladder and slowly lowers it down. She is careful not to scrape the rough stone
walls of the tower for fear of waking somebody. She feels the solid thud of the ladder bumping the ground. Diana
gingerly places her right foot on topmost rung. So far so good, the precariously thin wood holds. She releases her breath and
shifts her whole weight onto the ladder. It sags a bit, just enough to make her heart race. Cold beads of sweat forms on
her brow. Wiping them away, Diana quickly scampers down the ladder.""")
        ground()
    elif choice == "jump":
        print("\nDiana fell to her death.")
        print("Game Over: Diana DIED")
    else:
        print("\nInvalid command")
        ladder()

def ground():
    #STORY
    print("""\nDiana makes it to the ground. She catches her breath, her heart pounding with a mixture of relief, excitement,
and the knowledge that she will be severely punished if caught.
'I cannot leave the ladder here,' Diana muses, 'What to do?'
As if on queue, the ladder glows with a faint silver light and quickly retracts on itself. The individual rungs merge with
each other with an alarming speed. The top of the ladder swiftly glides down to the ground in a silver blur. Soon, the ladder
resembles a one foot by one foot picture frame.
\nThe moon is high up in the velvet black sky. The faint dots of distant stars are drowned out by the pale silver glow of
the moon. The chirping of the crickets are the only sounds Diana can hear. Ah, finally. Freedom.
\nDiana's celebration is short-lived. She hears footsteps on the gravel ground coming from her left. Desperately, she looks
around for a place to hide.""")
    #OPTIONS
    print("\nDiana can HIDE in the shadow of a large rock")
    print("Diana can SPRINT across the gravel pathway and disappear into the FOREST")
    choice = raw_input("What next? HIDE or SPRINT: ")
    choice = str.lower(choice)
    if choice == "hide":
        print("""\nDiana throws herself behind a rock and curls into a ball.""")
        oldwomanwalkingpast()
    elif choice == "sprint":
        print("""\nDiana tenses up her body and sprints across the gravel path into the forest opposite the dorm tower.
To anyone looking outside their window, she looks much like a silvery comet hurtling into the dense trees.""")
        forest()
    else:
        print("\nInvalid command")
        ground()

def oldwomanwalkingpast():
    #STORY
    print("""\nThe footsteps grow closer and closer. With every crunch, Diana winces. Suddenly the footsteps stop. Diana's
heart is in her throat. She quickly runs through a list of possible excuses, but found she had none. Diana curses herself
for taking this chance on such a bright night. But the moon! The moon is too attractive. She waits to be discovered, but
nothing happens. Curious, Diana slowly peeks out from behind the rock. An elderly woman wearing a bearskin cloak stands hunched
over her carved staff of willow. She lifts her head up to the moon then lowers it again, looking left and right. She lingers next to the rock
Diana is hiding behind for a few more moments then trudges off. Diana breathes a sigh of relief.
'Who is she? I've never seen her before,' Diana wonders, 'she's definitely not a Solari elder and she doesn't look like
a villager.""")
    #OPTIONS
    print("\nDiana can FOLLOW the old woman to investigate")
    print("Diana can WAIT for her to pass then go into the forest")
    choice = raw_input("What next? FOLLOW or WAIT: ")
    choice = str.lower(choice)
    if choice == "follow":
        print("""\nDiana waits until the old woman is out of sight before following the gravel path. She makes sure to
stay on the grass, lest the old woman hear her.""")
        gates()
    elif choice == "wait":
        print("""\nDiana waits until the old woman is out of sight then emerges from behind the rock. She makes sure the
gravel path is clear then walks into the forest.""")
        forest()
    else:
        print("\nInvalid command")
        oldwomanwalkingpast()

def forest():
    #STORY
    print("""\nDiana finds herself in the forest. Surrounded by the dark, looming trees that tower into the night sky,
Diana feels alone. Not that she has a problem with being alone, she has been alone for her whole life. It comforts her.
The ethereal light of the full moon filtered down from the canopy, illuminating the ground in uneven silver patches.
Diana wanders towards the gurgling sound of a small spring.
'Moonflowers are in full bloom tonight,' Diana notes.""")
    while inventory.count('MOONFLOWER') == 0:
        inventory.append('MOONFLOWER')
    print "A MOONFLOWER has been added to Diana's inventory. INVENTORY:", inventory
    print("There is a path following the stream curving off into the distance towards the right. It leads back to the Solari temple.")
    #OPTIONS
    print("\nDiana can FOLLOW the path")
    choice = raw_input("What next? FOLLOW: ")
    choice = str.lower(choice)
    if choice == "follow":
        print("""\nDiana follows the path, soaking in the calm of the night. Bliss...""")
        gates()
    else:
        print("\nInvalid command")
        forest()

def gates():
    #STORY
    print("""\nDiana finds herself in the temple courtyard. She sees an old woman wrapped in a bearskin cloak leaning
against the gate, seemingly exhausted. Diana desperately tries to stay hidden, but the silver moonlight reveals all in
the otherwise barren courtyard. The woman suddenly turns her head at her direction. Diana is spotted.
She cursed herself for being so careless. The old woman shakily extends out her wizened arm and gestures Diana to come
over. With nowhere to run, Diana obliges.
'Diana, I've been expecting you,' the old woman says.""")
    #OPTIONS
    print("\nDiana can ASK,'Who are you?'")
    print("Diana can SAY,'I don't know what you're talking about.'")
    choice = raw_input("What next? ASK or SAY: ")
    choice = str.lower(choice)
    if choice == "ask":
        print("""\n'Who are you?', Diana demands.'""")
        ask()
    elif choice == "say":
        print("""\n''I don't know what you're talking about,' Diana says evasively.""")
        say()
    else:
        print("\nInvalid command")
        gates()

def ask():
    #STORY
    print("""\nThe old woman laughs, 'I am many things. I am the night, the moon. I am also the day, and the sun. I have
lived through many ages when both sides worked side by side vanquishing the dark forces of this world. This age though...
I am afraid this body is to frail to do any more work.'
'You are much like me,' the old woman continued, 'would you like to learn?'""")
    #OPTIONS
    print("\nDiana can say YES")
    print("Diana can say NO")
    choice = raw_input("What next? YES or NO: ")
    choice = str.lower(choice)
    if choice == "yes":
        print("""\n'Yes,' Diana replied eagerly.""")
        test()
    elif choice == "no":
        print("""\n'No,' Diana replied, frowning.""")
        reject()
    else:
        print("\nInvalid command")
        ask()

def say():
    #STORY
    print("""\nThe old woman laughs, 'You show extraordinary talents. You're different than everybody. You find guidance
in the moon while others look to the sun. I can teach you many things. Would you like to learn?'""")
    #OPTIONS
    print("\nDiana can say YES")
    print("Diana can say NO")
    choice = raw_input("What next? YES or NO: ")
    choice = str.lower(choice)
    if choice == "yes":
        print("""\n'Yes,' Diana replied eagerly.""")
        test()
    elif choice == "no":
        print("""\n'No,' Diana replied, frowning.""")
        reject()
    else:
        print("\nInvalid command")
        ask()

def test():
    #STORY
    print("""\nThe old woman smiled, 'To test your devotion, bring to me the orchid that blooms at night.'""")
    #OPTIONS
    print("\nDiana can GIVE the MOONFLOWER")
    print("Diana can WALK to the FOREST")
    choice = raw_input("What next? GIVE or WALK: ")
    choice = str.lower(choice)
    if choice == "give":
        if inventory.count('MOONFLOWER') == 1:
            print("""\nDiana reaches into her satchel and presents the old lady with a moonflower she picked in the forest.""")
            inventory.remove('MOONFLOWER')
            print "MOONFLOWER has been removed from Diana's inventory. INVENTORY:", inventory
            path()
        else:
            print "\nDiana does not have a MOONFLOWER in her inventory. She must find a MOONFLOWER. INVENTORY:", inventory
            test()
    elif choice == "walk":
        print("""\nDiana walks toward the forest. As she makes it to the treeline, she calls back to the old woman to
wait for her.""")
        forest()
    else:
        print("\nInvalid command")
        test()

def reject():
    #STORY
    print("""\nThe old woman seems saddened.
'You had great things in store for you,' said the woman.
With that, she disappears in a shimmering silver light. The only thing left was a bearskin cloak that lies crumpled on
the ground.
Diana hears rapid footsteps coming towards her. Solari elders! There is nowhere for her to hide.""")
    print("Game Over: Diana was CAUGHT")

def path():
    #STORY
    print("""\nThe old woman accepts the offering with two hands.
'Come with me,' the old woman says, 'I will lead you to enlightenment.'
She sets off on a narrow path that winds its way up to the summit of Mount Targon.
'We must reach the summit before morning,' says the old woman.
Diana knows this is utterly impossible, but she stays silent.
\nDiana's desire to follow the woman and climb the mountain wars with everything the Solari taught. The mountain is for
the worthy, and Diana has never felt worthy of anything. They climb for hours, above the clouds and into the chill air
where the moon and stars glitter like diamonds. Despite her age, the woman keeps climbing, urging Diana onwards when she
stumbles or when the air grows thin and cold.
\nThee path suddenly ends at a deep crevice. Diana can barely make out the faint silver outline of the thin winding path on
the opposite side. The crevice is too wide to jump across but there is a narrow jagged path cut by hand leading to the right.
'This is where Pantheon, the Celestial Aspect of War, demonstrated his strength in a fit of rage many aeons ago,' comments
the old woman. She looks far off into the distance, as if recalling an old memory.""")
    #OPTIONS
    print("\nDiana can use the LADDER to get across the crevice")
    print("Diana can take the PATH to the right")
    choice = raw_input("What next? LADDER or PATH: ")
    choice = str.lower(choice)
    if choice == "ladder":
        print("""\nDiana reaches into her satchel and takes out the ladder.
'Ah, good. So you've come prepared,' the old woman says.
Without being commanded, the ladder extends itself to the required length. Diana places it across the crevice, making
sure it is secure.
'In the old days, skilled Lunari craftsmen could create such artifacts. Now, the knowledge is lost.'
The old woman quickly strides across the ladder, displaying a surprising agility and youthfulness. Diana soon follows
after her on all fours, gripping the sides of the ladder tightly. Diana breathes a sigh a relief as soon as she makes it
to the other side.
There is a sudden rumbling. 'Another avalanche,' Diana thinks. Only this time, it sounds closer. Without further warning,
blocks of ice and snow crash into the crevice, right where Diana is moments ago. Diana curses. 'There goes the ladder...'""")
        inventory.remove('LADDER')
        print "LADDER has been removed from Diana's inventory. INVENTORY:", inventory
        summit(hp)
    elif choice == "path":
        print("""\nDiana walks towards the path. It is too narrow for two people to walk side by side. There is a sudden
rumbling. 'Another avalanche,' Diana thinks. Only this time, it sounds closer. Without further warning, blocks of ice and
snow crash into the crevice. The violent shaking of the mountain almost throws Diana off balance. The old woman extends
a hand to steady her. The warmth of her touch on Diana's shoulder provides Diana with newfound energy. They continue along
the path.""")
        wolves(hp)
    else:
        print("\nInvalid command")
        path()

def wolves(hp):
    #STORY
    print("""\nDiana and the old woman trudge along the crevice for hours, looking for something to let them across the
other side. Diana is growing more tired and weary. Constant guidance from the old woman keep her going.
There is a flicker of dark masses moving quickly in the distance coming towards the pair. Diana does not notice them
until the masses are almost upon them. Mountain wolves! The pack leader jumps at Diana's throat but she manages to duck
in the last second. Instead, the wolf crashes into Diana's chest. She is forced into the snow by the wolf. She struggles
to breathe, trying with all her strength to get the animal off her chest. The wolf's gnashing teeth narrowly misses her
ear. She shifts her body, trying to gain leverage to push the wolf into the crevice. It is hopeless. Diana desperately
grabs at the wolf's mane, anything, in an attempt to inflict damage, but her grip is weakening. The wolf snaps at her neck
but Diana manages to use her left arm to deflect. Even then, a searing pain races up the right side of her torso. Diana screams.
A dark pool of blood is forming. To Diana's horror, she realizes it is coming from a large gash on her right shoulder.
'So this is how I die,' Diana thinks.
She catches a brief glimpse of the old woman. She is looking up towards the moon, seemingly unaware of Diana's plight.
What is she doing? All of a sudden, a blinding pillar of silver fire shoots down from the sky, illuminating the entire
bloody scene. The old woman acts as a conduit for the silver fire, holding out her palms and directing it towards the wolf
on top of Diana. The animal is blasted off into the crevice. With their leader gone, the rest of the wolves flee with
their tails between their legs.
The old woman helps Diana up. Diana's shoulder is drenched in blood and the white and gold cloak she wears is in tatters.
Diana barely manages a small 'thank you'. She is in excruciating pain. It is as if liquid metal is being poured into her
shoulder. The old woman reaches into her pouch and offers Diana a green Rejuvenation Bead. Diana pops it into her mouth
and immediately the pain is numbed.
Diana and the old woman slowly trudge along the crevice. Diana shifts the bead around in her mouth until it is fully
dissolved. After what seemed like hours the pair arrive at a point where the crevice is barely narrow enough to jump across.""")
    while hp == 100:
        hp = hp - 75
    print "\nDiana has lost 75 HP. She is at", hp, "HP."
    #OPTIONS
    print("Diana can JUMP across the crevice")
    choice = raw_input("What next? JUMP: ")
    choice = str.lower(choice)
    if choice == "jump":
        print(""""\nDiana gathers all her strength and jumps across the crevice. There is a brief jabbing pain in her right "
shoulder. Diana screams in agony and collapses in the snow. She quickly picks herself back up and follows the old woman.""")
        summit(hp)
    else:
        print("\nInvalid command")
        wolves(hp)

def summit(hp):
    #STORY
    print("""\nAs the night wears on, Diana loses track of time as the stars wheel overhead and all but the mountain
fades from view. Together, Diana and the woman climb ever upwards and each time her steps falter, she drew strength from
the pale glow of the moon. Eventually Diana falls to her knees, exhausted and weary beyond imagining, her entire body
is strained to the limits of exhaustion. When Diana looks up, it is to see that somehow they reached the mountaintop, a
feat that should not be possible in a single night. The summit is wreathed in cascades of spectral illumination, veils
of brilliant light, spirals of vivid color and the glimmering ghost of a vast city of silver and gold hovering in the air.
'This is what it used to be,' says the old woman as she steps into the vista, 'step in and you shall be enlightened.'""")
    #OPTIONS
    print("\nDiana can REFUSE")
    print("Diana can ACCEPT")
    choice = raw_input("What next? REFUSE or ACCEPT: ")
    choice = str.lower(choice)
    if choice == "refuse":
        print("""\nDiana is overwhelmed by the imposing images that sear into her mind. She turns her head in terror and
refuses. The woman looks saddened.
'I thought you were the one...' says the old woman as she and the vistas fade from view.
There is nothing. All becomes dark. Diana is alone in the cold, barren mountaintop. Her body is broken.""")
        while hp == 25:
            print("Pain returns to Diana's shoulder and spreads to her entire body. She gasps and tries to lift herself up. She cannot.")
            break
        print("The stars... they're beautiful. That is all Diana can think of as the dark and cold take her.")
        print("Game Over: Diana DIED")
    elif choice == "accept":
        print("""\nLooking into the light, Diana sees the promise of the emptiness within her being filled, of acceptance
and the chance to be part of something greater than she can ever imagine. This is what Diana has been seeking all her
life without truly knowing it, and fresh vitality flows through her limbs as she rises to her feet. She takes a hesitant
step towards the incredible vista, her resolve growing stronger with every breath.
The light surges and Diana screams as it pours into her, a union with something vast and inhuman, impossibly ancient and
powerful. The sensation is painful, but also joyous - a moment or an eternity that is both revelatory and hallucinatory.
When the light fades, the sense of loss is an ache like nothing she knew before. Diana looks for the old woman, but she
too is gone. Only the bearskin cloak mantling Diana's shoulders suggest she had existed at all.""")
        cave(hp)
    else:
        print("\nInvalid command")
        summit(hp)

def cave(hp):
    #STORY
    print("""\nDiana stumbles down the mountain in a fugue state, oblivious to her surroundings, until she finds herself
before a cleft in the mountainside; a cave mouth that would have been invisible but for the moonlight shadows. Cold and
needing shelter for the night, Diana seeks refuge within the cave. Inside, the narrow cleft widens into the crumbling
ruin of what might once have been a temple or vast audience chamber. Its crumbling walls are painted in faded frescoes
depicting warriors of silver and gold fighting back to back against an unending host of grotesque monsters as the sky
rains comets of searing light.
At the center of the chamber stands a crescent sword and a suit of armor unlike any other; a mail shirt of spun silver
rings and wondrously crafted warplate of polished steel. Reflected in the gleam of the armor, Diana sees her once sable
hair is now purest white, and a rune shines on her forehead with incandescent light. This is Diana's moment of truth.
She can turn away from this destiny or choose to embrace it.""")
    #OPTIONS
    choice = raw_input("\nWhat next? ACCEPT: ")
    choice = str.lower(choice)
    if choice == "accept":
        print("""\nDiana reaches out, and as her fingers touches the cold steel of the armor, her mind explodes with images
of lives she had never lived, memories she had never experienced and sensations she had never known. Scraps of ancient
history rages like a blizzard in her mind; secret knowledge she but dimly grasps and innumerable futures scatter like
wind-blown dust.
When the visions fade, Diana sees she is now fully clad in the silver warplate, armor that fits her as though wrought
especially for her. Her mind is still afire with newly acquired knowledge, but much of it remains frustratingly out of
reach, like a picture half in shadow, half in light. She is still Diana, but she is also something more, something eternal.
Feeling vindicated with this new knowledge, Diana knows she must return to the Solari Temple and tell the elders what she
learned.
\nDiana's mind returns to the present. While she knows she must fulfil her duties and enlighten the Solari,
her curiosity takes over. She examines her surroundings more closely.""")
        accept(hp)
    else:
        print("\nInvalid command")
        cave(hp)

def accept(hp):
    #STORY
    while inventory.count('SWORD') == 0:
        inventory.append('SWORD')
        inventory.append('ARMOR')
        print "\nSWORD and ARMOR have been added into Diana's inventory. INVENTORY: ", inventory
    print("""\nThere are two massive arches at either end of the great chamber. Both are ornately embroidered
with silver and gold. The chambers beyond the arches are shrouded in a hazy darkness. The ceiling, of the chamber, though
crumbling, depicts the full cycle of the moon. It circles the rune of the Lunari, the same rune that now shines on Diana's
forehead. To Diana's back, the mouth of the cave opens up into the clear starry night.""")
    #OPTIONS
    print("\nDiana can go BACK to the Solari Temple")
    print("Diana can go explore the RIGHT arch")
    print("Diana can go explore the LEFT arch")
    choice = raw_input("What next? BACK or RIGHT or LEFT: ")
    choice = str.lower(choice)
    if choice == "back":
        if inventory.count('HEALTH POTION') == 1:
            print("""\nDiana walks out of the Lunari temple brimming with anger. 'The Solari... They will learn the truth,' Diana
vows.""")
        elif inventory.count('LICH BANE') == 1:
            print("""\nDiana walks out of the Lunari temple brimming with anger. 'The Solari... They will learn the truth,' Diana
vows.""")
        else:
            print("""\nDiana shakes her head. 'Not now,' she thinks. I cannot let my own selfishness take over. She promises
to retrace her path up the mountain and explore the rest of the Lunari Temple later. Duty calls. She rips her gaze from
the ornate paintings and embroidery that decorate the walls and marches towards the cave entrance.""")
        solaritemple(hp)
    elif choice == "right":
        print("""\nDiana walks around the pedestal from which she found the crescent sword and the suit of armor and
wanders towards the right, taking in the breathtaking size and beauty of the chamber.""")
        right(hp)
    elif choice == "left":
        print("""\nDiana wanders towards the left of the chamber, admiring the craftsmanship of the wall paintings and
soaking in the strangely familiar scenes.""")
        left(hp)
    else:
        print("\nInvalid command")
        accept(hp)

def right(hp):
    #STORY
    print("""\nDiana finds herself in a long hallway. The faded paintings depict more battles where Lunari and Solari
fight as one against the dark forces of the world. Her footsteps echo and the rune on her forehead casts a warm silver
glow on the walls. Everything feels alive. It is as if the very walls of the temple know her. They welcome her.
All of a sudden, Diana finds herself facing a wall. Dead end. Upon further inspection, Diana realizes that the temple
extends further. An ancient memory is conjured up in Diana's mind. It is not her own, but of a life from ages ago. In the
memory, the hallway is brightly lit with silver lamps and the paintings freshly painted. Superimposed on the large
crumbling wall that now faces Diana is a grand staircase of gold and silver leading up. Diana follows the staircase in
her vision and sees that it leads to a great chamber that shines a bright silver. Diana blinks and returns to the present.
She sees a small opening high up where the staircase used to lead. It is at least 30 feet up and there are no adequate
handholds which Diana can use to climb the wall.""")
    #OPTIONS
    print("\nDiana can use LADDER to climb")
    print("Diana can RETURN to the main chamber")
    choice = raw_input("What next? LADDER or RETURN: ")
    choice = str.lower(choice)
    if choice == "ladder":
        if inventory.count('LADDER') == 1:
            print("""\nDiana pulls out the ladder from her satchel. Without being commanded, the ladder extends to the
required length. Diana places the ladder against the bare wall, making sure it is secure. She quickly climbs up, surprised
at the freedom of movement offered by the silver armor that now adorns her.""")
            lichbane(hp)
        else:
            print "\nDiana does not have LADDER in her inventory", inventory
            right(hp)
    elif choice == "return":
        print("""\nDiana looks up at the monolithic wall. 'I'll come back later better prepared,' Diana promises to herself.
She turns, her armored back facing the wall, and strides back to the main chamber.""")
        accept(hp)
    else:
        print("\nInvalid command")
        right(hp)

def lichbane(hp):
    #STORY
    print("""\nDiana finds herself in a chamber. It is smaller than the main chamber but nonetheless grand. The paintings
turn more violent. It depicts a power struggle between the Solari and the Lunari. It all starts during the time of peace,
when the dark forces of the world were banished into another reality. The Solari elders, in their arrogance, turn away
a gift from the Lunari. The Solari start to isolate themselves, believing in the superiority of the sun. Another panel
shows a bloody scene of betrayal. It depicts the Solari elders turning on the Lunari and the ensuing battle.
There is a small altar in the middle of the chamber. On the altar is a small pendant of two crossed swords, one silver
one gold. A small inscription carved into the stone altar reads:
            The Lich's Bane - A gift from the Lunari to the Solari
    May the wearer be granted strength against those who seek to destroy
Diana reaches out towards the pendant and picks it up. The thin silver chain glimmers under the luminescence of the rune
on Diana's forehead. She reaches over her head and puts on the pendant.""")
    while inventory.count('LICH BANE') == 0:
        inventory.append('LICH BANE')
    print "LICH BANE has been added into Diana's inventory. Diana's attacks deal more damage. INVENTORY:", inventory
    #OPTIONS
    print("\nDiana can RETURN to the main chamber")
    choice = raw_input("What next? RETURN: ")
    choice = str.lower(choice)
    if choice == "return":
        print("""\nDiana takes one last look at the chamber then leaves. She is careful to retract the ladder and place
it back in her satchel. She strides back towards the main chamber.""")
        accept(hp)
    else:
        print("\nInvalid command")
        lichbane(hp)

def left(hp):
    #STORY
    print("""\nDiana finds herself in a smaller chamber than the one she left. The paintings on the wall depict the decline
of the Lunari. Unnlike the paintings in the larger chamber, these panels depict battles between the Solari and the Lunari.
The Solari are crushing Lunari forces and destroying Lunari relics. The last panel depicts the Lunari retreating to their
temple, setting up traps and barricading themselves in.
In the middle of the chamber there is a small bubbling fountain. Diana walks towards it. A faded silver plaque reads:
                    The Fountain of Life
    May those who drink its waters be blessed with health
Diana realizes that she is thirsty. She had not brought any water with her from the dormitory, not expecting to make this
long journey. Diana cups her hands and places in the fountain. Cool water washes over her hand, yet it creates a warm feeling
within her. She brings her hands towards her mouth and takes a sip. The water is strangely sweet. She feels a warmness spread
from her mouth to the rest of her body.""")
    while hp == 25:
        print("""Diana feels this warmness linger around her injured shoulder. The soreness slowly fades. Diana inspects
the wound and tests her arm. It is healed.""")
        break
    print("""On the side of the fountain is a small stoppered vial filled with water. Diana places it in her satchel. 'This
will be useful,' thinks Diana.""")
    if hp == 25:
        hp = hp + 70
        print "\nDiana has gained 70 HP. HP:", hp
    elif hp == 100:
        hp = hp + 50
        print "\nDiana has gained 50 HP. HP:", hp
    else:
        hp = hp
        print "\nDiana has regained health. HP:", hp
    while inventory.count('HEALTH POTION') == 0:
        inventory.append('HEALTH POTION')
    print "HEALTH POTION has been added into Diana's inventory. INVENTORY:", inventory
    #OPTIONS
    print("\nDiana can RETURN to the main chamber")
    choice = raw_input("What next? RETURN: ")
    choice = str.lower(choice)
    if choice == "return":
        print("""\nDiana takes one last look at the fountain then strides back to the main chamber, her sense of betrayal
by the Solari growing stronger with every step.""")
        accept(hp)
    else:
        print("\nInvalid command")
        left(hp)

def solaritemple(hp):
    #STORY
    print("""\nFeeling vindicated with this new knowledge, Diana makes her way unerringly towards the Solari Temple,
knowing she must tell the elders what she learned. She is met at the temple gates by Leona, the master of the Ra-Horak
and the Solari's greatest warrior. Diana is brought before the temple elders, who listen with mounting horror as she
recounts what she learned of the Lunari. When she finishes her tale, the elders immediately denounce her as a heretic,
a blasphemer and peddler of false gods. For such a heinous crime, only one punishment can suffice; death.
Diana, stunned by the stubborn ignorance of the elders, does not resist as she is seized by the Ra-Horak. She is dragged
towards the middle of the courtyard and chained onto a pole. The chains dig deep into her neck, it is difficult for her
to breathe. The Ra-Horak and elders form a circle around her. They draw out their ceremonial swords and advance as one.
The Ra-Horak and elders stop when their swords barely prick Diana's neck.
'Death comes to all blasphemers,' the elders intone as they swing their swords upwards.
Diana is appalled. How can the elders reject what is so patently true? How can they turn their back on revelations
brought from the very summit of the holy mountain? Her fury builds at their willful blindness. With a scream of
rage-fueled frustration, Diana unleashes blazing orbs of silver fire that whirl around her. The chains that hold Diana
to the pole melt in the heat and she leaps up. Diana picks up her sword and lashes out. Wherever her sword strikes, silver
fire burns with killing light. Again and again, Diana lashes out. When her fury ebbs, Diana sees the carnage she had wrought.
The elders and Ra-Horak lie dead. Only Leona is left.
Diana looks Leona in the eye and sees hurt.
'How could you do this?' Leona asks.
Diana's heart melts. Leona is the only one who has shown Diana friendship. She is a sister to her. In many ways, she
is like her. They bonded over their isolation. Leona had been isolated from other initiates due to her prestigious role as
the Radiant Dawn, the Solari's chosen one. Diana had been isolated due to her rebellious thoughts.
'I am sorry, sister,' Diana replies, her resolve hardening.
Leona is one of them, she too must be struck down.""")
    combat(hp, leonahp)

def combat(hp, leonahp):
    #COMBAT
    print "\nDiana's HP:", hp
    print "Leona's HP:", leonahp
    while leonahp > 0:
        if hp > 0:
            #COMBAT OPTION 1 - CRESCENT STRIKE
            print("\nDiana can use CRESCENT STRIKE")
            if inventory.count('LICH BANE') == 1:
                print("CRESCENT STRIKE does 28 damage")
            else:
                print("CRESCENT STRIKE does 20 damage")
            #COMBAT OPTION 2 - PALE CASCADE
            print("\nDiana can use PALE CASCADE")
            if inventory.count('LICH BANE') == 1:
                print("PALE CASCADE does 14 damage")
            else:
                print("PALE CASCADE does 10 damage")
            #COMBAT OPTION 3 - LUNAR RUSH
            print("\nDiana can use LUNAR RUSH")
            if inventory.count('LICH BANE') == 1:
                print("LUNAR RUSH does 42 damage")
            else:
                print("LUNAR RUSH does 30 damage")
            #COMBAT OPTION 4 - HEALTH POTION
            while inventory.count('HEALTH POTION') == 1:
                print("""\nDiana can use HEALTH POTION
HEALTH POTION heals for 25 HP""")
                break
            #INPUT CHOICE
            choice = raw_input("\nWhat next? ")
            choice = str.lower(choice)
            #CRESCENT STRIKE OUTCOMES
            if choice == "crescent strike":
                print("\nDiana swings her crescent blade at Leona. Silver fire streaks out from the tip and curves towards Leona. The flames engulf her.")
                if inventory.count('LICH BANE') == 1:
                    leonahp = leonahp - 28
                else:
                    leonahp = leonahp - 20
                if leonahp > 0:
                    print("""And yet Leona still stands. The flames dissipate, her golden armor gleams in the sun. Leona counterattacks, her blade striking
Diana's chestplate with a loud crash of metal hitting metal.""")
                    hp = hp - 30
                else:
                    print("""Leona screams in pain. She crumples to the ground, defeated. 'Why, sister?' Leona croaks, 'Why?' She repeats her plea again
and again, her voice growing fainter each time.""")
            #PALE CASCADE OUTCOMES
            elif choice == "pale cascade":
                print("""\nDiana channels her rage and calls on the moon's power. Blazing orbs of silver fire whirl around her, forming a protective barrier.
Diana sends the deadly orbs of fire streaking towards Leona. Each orb crashes against Leona's golden armor with a spectacular flash of bright white light.""")
                if inventory.count('LICH BANE') == 1:
                    leonahp = leonahp - 14
                else:
                    leonahp = leonahp - 10
                if leonahp > 0:
                    print("""Leona stays planted, seemingly unaffected by Diana's attack. Leona counterattacks, her blade penetrating Diana's protective
barrier. Though the barrier takes the brunt of the attack, Leona's blade nonetheless connects with Diana's gardbrace, knocking her backwards.""")
                    hp = hp - 5
                else:
                    print("""One of the orbs finds an chink in Leona's armor and punches through. Leona screams in pain. She crumples to the ground, defeated.
'Why, sister?' Leona croaks, 'Why?' She repeats her plea again and again, her voice growing fainter each time.""")
            #LUNAR RUSH OUTCOMES
            elif choice == "lunar rush":
                print("""\nDiana raises her crescent blade and calls on the strength of the moon. She leaps towards Leona in a bright silver blur, crashing
blade first, into Leona. The two women tumble backwards.""")
                if inventory.count('LICH BANE') == 1:
                    leonahp = leonahp - 42
                else:
                    leonahp = leonahp - 30
                if leonahp > 0:
                    print("""Leona ends up on top. She quickly springs to her feet and raises her sword. She brings it down in an executioners arc. Diana
sits up and raises her arms just in time, her gauntlets taking the full blow. The impact jars her to the bone.""")
                    hp = hp - 75
                else:
                    print("""\nLeona screams in pain. Diana looks down. She is surprised to see that her blade has punched through Leona's armor. There is blood
everywhere. Leona looks straight into Diana's eyes, pleading with her.
'Please,' Leona whispers, 'I am sorry I couldn't protect you from them. Sister... I am so sorry... This is all my fault.'
Diana stares at her, emotions of sadness, anger, and frustration roiling inside. She thinks back to the days when the elders punished her for her inquisitiveness.
No one else would talk to her. No one would look at her. No one except for Leona. Her presence gave Diana warmth. She loved her.
But she is one of them. She is the Radiant Dawn, the avatar of the sun. It is her, in one of her past lives, that ordered the slaughter of the Lunari. Diana's gaze
hardens. She pushes down on her blade.""")
            #HEALTH POTION OUTCOME
            elif choice == "health potion":
                if inventory.count('HEALTH POTION') == 1:
                    print("""\nDiana reaches into her satchel and takes out the small vial with water from the fountain. She quickly twists
off the stopper and gulps it down. Warmth spreads from her throat, down to her chest and abdomen. The heat spreads down
her extremities and ending in a tingling feeling in her fingertips and toes. Diana feels rejuvenated.""")
                    hp = hp + 25
                    inventory.remove('HEALTH POTION')
                    print("\nDiana has regained 25 HP")
                else:
                    print("\nInvalid command")
            else:
                print("\nInvalid command")
            #DISPLAYING HP AFTER COMBAT CHOICE
            if hp > 0:
                print "\nDiana's HP:", hp
            else:
                print "\nDiana's HP: 0"
            if leonahp > 0:
                print "Leona's HP:", leonahp
            else:
                print "Leona's HP: 0"
                end()
        else:
            print("""\nDiana screams in pain. She crumples to the ground, defeated. Leona walks to her side and crouches next to her.
'How could you do this?' Leona asks again, tears streaking down her face.
'The Lunari are real... the elders lied...' Diana croaks, her voice growing fainter.
Blackness overtakes Diana. She is so tired. She closes her eyes.
\nGame Over: Diana DIED""")
            break

def end():
    print("""\nDiana stands over Leona, tears streaking down her face. Leona lies on her back, her armor smoking as if fresh
from the forge. Appalled at what she had done, Diana flees the site of the massacre, escaping into the wilds of Mount
Targon as the Solari reel from the savagery of her attack.

***

Hunted by the warriors of the Ra-Horak, Diana now seeks to piece together the fragmentary memories of the Lunari hidden
within her mind. Driven by half-remembered truths and glimpses of ancient knowledge, Diana has only one truth to cling
to - that the Lunari and the Solari need not be foes, that there is a greater destiny for her than that of a simple
warrior. What her destiny might be is unknown, but Diana will find it, whatever the cost.""")

dorm()
