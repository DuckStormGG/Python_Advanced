
1. `return address is None` should be `return self.address is None`
---
2. `return self.yob - now.year` should be ` return now.year - self.yob`
---
3. `self.name = self.name` should be `self.name = name`
---
4. `self.address == address` should be `self.address = address`
