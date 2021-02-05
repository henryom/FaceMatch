import os

def remove_ds(files):
    for f in files:
        if '.DS' in f:
            files.remove(f)
    return files

folders = remove_ds(os.listdir('TrainCroppedDataset'))

num = 0

for folder in folders:
	paths = remove_ds(os.listdir('TrainCroppedDataset/' + folder))
	for path in paths:
		command = 'cp TrainCroppedDataset/' + folder + '/' + path + ' Faces/Train/' + str(num) + '.jpg'
		os.system(command)
		num += 1