def checkio(data):
    if len(data)==4:
        #a=init_sophie b=inc_sophie c=init_man d=dec_man
        a,b,c,d=data
        while(a<c):
            a+=b
            if a>c:
                return c
            c-=d
        return a
            
    else:
        return False
   


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"
