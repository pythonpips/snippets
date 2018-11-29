"""author: @pythonpips"""

foo = [1, 2, 3]
bar = [4, 5, 6]
baz = [*foo, *bar]
print(baz)
# baz outputs [1, 2, 3, 4, 5, 6]