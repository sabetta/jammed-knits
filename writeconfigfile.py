'''
Code to write config file for sims
written sept 1 2023 by sarah gonzalez


this code sweeps over length for k=0.1mN/mm^2
'''
import pandas as pd

init = ["1","2","3","4"] 
length = [10.6, 10.7, 10.8, 10.9, 11, 11.1, 11.2, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12, 12.1]


for b in range(0, len(length)):
	for a in range(0, len(init)):
		str1 = "acrylic params - stockinette\n"
		str2 = "\n"
		str3 = "only lines starting with * mean anything\n"
		str4 = "\n"
		str5 = "*init_file " + init[a] + "\n"
		str6 = "*output_prefix len" + str(round(1000*length[b])) + "\n"
		str7 = "*stitch_length " + str(length[b]) + " mm\n"
		str8 = "*bending_modulus 0.045\n"
		str9 = "*regularization 0.002\n"
		str10 = "*yarn_radius 0.74\n"
		str11 = "*core_radius 0.325\n"
		str12 = "*interactions_per_segment 10\n"
		str13 = "*contact_rigidity 0.0001\n"
		str14 = "*contact_exponent 2.4\n"
		xstr15 = "*sweep_direction x\n"
		ystr15 = "*sweep_direction y\n"
		xstr16 = "*init_dimension 2.8\n"
		ystr16 = "*init_dimension 1.9\n"
		xstr17 = "*final_dimension 5.3\n"
		ystr17 = "*final_dimension 2.7\n"
		xstr18 = "*step_size 0.001\n"
		ystr18 = "*step_size 0.001\n"

		xinclude = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, str13, str14, xstr15, xstr16,xstr17,xstr18]
		yinclude = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, str13, str14, ystr15, ystr16,ystr17,ystr18]

		xfile = open(str(init[a]) + "k1config_x_len" + str(round(1000*length[b])) + ".dat", "a")
		xfile.writelines(xinclude)
		xfile.close()

		yfile = open(str(init[a]) + "k1config_y_len" + str(round(1000*length[b])) + ".dat", "a")
		yfile.writelines(yinclude)
		yfile.close()


param = open("stocklenk1.txt", "a")
blank = []
direction = ["y","x"] 

for b in range(0, len(length)):
	for a in range(0, len(init)): 
		for i in range(0,len(direction)):
			killme = str(init[a]) + "k1config_" + direction[i] + "_len" + str(round(1000*length[b])) + ".dat\n"
			blank.append(killme)


param.writelines(blank)
param.close()
		
