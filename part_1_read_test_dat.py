import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

fileText = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)
print(fileText)