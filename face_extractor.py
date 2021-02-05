import os

def remove_ds(files):
    for f in files:
        if '.DS' in f:
            files.remove(f)
    return files

folders = remove_ds(os.listdir('TestCroppedDataset'))

for folder in folders:
	paths = remove_ds(os.listdir('TestCroppedDataset/' + folder))
	for path in paths:
		command = 'cp TestCroppedDataset/' + folder + '/' + path + ' Faces/Test'
		os.system(command)