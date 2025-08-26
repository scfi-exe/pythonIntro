def greeting(name, age=28, color="red"):
    # Greets user with “name” from “input box” and “age”, if unavailable, default age is used

    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
    print(f"We hear you like the color {color.lower()}!")


# if we assign age=27 like this when we cal lthe function, then the order in which we supply our values to the function do not matter!
greeting(age=27, name="brian", color="Blue")
