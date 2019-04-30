#Test ecriture
# -*- coding: iso-8859-15 -*-
from Level import Level
from savelevel import savelevel
supe= Level('Test', 10, 20, 30)
a = [112]
b = [122]
c = [333]
d = [a, b, c]
supe.setPosition(d)
savelevel(supe)
