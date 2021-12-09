import time

print('hello welcome to cool python app')

print('what is your name young hero? ')
name = input("Enter name [pete|john|dork]:")
time.sleep(5)

if name == 'pete':
    print('Pete is my hero, he is the awesomist!!!!')
    print ("loading....")
    time.sleep (1)
    print ("u woke up this morning and ate rotten niwrnfvlwr for your breakfast")
elif name == 'john':
    print ("u woke up this morning and ate piez for your breakfast")
elif name == 'dork':
    print('Yes you are loser-boy')
    time.sleep(3)
    print ("u woke up this morning and ate cheese for your breakfast")
else:
    print(f'{name} is an invalid option.')



