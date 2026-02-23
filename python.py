languages = ['Spanish', 'English', 'Russian', 'Chinese']
for x,y in enumerate(languages,1):
    print(f"index--{x},language--{y}")

name=["abrar","joo","wuyan"]
ids=[1,2,3,4]

zip(name,ids)

for x,y in zip(name,ids):
    print(f"{x} is zipped to {y}")

numbers=[0,2,4,6,8,10]
cube=lambda x:x**3
cubed_num=list(map(cube,numbers))
print(cubed_num)