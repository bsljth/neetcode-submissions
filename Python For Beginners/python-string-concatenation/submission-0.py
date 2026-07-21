def concatenate(s1: str, s2: str) -> str:
    cat = s1 + s2

    if len(cat) > 10:
        return "Too long!"
    else:
        return cat



# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
