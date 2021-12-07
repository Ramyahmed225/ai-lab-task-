# -*- coding: utf-8 -*-
"""


@author: alquds
"""

from logic import *


# question 1.1
# in English : Carrots color is orange
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_for_question1 = And(
    Implication(carrots, orange))


# question 1.2
# in English : " if person is vegetarian , person likes carrots "
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))


# question 1.3
# in English : " student pass if he studies hard "
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)


# question 1.4
# in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)


# question 1.5
# in English : " which course teacher teach ? "
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)

# question 1.6
# in English : " if x & y are enemies, x hate y and x fight y "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
