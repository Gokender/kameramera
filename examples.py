from kameramera import tools

posometre = tools.Lightmeter(100, '1/1000', 3.5, 500)
print(posometre.shutter_speed, posometre.shutter_speed_norm)

posometre.shutter_speed = '1/2'
print(posometre.shutter_speed, posometre.shutter_speed_norm)

posometre.shutter_speed = '2'
print(posometre.shutter_speed, posometre.shutter_speed_norm)

print(posometre.film_speed)
posometre.film_speed = 400

print(posometre.film_speed)