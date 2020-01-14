print('\n'.join([' '.join(["%2s x%2s = %2s" % (j, i, i*j)
                           for j in range(1, i+1)]) for i in range(1, 10)]))

print(''.join(__import__('random').choice('\u2571\u2572')
              for i in range(50*24)))


print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))！
