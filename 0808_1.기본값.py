'''def profile(name,age,lang):
    print("name :{0}\tage : {1}\tlang :{2}"\
        .format(name, age, lang))

profile("kim", 20, "python")
profile("lee", 24, "java")'''

#same age,class,lang
def profile(name,age= 20,lang= "java"):
    print("name :{0}\tage : {1}\tlang :{2}"\
        .format(name, age, lang))

profile("kim")
profile("lee")

