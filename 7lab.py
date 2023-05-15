from PIL import Image, ImageFilter, ImageOps

f = '5.jpg'
image = Image.open(f)

def z1():
    image.show(f)
    print(image.size)
    print(image.mode)
    print(image.format)


def z2():
    z = '5.jpg'
    image = Image.open(z)

    x, y = image.size
    x //= 3
    y //= 3
    print(image.size)

    out = image.resize((x, y))
    out.show()
    print(out.size)

    c = image.transpose(Image.FLIP_TOP_BOTTOM)
    c.show()
    g = ImageOps.mirror(image)
    g.show()

    out.save("11.jpg")
    c.save("22.jpg")
    g.save("33.jpg")


def z3():
    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"
    f = "5.jpg"

    h = [a, b, c, d, f]

    for file in h:
        with Image.open(file) as img:
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            new_img.save("new" + file)


def z4():
    s = "1.jpg"
    v = "2.jpg"
    image1 = Image.open(s)
    image2 = Image.open(v)
    image1.paste(image2)
    image1.show()

z1()
z2()
z3()
z4()