import sys
import os
import numpy as np
from PIL import Image
from operator import itemgetter
# Hello

path = "train1"


folder_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
#print(folder_names)

# Each row is an image
img = np.zeros([94257, 2025], dtype = float)
labels = np.zeros([94257])

j = 0
for i in range(10):
	for image in os.listdir(path + "/" + folder_names[i]):
		train_image = path + "/" + folder_names[i] + "/" + image
		img[j] = np.asarray(Image.open(train_image).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
		img[j] = img[j] / 255.0
		labels[j] = folder_names[i]
		j += 1
y=labels
X=img

from sklearn.neighbors import KNeighborsClassifier

path = "train"
folder_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
#print(folder_names)

# Each row is an image
img = np.zeros([160, 2025], dtype = float)
labels = np.zeros([160])

j = 0
for i in range(10):
	for image in os.listdir(path + "/" + folder_names[i]):
		train_image = path + "/" + folder_names[i] + "/" + image
		img[j] = np.asarray(Image.open(train_image).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
		#img[j] = img[j] / 255.0
		labels[j] = folder_names[i]
		j += 1
valData=img
valLabels=labels
accuracies=[]
k=1

# train the k-Nearest Neighbor classifier with the current value of `k`
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# evaluate the model
score = model.score(valData, valLabels)
print("k=%d, accuracy=%.2f%%" % (k, score * 100))
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_jobs=-1,n_estimators= 10)
model.fit(X, y)
score = model.score(valData, valLabels)
print("k=%d, accuracy=%.2f%%" % (k+1, score * 100))

"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print("yaahoo")
model.fit(X_train, y_train)
# evaluate the model
print("oohaay")
score = model.score(X_test, y_test)
print("k=%d, accuracy=%.2f%%" % (k, score * 100))
"""


