import os
import UnityPy
import sys

def main():

	if getattr(sys, 'frozen', False):
		scriptPath = os.path.dirname(os.path.realpath(sys.executable))
	else:
		scriptPath = os.path.dirname(os.path.realpath(__file__))

	bundlePath = os.path.join(scriptPath, 'Backup', 'b29e1677d0e548f3b74e980a7fb8b638.bundle')
	dllPath = os.path.join(scriptPath, 'Backup', 'GameAssembly.dll')
	csvFileName = os.path.join(scriptPath, 'magnus_stats.csv')
	oBundlePath = os.path.join(scriptPath, 'Output', 'b29e1677d0e548f3b74e980a7fb8b638.bundle')
	oDllPath = os.path.join(scriptPath, 'Output', 'GameAssembly.dll')

	env = UnityPy.load(bundlePath)

	qMagAge = []

	dataFileName = ['MagnusMasterData_en', 'MagnusMasterData_jp']
	attrName = ['ucLevel','usnStatus','nPrice','unTimeChangeSecLimit','snTimeChangeMagnusNo',
			'ucCategory','ucSortCategory','ucDeck','ucAtkMotion','ucAtkEffect','ucAtkProcM',
			'ucAtkProcS','ucAtkComboCount','ucAtkCriticalBlank','ucAtkHit','ucDfdMotion',
			'ucDfdEffect','ucDfdProcM','ucDfdProcS','ucDfdComboCount','ucDfdCriticalBlank',
			'ucCampProcM','ucCampProcS','ucEquip','ucEquipProc','snAtkM1','snAtkM2','snAtkS1',
			'snAtkS2','snDfdM1','snDfdM2','snDfdS1','snDfdS2','snCampM1','snCampS1','scEquipHPMAX',
			'scEquipATK','scEquipDFD','scEquipAGL','scEquipResistAS','ucMagicAttr',
			'ucMagicAttrValue','usnOriginalSpiritNumber']


	qKey = [0xc74424387604b004488bd0c744243c80CBA4, 0xc744243877047804C744243CC04B0300,
			0xC74424387C047D04C744243CC04B0300, 0xC74424387F048004C744243C80970600,
			0xC744243881048204C744243CE0A50100, 0xC744243882047E04C744243CE0A50100,
			0xC744243883048F04C744243CE0A50100,	0xC744243885048604C744243CC07A1000, 
			0xC744243886048704C744243C80F52000, 0xC744243888048904C744243CE0A50100,
			0xC74424388A048004C744243CE0A50100, 0xC74424388B049704C744243CE0A50100, 
			0xC74424388D048E04C744243CC04B0300, 0xC74424388F049004C744243CC04B0300, 
			0xC744243891049204C744243CE0A50100, 0xC744243893049404C744243C002F0D00, 
			0xC744243895049604C744243C80970600, 0xC744243897048C04C744243CA08C0000, 
			0xC74424389A04A704C744243C80970600, 0xC74424389D049C04C744243C00D68300, 
			0xC7442438A5047E04C744243CA08C0000, 0xC7442438A7049B04C744243C002F0D00, 
			0xC7442438A8049904C744243CE0A50100, 0xC7442438AA047F04C744243C40190100, 
			0xC7442438AC048C04C744243CC04B0300, 0xC7442438AD04AE04C744243CC04B0300]
			

	for x in range(len(qKey)):
		if x == 0:
			qKey[x] = qKey[x].to_bytes(18, 'big')
		else:
			qKey[x] = qKey[x].to_bytes(16, 'big')



	qCard = [0x476, 0x477, 0x47c, 0x47f, 0x481, 0x482, 0x483, 0x485, 0x486, 0x48A,
			 0x48B, 0x48D, 0x48F, 0x491, 0x493, 0x495, 0x497, 0x49A, 0x49D, 0x4A7,
			 0x4A8, 0x4AA, 0x4AC, 0x4AD, 0x4A5, 0x488]

	attrValues = []

	csvFile = open(csvFileName, 'r')

	lines = csvFile.readlines()




	c = 0
	for line in lines:
		line = line.replace('\n','')
		line = line.split(',')
		if c > 0 and c < 1203:
			tempArray = []
			for x in range(2,41):
				tempArray.append(int(line[x]))
			tempArray2 = []
			for x in range(41,53):
				tempArray2.append(int(line[x]))
			tempArray.append(tempArray2)
			tempArray2 = []
			tempArray.append(int(line[53]))
			for x in range(54,61):
				tempArray2.append(int(line[x]))
			tempArray.append(tempArray2)
			tempArray.append(int(line[61]))

			attrValues.append(tempArray)
		c+=1


	for obj in env.objects:
		if obj.type.name == "MonoBehaviour":
			if obj.serialized_type.nodes:
				tree = obj.read_typetree()
				if tree['m_Name'] in dataFileName:
					for x in range(1201):
						if x < 1142:
							for y in range(43):
								(tree['magnusRoms'][x])[attrName[y]] = attrValues[x][y]
						if x >= 1142 and x in qCard:
							if len(qMagAge) < 26: # Don't add the values again from jp file.
								qMagAge.append(attrValues[x][3]*60)
					obj.save_typetree(tree)


		
	with open(oBundlePath, "wb") as f:
		f.write(env.file.save(packer='original'))

	try:
		os.remove(oDllPath)
	except:
		pass
		
	bFile = open(dllPath, "rb")
	contents = bFile.read()

	for x in range(len(qKey)):
		splice = qKey[x].hex()
		if x ==0: 
			splice = splice[:30]
			value = qMagAge[x].to_bytes(3, 'little')
		else:
			splice = splice[:24]
			value = qMagAge[x].to_bytes(4, 'little')		
			
		
		value = value.hex()

		splice = splice + value
		nBytes = int(len(splice)/2)

		splice = int(splice, 16)
		
		splice = splice.to_bytes(nBytes, 'big')
		
		contents = contents.replace(qKey[x], splice)

	bFile.close()

	bFile = open(oDllPath, "wb")
	bFile.write(contents)
	bFile.close()

def mask_high(value,bits):
	#Value is the number to be masked, bits is how many bits to keep
	value = value - (value>>bits<<bits)
	return(value)

if __name__ == "__main__":
    main()	

