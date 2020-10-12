products_list = [29.25, 48.99, 99.98, 124.65, 214.30, 543.90, 799.85]
print('Table:\nFirst  Residue  Sale')
for a in products_list:
    products_list = a
    product_sale=float(round(a * 0.6, 2))
    product_residue =float(round(a * 0.4, 2))
    print(f'{products_list}   {product_residue}   {product_sale} ')
