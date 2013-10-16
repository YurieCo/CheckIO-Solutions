def checkio(text):
    """
    string with dot separated numbers, which inserted after every third digit from right to left
    """
    words=text.split(' ')
    output=[]
    for word in words:
        if word.isdigit():
            res=''
            count=0
            for i in reversed(range(len(word))):
                res=word[i]+res
                count+=1
                if count%3==0 and i!=0:
                    res='.' + res
            output.append(res)
        else:
            output.append(word)
    output=" ".join(output)
    return output
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('123456') == '123.456', "1st example"
    assert checkio('333') == '333', "2nd example"
    assert checkio('9999999') == '9.999.999', "3rd example"
    assert checkio('123456 567890') == '123.456 567.890', "4th example"
    assert checkio('price is 5799') == 'price is 5.799', "5th example"
    assert checkio('he was born in 1966th') == 'he was born in 1966th', "6th example"
