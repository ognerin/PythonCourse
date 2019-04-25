def save_result(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        
        with open(func.__name__ + '.txt', 'a') as f:
            f.write(str(return_value) + '\n')
            
        return return_value
        
    return wrapper
    

@save_result
def test_func():
    a = 3
    for i in range(3):
        a = a + 1
    return(a)
    
    
def main():
    print(test_func())

if __name__ == '__main__':
    main()
