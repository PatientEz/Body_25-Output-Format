import  numpy as np
import  cv2
import matplotlib.pyplot as plt
kp = np.load("./35.npy")
print(kp.shape)
print(kp)
#图片大小为480x466
tink = np.ones((480,466),dtype='float64')
tink = tink
print(tink.shape)
for i in range(kp.shape[0]):
    for j in range(kp.shape[1]):
        x = kp[i][j][0]
        y = kp[i][j][1]
        score =  kp[i][j][2]
        #color =  score
        color = 1
        tink[int(y)][int(x)] = 240 * color / 25
        tink[int(y)+1][int(x)] = 240 * color / 25
        tink[int(y)][int(x)+1] = 240 * color / 25
        tink[int(y)-1][int(x)] = 240 * color / 25
        tink[int(y)][int(x)-1] = 240 * color / 25
        tink[int(y) + 1][int(x)+1] = 240 * color / 25
        tink[int(y)-1][int(x) + 1] = 240 * color / 25
        tink[int(y) - 1][int(x)-1] = 240 * color / 25
        tink[int(y) + 1][int(x) - 1] = 240 * color / 25

plt.imshow(tink,cmap="gray")
plt.axis('off')
plt.show()