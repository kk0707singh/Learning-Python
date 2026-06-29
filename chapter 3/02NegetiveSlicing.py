name = "Sidharth"
print(name[0:4])
print(name[-8: -3])

print(name[:6])     #will start assuming 0 before  :
print(name[2:])     #will assume len-1


#slicing with skipped values
anothername = "krishnakantisagoodpersonheorksveryhardandalsorespecteveryone"
print(len(anothername))
print(anothername[0:60:4])