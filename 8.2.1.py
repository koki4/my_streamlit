import matplotlib.pyplot as plt
ax = plt.subplot()
print(f"ax={ax} fig={ax.figure}")

fig, ax = plt.subplots(1,1)
print(f"1. ax={ax}") #axはAxesSubplotオブジェクト

fig, axes = plt.subplots(1,3) #3つの要素のリスト
print(f"2. len(axes)={len(axes)} axes[0]={axes[0]}")

fig, axes = plt.subplots(3,1) #3つの要素のリスト
print(f"3. len(axes)={len(axes)} axes[0]={axes[0]}")

fig, axes = plt.subplots(4,3) #4行3列のリストのリスト
fig.suptitle("4行3列のリストのリスト")
axes[1,1].set_title("sepal")
print(f"4. len(axes)={len(axes)} axes[0,0]={axes[0,0]}")

plt.show()