print("Import package_1. This has a '__init__.py' so additional attributes will be bound to the symbol.")
import package_1
print("Here is proof that 'package_1' was imported:")
print(("package_1" in locals()))
print("Here is proof that the nested module is now an attribute of package_1: ")
print(("module_1" in dir(package_1)))
print("functions within the nested modules can be used: ")
package_1.module_1.function_1()
print("\n")

print("Import package_2. This does not have a '__init__.py' so nested modules will not automatically be bound as modules.")
import package_2
print("Here is proof that 'package_2' was imported:")
print(("package_2" in locals()))
print("Here is proof that the nested module is not an attribute of package_2: ")
print(("module_2" in dir(package_2)))

print("\n")

print("It is still possible to use the code in module_2.")
import package_2.module_2

print("Here is proof that the nested module is now an attribute of package_2: ")
print(("module_2" in dir(package_2)))

print("Now we can use that code: ")

package_2.module_2.function_2()
