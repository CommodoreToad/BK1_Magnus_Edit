BK1 MagnusEdit v1.0

Instructions
------------

This tool will allow you to edit any non-quest Magnus stat and the age time for any quest Magnus that already ages. This bundle includes the original python 3 script and an executable built in 64 bit Windows. 
Either can be used, but python will need to be installed along with the UnityPy module for the py script.

PLEASE FOLLOW ALL INSTRUCTIONS TO AVOID DAMAGING YOUR GAME. THERE ARE CURRENTLY VERY LITTLE GUARD RAILS FROM MISTAKES. MAKE A SAVE FOR YOUR GAME BEFORE EDITING ANY FILES AND USE THIS TOOL AT YOUR OWN RISK.


First Time Requirements
1) Copy '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\GameAssembly.dll' to '\BK1MagnusEdit\Backup'
2) Copy '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\Batenkaitos_Data\StreamingAssets\aa\StandaloneWindows64\b29e1677d0e548f3b74e980a7fb8b638.bundle to '\BK1MagnusEdit\Backup'

'\BK1MagnusEdit\Backup' contains the original data, and you can use these files to restore your game to its original state in case something goes wrong. This folder also contains a copy of 'magnus_stats.csv'. DO NOT MOVE THIS FILE. 
You can use this file to reset your game to its original state.

Changing Magnus Parameters
1) All of the Magnus parameters are located in '\BK1MagnusEdit\magnus_stats.csv'. This file can easily be edited in a spreadsheet application. 
2) DO NOT DELETE ANY ROW OR COLUMN
3) The "Magnus Number" and "Magnus Name" columns are for informational purposes only. Do not edit these.
4) Any change must be a WHOLE NUMBER. Negative numbers may have unexpected behavior. Do not use excessively large values for that column, you may exceed the variable size.
5) The only thing you can change for quest Magnus is the age time for Magnus that already age. Any other changes will be ignored.
6) Save the csv file when you are done.

Patching the Game Files
1) Run MagnusEdit.exe or MagnusEdit.py. This should complete in the background in about 20 seconds.
2) ENSURE YOU HAVE ORIGINAL BACKUPS OF YOUR DLL AND BUNDLE FILE
3) Copy the dll in '\BK1MagnusEdit\Output\' and overwrite '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\GameAssembly.dll'
4) Copy the bundle in '\BK1MagnusEdit\Output\' and overwrite '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\Batenkaitos_Data\StreamingAssets\aa\StandaloneWindows64\b29e1677d0e548f3b74e980a7fb8b638.bundle
5) Start the game!


Magnus Parameters
-----------------

NOTE: For Quest Magnus, every parameter will be ignored except for time change.

Level- Level of the Magnus. It is unknown what this directly does but probably affects the battle dialogue.

Status- How the Magnus is used in game. These numbers are "weird" because they are binary combinations of flags. The flags are as follows:

	Bit	Flag
	1 to 7	Not used
	8	Cannot be used on ally
	9	Must be used after same element
	10	Can be used with yell/aura
	11	Can't be sold/thrown away
	12	Can equip
	13	Camp item
	14	Can use to defend
	15	Can use to attack
	16	Can be added to deck

	This is the list of numbers used in game

	57984- Add to deck, attack, defend, use with yell/aura, cannot use on ally. 					Example- Most swords and paddles
	49792- Add to deck, attack, use with yell/aura, cannot use on ally. 						Example- Most other character weapons
	41600- Add to deck, defend, use with yell/aura, cannot use on ally. 						Example- Most armors
	58240- Add to deck, attack, defend, use with yell/aura, must be used after same element, cannot use on ally. 	Example- All yells
	50176- Add to deck, attack, can't be sold/thrown away. 								Example- Broken earth sphere, escape, cameras
	58368- Add to deck, attack, defend, can't be sold/thrown away. 							Example- Sword of the Heavens
	50816- Add to deck, attack, can't be sold/thrown away. 								Example- Broken Sword of the Heavens  
	49152- Add to deck, attack. 											Example- Many miscellaneous battle Magnus, pass
	49280- Add to deck, attack, cannot use on ally. 								Example- Many miscellaneous battle Magnus, voices
	16512- Attack, cannot use on ally. 										Example Spirit finishers
	41344- Add to deck, defend, Must be used after same element, cannot use on ally. 				Example- Auras 
	1024-  Can't be sold/thrown away. 										Example- Class up items, constellations, quest Magnus
	2048-  Can equip, can't be sold/thrown away. 									Example- Equip items
	4096-  Camp item. 												Example- All camp items
	57344- Add to deck, attack, defend. 										Example- Many miscellaneous battle Magnus
	40960- Add to deck, defend. 											Example Magic beans, some other battle Magnus
	49664- Add to deck, attack, can be used with yell/aura. 							Example- Many miscellaneous battle Magnus
	57472- Add to deck, attack, defend, cannot use on ally. 							Example- A few miscellaneous battle Magnus

