class ProductOfNumbers:

    def __init__(self):
        self.products=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.products=[1]
        else:
            self.products.append(self.products[-1]*num)        

    def getProduct(self, k: int) -> int:
        if len(self.products)-1 >=k:
            prod=self.products[-1]//self.products[len(self.products)-1-k]
            return prod
        else:
            return 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)