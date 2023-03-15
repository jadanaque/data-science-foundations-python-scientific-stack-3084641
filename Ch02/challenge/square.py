# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

# %%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5
# %%
img[350:850, 190:195, 2] = 1
img[350:850, 675:680, 2] = 1
img[350:355, 190:680, 2] = 1
img[845:850, 190:680, 2] = 1

# %% Another Approach
img[350:850, 190:195] = [0, 0, 1]
img[350:850, 675:680] = [0, 0, 1]
img[350:355, 190:680] = [0, 0, 1]
img[845:850, 190:680] = [0, 0, 1]
plt.imshow(img)

# %%