Price- Cost to buy. The sell price is the price/100 rounded down, with the minimum price 1 G.

Time Change- The time the Magnus will age in seconds. A time of 0 will not age. 

Magnus Change- Magnus change number. A value of 0 will age the Magnus into nothing.

Combo Cat- Magnus SP combo category. There are probably 4 levels of each category for 1-100, but I am listing only the ones that are used.  
	   In general you can use a higher level for a lower level SP combo unless that higher level is required for a different SP combo.

	0	None
	4	Fire 1- Only for recipes
	5	Fire 2
	6	Fire 3
	7	Fire 4
	8	Water 1- Only for recipes
	9	Water 2
	10	Water 3
	11	Water 4
	12	Light 1
	13	Light 2
	14	Light 3
	15	Light 4
	16	Dark 1
	17	Dark 2
	18	Dark 3
	19	Dark 4
	21	Chronos 1
	22	Chronos 2
	23	Chronos 3
	25	Wind 1 
	26	Wind 2 
	27	Wind 3 
	28	Wood 1- Only for recipes
	29	Wood 2
	30	Wood 3
	32	Wine 1- Only for recipes
	33	Wine 2
	34	Wine 3
	36	Japanese Wine 1- Only for recipes
	37	Japanese Wine 2
	41	Fish 1
	42	Fish 2
	45	Fruit 1
	46	Fruit 2
	49	Meat 1
	50	Meat 2
	52	Flower 1- Only for recipes
	53	Flower 2
	54	Flower 3
	56	Doll 1- Only for recipes
	57	Doll 2
	58	Doll 3
	64	Charcoal 1
	68	Ice
	72	Sword 1- Only for recipes
	73	Sword 2
	74	Sword 3
	75	Sword 4
	76	Dessert- Only for recipes
	77	Dessert
	85	Paper 1
	86	Paper 2
	89	Vegetables 1
	92	Bird 1
	96	Rice 1
	128	Voice 1
	129	Constellation
	130	Photo
	131	Quest Magnus
	132	Enemy Cards
	133	Camera
	
Sort Cat- Sorting Category
	
	10	Non-magic weapons
	20	Magic weapons
	30	Finishers
	40	Yells
	50	Body armors
	60	Head armors
	70	Shields
	80	Auras
	90	Support
	120	Miscellaneous
	170	Class promotion
	150	Camp
	160	Equipment
	220	Constellations
	230	Photos
	250	Quest
	255	Battle cards not in deck (Spirit Finishers/Enemy Magnus)

User- User(s) of the Magnus not including equipment
	
	0 	 None
	1  	Kalas  (Bit 1)
	2  	Xelha  (Bit 2)
	4  	Gibari (Bit 3)
	8  	Lyude  (Bit 4)
	16 	Savyna (Bit 5)
	32 	Mizuti (Bit 6)
	
	For multiple users, add the corresponding numbers together, i.e., Kalas + Lyude would be 9. 

Attack Motion- Motion for the Attack

	0    	None
	1     	Normal Attack
	3	Buff?
	5     	Voice
	6     	Camera
	3     	Use item
	7     	Escape
	10-18 	Finisher for that user
	19-24 	Spirit Finisher

Attack Effect- Effect for the Attack

	0    	None
	1     	?
	8	?
	9     	?
	10     	?

Attack Type

	0	None
	1	Attack
	2	Heal
	4	Voice
	5	Take Picture
	7	Escape

