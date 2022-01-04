from banco import *


bradesco = Bradesco('Felipe', 10000)
itau = Itau('Alex', 5000)
santander = Conta_teste('Seila', 1000)


itau.tranferir(5000, santander)
# itau.tranferir(3000, bradesco)
# itau.tranferir(3000, bradesco)

# bradesco.tranferir(4000, santander)
# bradesco.tranferir(6500, itau)
# bradesco.extrato()
itau.tranferir(4000, bradesco)
itau.extrato()
santander.extrato()
bradesco.extrato()