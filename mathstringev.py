import sys
from io import StringIO

def lstost(ls):
    buffer = StringIO()
    for a in ls:
        buffer.write(str(a))
    ans = buffer.getvalue()
    buffer.close()
    return ans

def ditchSpaces(st):
    """Returns the same string but without the spaces"""
    strBuffer = StringIO()
    for char in st:
        if (char!=" "):
            strBuffer.write(char)
    ans = strBuffer.getvalue()
    strBuffer.close()
    return ans

def eval(tst):
    st = ditchSpaces(tst)
    rawChars = []
    parCount = 0
    stBuff1 = StringIO() #For raw without parentheses
    stBuff2 = StringIO() #For inside parentheses
    for char in st:
        if (char == "("):
            parCount += 1
            if (parCount == 1):
                # It gets here when it opens a parentheses from raw
                rawChars.append(stBuff1.getvalue())
                stBuff1.close()
                stBuff1 = StringIO()
                continue

        elif (char == ")"):
            parCount -= 1
            if (parCount == 0):
                # it gets here when it closes the previous from-raw parentheses that it opened
                rawChars.append(str(eval(stBuff2.getvalue())))
                stBuff2.close()
                stBuff2 = StringIO()
                continue
       
        if (parCount == 0):
            stBuff1.write(char)
        
        else:
            stBuff2.write(char)
    rawChars.append(stBuff1.getvalue())

    #When it gets here it means that it solved everything inside each parenthesis
    #and now it has a raw string that it has to solve with good 'ol precedence
    return evalTokens(getTokens(lstost(rawChars)))

def getTokens(st):
    opSet = {'*','/','+','-','^'}
    tokens = []
    strObj = StringIO()
    sign = 1
    for ch in st:
        if ch in opSet:
            stVal = strObj.getvalue()
            if (stVal==''):
                if (ch=='-'):
                    sign = -1                    
                else:
                    print("This should never get here. There are two simbols that are not allowed together")
            else:
                tokens.append(sign*float(strObj.getvalue()))
                tokens.append(ch)
                strObj.close()
                strObj = StringIO()
                sign = 1
        else:
            strObj.write(ch)
    tokens.append(sign*float(strObj.getvalue()))
    strObj.close()
    return tokens

def evalTokens(tokens):
    token = tokens
    i = 0
    while(True):
        if i>=len(token):
                break
        if (token[i]=='^'):
            temp = token[i-1]**token[i+1]
            token.pop(i-1) #i+1
            token.pop(i-1) #former i
            token.pop(i-1) #former i+1
            token.insert(i-1,temp)
        else:
            i += 1
    i = 0
    while(True):
        if i>=len(token):
                break
        if (token[i]=='*'):
            temp = token[i-1]*token[i+1]
            token.pop(i-1) #i+1
            token.pop(i-1) #former i
            token.pop(i-1) #former i+1
            token.insert(i-1,temp)
        else:
            i += 1
    i = 0
    while(True):
        if i>=len(token):
                break
        if (token[i]=='/'):
            temp = token[i-1]/token[i+1]
            token.pop(i-1) #i+1
            token.pop(i-1) #former i
            token.pop(i-1) #former i+1
            token.insert(i-1,temp)
        else:
            i += 1
    i = 0
    while(True):
        if i>=len(token):
                break
        if (token[i]=='+'):
            temp = token[i-1]+token[i+1]
            token.pop(i-1) #i+1
            token.pop(i-1) #former i
            token.pop(i-1) #former i+1
            token.insert(i-1,temp)
        else:
            i += 1
    i = 0
    while(True):
        if i>=len(token):
                break
        if (token[i]=='-'):
            temp = token[i-1]-token[i+1]
            token.pop(i-1) #i+1
            token.pop(i-1) #former i
            token.pop(i-1) #former i+1
            token.insert(i-1,temp)
        else:
            i += 1

    if (token[0]==int(token[0])):
        return int(token[0])
    return token[0]
    
def main():
    args = sys.argv
    if (len(args)>1):
        args.pop(0)
        for a in args:
            print("{} = {}".format(a,eval(str(a))))
    else:
        print("No input found in execution arguments. Input mathematical string now:")
        st = input()
        print("{} = {}".format(st,eval(str(st))))

main()