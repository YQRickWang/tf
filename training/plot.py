import numpy as np
import re
import matplotlib.pyplot as plt 

txt_name = 'Pytorch_Untied'
f = open(txt_name+'.txt', 'r')
lines = f.readlines()

step = []
train_loss = []
val_loss = []
angle_losses = []

for l in lines:
	if l.startswith('Global step:'):
		step.append(int(re.search('[0-9]+',l).group(0)))
	elif l.startswith('Train loss avg:'):
		train_loss.append(float(re.search('[0-9]+.[0-9]+',l).group(0)))
	elif l.startswith('Val loss:'):
		val_loss.append(float(re.search('[0-9]+.[0-9]+',l).group(0)))
	elif l.startswith('walking '):
		_ = re.findall('[0-9]+.[0-9]+',l)
		angle_losses.append([float(i) for i in _])

angle_losses = np.array(angle_losses)

def select_best_performed_angle_losses():
	return angle_losses.min(axis=0)

print(select_best_performed_angle_losses())

# plt.plot(step, train_loss, linewidth=4,label="train_loss")
# plt.plot(step, val_loss, linewidth=4,label="val_loss")
# plt.plot(step, angle_losses[:,0], linewidth=1,label="80")
# plt.plot(step, angle_losses[:,1], linewidth=1,label="160")
# plt.plot(step, angle_losses[:,2], linewidth=1,label="320")
# plt.plot(step, angle_losses[:,3], linewidth=1,label="400")
# plt.legend()
# # plt.show()
# plt.savefig(txt_name+'.jpg')