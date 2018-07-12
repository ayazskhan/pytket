# Copyright 2018 Cambridge Quantum Computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pytket._cpptket import Gates, Command, route, SquareGrid, QCommands, initial_placement
from pytket._route_wrapper import route_circuit

def rep(ob):
    st = str(ob.gate).replace('Gates.', '')
    if ob.is_parametrized():
        st += "({a:.3f})".format(a=ob.get_parameter())
    st += " {q}".format(q=ob.control)
    if ob.is_two_qubit():
        st += " {t}".format(t=ob.target)
    return st

def getiter(ob):
    return ob.get_list().__iter__()

def rep_qcoms(qcoms):
    st = ""
    for com in qcoms:
        st += str(com) + '\n'
    return st

setattr(Command, "__repr__", rep)
setattr(QCommands, "__iter__", getiter)
setattr(QCommands, "__repr__", rep_qcoms)