import numpy

"""
Generate npz files

This program run for the specific case of the UCF_CC_50 dataset.
You should adapt the code for your dataset.
"""

def file_lister(extension, suffix, prefix):

  my_list = []

  name = 1

  for i in range(50):
    filename = prefix + str(name) + suffix + extension
    #print(filename)
    name += 1
    my_list.append(filename)

  return my_list

pictures = file_lister(".jpg", "", "")
dot_pictures = file_lister(".png", "", "dot_")

# dot annotation
trn_lb = dot_pictures[:35]
val_lb = dot_pictures[35:]

# original images
trn_lst = pictures[:35]
val_lst = pictures[35:]

# print(pictures)
# print()
# print(dot_pictures)
# print()
#
#
# print(trn_lst)
# print()
# print(val_lst)
# print()
#
# print(trn_lb)
# print()
# print(val_lb)
# print()

numpy.savez("../meta/ucf_cc_50.npz", trn_lb=trn_lb, trn_lst=trn_lst, val_lst=val_lst, val_lb=val_lb)
