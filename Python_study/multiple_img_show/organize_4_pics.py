# 1 2 3 4 jpg show them by 2 times 2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_list = []
fig_size = 8
fig = plt.figure(figsize=(fig_size,fig_size))
for i in range(0,4):
    image_list.append(mpimg.imread(str(i+1) + '.jpg'))
    fig.add_subplot(2,2,i+1)
    plt.imshow(image_list[-1])
plt.show()
