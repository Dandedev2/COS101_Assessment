def area_of_circle():
    radius = float(input('Enter radius: '))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input('Enter your distance: '))
    time = int(input('Enter your time: '))
    velocity = distance/time
    print(velocity)

#calculate_velocity()

print('Welcome To Physics 101 Class')

topic = input('Do you need fast and reliable answer on the topic: ' 'Dimension Of Physical Quantities')


print('Okay')
print('We provide simple and adequate answer to the equation required on physical quantities')

    #print('We work only on physical quantities')
print('We have 5 formulae with the corresponding answers if required')
print('(A) Force')
print('(B) Impulse')
print('(C) Acceleration')
print('(D) Density')
print('(E) Pressure')


def a():
    mass = float(input('Enter your mass: '))
    acceleration = int(input('Enter your acceleration: '))
    a = mass * acceleration
    print(a)

#calculate_force()

def b():
    force = float(input('Enter your force: '))
    time = int(input('Enter your time: '))
    b = force * time
    print(b)

#calculate_impulse()

def c():
    velocity = float(input('Enter your velocity: '))
    time = int(input('Enter your time: '))
    c = velocity/time
    print(c)

#calculate_acceleration()

def d():
    mass = float(input('Enter your mass: '))
    volume = int(input('Enter your volume: '))
    d = mass/volume
    print(d)

#calculate_density()

def e():
    force = float(input('Enter your force: '))
    area = int(input('Enter your area: '))
    e = force/area
    print(e)

#calculate_pressure()

print('Thanks for checking our knowledge')

def main():
    choice = input("Choose option")

    if choice == "a":
        a()

    if choice == "b":
        b()

    if choice == "c":
        c()

    if choice == "d":
        d()

    if choice == "e":
        e()

if __name__ == '__main__':
    main()