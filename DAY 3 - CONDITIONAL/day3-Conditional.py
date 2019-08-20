# THE ZEN OF PYTHON BY TIM PETERS
import this

# if n is odd, print weird. if even print not weird (see readme)
N = int(input().strip())

if N % 2 == 1:
    print('Weird')
elif N < 5:
    print('Not Weird')
elif N <= 20:
    print('Weird')
else:
    print('Not Weird')
    # TESTING QUOTATION "" VS ''
    print("einstein said: \"Do yur thang bbg, it's your time ta shineee\"")
    print(str(3/2))
    # done
