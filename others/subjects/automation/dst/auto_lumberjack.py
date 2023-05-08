from pyautogui import *

while True:
    tall = list(locateAllOnScreen('images/trees/tall_tree.png'))
    small = list(locateAllOnScreen('images/trees/small_tree.png'))
    print(small)
    trees = tall + small
    for tree in trees:
        click(tree[0], tree[1])
        press('space', 6)
        del trees[trees.index(tree)]