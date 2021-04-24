from container_package import container


c1 = container.universal("AFN")

print(type(c1))
print(c1.return_bic())

c2 = container.universal("AFN")

print(type(c2))
print(c2.return_bic())

c3 = container.reefer("AFN")

print(type(c3))
print(c3.return_bic())
print(c3.return_bic())

c4 = container.universal("AFN")
print(c4.return_bic())
