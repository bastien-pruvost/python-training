import qrcode
img = qrcode.make('https://pruvostbastien.fr')

img.save("portfolio_qrcode.png", "PNG")
