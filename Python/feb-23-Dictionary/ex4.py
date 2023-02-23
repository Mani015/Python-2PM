
games= {'volleyball':6,'cricket':11,'football':11,'kabbadi':7,'chess':2,'carrom':4}
print(games)
# get method uses to how to get the particular value of key
print(games.get('cricket'))
# 11
print(games.get('kabbadi'))
# 7
print(games.get('tennis'))
# None


print(games.get('carrom'))
# 4