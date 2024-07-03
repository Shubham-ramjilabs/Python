String="Hello World"
#slicing string using positive index 
print("slicing string using positive index")   
print(String[:],"---we can not give start and end point")
print(String[6:11])
print(String[2:],"---we can not give end point")
print(String[:4],"---we can not give start point")
print(String[0:0],"----we can give staring point and end point =0")
print(String[0:11:2],"---we can gieve the step value")

print("---------")
print("slicing string using negative index")
#slicing string using negative index
print(String[-6:-1])
print(String[:-1],"---we can not give start point")
print(String[-1:],"---we can not give end point")
print(String[0:0],"----we can give staring point and end point =0")
print(String[-11:-1:2],"---we can gieve the step value")
print(String[::-1],"---reverse the string")