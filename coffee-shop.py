print('----- ORDER YOUR COFFEE -----')

sizeList = ['small', 'medium', 'large']
typeList = ['brewed', 'espresso', 'cold brew']
flavorQList = ['y', 'n']
flavorList = ['hazelnut', 'vanilla', 'caramel']

size = input('* Choose size (small, medium, large)? ')
sizeLower = size.lower()

while sizeLower not in sizeList:
    print('Wrong entry. Try again.')
    size = input('* Choose size (small, medium, large)? ')
    sizeLower = size.lower()

type = input('* Choose type (brewed, espresso, cold brew)? ')
typeLower = type.lower()

while typeLower not in typeList:
    print('Wrong entry. Try again.')
    type = input('* Choose type (brewed, espresso, cold brew)? ')
    typeLower = type.lower()

flavorQ = input('* Do you want to add syrup? (y/n) ')
flavorQLower = flavorQ.lower()

while flavorQLower not in flavorQList:
    print('Wrong entry. Try again')
    flavorQ = input('* Do you want to add syrup? (y/n) ')
    flavorQLower = flavorQ.lower()

if flavorQLower in flavorQList and sizeLower in sizeList and flavorQLower == 'n':
    print('* ORDER SUMMARY: ', sizeLower, 'cup of', typeLower, 'coffee.')
    if sizeLower == 'small':
        size = 2
    if sizeLower == 'medium':
        size = 3
    if sizeLower == 'large':
        size = 4

    if typeLower == 'brewed':
        type = 0
    if typeLower == 'espresso':
        type = 0.50
    if typeLower == 'cold brew':
        type = 1

    priceNoFlavor = size + type
    print('-- Total before tip: $', priceNoFlavor)
    priceNoFlavorTip = round(((priceNoFlavor * 0.15) + priceNoFlavor), 2)
    print('-- Total with 15% tip: $', priceNoFlavorTip)

elif flavorQLower in flavorQList and sizeLower in sizeList and flavorQLower == 'y':
    flavor = input('* Choose syrup flavor (hazelnut, vanilla, caramel)? ')
    flavorLower = flavor.lower()

    while flavorLower not in flavorList:
        print('Wrong entry. Try again')
        flavor = input('* Choose syrup flavor (hazelnut, vanilla, caramel)? ')
        flavorLower = flavor.lower()

    print('* ORDER SUMMARY: ', sizeLower, 'cup of', typeLower, 'coffee with', flavorLower, 'syrup.')
    if sizeLower == 'small':
        size = 2
    if sizeLower == 'medium':
        size = 3
    if sizeLower == 'large':
        size = 4

    if typeLower == 'brewed':
        type = 0
    if typeLower == 'espresso':
        type = 0.50
    if typeLower == 'cold brew':
        type = 1

    if flavorLower == 'hazelnut':
        flavor = 0.50
    if flavorLower == 'vanilla':
        flavor = 0.50
    if flavorLower == 'caramel':
        flavor = 0.50

    priceFlavor = size + type + flavor
    print('-- Total before tip: $', priceFlavor)
    PriceFlavorTip = round(((priceFlavor * 0.15) + priceFlavor), 2)
    print('-- Total with 15% tip: $', PriceFlavorTip)