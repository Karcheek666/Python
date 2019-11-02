import random
fliped  = 0
heads = 0
tails = 0
i = 0

repeat = int(input('Enter the number of times you want to flip the coin: '))
repeat = repeat - 1
while i <= repeat:
    flip = random.randrange(2)
    i = i + 1
    if flip %2 == 0:
        heads = heads + 1
    else:
        tails = tails + 1

repeat = repeat + 1
tail_percentage = (tails/repeat) * 100
heads_percentage = (heads/repeat)  * 100


print('^^^Flip results are given above^^^')
print('The coin was flipped ', str(repeat) + ' times.')
print('The outcome was Tails '+ str(int(tail_percentage/100*repeat)) + ' times.')
print('The outcome was Heads ' + str(int(heads_percentage/100*repeat)) + ' times.')

if heads > tails:
    difference = heads - tails
     
elif tails > heads:
    difference = tails - heads
    
else:
    difference = 0
    
    
print('The differnce is ', str(difference))
