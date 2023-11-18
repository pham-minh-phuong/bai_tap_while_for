Original_Price=(4.95, 9.95,14.95,19.95,24.95)
Sale= 60
print ( "Original Price| Discount Amount| New Price")
print("-"*54)
for Price in Original_Price:
    Discount_Amount= Price*(Sale/100)
    New_Price= Price-Discount_Amount
    print(f"${Price:11.2f}  |   ${Discount_Amount:9.2f}   |   ${New_Price:10.2f}")