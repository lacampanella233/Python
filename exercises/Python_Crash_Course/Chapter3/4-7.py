# 将使用 A, B, C... 等大写字母替代具体人名.

# 3-4 

guest = ['A','B','C']
print("I would invite " + str(guest) + " for dinner.")

# 3-5

# 假设嘉宾 C 无法赴约, 将 C 换为 D

print("Guset C can't make it to the dinner.")
guest[2] = 'D'
print("I would invite " + str(guest) + " for dinner now.")

# 3-6

# 继续邀请嘉宾 E, F, G

print("A bigger table is found, therefore more guests will be invited.")
guest.insert(0,'E')
guest.insert(2,'F')
guest.append('G')
print("I would invite " + str(guest) + " for dinner now.")

# 3-7

print("The bigger table is unfortunately unavailable, so only two guests will be invited.")

# 删除 4 个嘉宾

print("Dear " + guest.pop().title() + ", I'm sorry to inform that I can't invite you for dinner.")
print("Dear " + guest.pop().title() + ", I'm sorry to inform that I can't invite you for dinner.")
print("Dear " + guest.pop().title() + ", I'm sorry to inform that I can't invite you for dinner.")
print("Dear " + guest.pop().title() + ", I'm sorry to inform that I can't invite you for dinner.")

print("Dear " + guest[0] + ", you're still in inviting list.")
print("Dear " + guest[1] + ", you're still in inviting list.")

del guest[0]
del guest[0]

print("The list is " + str(guest) + ", which is expected to be empty.")