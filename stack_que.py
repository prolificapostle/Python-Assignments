from sys import getsizeof

testt = [a ** 2 for a in range(100000)]
testtt = (a ** 2 for a in range(100000))
print(getsizeof(testt))
print(getsizeof(testtt))

browser_history = []

browser_history.append("google.com")
browser_history.append("semicolon.africa")
browser_history.append("yahoo.com")
browser_history.append("microsoft.com")
print(browser_history)
browser_history.pop()
print(browser_history)
print(f"redirecting to {browser_history[-1]}")
