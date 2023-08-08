# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


exFloat = 1.23 + 2.80;

print(exFloat);
print(round(exFloat,2));


pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs
# subtotal is the sum of all prices before any sales taxes or discounts are added
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)

print(round(16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39 ,2));