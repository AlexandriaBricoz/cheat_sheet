#-ecnn naponb conepnT CMMBONbI n6bIx 2 Ha6opoB BepHyTb Good
#ecnu naponb conepxT CNMBonbl no6bIx 3 Ha6opoB,BepHyTb Very Good
import string
def password_strength(value:str)->str:
    if len(value)<8:
        return 'Too Weak'
    digits = string.digits
    Lowers = string.ascii_lowercase
    uppers = Lowers.upper()
    count = 0
    for symbols in (digits,Lowers,uppers):
        if any(e in symbols for e in value):
            count+=1
            continue #переходит к следующей итерации
    if count == 2:
        return 'Good'
    if count == 3:
        return 'Very Good'
    return 'Weak'

if __name__ == '__main__':
    assert password_strength('')=='Too Weak'
    assert password_strength('1234567')== 'Too Weak'
    assert password_strength('gazwsxe')=='Too Weak'
    assert password_strength('QAZWSXE') == 'Too Weak'
    assert password_strength('QAaa1')=='Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('123456788990')=='Weak'
    assert password_strength('aqzwsxed') == 'Weak'
    assert password_strength('agzwsxedwed')== 'Weak'
    assert password_strength('QAZWSXED') == 'Weak'
    assert password_strength('QAZWSXEDRFT')=='Weak'
    assert password_strength('1234gazw') == 'Good'
    assert password_strength('1234gazwws') == 'Good'
    assert password_strength('12340AZW') == 'Good'
    assert password_strength('1234QAZWOW') == 'Good'
    assert password_strength('aszxQAZW') == 'Good'
    assert password_strength('aszxasQAZW') == 'Good'
    assert password_strength('123qazQAZ') == 'Very Good'
    assert password_strength('12334556Zz') == 'Very Good'
    assert password_strength('gazwsxeSdz1') == 'Very Good'
    assert password_strength('QAZWSXEDCZ1a') =='Very Good'
