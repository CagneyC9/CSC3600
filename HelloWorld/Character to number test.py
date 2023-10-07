charstr='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars=list(charstr)
nums=[str(i) for i in range(1,53)]
with open('data.txt','r') as f:
    data=f.read()
output=''
for i in range(len(data)):
    if data[i] in chars:
        pos=chars.index(data[i])
        output=output+nums[pos]+' '
    elif data[i]==' ':
        output=output+'\t'
    else:
        output=output+data[i]+' '
print('Output of Two Lists: '+output)