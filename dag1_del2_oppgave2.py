from dag1_del1_oppgave3 import dice_throw

ti = dice_throw(6, 10)
hundre = dice_throw(6, 100)
tusen = dice_throw(6, 1000)

print(f"{ti.count(6)}/10")
print(f"{hundre.count(6)}/100")
print(f"{tusen.count(6)}/1000")
