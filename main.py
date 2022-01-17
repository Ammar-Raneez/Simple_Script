import simple_script

while True:
    text = input('simplescript > ')
    result, error = simple_script.run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)
