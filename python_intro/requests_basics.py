import requests
from selenium import webdriver


res = requests.post("http://automationpractice.com/index.php?controller=authenticationemail=aaatest%40gmail.com&passwd=test1&back=my-account&SubmitLogin")
headers = res.headers

cookies = {
    "name": "PrestaShop-a30a9934ef476d11b6cc3c983616e364",
    "value": "PXrPql8A805Y%2B1%2Ftd13wmfFodHIFUlIo9C5d69xjzBUQU14ocL8%2FjoXDD5y6yZeg6v8qiSUp2CeXMp7jWPTbQHjsjuyePPr6lX8xPlhUaOtjPMFYWr9y%2FYeZzKUsbyUaIBk5wKh1mOziH%2FjVbgCt%2FrtLrJkzF7tCDxh2DWpdm5eU%2FzM%2FDajGTAc6sN9cExMKDoWlFE86JkJcf%2FUKrbSzXIKKXGaDgrpjRWS55AIalDAl8ehW77Hs8qYyVKH9MJKZwibGHCTUXS71%2BgngDEqKg9fAJphE7dG8J00PaDAGTaKEXxga%2FqnHpqvbFvm93Cau0Kc2jipMjNwnEa%2FRyhc134GwLa%2BMs9JuN8qejyGliRwoeFeXyETcJECdSwORhvYHcCHL9%2BSbXQdh8cfQN67QsmttNv%2FE3kcDAm%2Fn2WnhcW8sR9R5EIw7PUKDuxxjrsKRrf3PvEp4R8o%2B12iOMWXgM9dKMKKiLRw1kleBZeGOopo%3D000353"
}



class Test:

    @staticmethod
    def tesdt():
        pass

Test.tesdt()
