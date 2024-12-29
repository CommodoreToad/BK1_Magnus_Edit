BK1 MagnusEdit v1.0

This mod will allow you to edit any non-quest Magnus stat and the age time for any quest Magnus that already ages. This bundle includes the original python 3 script and an executable built in 64 bit Windows. 
Either can be used, but python will need to be installed along with the UnityPy module for the py script.

PLEASE FOLLOW ALL INSTRUCTIONS TO AVOID DAMAGING YOUR GAME. THERE ARE CURRENTLY VERY LITTLE GUARD RAILS FROM MISTAKES. MAKE A SAVE FOR YOUR GAME BEFORE EDITING ANY FILES AND USE THIS MOD AT YOUR OWN RISK.


First Time Requirements
1) Copy '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\GameAssembly.dll' to '\BK1MagnusEdit\Backup'
2) Copy '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\Batenkaitos_Data\StreamingAssets\aa\StandaloneWindows64\b29e1677d0e548f3b74e980a7fb8b638.bundle to '\BK1MagnusEdit\Backup'

'\BK1MagnusEdit\Backup' contains the original data, and you can use these files to restore your game to its original state in case something goes wrong. This folder also contains a copy of 'magnus_stats.csv'. DO NOT MOVE THIS FILE. 
You can use this file to reset your game to its original state.

Changing Magnus Parameters
1) All of the Magnus parameters are located in '\BK1MagnusEdit\magnus_stats.csv'. This file can easily be edited in a spreadsheet application. 
2) DO NOT DELETE ANY ROW OR COLUMN
3) The "Magnus Number" and "Magnus Name" columns are for informational purposes only. Do not edit these.
4) Any change must be an WHOLE NUMBER. Negative numbers may have unexpected behavior. Do not use excessivly large values for that column, you may exceed the variable size.
5) The only thing you can change for quest Magnus is the age time for Magnus that already age. Any other changes will be ignored.
6) Save the csv file when you are done.

Patching the Game Files
1) Run MagnusEdit.exe or MagnusEdit.py. This should complete in the background in about 20 seconds.
2) ENSURE YOU HAVE ORIGINAL BACKUPS OF YOUR DLL AND BUNDLE FILE
3) Copy the the dll in '\BK1MagnusEdit\Output\' and overwrite '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\GameAssembly.dll'
4) Copy the bundle in '\BK1MagnusEdit\Output\' and overwrite '\steamapps\common\BatenKaitos HD Remaster\Batenkaitos1\Batenkaitos_Data\StreamingAssets\aa\StandaloneWindows64\b29e1677d0e548f3b74e980a7fb8b638.bundle
5) Start the game!

