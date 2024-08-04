with open (r"D:\python\Python\stocks.csv","r") as f , open(r"D:\python\Python\output.csv","w") as out:
    out.write("company name,PE ratio,PB ratio \n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        esp = float(tokens[2])
        book = float(tokens[3])
        pe = round(price/esp,2)
        pb = round(price/book,2)
        out.write(f"{stock},{pe},{pb}\n")

