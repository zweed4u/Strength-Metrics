#!/usr/bin/python3
# 1RM metrics: http://www.exrx.net/Testing/WeightLifting/StrengthStandards.htm

import inspect


class StrengthMetrics:
    def __init__(self, gender, weight):
        self.gender = gender
        self.weight = weight

    def press(self):
        male_table = {
            114: {
                'Untrained': 55,
                'Novice': 75,
                'Intermediate': 90,
                'Advanced': 110,
                'Elite': 130
            },
            123: {
                'Untrained': 60,
                'Novice': 80,
                'Intermediate': 100,
                'Advanced': 115,
                'Elite': 140
            },
            132: {
                'Untrained': 65,
                'Novice': 85,
                'Intermediate': 105,
                'Advanced': 125,
                'Elite': 150
            },
            148: {
                'Untrained': 70,
                'Novice': 95,
                'Intermediate': 120,
                'Advanced': 140,
                'Elite': 170
            },
            165: {
                'Untrained': 75,
                'Novice': 100,
                'Intermediate': 130,
                'Advanced': 155,
                'Elite': 190
            },
            181: {
                'Untrained': 80,
                'Novice': 110,
                'Intermediate': 140,
                'Advanced': 165,
                'Elite': 220
            },
            198: {
                'Untrained': 85,
                'Novice': 115,
                'Intermediate': 145,
                'Advanced': 175,
                'Elite': 235
            },
            220: {
                'Untrained': 90,
                'Novice': 120,
                'Intermediate': 155,
                'Advanced': 185,
                'Elite': 255
            },
            242: {
                'Untrained': 95,
                'Novice': 125,
                'Intermediate': 160,
                'Advanced': 190,
                'Elite': 265
            },
            275: {
                'Untrained': 95,
                'Novice': 130,
                'Intermediate': 165,
                'Advanced': 195,
                'Elite': 275
            },
            319: {
                'Untrained': 100,
                'Novice': 135,
                'Intermediate': 170,
                'Advanced': 200,
                'Elite': 280
            },
            320: {
                'Untrained': 100,
                'Novice': 140,
                'Intermediate': 175,
                'Advanced': 205,
                'Elite': 285
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Press metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]

    def bench(self):
        male_table = {
            114: {
                'Untrained': 85,
                'Novice': 110,
                'Intermediate': 130,
                'Advanced': 180,
                'Elite': 220
            },
            123: {
                'Untrained': 90,
                'Novice': 115,
                'Intermediate': 140,
                'Advanced': 195,
                'Elite': 240
            },
            132: {
                'Untrained': 100,
                'Novice': 125,
                'Intermediate': 155,
                'Advanced': 210,
                'Elite': 260
            },
            148: {
                'Untrained': 110,
                'Novice': 140,
                'Intermediate': 170,
                'Advanced': 235,
                'Elite': 290
            },
            165: {
                'Untrained': 120,
                'Novice': 150,
                'Intermediate': 185,
                'Advanced': 255,
                'Elite': 320
            },
            181: {
                'Untrained': 130,
                'Novice': 165,
                'Intermediate': 200,
                'Advanced': 275,
                'Elite': 345
            },
            198: {
                'Untrained': 135,
                'Novice': 175,
                'Intermediate': 215,
                'Advanced': 290,
                'Elite': 360
            },
            220: {
                'Untrained': 140,
                'Novice': 185,
                'Intermediate': 225,
                'Advanced': 305,
                'Elite': 380
            },
            242: {
                'Untrained': 145,
                'Novice': 190,
                'Intermediate': 230,
                'Advanced': 315,
                'Elite': 395
            },
            275: {
                'Untrained': 150,
                'Novice': 195,
                'Intermediate': 240,
                'Advanced': 325,
                'Elite': 405
            },
            319: {
                'Untrained': 155,
                'Novice': 200,
                'Intermediate': 245,
                'Advanced': 335,
                'Elite': 415
            },
            320: {
                'Untrained': 160,
                'Novice': 205,
                'Intermediate': 250,
                'Advanced': 340,
                'Elite': 425
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Bench Press metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]

    def squat(self):
        male_table = {
            114: {
                'Untrained': 80,
                'Novice': 145,
                'Intermediate': 175,
                'Advanced': 240,
                'Elite': 320
            },
            123: {
                'Untrained': 85,
                'Novice': 155,
                'Intermediate': 190,
                'Advanced': 260,
                'Elite': 345
            },
            132: {
                'Untrained': 90,
                'Novice': 170,
                'Intermediate': 205,
                'Advanced': 280,
                'Elite': 370
            },
            148: {
                'Untrained': 100,
                'Novice': 190,
                'Intermediate': 230,
                'Advanced': 315,
                'Elite': 410
            },
            165: {
                'Untrained': 110,
                'Novice': 205,
                'Intermediate': 250,
                'Advanced': 340,
                'Elite': 445
            },
            181: {
                'Untrained': 120,
                'Novice': 220,
                'Intermediate': 270,
                'Advanced': 370,
                'Elite': 480
            },
            198: {
                'Untrained': 125,
                'Novice': 230,
                'Intermediate': 285,
                'Advanced': 390,
                'Elite': 505
            },
            220: {
                'Untrained': 130,
                'Novice': 245,
                'Intermediate': 300,
                'Advanced': 410,
                'Elite': 530
            },
            242: {
                'Untrained': 135,
                'Novice': 255,
                'Intermediate': 310,
                'Advanced': 425,
                'Elite': 550
            },
            275: {
                'Untrained': 140,
                'Novice': 260,
                'Intermediate': 320,
                'Advanced': 435,
                'Elite': 570
            },
            319: {
                'Untrained': 145,
                'Novice': 270,
                'Intermediate': 325,
                'Advanced': 445,
                'Elite': 580
            },
            320: {
                'Untrained': 150,
                'Novice': 275,
                'Intermediate': 330,
                'Advanced': 455,
                'Elite': 595
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Squat metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]

    def deadlift(self):
        male_table = {
            114: {
                'Untrained': 95,
                'Novice': 180,
                'Intermediate': 205,
                'Advanced': 300,
                'Elite': 385
            },
            123: {
                'Untrained': 105,
                'Novice': 195,
                'Intermediate': 220,
                'Advanced': 320,
                'Elite': 415
            },
            132: {
                'Untrained': 115,
                'Novice': 210,
                'Intermediate': 240,
                'Advanced': 340,
                'Elite': 440
            },
            148: {
                'Untrained': 125,
                'Novice': 235,
                'Intermediate': 270,
                'Advanced': 380,
                'Elite': 480
            },
            165: {
                'Untrained': 135,
                'Novice': 255,
                'Intermediate': 295,
                'Advanced': 410,
                'Elite': 520
            },
            181: {
                'Untrained': 150,
                'Novice': 275,
                'Intermediate': 315,
                'Advanced': 440,
                'Elite': 550
            },
            198: {
                'Untrained': 155,
                'Novice': 290,
                'Intermediate': 335,
                'Advanced': 460,
                'Elite': 565
            },
            220: {
                'Untrained': 165,
                'Novice': 305,
                'Intermediate': 350,
                'Advanced': 480,
                'Elite': 585
            },
            242: {
                'Untrained': 170,
                'Novice': 320,
                'Intermediate': 365,
                'Advanced': 490,
                'Elite': 595
            },
            275: {
                'Untrained': 175,
                'Novice': 325,
                'Intermediate': 375,
                'Advanced': 500,
                'Elite': 600
            },
            319: {
                'Untrained': 180,
                'Novice': 335,
                'Intermediate': 380,
                'Advanced': 505,
                'Elite': 610
            },
            320: {
                'Untrained': 185,
                'Novice': 340,
                'Intermediate': 390,
                'Advanced': 510,
                'Elite': 615
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Deadlift metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]

    def clean(self):
        male_table = {
            114: {
                'Untrained': 55,
                'Novice': 105,
                'Intermediate': 125,
                'Advanced': 175,
                'Elite': 205
            },
            123: {
                'Untrained': 60,
                'Novice': 110,
                'Intermediate': 135,
                'Advanced': 185,
                'Elite': 225
            },
            132: {
                'Untrained': 65,
                'Novice': 120,
                'Intermediate': 150,
                'Advanced': 200,
                'Elite': 240
            },
            148: {
                'Untrained': 75,
                'Novice': 135,
                'Intermediate': 165,
                'Advanced': 225,
                'Elite': 265
            },
            165: {
                'Untrained': 80,
                'Novice': 145,
                'Intermediate': 180,
                'Advanced': 245,
                'Elite': 290
            },
            181: {
                'Untrained': 85,
                'Novice': 160,
                'Intermediate': 195,
                'Advanced': 265,
                'Elite': 310
            },
            198: {
                'Untrained': 90,
                'Novice': 165,
                'Intermediate': 205,
                'Advanced': 280,
                'Elite': 325
            },
            220: {
                'Untrained': 95,
                'Novice': 175,
                'Intermediate': 215,
                'Advanced': 295,
                'Elite': 345
            },
            242: {
                'Untrained': 100,
                'Novice': 185,
                'Intermediate': 225,
                'Advanced': 305,
                'Elite': 355
            },
            275: {
                'Untrained': 105,
                'Novice': 190,
                'Intermediate': 230,
                'Advanced': 315,
                'Elite': 365
            },
            319: {
                'Untrained': 110,
                'Novice': 195,
                'Intermediate': 235,
                'Advanced': 320,
                'Elite': 375
            },
            320: {
                'Untrained': 115,
                'Novice': 200,
                'Intermediate': 240,
                'Advanced': 330,
                'Elite': 385
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Clean metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]

    def snatch(self):
        male_table = {
            114: {
                'Untrained': 45,
                'Novice': 80,
                'Intermediate': 95,
                'Advanced': 135,
                'Elite': 160
            },
            123: {
                'Untrained': 50,
                'Novice': 85,
                'Intermediate': 105,
                'Advanced': 145,
                'Elite': 175
            },
            132: {
                'Untrained': 55,
                'Novice': 95,
                'Intermediate': 115,
                'Advanced': 155,
                'Elite': 185
            },
            148: {
                'Untrained': 60,
                'Novice': 105,
                'Intermediate': 130,
                'Advanced': 175,
                'Elite': 205
            },
            165: {
                'Untrained': 65,
                'Novice': 115,
                'Intermediate': 140,
                'Advanced': 190,
                'Elite': 225
            },
            181: {
                'Untrained': 70,
                'Novice': 125,
                'Intermediate': 150,
                'Advanced': 205,
                'Elite': 240
            },
            198: {
                'Untrained': 75,
                'Novice': 130,
                'Intermediate': 160,
                'Advanced': 220,
                'Elite': 250
            },
            220: {
                'Untrained': 80,
                'Novice': 135,
                'Intermediate': 170,
                'Advanced': 230,
                'Elite': 265
            },
            242: {
                'Untrained': 85,
                'Novice': 140,
                'Intermediate': 175,
                'Advanced': 235,
                'Elite': 275
            },
            275: {
                'Untrained': 90,
                'Novice': 145,
                'Intermediate': 180,
                'Advanced': 245,
                'Elite': 285
            },
            319: {
                'Untrained': 95,
                'Novice': 150,
                'Intermediate': 185,
                'Advanced': 250,
                'Elite': 290
            },
            320: {
                'Untrained': 100,
                'Novice': 155,
                'Intermediate': 190,
                'Advanced': 260,
                'Elite': 300
            }
        }
        my_weight_class = min(list(male_table.keys()),
                              key=lambda x: abs(x - self.weight))
        print(
            f'Power Snatch metrics for your weight class ({my_weight_class} at {self.weight}):\n{male_table[my_weight_class]}\n')
        return male_table[my_weight_class]


MyReport = StrengthMetrics('M', 184)

# Run all methods in the class
attributes = (getattr(MyReport, name) for name in dir(MyReport))
methods = filter(inspect.ismethod, attributes)
for method in methods:
    try:
        method()
    except TypeError:
        # Can't handle methods with required arguments.
        pass

reference_string = """
Untrained:
Expected level of strength in a healthy individual who has not trained on the exercise before but can perform it correctly. This represents the minimum level of strength required to maintain a reasonable quality of life in a sedentary individual.

Novice:
A person training regularly for a period of 3-9 months. This strength level supports the demands of vigorous recreational activities.

Intermediate:
A person who has engaged in regular training for up to two years. The intermediate level indicates some degree of specialization in the exercises and a high level of performance at the recreational level.

Advanced:
An individual with multi-year training experience with definite goals in the higher levels of competitive athletics.

Elite:
Refers specifically to athletes competing in strength sports. Less than 1% of the weight training population will attain this level.
"""
print(f'For reference: {reference_string}')
