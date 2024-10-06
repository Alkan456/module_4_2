def test_function ():

    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function()
#Вызвать функцию inner_function вне функции test_function невозмоно, так как inner принадлежит к локальному
#пространству имён и существует только внутри функции test_function