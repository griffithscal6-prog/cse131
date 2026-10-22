def dollars_from_euro(euro):
    '''Convert dollars from euros.'''
    return round(euro * 1.13, 2)

def main():
    while True:
        print(dollars_from_euro(float(input("Enter the amount in euros: "))))
        automate()

def automate():
    assert 11.3 == dollars_from_euro(10)
    assert 22.6 == dollars_from_euro(20)
    assert 56.5 == dollars_from_euro(50)
    assert 113.0 == dollars_from_euro(100)
    assert 226.0 == dollars_from_euro(200)

main()