Attack Mod- Attack Modifier
	
	0	None
	8	Death
	9	Petrify (Do not use, not implemented)
	10	Sleep	
	11	Paralysis
	12	Freezing
	13	Flames
	14	Poison
	15	Regen (Do not use, not implemented)
	16	Slow (Do not use, not implemented)
	17 	Haste (Do not use, not implemented)
	18 	Headache
	19	Confusion
	20	Cure Death
	21 	Cure Petrify (Do not use, not implemented)
	22	Cure Sleep
	23 	Cure Paralysis
	24	Cure Freezing
	25	Cure Flames
	26	Cure Poison
	27	Cure Regen (Do not use, not implemented)
	28 	Cure Slow (Do not use, not implemented)
	29 	Cure Haste (Do not use, not implemented)
	30 	Cure Headache
	31 	Cure Confusion
	32	Cure All
	33	Death Resistance 
	34	Petrify Resistance (Do not use, not implemented)
	35	Sleep Resistance 
	36	Paralysis Resistance 
	37	Freezing Resistance 
	39	Flames Resistance 
	39	Poison Resistance 
	40	Regen Resistance (Do not use, not implemented)
	41	Slow Resistance (Do not use, not implemented)
	42	Haste Resistance (Do not use, not implemented)
	43	Headache Resistance 
	44	Confusion Resistance 
	45	All Resistance 
	46	Death Susceptibility 
	47	Petrify Susceptibility (Do not use, not implemented)
	48	Sleep Susceptibility 
	49	Paralysis Susceptibility 
	50	Freezing Susceptibility 
	51	Flames Susceptibility 
	52	Poison Susceptibility 
	53	Regen Susceptibility (Do not use, not implemented)
	54	Slow Susceptibility (Do not use, not implemented)
	55	Haste Susceptibility (Do not use, not implemented)
	56	Headache Susceptibility 
	57	Confusion Susceptibility 
	58	All Susceptibility

Attack Combo- Attack combo#

ucAtkCriticalBlank- ?

ucAtkHit- ?

Defense Motion- Motion of the Defense

	0	None
	2	Normal Defend
	25	Aura Level 1
	26	Aura Level 2
	27	Aura Level 3
	28	Aura Level 4
	29	Aura Level 5
	30	Aura Level 6
	
Defense Effect- Effect of the Defense
	
	17-57	Auras

Defense Type

	3	Defense

Defense Mod- Defense modifier, see attack modifier. 

Defense Combo- Defense Combo#

ucDfdCriticalBlank- ?
	
Camp Mod- Camp modifier

	1	Heal HP%
	2	Permanent HP Increase
	3	Permanent Exp Increase 
	7	Revive Character
	8	Cure Flames
	10	Cure Poison
	12	Permanent Attack Increase
	13 	Permanent Defense Increase
	14	Permanent Vitality Increase
	15	Permanent Agility Increase

Camp Mod 2- Not used

Equip User- Character who can equip this Magnus.

	0 	 None
	1  	Kalas  (Bit 1)
	2  	Xelha  (Bit 2)
	4  	Gibari (Bit 3)
	8  	Lyude  (Bit 4)
	16 	Savyna (Bit 5)
	32 	Mizuti (Bit 6)

Equid Mod- Equipment modifier, see attack modifier

Attack- The base neutral attack

Attack 2- Only used by voice and camera

Attk Mod %- Attack modifier proc%

snAtkS2- ?

Defense- Base neutral defense

Def Mod%- Defense modifier proc%

snDfdS1- Not used

snDfdS2- ?

Camp Amp- Camp modifier amplitude

	For experience, the value is amplitude x 1000

snCampS1- Not used

Equip HP- Equipment HP Increase

Equip Attk- Equipment Attack Increase

Equip Def- Equipment Defense Increase

Equip Agi- Equipment Agility Increase

Equip Resitance- Status Resistance

	Column	Effect
	1	Death
	2	Petrify
	3	Sleep
	4	Paralysis
	5	Freezing
	6	Flames
	7	Poison
	8	Regen
	9	Slow
	10	Haste
	11	Headache
	12	Confusion

Magnus Element
	
	0	Neutral
	1	Fire
	2	Water
	3	Light
	4	Dark
	5	Chronos
	6	Wind

Bonus- Bonus Attack/Defense

	Column	Element
	1	Neutral
	2	Fire
	3	Water
	4	Light
	5	Dark
	6	Chrono
	7	Wind

Spirit Num- Spirit Numbers that appear on the card. Each number is stored in 1 nibble, bit shifted by 0, 4, 8, or 12 bits (depending on the spirit number), and added together.
	       Use the table below to calculate the spirit numbers you want on the card. As an example, if you want UR-Odd, LL-Even, UL-1-9, and LR-1-9, you would do 1+32+768+16384=17185


		Upper Right	Lower Left	Upper Left	Lower right
	Odd	1		16		256		4096
	Even	2		32		512		8192
	1-8	3		48		768		12288
	1-9	4		64		1024		16384
	7-9	5		80		1280		20480
	9	6		96		1536		24576

	If you want to go backwards, convert to a binary number, separate each nibble, and convert each nibble to a value.

	Example: Void Phantom is 25618. In binary, this is 0110 0100 0001 0010

	0110 is 6 (9 in LR)
	0100 is 4 (1-9 in UL)
	0001 is 1 (Odd in LL)
	0010 is 2 (Even in UR)
