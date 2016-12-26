class Neuron:
  def __init__(self, inbound_neurons=[]):
    self.inbound_neurons = inbound_neurons
    self.outbound_neurons = []
    self.value = None
    for n in self.inbound_neurons:
      n.outbound_neurons.append(self)

  def forward(self):
    raise NotImplemented


class Input(Neuron):
  def __init__(self):
    Neuron.__init__(self)

  def forward(self, value=None):
      if value is not None:
        self.value = value


class Add(Neuron):
  def __init__(self, x, y):
    Neuron.__init__(self, [x, y])

    def forward(self):
      self.value = sum(c.value for c in self.inbound_neurons)






def topological_sort(feed_dict):

  input_neurons = [n for n in feed_dict.keys()]

  G = {}
  neurons = [n for n in input_neurons]
  while len(neurons) > 0:
    n = neurons.pop(0)
    if n not in G:
      G[n] = {'in': set(), 'out': set()}
    for m in n.outbound_neurons:
      if m not in G:
        G[m] = {'in': set(), 'out': set()}
        G[n]['out'].add(m)
        G[m]['in'].add(n)
        neurons.append(m)

  L = []
  S = set(input_neurons)
  while len(S) > 0:
    n = S.pop()

    if isinstance(n, Input):
      n.value = feed_dict[n]

    L.append(n)
    for m in n.outbound_neurons:
      G[n]['out'].remove(m)
      G[m]['in'].remove(n)
      # if no other incoming edges add to S
      if len(G[m]['in']) == 0:
        S.add(m)
  return L


def forward_pass(output_neuron, sorted_neurons): 

  for n in sorted_neurons:
    n.forward()

  return output_neuron.value


# from miniflow import *

x, y = Input(), Input()

f = Add(x, y)

feed_dict = {x: 10, y: 5}

sorted_neurons = topological_sort(feed_dict)
output = forward_pass(f, sorted_neurons)

# NOTE: because topological_sort set the values for the `Input` neurons we could also access
# the value for x with x.value (same goes for y).
print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))
